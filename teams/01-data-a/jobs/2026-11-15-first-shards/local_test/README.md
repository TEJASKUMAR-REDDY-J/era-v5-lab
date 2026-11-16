# Local test: real code-go parts through clean, F2 and C3 shards (15 Nov)

Code: `g1-pipeline` at `192d8a01e6f434fa07030d27011dbd206f11b74d` (the shard manifests' `created_by`).
Inputs: tokenizer sample v0 (`sample_manifest.json` sha256 `7fd647c8…`), `train/code-go/part-00000.parquet` and `part-00001.parquet`.
Tokenizer: C3 `tokenizer.json`, sha256 `15468e66…02ddc3`. Machine: Windows laptop, Python 3.12.7, pyarrow 21/23, tokenizers 0.20.3.

## Commands

From the repository root. `<run>` is `out/shardjob/sj-real`.

1. Clean, real `clean.py` (`clean_sha256` 22d818c7…), the two parts only:

   ```bash
   python -I teams/01-data-a/pipeline/run_pipeline.py --config <a-clean.json>
   ```
   `a-clean.json`: `"to": "clean"`, `stages.clean` = `{"mode": "run", "settings": "teams/01-data-a/spec_v1/clean.json", "input": <sample>, "manifest_sha256": "7fd647c8…", "expected_parts": {"train": 48, "heldout": 38}, "only": ["train/code-go/part-00000.parquet", "train/code-go/part-00001.parquet"]}`.

2. The pipeline on the cleaned parts: clean adopted; overlap and dedup adopted from stand-ins in their real formats with nothing removed
   (`overlap.py` and `dedup.py` are in TSAI #255, not yet on `g1-pipeline`); apply, F2 (`run_f2.py`, full v2 set), survivor loss and ledger run for real.

3. Shards with the real C3 (the same command the runner's shards stage runs):

   ```bash
   python teams/01-data-a/shards/run_shards.py --input <run>/final --manifest <run>/pipeline_manifest.json --tokenizer <c3>/tokenizer.json --out <run>/shards --pack code-go
   ```
   Run without `-I` here because `tokenizers` was installed in user site-packages on this machine. The runner calls its scripts with `python -I`,
   so the job's environment needs `tokenizers`, `torch`, `numpy` and `pyarrow` installed in the environment itself.

4. Independent checks:

   ```bash
   python teams/09-evaluation/decontam/decode_shard.py <run>/shards --tokenizer <c3>/tokenizer.json --out <dir>
   python -I teams/01-data-a/pipeline/reconcile_shards.py --ledger <run>/ledger --shards <run>/shards --out <run>/reconcile
   ```

## Results

| Stage | In | Out | Time |
|---|---:|---:|---:|
| clean | 83,267 | 76,955: keep 31,857, fix 45,098, drop 6,312; 0 errors | 349 s |
| apply (nothing removed) | 76,955 | 76,955 | 1 s |
| F2 | 76,955 | 76,859: 96 dropped (68 in part-00000, 28 in part-00001); 0 errors | 951 s |
| ledger | 76,955 | kept 76,859, dropped by F2 96 | 2 s |
| shards | 76,859 | 76,801 docs, 76,160,616 tokens, 2 shards; left out 58 secret-like, 0 empty, 0 special, 0 round-trip; 0 truncated | 538 s, peak RSS 3.6 GiB |
| `decode_shard.py` (G9, #458) | 2 shards | decoded 2 of 2: header, index, docs.parquet, manifest hashes, vocab, EOS placement | 33 s |
| reconcile | 76,859 kept | 76,801 in a shard, 58 left out (secret) | seconds |

Rates on one core: F2 about 81 docs/s on code; the shard writer about 143 docs/s, 141K tokens/s.
Part-00000 alone is 56.1M tokens, 84% of the 2^26 limit: a larger part would be cut today (gate 1 in the request).

## Review follow-ups (16 Nov)

**Raw-to-final ledger (mode B).** The same run's ledger, built again with the raw parts:

```bash
python -I teams/01-data-a/pipeline/ledger.py --cleaned <clean> --remove-list <dedup>/remove_list.csv --groups <dedup>/dedup_groups.csv \
    --f2 <run>/final --log <dedup>/dedup_log.jsonl --raw <sample> --out <ledger_B>
```

`clean_mode` B: 83,267 raw rows = 76,955 cleaned + 6,312 dropped by clean; kept 76,859 = 76,955 - 0 removed by dedup - 96 dropped by F2;
45,098 fixed by clean, the cleaning report's count. No `clean_action` is `unknown`. 10 s.

**Reconcile scope.** A copy of the shard folder whose `shards_summary.json` has no `code-go` part, as if the shard stage had left the pack out:

| Scope | Result |
|---|---|
| default (`--pack` not given: the packs in `shards_summary.json`) | passes: 76,859 `not_selected` |
| `--pack code-go` (the listed packs, as `stages.shards.packs` passes them) | fails: "every kept document of a selected pack is in a shard or left out for a stated reason", 76,859 `missing` |

**p1536.** The shard step again on the same final parts with TSAI's frozen p1536 (`e6b93a93…`). `shard_writer.py` still pins C3, so it ran
with `--any-tokenizer` (shards marked `dataset_version` "test"):

```bash
python teams/01-data-a/shards/run_shards.py --input <run>/final --manifest <run>/pipeline_manifest.json --tokenizer <p1536>/tokenizer.json \
    --out <run>/shards_p1536 --pack code-go --any-tokenizer
```

2 shards, 76,801 docs (the same docs as with C3), 76,954,265 tokens: +1.0% on code against C3's 76,160,616, as G3 reports for p1536.
Left out 58 secret-like, 0 truncated; 290 s, peak RSS 3.5 GiB. G9's `decode_shard.py` from #484 (it accepts p1536) decodes 2 of 2 in 23 s, and
reconcile (`--pack code-go`) gives 76,801 in a shard and 58 left out. Their summary, manifests and reconcile summary are in `p1536/`.

## Files here

IDs, counts and hashes only, no document text: `shards_summary.json`, the two shard manifests (`code-go-train-00000N.json`),
their `.dump.md`, `cleaning_pipeline.json` and `reconcile_summary.json`. The `.bin`, `.idx.npy` and `.docs.parquet` stay local.
`cleaning_pipeline.json` records the stand-in dedup (0 rows removed), so these shards are test evidence, not training shards.
