"""No-op overlap and dedup folders, for a local smoke test of the shard job on cleaned parts that did not go through dedup.

  python -I teams/01-data-a/jobs/2026-11-15-first-shards/local_test/noop_dedup.py --cleaned <cleaned> --out <folder>

<cleaned> is a clean job's output: <cleaned>/<split>/<pack>/<part>.parquet (and its job_summary.json, which the shard writer reads).
Writes <folder>/overlap and <folder>/dedup in the formats run_pipeline.py adopts, with nothing found and nothing removed:
overlap_summary.json lists every cleaned part with its row count, and dedup_summary.json names the overlap files it "checked".
For a smoke test only: the real overlap and dedup are TSAI jobs (dedup/overlap.py and dedup/dedup.py, #255).
"""
import argparse, csv, hashlib, json, sys
from pathlib import Path
import pyarrow.parquet as pq

REMOVE_HEADER = ["pack_id", "split", "part", "row_in_part", "doc_id"]
GROUP_HEADER = ["group_id", "group_size", "priority_rule", "role", "pack_id", "split", "part", "row_in_part", "doc_id"]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_csv(path, header):
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(header)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cleaned", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    parts = [{"part": p.relative_to(a.cleaned).as_posix(), "documents": pq.ParquetFile(p).metadata.num_rows}
             for split in ("train", "heldout") for p in sorted((a.cleaned / split).rglob("*.parquet"))]
    if not parts:
        sys.exit(f"--cleaned {a.cleaned}: no <split>/<pack>/<part>.parquet")
    total = sum(p["documents"] for p in parts)
    ov, dd = a.out / "overlap", a.out / "dedup"
    for d in (ov, dd):
        if d.exists():
            sys.exit(f"{d} exists: give a new --out")
        d.mkdir(parents=True)
    (ov / "overlap_matches.csv").write_text("row_a,row_b\n", encoding="utf-8")
    (ov / "overlap_docs.parquet").write_bytes(b"no-op overlap: smoke test only")
    files = {n: sha256(ov / n) for n in ("overlap_matches.csv", "overlap_docs.parquet")}
    (ov / "overlap_summary.json").write_text(json.dumps({
        "status": "complete", "documents_all": total, "config": {"no_op": True},
        "inputs": {"parts": parts}, "outputs": {n: {"sha256": s} for n, s in files.items()}}, indent=1), encoding="utf-8")
    write_csv(dd / "remove_list.csv", REMOVE_HEADER)
    write_csv(dd / "dedup_groups.csv", GROUP_HEADER)
    (dd / "dedup_log.jsonl").write_text("", encoding="utf-8")
    (dd / "dedup_summary.json").write_text(json.dumps({
        "status": "complete", "overlap_run": {"documents_all": total, "checked_sha256": files}, "documents_all": total,
        "removed": 0, "heldout_removed": 0, "config": {"no_op": True, "cross_pack": False, "pack_order": [], "licence_usable": {},
                                                       "default_licence_usable": True, "gold_dirs": []}}, indent=1), encoding="utf-8")
    print(json.dumps({"parts": len(parts), "documents": total, "overlap": ov.as_posix(), "dedup": dd.as_posix()}))


if __name__ == "__main__":
    main()
