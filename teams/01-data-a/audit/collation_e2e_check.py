"""End-to-end check on a trial copy: the pipeline's clean stage output against the collation's rule-by-rule replay, every
document of every part; then the collated cards on the same documents. Counts only. Exit code 1 if any document differs.

    python -I teams/01-data-a/audit/collation_e2e_check.py <trial copy> <clean job output folder, relative to the repository>
"""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from pathlib import Path
import pyarrow.parquet as pq

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "teams/01-data-a/audit"))
import collation_replay as replay
import collated_medicine_check as check

RAW, JOB = Path(sys.argv[1]), REPO / sys.argv[2]
check.load()
c = replay.c
tot, per = Counter(), {}
for raw in sorted(RAW.rglob("part-*.parquet")):
    rel = raw.relative_to(RAW)
    split, pack = rel.parts[0], rel.parts[1]
    out = {r["doc_id"]: r["text"] for r in pq.read_table(JOB / rel, columns=["doc_id", "text"]).to_pylist()}
    family = c._FAMILY.get(pack)
    n = Counter()
    if family is None:  # no rules: the job copies the part through
        n["passthrough"] = sum(1 for r in pq.read_table(raw, columns=["doc_id"]).to_pylist() if r["doc_id"] in out)
    else:
        now = replay.rules(pack)
        new, _ = check.with_cards(pack) if any(pack in check.packs_of(k) for k in check.cards) else (now, None)
        for doc in pq.read_table(raw, columns=replay.COLUMNS).to_pylist():
            doc["pack_id"] = pack
            _, a = replay.trace(dict(doc), now)
            got = out.get(doc["doc_id"])
            n["same" if got == a else "DIFFERENT"] += 1
            _, b = replay.trace(dict(doc), new)
            n["cards: " + ("same" if a == b else "kept" if a is None else "dropped" if b is None else "changed")] += 1
    per[str(rel)] = n
    tot.update(n)
for k, n in per.items():
    if n["DIFFERENT"]:
        print("DIFFERENT", k, dict(n))
print(len(per), "parts;", dict(tot))
sys.exit(1 if tot["DIFFERENT"] else 0)
