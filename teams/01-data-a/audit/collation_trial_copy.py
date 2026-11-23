"""A small copy of tokenizer sample v0 for an end-to-end trial: every one of the 86 parts, with its first N rows plus the
audited documents of collation_docs.csv that are in it, and a manifest in the sample's own form (sizes and sha256 of the copies).

    python -I teams/01-data-a/audit/collation_trial_copy.py <tokenizer_sample_v0> <out folder> 150 teams/01-data-a/audit/collation_docs.csv
"""
import csv, hashlib, json, sys
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.compute as pc

SRC, OUT, N = Path(sys.argv[1]), Path(sys.argv[2]), int(sys.argv[3])
labelled = {r["doc_id"] for r in csv.DictReader(open(sys.argv[4], encoding="utf-8"))}
man = json.loads((SRC / "sample_manifest.json").read_text(encoding="utf-8"))
shards = []
for s in man["shards"]:
    t = pq.read_table(SRC / s["path"])
    keep = pc.or_(pc.is_in(t["doc_id"], value_set=pa.array(sorted(labelled))),
                  pc.is_in(t["doc_id"], value_set=t["doc_id"].slice(0, N).combine_chunks()))
    t = t.filter(keep)
    dst = OUT / s["path"]; dst.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(t, dst)
    b = dst.read_bytes()
    shards.append(dict(s, rows=t.num_rows, text_bytes=sum(len(x.encode()) for x in t["text"].to_pylist()), bytes=len(b),
                       sha256=hashlib.sha256(b).hexdigest()))
m = dict(man, name=man["name"] + f" (trial copy: first {N} rows of each part plus the audited documents)",
         total_docs=sum(s["rows"] for s in shards), shards=shards)
(OUT / "sample_manifest.json").write_text(json.dumps(m, indent=1), encoding="utf-8")
print(len(shards), "parts,", m["total_docs"], "rows")
