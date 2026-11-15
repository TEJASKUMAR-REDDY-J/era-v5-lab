# Job request: first training shards (every pack: code, code-adjacent, English, Indic, math, science)

Status: **draft**. It is submitted when the gates under "Before submission" are met. Week 3 tasks 4.3, 4.5 and 4.6.

```text
Team:            01-data-a
Owner:           TEJASKUMAR-REDDY-J
Lead approval:   Pending (team lead review of this pull request)
Question:        Do the first training shards (shard format v1, frozen C3) hold every document the pipeline kept, for every pack, with manifests that match their files by count, hash, source, lane and licence?
Script:          teams/01-data-a/pipeline/run_pipeline.py (shards stage: teams/01-data-a/shards/run_shards.py -> shard_writer.py; reconcile: pipeline/reconcile_shards.py), branch g1-pipeline, commit pinned at submission
Command:         python -I teams/01-data-a/pipeline/run_pipeline.py --config teams/01-data-a/jobs/2026-11-15-first-shards/shards.json
Config:          teams/01-data-a/jobs/2026-11-15-first-shards/shards.json (from shards.template.json, with task 4's run_id and returned folders); pack table: 2026-11-15-first-shards/pack_metadata.json
Inputs:          TSAI's returned clean, overlap and dedup outputs of the task 4 job; G3's frozen C3 tokenizer.json (sha256 15468e66...); no network
Hardware:        CPU; 4 vCPU, 16 GiB RAM (F2: about 1.1 GiB per worker; shard writer: 3.6 GiB peak per part measured); no GPU
Max time:        To be set from task 4's input size; about 10 hours one part at a time for the sample's 48 train parts at the local rates below
Precision:       not used
Measures:        Per shard: shard_id, pack, lane, licence, docs, tokens, sha256 of .bin/.idx.npy/.docs.parquet/manifest; per part: rows in part, rows read, left out by reason, truncated; reconcile status per kept doc; wall time and peak RSS per stage
Expected result: Every train part of all 38 packs is written: 0 failed, 0 skipped, 0 truncated; held-out parts are not_sharded; every manifest has capability_lane and license; reconcile: kept = in shards + left out by the writer; about 48 shards or more (48 train parts in the sample, one shard of up to 2^26 tokens per part, more where a part rolls over)
Outputs:         out/pipeline/<run_id>/shards/ (the .bin, .idx.npy and .docs.parquet stay with TSAI); returned to git: shards_summary.json, every <shard_id>.json, .quality_report.json and .dump.md, cleaning_pipeline.json, reconcile/reconcile_summary.json, pipeline_manifest.json, logs/ (under 50 MB)
Test log:        teams/01-data-a/jobs/2026-11-15-first-shards/local_test/README.md
```

## What the job makes

- **Shard format v1** (`teams/01-data-a/shards/shard_format_v1.md`): one pack and one split per shard; whole documents, never split; each document ends with EOS `<|endoftext|>` 130822; token IDs as little-endian uint32 after a 1,024-byte header; `.idx.npy` holds the document starts. No packing into 4k, 8k or 16k sequences: the sequence length is a training setting.
- **Shard size:** up to 2^26 = 67,108,864 tokens (about 256 MiB per `.bin`). This is a storage size, not a context length; one shard holds about 8,192 sequences of 8k tokens.
- **Shard IDs:** `<pack>-train-<6 digits>`, written by the job into each manifest and `shards_summary.json`. IDs are never assigned by hand.
- **Splits:** only `train/` parts are sharded. `heldout/` parts are reported as `not_sharded` (the sample README: "Do not train on it"; G3 used them to choose and check C3).
- **Packs:** all 38 packs of the sample, 48 train parts. No `packs` filter in the config.

## Lane and licence in every manifest

Each shard manifest carries `capability_lane` and `license`, taken from the pack's `lane` and `license` in [pack_metadata.json](2026-11-15-first-shards/pack_metadata.json) (the job's `pack_table`; `language`, `script` and `domain` are those of `shards/pack_table.json`).

| Lane (`capability_lane`) | Packs |
|---|---|
| `code` | `code-cpp`, `code-go`, `code-java`, `code-js-ts`, `code-python`, `code-rust` |
| `code-adjacent` | `cadj-commits`, `cadj-notebooks`, `cadj-stackexchange` |
| `english` | `en-dclm`, `en-fineweb-edu`, `en-nemotroncc`, `en-nemotroncc-synth` |
| `indic` | the 22 `ind-*` packs |
| `math` | `math-finemath`, `math-megamath` |
| `science` | `sci-finepdfs` |

- **Licence:** every manifest gets `license` and `license_source`, for traceability. `license` is G10's licence text for the pack, copied word for word from G10's licence table (`teams/10-post-training/licences/licence_table.md`, Stage 0: foundation data), the only source for it; `license_source` names that file and the commit it was read from.
  - **Filled (8 packs, TSAI main `ae4c03d`):** `code-python`, `code-go`, `code-js-ts`, `ind-mr-fw2`, `ind-kn-fw2`, `ind-ta-sangraha-v`, `ind-hi-hplt`, `ind-hi-indiccorp`.
  - **Pending (30 packs):** no row in G10's table yet. They keep `license: null` and `license_source: "pending: …"`, and are not sharded until G10 adds their rows.
- **Admission:** a licence in the manifest records the source's licence when the shard was written. Whether a shard is admitted to training stays TSAI's decision, recorded in the release's `admission.jsonl` (shard format v1, "Dataset level").

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

These two shards are test evidence (`dataset_version` "sample", dedup not real), not first training shards. They were written before
the `license` field: their manifests have `capability_lane` but no `license`.

## Before submission

| # | Gate | Owner | State |
|---|---|---|---|
| 1 | **Rollover:** a part over 2^26 tokens goes on into the next shard; `truncated > 0` fails the stage. Today the writer drops the rest of the part. Part `code-go/part-00000` is already 56.1M of 67.1M tokens | Data A shards (4.3) | to do |
| 2 | **Shard IDs with rollover:** a running number per pack and split over the parts in order, and a part-to-shards map in `shards_summary.json`. Today the shard number is the part number | Data A shards (4.3) | to do |
| 3 | **Atomic write and resume:** files written to `.tmp` and renamed, manifest last; a rerun skips shards that verify. Today a rerun into the same folder is refused | Data A shards (4.3) | to do |
| 4 | **Empty parts:** a part with no document left gets its own status, not a failure and not a 0-token shard | Data A shards (4.3) | to do |
| 5 | **Lane and licence in the manifest:** `pack_table.py` takes `license` and `license_source`, and the writer writes both into the manifest next to `capability_lane`; a pack with a `null` lane or licence is refused. Today `pack_table.py` accepts exactly `language`, `script`, `domain`, `lane` (so it refuses this job's table), `shards/pack_table.json` has `lane: null` for the 32 non-code packs, and the manifest has no `license` | Data A shards (4.3) | to do |
| 6 | **Licences from G10's table** for the 30 packs with no row yet: `code-cpp`, `code-java`, `code-rust`, the 3 `cadj-*`, the 4 `en-*`, the 2 `math-*`, `sci-finepdfs` and 17 `ind-*` packs | G10 | 8 of 38 filled |
| 7 | **Lane names confirmed:** `code`, `code-adjacent`, `english`, `indic`, `math`, `science` | TSAI, G7 | to confirm |
| 8 | **Held-out:** stays `not_sharded`, or becomes `validation` shards | G3, G9 | to confirm |
| 9 | **Task 4 run:** run_id, returned folders and pins (clean, overlap, dedup), so `shards.json` can be filled in | Data A lead (task 4) | open |
| 10 | **Rehearsal (4.5):** a forced multi-shard part and a kill/restart on real stages, with independent checks | Data A pipeline and shards | after 1 to 5 |

## After the job

1. The returned shard list is the canonical inventory (task 6.1): shard ID, pack, split, lane, licence, the four sha256, docs, tokens, C3 and EOS, lineage, download reference.
2. Rotators (R1) get two shards each from that inventory, across the lanes; task 6 decodes 20 documents of every shard with G9's `decode_shard.py`.
3. G9 scans the returned shards (task 6.3).

## Rules kept

The job reads only its inputs, needs no network and no keys, and writes only under `./out/`. No shard bytes, document text or signed URLs go into git; the returned metadata holds IDs, counts and hashes only.
