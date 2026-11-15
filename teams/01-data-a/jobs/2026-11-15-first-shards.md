# Job request: first training shards (code, math, science, English)

Status: **draft**. It is submitted when the gates under "Before submission" are met. Week 3 tasks 4.3, 4.5 and 4.6.

```text
Team:            01-data-a
Owner:           TEJASKUMAR-REDDY-J
Lead approval:   Pending (team lead review of this pull request)
Question:        Do the first training shards (shard format v1, frozen C3) hold every document the pipeline kept for the code, math, science and English packs, with manifests that match their files by count, hash and source?
Script:          teams/01-data-a/pipeline/run_pipeline.py (shards stage: teams/01-data-a/shards/run_shards.py -> shard_writer.py; reconcile: pipeline/reconcile_shards.py), branch g1-pipeline, commit pinned at submission
Command:         python -I teams/01-data-a/pipeline/run_pipeline.py --config teams/01-data-a/jobs/2026-11-15-first-shards/shards.json
Config:          teams/01-data-a/jobs/2026-11-15-first-shards/shards.json (from shards.template.json, with task 4's run_id and returned folders)
Inputs:          TSAI's returned clean, overlap and dedup outputs of the task 4 job; G3's frozen C3 tokenizer.json (sha256 15468e66...); no network
Hardware:        CPU; 4 vCPU, 16 GiB RAM (F2: about 1.1 GiB per worker; shard writer: 3.6 GiB peak per part measured); no GPU
Max time:        To be set from task 4's input size (local rates below); about 6 hours for the 23 train parts of the sample at the measured rates
Precision:       not used
Measures:        Per shard: shard_id, docs, tokens, sha256 of .bin/.idx.npy/.docs.parquet/manifest; per part: rows in part, rows read, left out by reason, truncated; reconcile status per kept doc; wall time and peak RSS per stage
Expected result: Every train part of the 13 packs is written, 0 failed, 0 skipped, 0 truncated; held-out parts are not_sharded; reconcile: kept = in shards + left out by the writer; about 20 to 30 shards (23 train parts in the sample, one shard of up to 2^26 tokens per part)
Outputs:         out/pipeline/<run_id>/shards/ (the .bin, .idx.npy and .docs.parquet stay with TSAI); returned to git: shards_summary.json, every <shard_id>.json, .quality_report.json and .dump.md, cleaning_pipeline.json, reconcile/reconcile_summary.json, pipeline_manifest.json, logs/ (under 50 MB)
Test log:        teams/01-data-a/jobs/2026-11-15-first-shards/local_test/README.md
```

## What the job makes

- **Shard format v1** (`teams/01-data-a/shards/shard_format_v1.md`): one pack and one split per shard; whole documents, never split; each document ends with EOS `<|endoftext|>` 130822; token IDs as little-endian uint32 after a 1,024-byte header; `.idx.npy` holds the document starts. No packing into 4k, 8k or 16k sequences: the sequence length is a training setting.
- **Shard size:** up to 2^26 = 67,108,864 tokens (about 256 MiB per `.bin`). This is a storage size, not a context length; one shard holds about 8,192 sequences of 8k tokens.
- **Shard IDs:** `<pack>-train-<6 digits>`, written by the job into each manifest and `shards_summary.json`. IDs are never assigned by hand.
- **Splits:** only `train/` parts are sharded. `heldout/` parts are reported as `not_sharded` (the sample README: "Do not train on it"; G3 used them to choose and check C3).
- **Lanes:** code (`code-*`), math (`math-*`), science (`sci-finepdfs`), English (`en-*`). The `cadj-*` packs are left out until their lane is decided.

## Tokenizer

G3's frozen C3 sample-v0, `tokenizer.json` sha256 `15468e66457b43af79f695cbe585c0d03e3cfe7a4a5d04d189dd3c6b9f02ddc3`
(`teams/03-tokenizer/release/README.md`, `release/SHA256SUMS`). The file is not in the repository (8 MB, over the pr-guard limit).
Stage it at `teams/03-tokenizer/release/tokenizer.json` from G3's release (Kaggle dataset `sohiyiy/c3-sample-v0`) and check it with
`python teams/03-tokenizer/release/verify_release.py teams/03-tokenizer/release/tokenizer.json`. The shard writer refuses any file with another sha256.

## Local test (real data)

Two `code-go` train parts of tokenizer sample v0 on a Windows laptop: real `clean.py`, real F2 (G9 fingerprints v2, full set), real C3 shards.
Overlap and dedup were stand-ins in their real formats with nothing removed: `overlap.py` and `dedup.py` are in TSAI #255 and not yet on `g1-pipeline`.
Details and commands: [local_test/README.md](2026-11-15-first-shards/local_test/README.md).

| Stage | In | Out | Time |
|---|---:|---:|---:|
| clean (`clean.py` 22d818c7…) | 83,267 | 76,955 (6,312 dropped, 45,098 fixed), 0 errors | 349 s |
| F2 (`run_f2.py`, set 2826a3b8…) | 76,955 | 76,859 (96 dropped), 0 errors | 951 s |
| shards (C3) | 76,859 | 76,801 docs in 2 shards, 58 left out (secret-like), 0 truncated | 538 s, peak 3.6 GiB |
| G9 `decode_shard.py` (#458) | 2 shards | 2 of 2 pass | 33 s |
| reconcile | 76,859 kept | 76,801 in shards + 58 left out | seconds |

| Shard | Docs | Tokens | `.bin` bytes |
|---|---:|---:|---:|
| `code-go-train-000000` | 56,588 | 56,111,803 | 224,448,236 |
| `code-go-train-000001` | 20,213 | 20,048,813 | 80,196,276 |

These two shards are test evidence (`dataset_version` "sample", dedup not real), not first training shards.

## Before submission

| # | Gate | Owner | State |
|---|---|---|---|
| 1 | **Rollover:** a part over 2^26 tokens goes on into the next shard; `truncated > 0` fails the stage. Today the writer drops the rest of the part. Part `code-go/part-00000` is already 56.1M of 67.1M tokens | Data A shards (4.3) | to do |
| 2 | **Shard IDs with rollover:** a running number per pack and split over the parts in order, and a part-to-shards map in `shards_summary.json`. Today the shard number is the part number | Data A shards (4.3) | to do |
| 3 | **Atomic write and resume:** files written to `.tmp` and renamed, manifest last; a rerun skips shards that verify. Today a rerun into the same folder is refused | Data A shards (4.3) | to do |
| 4 | **Empty parts:** a part with no document left gets its own status, not a failure and not a 0-token shard | Data A shards (4.3) | to do |
| 5 | **Lanes:** `pack_table.json` has `lane: null` for every non-code pack, so the stage skips math, science and English. Lane names to confirm: `code`, `math`, `science`, `english` | Data A shards, with TSAI / G7 | to confirm |
| 6 | **Licence and admission:** the format keeps licence out of the manifest, in a release-level `admission.jsonl` (append-only). Nothing writes it yet. G10's licence table (Stage 0) lists 3 of these 13 packs | Data A shards; G10 rows; TSAI admits | to do |
| 7 | **Held-out:** stays `not_sharded`, or becomes `validation` shards | G3, G9 | to confirm |
| 8 | **Task 4 run:** run_id, returned folders and pins (clean, overlap, dedup), so `shards.json` can be filled in | Data A lead (task 4) | open |
| 9 | **Rehearsal (4.5):** a forced multi-shard part and a kill/restart on real stages, with independent checks | Data A pipeline and shards | after 1 to 4 |

## After the job

1. The returned shard list is the canonical inventory (task 6.1): shard ID, pack, split, the four sha256, docs, tokens, C3 and EOS, lineage, download reference.
2. Rotators (R1) get two shards each from that inventory, across the four lanes; task 6 decodes 20 documents of every shard with G9's `decode_shard.py`.
3. G9 scans the returned shards (task 6.3).

## Rules kept

The job reads only its inputs, needs no network and no keys, and writes only under `./out/`. No shard bytes, document text or signed URLs go into git; the returned metadata holds IDs, counts and hashes only.
