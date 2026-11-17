"""Exact-duplicate count over all shards: hash each document's token IDs (EOS included). IDs and counts only."""
import glob, hashlib, json, sys
from collections import defaultdict
import numpy as np
B = sys.argv[1]
seen = defaultdict(list)  # hash -> [(shard, pos)]
tot = 0
for b in sorted(glob.glob(B + "/*.bin")):
    sid = b.split("\\")[-1].split("/")[-1][:-4]
    idx = np.load(b[:-4] + ".idx.npy")
    pay = np.memmap(b, dtype="<u4", mode="r", offset=1024)
    for i in range(len(idx) - 1):
        seen[hashlib.blake2b(pay[idx[i]:idx[i + 1]].tobytes(), digest_size=16).digest()].append((sid, i))
    tot += len(idx) - 1
groups = [v for v in seen.values() if len(v) > 1]
extra = sum(len(v) - 1 for v in groups)
within = sum(1 for v in groups if len({s for s, _ in v}) == 1)
per_pack = defaultdict(int)
for v in groups:
    for s, _ in v[1:]:
        per_pack[s.rsplit("-train-", 1)[0]] += 1
cross_pack = sum(1 for v in groups if len({s.rsplit("-train-", 1)[0] for s, _ in v}) > 1)
out = {"docs": tot, "unique": len(seen), "dup_groups": len(groups), "extra_copies": extra,
       "extra_pct": round(100 * extra / tot, 3), "groups_within_one_shard": within, "groups_across_packs": cross_pack,
       "largest_group": max((len(v) for v in groups), default=0),
       "extra_by_pack": dict(sorted(per_pack.items(), key=lambda x: -x[1]))}
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[2], "w"), indent=1)
