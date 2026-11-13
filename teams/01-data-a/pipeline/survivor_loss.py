"""Count and list the dedup groups whose survivor F2 dropped (TSAI, 12 Nov: accept the loss, count and list the groups).

  python -I teams/01-data-a/pipeline/survivor_loss.py --groups <dedup_groups.csv> --f2 <final_dir> --out <dir>

Dedup keeps one copy of each duplicate group (several when the group has held-out copies) and F2 runs after it. When F2
drops a survivor, that copy is gone and the removed copies are not brought back (dedup_design_v1.md, the F2 step).

INPUT
=====
--groups is dedup.py's dedup_groups.csv: group_id, group_size, priority_rule, role (survivor or removed), pack_id, split,
part, row_in_part, doc_id. --f2 is the folder F2 wrote, one run per split: <final>/<split>/<part>.f2.json, each with
run_f2.py's "dropped" list ({doc_id, items, offset}) and "set_sha256". A survivor is matched on (split, part, doc_id):
doc_id alone is not a key (in sample v0, 22,773 doc_ids sit in two parts of the same pack and split).

A GROUP IS
==========
  lost          it had at least one survivor and F2 dropped all of them: no copy is left in the final data
  partly_hit    F2 dropped some of its survivors, not all (a group with several held-out survivors)
  untouched     F2 dropped none of its survivors
  (without_survivor: dedup kept no copy, as with no usable licence; F2 cannot change it)

CHECKS (exit code 1 on failure)
===============================
dedup_groups.csv has dedup.py's header; every part that holds a survivor has an F2 report (else F2 did not cover it);
every F2 report names the same set_sha256.

OUTPUT
======
<out>/survivor_loss.csv: one row per survivor F2 dropped (status, group_id, group_size, priority_rule, pack_id, split,
part, row_in_part, doc_id, f2_items, offset). <out>/survivor_loss_summary.json: group counts, counts per pack, the
set_sha256, the sha256 of dedup_groups.csv and of this file. IDs, benchmark item IDs and offsets only, never text.
"""
import sys
sys.dont_write_bytecode = True

import argparse, csv, hashlib, json
from collections import defaultdict
from pathlib import Path

GROUP_HEADER = ["group_id", "group_size", "priority_rule", "role", "pack_id", "split", "part", "row_in_part", "doc_id"]
SUFFIX = ".f2.json"


class Stop(Exception):
    """A check failed: the message says which and where."""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_groups(path):
    groups = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != GROUP_HEADER:
            raise Stop(f"{path}: header is {reader.fieldnames}, expected dedup.py's {GROUP_HEADER}")
        for r in reader:
            r["part"] = r["part"].replace("\\", "/")
            groups[r["group_id"]].append(r)
    return groups


def read_f2(final):
    """{(split, part): {doc_id: dropped entry}} and the set_sha256 all reports share."""
    final = Path(final)
    reports = sorted(final.rglob("*" + SUFFIX))
    if not reports:
        raise Stop(f"--f2 {final}: no *{SUFFIX} reports")
    dropped, sets = {}, set()
    for path in reports:
        rel = path.relative_to(final).as_posix()
        split, _, part = rel.partition("/")
        part = part[: -len(SUFFIX)]
        data = json.loads(path.read_text(encoding="utf-8"))
        sets.add(data.get("set_sha256"))
        dropped[(split, part)] = {d["doc_id"]: d for d in data.get("dropped", [])}
    if len(sets) != 1 or None in sets:
        raise Stop(f"the F2 reports name {len(sets)} different set_sha256 values: {sorted(map(str, sets))}")
    return dropped, sets.pop(), len(reports)


def report(groups_csv, final, out):
    groups_csv, out = Path(groups_csv), Path(out)
    groups = read_groups(groups_csv)
    dropped, set_sha, n_reports = read_f2(final)
    uncovered = sorted({(m["split"], m["part"]) for ms in groups.values() for m in ms if m["role"] == "survivor"}
                       - set(dropped))
    if uncovered:
        raise Stop(f"{len(uncovered)} part(s) hold a dedup survivor but have no F2 report, e.g. "
                   f"{uncovered[0][0]}/{uncovered[0][1]}: F2 did not cover them")

    counts = {"total": len(groups), "with_survivor": 0, "without_survivor": 0, "lost": 0, "partly_hit": 0, "untouched": 0}
    rows, by_pack = [], defaultdict(lambda: {"lost": 0, "partly_hit": 0})
    for gid in sorted(groups, key=lambda g: (len(g), g)):
        survivors = [m for m in groups[gid] if m["role"] == "survivor"]
        if not survivors:
            counts["without_survivor"] += 1
            continue
        counts["with_survivor"] += 1
        hit = [(m, dropped[(m["split"], m["part"])][m["doc_id"]]) for m in survivors
               if m["doc_id"] in dropped[(m["split"], m["part"])]]
        status = "untouched" if not hit else "lost" if len(hit) == len(survivors) else "partly_hit"
        counts[status] += 1
        for m, d in hit:
            by_pack[m["pack_id"]][status] += 1
            rows.append({"status": status, **{k: m[k] for k in GROUP_HEADER if k != "role"},
                         "f2_items": " ".join(d.get("items", [])), "offset": d.get("offset", "")})

    out.mkdir(parents=True, exist_ok=True)
    with (out / "survivor_loss.csv").open("w", newline="", encoding="utf-8") as f:
        fields = ["status"] + [k for k in GROUP_HEADER if k != "role"] + ["f2_items", "offset"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    summary = {"tool": "survivor_loss.py", "code_sha256": sha256(Path(__file__)), "groups_sha256": sha256(groups_csv),
               "set_sha256": set_sha, "f2_reports": n_reports, "groups": counts,
               "survivors_dropped_by_f2": len(rows), "by_pack": {p: by_pack[p] for p in sorted(by_pack)}}
    (out / "survivor_loss_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8", newline="\n")
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--groups", type=Path, required=True, help="dedup.py's dedup_groups.csv")
    ap.add_argument("--f2", type=Path, required=True, help="F2's output folder: <split>/<part>.f2.json")
    ap.add_argument("--out", type=Path, required=True, help="where survivor_loss.csv and the summary go")
    args = ap.parse_args()
    try:
        s = report(args.groups, args.f2, args.out)
    except Stop as e:
        sys.exit(f"survivor_loss: {e}")
    print(json.dumps({**s["groups"], "survivors_dropped_by_f2": s["survivors_dropped_by_f2"]}))


if __name__ == "__main__":
    main()
