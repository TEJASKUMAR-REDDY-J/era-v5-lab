# Shard `code-go-train-000001`

Written by `shard_writer.py` from `train/code-go/part-00001.parquet`, after `clean.py`, dedup (0 of this part's 20,253 docs removed) and F2 (28 dropped; fingerprints `2826a3b88321`): the first 20,213 docs that fit in 67,108,864 tokens, of 20,225 rows read.

Tokenizer `15468e66457b` (C3, frozen); EOS `<|endoftext|>` id 130822 after each doc; no BOS, no language tag.

Left out: 12 secret-like, 0 empty, 0 with a special id inside, 0 not round-tripping (doc_ids in `code-go-train-000001.quality_report.json`).

| file | bytes | sha256 |
|---|---:|---|
| `code-go-train-000001.bin` | 80,196,276 | `128d9d89112f05c7…` |
| `code-go-train-000001.idx.npy` | 161,840 | `ecf1ef610b3c4c4f…` |
| `code-go-train-000001.docs.parquet` | 611,300 | `d8022e1ebdfc75ec…` |
| `cleaning_pipeline.json` | 772 | `9844819bf4708efe…` |
| `code-go-train-000001.quality_report.json` | 8,027 | `b9d9fb8b476b5889…` |

## `code-go-train-000001.bin`

- header, 1,024 bytes = 256 little-endian int32: `20261025` (magic), `2` (version), `20,048,813` (token count), then zeros
- then 20,048,813 little-endian uint32 token IDs; every doc ends with 130822, and no other special id occurs
- tokens per character: median 0.285, max 0.953

## `code-go-train-000001.idx.npy`

int64, 20,214 entries (start of each doc, then token_count): `[0, 323, 470, 820, 1203] … [20046171, 20048813]`

## `code-go-train-000001.docs.parquet`

One row per doc in shard order, IDs and counts only. First rows:

| doc_id | input_part | input_row | n_tokens | n_chars | lang_label |
|---|---|---:|---:|---:|---|
| `bca061a4cf90b329` | `train/code-go/part-00001.parquet` | 0 | 323 | 1,203 | code |
| `009e279dfca8ad00` | `train/code-go/part-00001.parquet` | 1 | 147 | 477 | code |
| `ded7462c63ff1929` | `train/code-go/part-00001.parquet` | 2 | 350 | 1,012 | code |
| `1922dd43189cde78` | `train/code-go/part-00001.parquet` | 3 | 383 | 1,276 | code |
| `edc27d46452dd366` | `train/code-go/part-00001.parquet` | 4 | 431 | 1,565 | code |
