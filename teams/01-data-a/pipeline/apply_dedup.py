"""Apply dedup.py's remove list: copy the cleaned parts without the rows it names, everything else unchanged.

  python -I teams/01-data-a/pipeline/apply_dedup.py --cleaned <cleaned_dir> --remove-list <remove_list.csv> --out <dir>

This is the "filters the cleaned parts with remove_list.csv" step of dedup/dedup_design_v1.md ("Pipeline and hand-off to
TSAI"), between dedup.py and F2. It decides nothing: dedup.py chose what goes, this only carries it out, and checks it.

INPUT
=====
--cleaned is the folder overlap.py read: <cleaned>/train/**.parquet and <cleaned>/heldout/**.parquet. A "part" is a file's
path relative to its split folder (code-go/part-00000.parquet) and row_in_part is its 0-based row in file order, as
overlap.py numbers them. --remove-list is dedup.py's remove_list.csv: pack_id, split, part, row_in_part, doc_id. Parts are
compared with / as the separator, so a list written on Linux matches files on Windows and back.

doc_id alone is not a key: in the cleaned sample v0, 22,773 doc_ids sit in two parts of the same pack and split. A row is
found by (split, part, row_in_part), and its doc_id and pack_id must then match the list.

CHECKS (any failure stops the run before anything is written; exit code 1)
==========================================================================
  - the header is exactly dedup.py's, no row is listed twice, row_in_part is a whole number >= 0
  - no held-out row: dedup never removes a held-out document (source_priority_v1.md rule 0), so one in the list means
    the list is broken
  - every listed part exists, every listed row is inside it, and the doc_id and pack_id at that row are the listed ones;
    a mismatch means the list came from another cleaning run than these parts
  - --out is not inside --cleaned, nor the other way round
After writing, kept + removed must equal the rows of every part, and every listed row must have been removed once.

OUTPUT
======
<out>/<split>/<part> for every part, with the same schema and unchanged text. A part with nothing to remove is copied
byte for byte, so its sha256 shows it is untouched. Files are written to .tmp and renamed. <out>/apply_dedup_summary.json
holds the remove list's sha256 and row count, this file's sha256, and per part: rows, removed, kept, the input and output
sha256 and whether it was copied; then totals and counts per pack and split. IDs, counts and hashes only, never text.
A rerun with the same remove list and code skips each part whose input and output still have the recorded sha256, so a
stopped run resumes.
"""
import sys
sys.dont_write_bytecode = True

import argparse, csv, hashlib, json, shutil
from collections import Counter, defaultdict
from pathlib import Path

HEADER = ["pack_id", "split", "part", "row_in_part", "doc_id"]
SPLITS = ("train", "heldout")
BATCH = 1000
SUMMARY = "apply_dedup_summary.json"


class Stop(Exception):
    """A check failed: the message says which and where."""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def posix(part):
    return part.replace("\\", "/")


def read_remove_list(path, splits):
    """{(split, part): {row: (pack_id, doc_id)}} and the number of rows, after the per-row checks."""
    todo, n = defaultdict(dict), 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header != HEADER:
            raise Stop(f"{path}: header is {header}, expected dedup.py's {HEADER}")
        for line, rec in enumerate(reader, start=2):
            if len(rec) != len(HEADER):
                raise Stop(f"{path} line {line}: {len(rec)} fields, expected {len(HEADER)}")
            pack, split, part, row, doc_id = rec
            if split == "heldout":
                raise Stop(f"{path} line {line}: a held-out row ({part} row {row}). Dedup never removes held-out "
                           "documents (source_priority_v1.md rule 0), so this remove list is broken")
            if split not in SPLITS:
                raise Stop(f"{path} line {line}: split {split!r} is not train or heldout")
            if split not in splits:
                raise Stop(f"{path} line {line}: split {split} is not among --splits {list(splits)}")
            if not row.isdigit():
                raise Stop(f"{path} line {line}: row_in_part {row!r} is not a whole number >= 0")
            part, row = posix(part), int(row)
            if row in todo[(split, part)]:
                raise Stop(f"{path} line {line}: {split}/{part} row {row} is listed twice")
            todo[(split, part)][row] = (pack, doc_id)
            n += 1
    return dict(todo), n


def find_parts(cleaned, splits):
    """[(split, part, path)] for every Parquet file under the selected split folders, as overlap.py finds them."""
    parts = []
    for split in splits:
        folder = cleaned / split
        if not folder.is_dir():
            raise Stop(f"--cleaned {cleaned} has no {split}/ folder")
        parts += [(split, f.relative_to(folder).as_posix(), f) for f in sorted(folder.rglob("*.parquet")) if f.is_file()]
    if not parts:
        raise Stop(f"--cleaned {cleaned}: no Parquet parts under {list(splits)}")
    return parts


def check_rows(path, split, part, listed):
    """Every listed row is inside the file and holds the listed pack_id and doc_id. Reads two columns only."""
    import pyarrow.parquet as pq
    pf = pq.ParquetFile(path)
    missing = {"doc_id", "pack_id"} - set(pf.schema_arrow.names)
    if missing:
        raise Stop(f"{split}/{part}: no {', '.join(sorted(missing))} column")
    t = pf.read(columns=["doc_id", "pack_id"])
    doc_ids, packs = t.column("doc_id").to_pylist(), t.column("pack_id").to_pylist()
    for row, (pack, doc_id) in sorted(listed.items()):
        if row >= len(doc_ids):
            raise Stop(f"{split}/{part}: row {row} is listed, but the part has {len(doc_ids)} rows")
        if doc_ids[row] != doc_id:
            raise Stop(f"{split}/{part} row {row}: doc_id is {doc_ids[row]!r}, the remove list says {doc_id!r}. "
                       "The list was made from another cleaning run than these parts")
        if packs[row] != pack:
            raise Stop(f"{split}/{part} row {row}: pack_id is {packs[row]!r}, the remove list says {pack!r}")


def pack_counts(path):
    import pyarrow.parquet as pq
    return Counter(pq.read_table(path, columns=["pack_id"]).column("pack_id").to_pylist())


def filter_part(src, tmp, listed):
    """Write src without the listed rows to tmp; return (rows, kept, removed per pack, rows per pack)."""
    import pyarrow as pa
    import pyarrow.parquet as pq
    pf = pq.ParquetFile(src)
    rows = kept = 0
    removed, per_pack = Counter(), Counter()
    with pq.ParquetWriter(tmp, pf.schema_arrow) as w:
        for batch in pf.iter_batches(batch_size=BATCH):
            packs = batch.column("pack_id").to_pylist()
            keep = [rows + i not in listed for i in range(batch.num_rows)]
            for p, k in zip(packs, keep):
                per_pack[p] += 1
                if not k:
                    removed[p] += 1
            w.write_table(pa.Table.from_batches([batch], schema=pf.schema_arrow).filter(pa.array(keep, pa.bool_())))
            rows += batch.num_rows
            kept += sum(keep)
    return rows, kept, removed, per_pack


def write_json(path, data):
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")
    tmp.replace(path)


def apply(cleaned, remove_list, out, splits=SPLITS):
    """Run the checks, then write <out>. Returns the summary dict. Raises Stop on any failed check."""
    cleaned, remove_list, out = Path(cleaned), Path(remove_list), Path(out)
    rc, ro = cleaned.resolve(), out.resolve()
    if rc == ro or rc in ro.parents or ro in rc.parents:
        raise Stop(f"--out {out} and --cleaned {cleaned} overlap: the output would be read as input")
    todo, n_listed = read_remove_list(remove_list, splits)
    parts = find_parts(cleaned, splits)
    known = {(s, p) for s, p, _ in parts}
    absent = sorted(k for k in todo if k not in known)
    if absent:
        raise Stop(f"{len(absent)} listed part(s) not found under --cleaned, e.g. {absent[0][0]}/{absent[0][1]}")
    for split, part, path in parts:  # every check before anything is written
        if (split, part) in todo:
            check_rows(path, split, part, todo[(split, part)])

    rl_sha, code_sha = sha256(remove_list), sha256(Path(__file__))
    old = {}
    if (out / SUMMARY).is_file():
        prev = json.loads((out / SUMMARY).read_text(encoding="utf-8"))
        if prev.get("remove_list", {}).get("sha256") == rl_sha and prev.get("code_sha256") == code_sha:
            old = {(p["split"], p["part"]): p for p in prev.get("parts", [])}

    summary = {"tool": "apply_dedup.py", "code_sha256": code_sha, "cleaned": cleaned.as_posix(),
               "remove_list": {"path": remove_list.as_posix(), "sha256": rl_sha, "rows": n_listed},
               "splits": list(splits), "parts": []}
    out.mkdir(parents=True, exist_ok=True)
    for split, part, src in parts:
        dst = out / split / part
        listed = todo.get((split, part), {})
        in_sha = sha256(src)
        prev = old.get((split, part))
        if prev and prev["input_sha256"] == in_sha and dst.is_file() and sha256(dst) == prev["output_sha256"]:
            summary["parts"].append({**prev, "skipped": True})
            write_json(out / SUMMARY, summary)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        tmp = dst.with_name(dst.name + ".tmp")
        if listed:
            rows, kept, removed, per_pack = filter_part(src, tmp, listed)
            if rows - kept != len(listed) or sum(removed.values()) != len(listed):
                tmp.unlink()
                raise Stop(f"{split}/{part}: removed {rows - kept} rows, the list names {len(listed)}")
        else:
            shutil.copyfile(src, tmp)
            per_pack, removed = pack_counts(tmp), Counter()
            rows = kept = sum(per_pack.values())
        tmp.replace(dst)
        summary["parts"].append({
            "split": split, "part": part, "rows": rows, "removed": rows - kept, "kept": kept,
            "input_sha256": in_sha, "output_sha256": sha256(dst), "copied": not listed, "skipped": False,
            "packs": {p: {"rows": per_pack[p], "removed": removed[p]} for p in sorted(per_pack)}})
        write_json(out / SUMMARY, summary)

    by_pack = defaultdict(lambda: defaultdict(Counter))
    for p in summary["parts"]:
        for pack, c in p["packs"].items():
            by_pack[pack][p["split"]].update(rows=c["rows"], removed=c["removed"])
    summary["by_pack"] = {pack: {sp: {"rows": c["rows"], "removed": c["removed"], "kept": c["rows"] - c["removed"]}
                                 for sp, c in sorted(splits_.items())} for pack, splits_ in sorted(by_pack.items())}
    totals = Counter()
    for p in summary["parts"]:
        totals.update(rows=p["rows"], removed=p["removed"], kept=p["kept"])
    summary["totals"] = {k: totals[k] for k in ("rows", "removed", "kept")}
    if summary["totals"]["removed"] != n_listed or summary["totals"]["rows"] != summary["totals"]["kept"] + n_listed:
        raise Stop(f"removed {summary['totals']['removed']} rows in all, the list names {n_listed}")
    write_json(out / SUMMARY, summary)
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cleaned", type=Path, required=True, help="folder with train/ and heldout/ cleaned parts")
    ap.add_argument("--remove-list", type=Path, required=True, help="dedup.py's remove_list.csv")
    ap.add_argument("--out", type=Path, required=True, help="output folder (gets train/, heldout/ and the summary)")
    ap.add_argument("--splits", nargs="+", default=list(SPLITS), choices=SPLITS)
    args = ap.parse_args()
    try:
        s = apply(args.cleaned, args.remove_list, args.out, tuple(args.splits))
    except Stop as e:
        sys.exit(f"apply_dedup: {e}")
    print(json.dumps({"parts": len(s["parts"]), **s["totals"]}))


if __name__ == "__main__":
    main()
