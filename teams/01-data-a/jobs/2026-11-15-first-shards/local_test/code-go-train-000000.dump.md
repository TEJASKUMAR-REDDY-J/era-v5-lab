# Shard `code-go-train-000000`

Written by `shard_writer.py` from `train/code-go/part-00000.parquet`, after `clean.py`, dedup (0 of this part's 56,702 docs removed) and F2 (68 dropped; fingerprints `2826a3b88321`): the first 56,588 docs that fit in 67,108,864 tokens, of 56,634 rows read.

Tokenizer `15468e66457b` (C3, frozen); EOS `<|endoftext|>` id 130822 after each doc; no BOS, no language tag.

Left out: 46 secret-like, 0 empty, 0 with a special id inside, 0 not round-tripping (doc_ids in `code-go-train-000000.quality_report.json`).

| file | bytes | sha256 |
|---|---:|---|
| `code-go-train-000000.bin` | 224,448,236 | `17195ad197018f18…` |
| `code-go-train-000000.idx.npy` | 452,840 | `84a7600ae4a5dcdb…` |
| `code-go-train-000000.docs.parquet` | 1,673,579 | `8f42b2e2915933e4…` |
| `cleaning_pipeline.json` | 772 | `9844819bf4708efe…` |
| `code-go-train-000000.quality_report.json` | 16,842 | `3320e417a63f7bab…` |

## `code-go-train-000000.bin`

- header, 1,024 bytes = 256 little-endian int32: `20261025` (magic), `2` (version), `56,111,803` (token count), then zeros
- then 56,111,803 little-endian uint32 token IDs; every doc ends with 130822, and no other special id occurs
- tokens per character: median 0.286, max 2.072

## `code-go-train-000000.idx.npy`

int64, 56,589 entries (start of each doc, then token_count): `[0, 277, 740, 1093, 2706] … [56109693, 56111803]`

## `code-go-train-000000.docs.parquet`

One row per doc in shard order, IDs and counts only. First rows:

| doc_id | input_part | input_row | n_tokens | n_chars | lang_label |
|---|---|---:|---:|---:|---|
| `fc4480874e37f39a` | `train/code-go/part-00000.parquet` | 0 | 277 | 822 | code |
| `0a75201e65a3b0fe` | `train/code-go/part-00000.parquet` | 1 | 463 | 1,154 | code |
| `baf24c8ead388f0e` | `train/code-go/part-00000.parquet` | 2 | 353 | 1,404 | code |
| `8aa4a8a561c78f97` | `train/code-go/part-00000.parquet` | 3 | 1,613 | 5,506 | code |
| `4f31218c22e083ae` | `train/code-go/part-00000.parquet` | 4 | 137 | 521 | code |
