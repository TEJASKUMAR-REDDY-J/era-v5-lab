"""Build shard_check.md from the per-shard *.checks.json written by shard_check.py."""
import json
import sys
from collections import defaultdict
from pathlib import Path

d = Path(sys.argv[1])
run = json.loads((d / "run.json").read_text(encoding="utf-8"))
shards = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(d.glob("*.checks.json"))]

by_pack = defaultdict(list)
for s in shards:
    by_pack[s["manifest"]["pack_id"]].append(s)
overlap = {p: ss for p, ss in by_pack.items()
           if len({part for s in ss for part in s["input_parts"]}) != sum(len(s["input_parts"]) for s in ss)}

fails = defaultdict(list)
for s in shards:
    for r in s["checks"]:
        if r["status"] != "PASS":
            fails[r["check"]].append(s["shard_id"])

tot_docs = sum(s["quality_counts"]["docs_in_shard"] for s in shards)
tot_tok = sum(s["manifest"]["token_count"] for s in shards)
dec = [x for s in shards for x in s["decoded_documents"]]
L = []
L.append("# Data A shard check (task 6)\n")
L.append(f"Checked against repository commit `{run['repository_commit']}`. Bundle: TSAI **p1536 tokenizer sample-v0**, "
         f"{len(shards)} shards in {len(by_pack)} packs. **These are sample-v0 shards**: integrity evidence, not training admission or G9 clearance.\n")
L.append(f"Checker `check_shard.py` (#482) SHA-256 `{run['checker_sha256']}`; tokenizer p1536 `{run['tokenizer_sha256']}` "
         f"({run['special_token_count']} special IDs). Environment: " + ", ".join(f"{k} {v}" for k, v in run["environment"].items()) + ".\n")
L.append("## Result\n")
L.append(f"- {len(shards)} shards, {tot_docs:,} documents, {tot_tok:,} tokens (EOS included).")
L.append(f"- Decode: {len(dec)} documents ({len(shards)} x 20). End with EOS {sum(x['ends_with_eos'] for x in dec)}/{len(dec)}; "
         f"U+FFFD {sum(x['replacement_chars'] for x in dec)}; re-encode identical {sum(x['reencode_matches'] for x in dec)}/{len(dec)}; "
         f"decoded length = `n_chars` {sum(x['decoded_chars'] == x['n_chars'] for x in dec)}/{len(dec)}.")
L.append(f"- Source parts overlapping between shards of one pack: {', '.join(overlap) if overlap else 'none'}.")
if fails:
    for c, ids in fails.items():
        note = " (issue #503)" if "dedup" in c.lower() else (
            " (not a defect: `n_chars` is the cleaned-text length before p1536 normalization; all these docs re-encode to identical IDs, "
            "0 U+FFFD; 35/41 equal normalizer(raw sample) exactly, 6 differ only by clean.py edits; see `shard_check/n_chars_mismatch_explained.json`)"
            if "n_chars" in c else "")
        L.append(f"- FAIL `{c}`{note}: {len(ids)}/{len(shards)} shards" + ("" if len(ids) == len(shards) else ": " + ", ".join(ids)))
else:
    L.append("- No failed checks.")
L.append("")
L.append("## Per shard\n")
L.append("| Shard | Docs | Tokens | Source part | Rows read / kept / left out | `.bin` SHA-256 (manifest match) | Checks | Decode 20 | Failed |")
L.append("|---|---:|---:|---|---|---|---|---|---|")
for s in shards:
    m, q, c, dd = s["manifest"], s["quality_counts"], s["counts"], s["decoded_documents"]
    ok = all(x["ends_with_eos"] and x["replacement_chars"] == 0 and x["reencode_matches"]
             and x["decoded_chars"] == x["n_chars"] for x in dd)
    binok = s["artifact_sha256"][s["shard_id"] + ".bin"] == m["payload_sha256"]
    L.append(f"| `{s['shard_id']}` | {q['docs_in_shard']:,} | {m['token_count']:,} | {', '.join(s['input_parts'])} | "
             f"{q['rows_read']:,} / {q['docs_in_shard']:,} / {sum(q['left_out'].values()):,} | "
             f"`{s['artifact_sha256'][s['shard_id'] + '.bin'][:16]}…` ({'yes' if binok else 'see JSON'}) | "
             f"{c['PASS']} P / {c['FAIL']} F / {c['NOT CHECKED']} NC | {'PASS' if ok else 'FAIL'} ({len(dd)}) | "
             + ("; ".join(f"{r['check']} ({'#503' if 'dedup' in r['check'] else 'n_chars ' + r['observed'] + '/20 match, normalization' if 'n_chars' in r['check'] else r['observed']})"
                          for r in s["checks"] if r["status"] != "PASS") or "none") + " |")
L.append("")
L.append("Per-shard evidence (every check with expected/observed, all artifact hashes, decoded-document positions, IDs, counts and "
         "SHA-256 of decoded text, never text): `shard_check/<shard>.checks.json`. Reproduce with `shard_check/shard_check.py` (the checker `teams/01-data-a/audit/check_shard.py` is on TSAI main, #482).\n")
dv = json.loads((d / "dedup_vs_shards.json").read_text(encoding="utf-8"))
ex = json.loads((d / "exact_dups.json").read_text(encoding="utf-8"))
L.append("## Dedup\n")
L.append(f"`dedup: null` (#503): this bundle was written before dedup v1 ran. The dedup job (#255, results #547, 17 Nov) removes "
         f"{dv['remove_list']:,} documents; {dv['removed_docs_whose_part_is_in_the_41_shards']} of them are in parts these shards hold, and all "
         f"{dv['removed_docs_present_in_shards']} are still in the shards (largest: "
         + ", ".join(f"{k} {v}" for k, v in list(dv["present_by_pack"].items())[:4]) + "). Exact duplicates by token IDs across all shards: "
         f"{ex['extra_copies']} extra copies in {ex['docs']:,} documents ({ex['dup_groups']} groups, none across packs). The first training "
         "shards need to be written from the deduplicated parts and record the dedup version. Evidence: `shard_check/dedup_vs_shards.json`, "
         "`shard_check/exact_dups.json` (`shard_check/dupcheck.py`; `remove_list.csv` from `teams/01-data-a/jobs/results/2026-11-14-dedup/` "
         "on TSAI main).\n")
L.append("## Coverage\n")
L.append("Byte-level checks cover every document of every shard (token range, specials, EOS, index/metadata agreement, hashes vs manifest). "
         "Decode covers 20 evenly spread documents per shard, first and last included, checked for round-trip consistency, not read for "
         "cleaning quality. Original cleaned parts and F2 payload were not re-scanned; provenance references were checked for consistency.")
(d.parent / "shard_check.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("wrote", d.parent / "shard_check.md")
