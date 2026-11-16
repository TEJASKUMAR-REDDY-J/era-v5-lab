# Job request: first training shards (every pack: code, code-adjacent, English, Indic, math, science)

Status: **draft**. It is submitted when the gates under "Before submission" are met. Week 3 tasks 4.3, 4.5 and 4.6.

```text
Team:            01-data-a
Owner:           TEJASKUMAR-REDDY-J
Lead approval:   Pending (team lead review of this pull request)
Question:        Do the first training shards (shard format v1, frozen p1536) hold every document the pipeline kept, for every pack and part of the input manifest, with every raw document accounted for from raw to final, and manifests that match their files by count, hash, source, lane and licence?
Script:          teams/01-data-a/pipeline/run_pipeline.py (ledger: pipeline/ledger.py in mode B; shards stage: teams/01-data-a/shards/run_shards.py -> shard_writer.py; reconcile: pipeline/reconcile_shards.py), branch g1-pipeline, commit pinned at submission
Command:         python -I teams/01-data-a/pipeline/run_pipeline.py --config teams/01-data-a/jobs/2026-11-15-first-shards/shards.json
Config:          teams/01-data-a/jobs/2026-11-15-first-shards/shards.json (from shards.template.json, with task 4's run_id, returned folders and raw input folder); pack table: 2026-11-15-first-shards/pack_metadata.json; expected inventory: 2026-11-15-first-shards/expected_inventory.json
Inputs:          TSAI's returned clean, overlap and dedup outputs of the task 4 job; the raw input parts the clean job read (for the raw-to-final ledger); TSAI's frozen p1536 tokenizer.json (sha256 e6b93a93...); no network
Hardware:        CPU; 4 vCPU, 16 GiB RAM (F2: about 1.1 GiB per worker; shard writer: 3.6 GiB peak per part measured); no GPU
Max time:        To be set from task 4's input size; about 10 hours one part at a time for the sample's 48 train parts at the local rates below
Precision:       not used
Measures:        Per part: raw rows, dropped by clean, removed by dedup, dropped by F2, kept (ledger, mode B), rows read by the writer, left out by reason, truncated; per shard: shard_id, pack, lane, licence, docs, tokens, sha256 of .bin/.idx.npy/.docs.parquet/manifest; reconcile status per kept doc; wall time and peak RSS per stage
Expected result: Ledger in mode B: per part, raw = cleaned + dropped by clean, and kept = cleaned - removed by dedup - dropped by F2; no clean_action "unknown". Every train part of expected_inventory.json is written (0 failed, 0 skipped, 0 truncated); every heldout part is not_sharded; no inventory part or pack is missing and no unlisted part appears. Reconcile over the 38 listed packs: kept = in shards + left out by the writer. Every manifest has capability_lane and license. About 48 shards or more (48 train parts, one shard of up to 2^26 tokens per part, more where a part rolls over)
Outputs:         out/pipeline/<run_id>/shards/ (the .bin, .idx.npy and .docs.parquet stay with TSAI); returned to git: shards_summary.json, every <shard_id>.json, .quality_report.json and .dump.md, cleaning_pipeline.json, ledger/ledger_summary.json, reconcile/reconcile_summary.json, pipeline_manifest.json, logs/ (under 50 MB)
Test log:        teams/01-data-a/jobs/2026-11-15-first-shards/local_test/README.md
```

## What the job makes

- **Shard format v1** (`teams/01-data-a/shards/shard_format_v1.md`): one pack and one split per shard; whole documents, never split; each document ends with EOS `<|endoftext|>` 130822; token IDs as little-endian uint32 after a 1,024-byte header; `.idx.npy` holds the document starts. No packing into 4k, 8k or 16k sequences: the sequence length is a training setting.
- **Shard size:** up to 2^26 = 67,108,864 tokens (about 256 MiB per `.bin`). This is a storage size, not a context length; one shard holds about 8,192 sequences of 8k tokens.
- **Shard IDs:** `<pack>-train-<6 digits>`, written by the job into each manifest and `shards_summary.json`. IDs are never assigned by hand.
- **Splits:** only `train/` parts are sharded. `heldout/` parts are reported as `not_sharded` (the sample README: "Do not train on it"; G3 used them to choose and check the tokenizer).
- **Packs:** all 38 packs of the input manifest, 48 train parts, listed in the config (`stages.shards.packs`) from the expected inventory.
- **F2** runs inside this job (`stages.f2`, after apply and before the ledger and shards). TSAI confirmed that no separate F2 job is needed.

## Accounting and coverage

**Raw to final (ledger mode B).** `stages.ledger.raw` is the raw input folder the clean job read. The ledger then joins every raw part to its
cleaned part and gives every document one row from raw to final: `keep`, `fix` or `drop` by clean, removed by dedup, dropped by F2, kept.
Per part, the ledger's drops and rows must equal the cleaning report's, and a raw part whose sha256 is not the one the clean job read stops the run.
Without `raw` the ledger starts at the cleaned documents, `clean_action` is `unknown` and documents dropped by clean are not in it.

**Expected inventory.** [expected_inventory.json](2026-11-15-first-shards/expected_inventory.json) lists every part of the input manifest
(for the sample: the pinned `tokenizer_sample_v0_manifest.json`, sha256 `7fd647c8…`; task 4's approved manifest replaces it) with its raw sha256,
rows and the status its shards must end in: `written` for the 48 train parts, `not_sharded` for the 38 heldout parts. It does not come from
the job's output. Two uses:
- `stages.shards.packs` lists its 38 packs, so reconcile's scope is the expected packs, not the packs found in `shards_summary.json`. A pack whose
  kept documents are in no shard then fails as `missing` instead of passing as `not_selected` (local test below).
- The inventory check (gate 12) compares it with the ledger and `shards_summary.json` and fails on any missing or unlisted part or pack,
  including one that never reached the ledger.

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
  - **All 38 packs filled** from G10's week 3 table: branch `saitej123/era-v5-lab` `g10-week3-post-training` at `fb7d5e6` (16 Nov), Stage 0. On TSAI main (`ae4c03d`) the table has 8 of these rows so far; `license_source` is repinned to TSAI main once G10's table is merged there.
  - A pack with no row keeps `license: null` and `license_source: "pending: …"`, and is not sharded.
- **Admission:** a licence in the manifest records the source's licence when the shard was written. Whether a shard is admitted to training stays TSAI's decision, recorded in the release's `admission.jsonl` (shard format v1, "Dataset level").

## Tokenizer

TSAI's Gate 3 notice of 15 Nov froze **p1536** in place of C3: C3 sample-v0 plus 1,536 Indic merges per script, `tokenizer.json` sha256
`e6b93a93a60520d7b1af2e9242485f443b5596a1e116b8f8798d83bbad25a64b` (G3: `teams/03-tokenizer/train/p1536_s0_manifest.json`, `COMPARE.md`).
Same vocab (131,072), merges (130,460) and special-token ids as C3 (EOS 130822, BOS 130725); code and English encode as with C3, Indic text
encodes differently. The file is not in the repository. Stage it at `teams/03-tokenizer/release/tokenizer.json` from G3's Kaggle dataset
`sohiyiy/p1536-sample-v0` and check its sha256. G9's `decode_shard.py` accepts p1536 in #484. The shard writer still pins C3 (gate 11).

## Local test (real data)

Two `code-go` train parts of tokenizer sample v0 on a Windows laptop: real `clean.py`, real F2 (G9 fingerprints v2, full set), shards with C3 and
with p1536, the ledger in mode B and reconcile. Overlap and dedup were stand-ins in their real formats with nothing removed: `overlap.py` and
`dedup.py` are in TSAI #255 and not yet on `g1-pipeline`. Details and commands: [local_test/README.md](2026-11-15-first-shards/local_test/README.md).

| Stage | In | Out | Time |
|---|---:|---:|---:|
| clean (`clean.py` 22d818c7…) | 83,267 | 76,955 (6,312 dropped, 45,098 fixed), 0 errors | 349 s |
| F2 (`run_f2.py`, set 2826a3b8…) | 76,955 | 76,859 (96 dropped), 0 errors | 951 s |
| ledger, mode B (`--raw` = the raw parts) | 83,267 raw | 76,955 cleaned + 6,312 dropped by clean; 76,859 kept; 0 `unknown` | 10 s |
| shards (C3) | 76,859 | 76,801 docs in 2 shards, 58 left out (secret-like), 0 truncated | 538 s, peak 3.6 GiB |
| shards (p1536, `--any-tokenizer`) | 76,859 | 76,801 docs in 2 shards, 76,954,265 tokens (+1.0% vs C3 on code), 58 left out (secret-like), 0 truncated | 290 s, peak 3.5 GiB |
| G9 `decode_shard.py` (#458) | 2 C3 shards | 2 of 2 pass | 33 s |
| G9 `decode_shard.py` (#484, accepts p1536) | 2 p1536 shards | 2 of 2 pass | 23 s |
| reconcile (C3 and p1536 shards, scope `code-go`) | 76,859 kept | 76,801 in shards + 58 left out, both | seconds |
| reconcile, a pack omitted from the shard output | 76,859 kept | default scope: passes, 76,859 `not_selected`; scope = the listed packs: **fails**, 76,859 `missing` | seconds |

| Shard | Docs | Tokens | `.bin` bytes |
|---|---:|---:|---:|
| `code-go-train-000000` (C3) | 56,588 | 56,111,803 | 224,448,236 |
| `code-go-train-000001` (C3) | 20,213 | 20,048,813 | 80,196,276 |
| `code-go-train-000000` (p1536) | 56,588 | 56,698,571 | 226,795,308 |
| `code-go-train-000001` (p1536) | 20,213 | 20,255,694 | 81,023,800 |

These shards are test evidence (dedup not real), not first training shards. The p1536 shards were written with `--any-tokenizer` (gate 11), so
they are marked `dataset_version` "test". None of them has the `license` field yet (gate 5).

## Before submission

| # | Gate | Owner | State |
|---|---|---|---|
| 1 | **Rollover:** a part over 2^26 tokens goes on into the next shard; `truncated > 0` fails the stage. Today the writer drops the rest of the part. Part `code-go/part-00000` is already 56.1M of 67.1M tokens | Data A shards (4.3) | to do |
| 2 | **Shard IDs with rollover:** a running number per pack and split over the parts in order, and a part-to-shards map in `shards_summary.json`. Today the shard number is the part number | Data A shards (4.3) | to do |
| 3 | **Atomic write and resume:** files written to `.tmp` and renamed, manifest last; a rerun skips shards that verify. Today a rerun into the same folder is refused | Data A shards (4.3) | to do |
| 4 | **Empty parts:** a part with no document left gets its own status, not a failure and not a 0-token shard | Data A shards (4.3) | to do |
| 5 | **Lane and licence in the manifest:** `pack_table.py` takes `license` and `license_source`, and the writer writes both into the manifest next to `capability_lane`; a pack with a `null` lane or licence is refused. Today `pack_table.py` accepts exactly `language`, `script`, `domain`, `lane` (so it refuses this job's table), `shards/pack_table.json` has `lane: null` for the 32 non-code packs, and the manifest has no `license` | Data A shards (4.3) | to do |
| 6 | **Licences from G10's table:** all 38 filled from G10's week 3 branch (`fb7d5e6`); repin `license_source` to TSAI main when G10's table is merged there | G10; Data A shards | 38 of 38 filled, merge pending |
| 7 | **Lane names confirmed:** `code`, `code-adjacent`, `english`, `indic`, `math`, `science` | TSAI, G7 | to confirm |
| 8 | **Held-out:** stays `not_sharded`, or becomes `validation` shards | G3, G9 | to confirm |
| 9 | **Task 4 run:** run_id, returned folders, raw input folder and pins (clean, overlap, dedup), and its approved input manifest, so `shards.json` and `expected_inventory.json` can be filled in | Data A lead (task 4) | open |
| 10 | **Rehearsal (4.5):** a forced multi-shard part and a kill/restart on real stages, with independent checks | Data A pipeline and shards | after 1 to 5, 11, 12 |
| 11 | **p1536 in the writer:** `shard_writer.py` pins p1536's sha256 (`e6b93a93…`) in place of C3's, and G3's `release/` names p1536 (README, `SHA256SUMS`, `verify_release.py`) | Data A shards (4.3); G3 | to do |
| 12 | **Inventory and raw ledger required:** the run takes `expected_inventory.json` and fails when a listed pack or part is missing from the ledger or `shards_summary.json`, has another status than listed, or when an unlisted part appears; a production run without `stages.ledger.raw` is refused | Data A pipeline (with the reconcile owner) | to do |

## After the job

1. The returned shard list is the canonical inventory (task 6.1): shard ID, pack, split, lane, licence, the four sha256, docs, tokens, tokenizer and EOS, lineage, download reference.
2. Rotators (R1) get two shards each from that inventory, across the lanes; task 6 decodes 20 documents of every shard with G9's `decode_shard.py`.
3. G9 scans the returned shards (task 6.3).

## Rules kept

The job reads only its inputs, needs no network and no keys, and writes only under `./out/`. No shard bytes, document text or signed URLs go into git; the returned metadata holds IDs, counts and hashes only.
