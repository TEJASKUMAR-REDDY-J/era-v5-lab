"""Stand-in for run_f2.py in the runner's tests: same command line, same outputs, no fingerprint set.

The real F2 needs G9's full fingerprint set (about 1.1 GB) and lives in its own PR with its own tests, so the runner's
tests use this instead. It drops the doc_ids named in the FAKE_F2_DROP environment variable (comma-separated) and writes
run_f2.py's files: <out>/<rel>.parquet, <out>/<rel>.parquet.f2.json and <out>/f2_summary.json.
"""
import argparse, hashlib, json, os
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

SET = "2826a3b883210c653979103c09ce1c79e40fc4f7034b54027f2836482370d22a"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--inputs", type=Path, nargs="+", required=True)
ap.add_argument("--out", type=Path, required=True)
args = ap.parse_args()
drop = set(filter(None, os.environ.get("FAKE_F2_DROP", "").split(",")))
reports = []
for root in args.inputs:
    for src in sorted(root.rglob("*.parquet")):
        rel = src.relative_to(root)
        dst = args.out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        t = pq.read_table(src)
        ids = t.column("doc_id").to_pylist()
        keep = [d not in drop for d in ids]
        pq.write_table(t.filter(pa.array(keep, pa.bool_())), dst)
        dropped = [{"doc_id": d, "items": ["fake:1"], "offset": 0} for d, k in zip(ids, keep) if not k]
        r = {"input": src.as_posix(), "input_sha256": sha(src), "output_sha256": sha(dst), "set_sha256": SET,
             "run_f2_py_sha256": sha(__file__), "rows": len(ids), "kept": sum(keep), "dropped_by_f2": len(dropped),
             "errors": [], "seconds": 0.0, "dropped": dropped}
        dst.with_name(dst.name + ".f2.json").write_text(json.dumps(r), encoding="utf-8")
        reports.append(r)
args.out.mkdir(parents=True, exist_ok=True)
total = {k: sum(r[k] for r in reports) for k in ("rows", "kept", "dropped_by_f2")}
(args.out / "f2_summary.json").write_text(json.dumps({"set_sha256": SET, "files": len(reports), **total, "errors": 0}),
                                          encoding="utf-8")
