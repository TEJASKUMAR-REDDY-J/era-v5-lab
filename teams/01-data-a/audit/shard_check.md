# Data A shard check (task 6)

Checked against repository commit `0ebfb8d74c23814a5f871e35adf935b0c3b04dd9`. Bundle: TSAI **p1536 tokenizer sample-v0**, 41 shards in 31 packs. **These are sample-v0 shards**: integrity evidence, not training admission or G9 clearance.

Checker `check_shard.py` (#482) SHA-256 `196c20ff70f7bdd6551a4a54dd3df1d6c5647e4d510a32276cd64bae24f6f007`; tokenizer p1536 `e6b93a93a60520d7b1af2e9242485f443b5596a1e116b8f8798d83bbad25a64b` (356 special IDs). Environment: python 3.12.7, numpy 1.26.4, pyarrow 21.0.0, tokenizers 0.20.3.

## Result

- 41 shards, 1,200,725 documents, 1,009,387,985 tokens (EOS included).
- Decode: 820 documents (41 x 20). End with EOS 820/820; U+FFFD 0; re-encode identical 820/820; decoded length = `n_chars` 779/820.
- Source parts overlapping between shards of one pack: none.
- FAIL `cleaning_pipeline records a dedup version` (issue #503): 41/41 shards
- FAIL `decode: decoded length equals metadata n_chars` (not a defect: `n_chars` is the cleaned-text length before p1536 normalization; all these docs re-encode to identical IDs, 0 U+FFFD; 35/41 equal normalizer(raw sample) exactly, 6 differ only by clean.py edits; see `shard_check/n_chars_mismatch_explained.json`): 3/41 shards: ind-bn-fw2-train-000000, ind-bn-sangraha-v-train-000000, ind-hi-indiccorp-train-000000

## Per shard

| Shard | Docs | Tokens | Source part | Rows read / kept / left out | `.bin` SHA-256 (manifest match) | Checks | Decode 20 | Failed |
|---|---:|---:|---|---|---|---|---|---|
| `code-cpp-train-000000` | 40,355 | 66,915,318 | code-cpp_part-00000_clean.parquet | 40,363 / 40,355 / 8 | `511b3e97a96627c2…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-cpp-train-000001` | 14,145 | 23,634,925 | code-cpp_part-00001_clean.parquet | 14,148 / 14,145 / 3 | `161b269499bf8138…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-go-train-000000` | 56,588 | 56,698,571 | code-go_part-00000_clean.parquet | 56,634 / 56,588 / 46 | `b68bf390d5800853…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-go-train-000001` | 20,213 | 20,255,694 | code-go_part-00001_clean.parquet | 20,225 / 20,213 / 12 | `36430989fd7f5caf…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-java-train-000000` | 62,421 | 56,003,499 | code-java_part-00000_clean.parquet | 62,430 / 62,421 / 9 | `d885478b8a77ebfe…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-java-train-000001` | 22,228 | 19,878,065 | code-java_part-00001_clean.parquet | 22,232 / 22,228 / 4 | `c8e3aca96a7f6c16…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-js-ts-train-000000` | 85,508 | 58,203,242 | code-js-ts_part-00000_clean.parquet | 85,538 / 85,508 / 30 | `61d72a9aa9c8078e…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-js-ts-train-000001` | 30,441 | 20,653,602 | code-js-ts_part-00001_clean.parquet | 30,449 / 30,441 / 8 | `62e7aa3793863ace…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-python-train-000000` | 53,221 | 60,537,332 | code-python_part-00000_clean.parquet | 53,259 / 53,221 / 38 | `bf6c275f296566cb…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-python-train-000001` | 19,116 | 21,509,045 | code-python_part-00001_clean.parquet | 19,125 / 19,116 / 9 | `537723be5641f3ae…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-rust-train-000000` | 43,116 | 59,530,999 | code-rust_part-00000_clean.parquet | 43,132 / 43,116 / 16 | `9468c56cccae9055…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `code-rust-train-000001` | 15,028 | 21,040,035 | code-rust_part-00001_clean.parquet | 15,032 / 15,028 / 4 | `b747ac07155d28fb…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-dclm-train-000000` | 45,032 | 53,960,422 | en-dclm_part-00000_clean.parquet | 45,336 / 45,032 / 304 | `1fccdcc4c15bb22e…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-dclm-train-000001` | 14,735 | 17,781,210 | en-dclm_part-00001_clean.parquet | 14,839 / 14,735 / 104 | `2b6e1f71836f0824…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-fineweb-edu-train-000000` | 53,444 | 52,995,687 | en-fineweb-edu_part-00000_clean.parquet | 53,538 / 53,444 / 94 | `6625fc47c89e34bf…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-fineweb-edu-train-000001` | 17,725 | 17,662,417 | en-fineweb-edu_part-00001_clean.parquet | 17,752 / 17,725 / 27 | `f1b97344614f7f54…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-nemotroncc-synth-train-000000` | 146,778 | 50,712,366 | en-nemotroncc-synth_part-00000_clean.parquet | 147,566 / 146,778 / 788 | `2be6f68c01d036a9…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-nemotroncc-synth-train-000001` | 49,008 | 16,961,507 | en-nemotroncc-synth_part-00001_clean.parquet | 49,298 / 49,008 / 290 | `2d041dc03bfbaabb…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-nemotroncc-train-000000` | 65,284 | 50,343,044 | en-nemotroncc_part-00000_clean.parquet | 66,048 / 65,284 / 764 | `3b64c48e320d38c5…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `en-nemotroncc-train-000001` | 21,912 | 16,778,602 | en-nemotroncc_part-00001_clean.parquet | 22,177 / 21,912 / 265 | `a7b14cbbbfc45f81…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-bn-fw2-train-000000` | 10,704 | 7,127,920 | ind-bn-fw2_part-00000_clean.parquet | 10,704 / 10,704 / 0 | `ecf0822aca757724…` (yes) | 56 P / 2 F / 0 NC | FAIL (20) | cleaning_pipeline records a dedup version (#503); decode: decoded length equals metadata n_chars (n_chars 0/20 match, normalization) |
| `ind-bn-sangraha-v-train-000000` | 10,112 | 8,014,810 | ind-bn-sangraha-v_part-00000_clean.parquet | 10,116 / 10,112 / 4 | `dec1b695aca02613…` (yes) | 56 P / 2 F / 0 NC | FAIL (20) | cleaning_pipeline records a dedup version (#503); decode: decoded length equals metadata n_chars (n_chars 0/20 match, normalization) |
| `ind-gu-fw2-train-000000` | 22,689 | 16,066,252 | ind-gu-fw2_part-00000_clean.parquet | 22,689 / 22,689 / 0 | `d10b573a08bcecf7…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-hi-fw2-train-000000` | 13,773 | 8,988,818 | ind-hi-fw2_part-00000_clean.parquet | 13,773 / 13,773 / 0 | `e64b18601f2ffc82…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-hi-hplt-train-000000` | 8,386 | 8,090,716 | ind-hi-hplt_part-00000_clean.parquet | 8,418 / 8,386 / 32 | `e7e357d21beceaca…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-hi-indiccorp-train-000000` | 109,668 | 9,343,359 | ind-hi-indiccorp_part-00000_clean.parquet | 109,674 / 109,668 / 6 | `6be0f58e567a0f8a…` (yes) | 56 P / 2 F / 0 NC | FAIL (20) | cleaning_pipeline records a dedup version (#503); decode: decoded length equals metadata n_chars (n_chars 19/20 match, normalization) |
| `ind-hi-sangraha-s-train-000000` | 7,467 | 5,988,971 | ind-hi-sangraha-s_part-00000_clean.parquet | 7,467 / 7,467 / 0 | `4b92b39b42756680…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-hi-sangraha-v-train-000000` | 14,483 | 9,254,413 | ind-hi-sangraha-v_part-00000_clean.parquet | 14,489 / 14,483 / 6 | `78aca29173b76840…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-kn-fw2-train-000000` | 7,735 | 4,737,714 | ind-kn-fw2_part-00000_clean.parquet | 7,735 / 7,735 / 0 | `7224b101435879f7…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-kn-sangraha-s-train-000000` | 5,185 | 5,217,346 | ind-kn-sangraha-s_part-00000_clean.parquet | 5,185 / 5,185 / 0 | `41fe68ef433fe861…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-kn-sangraha-v-train-000000` | 8,354 | 4,761,130 | ind-kn-sangraha-v_part-00000_clean.parquet | 8,357 / 8,354 / 3 | `8d978e3e1929ceb9…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-mr-fw2-train-000000` | 11,250 | 7,146,419 | ind-mr-fw2_part-00000_clean.parquet | 11,250 / 11,250 / 0 | `c6aa0cf3adb8e3f0…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-mr-sangraha-v-train-000000` | 12,164 | 7,259,040 | ind-mr-sangraha-v_part-00000_clean.parquet | 12,171 / 12,164 / 7 | `043e1ff61f9f7db2…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-sa-fw2-train-000000` | 5,667 | 13,940,676 | ind-sa-fw2_part-00000_clean.parquet | 5,667 / 5,667 / 0 | `a6d8546c5f48e7e1…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-ta-sangraha-v-train-000000` | 6,795 | 4,497,005 | ind-ta-sangraha-v_part-00000_clean.parquet | 6,796 / 6,795 / 1 | `418b46986e796f80…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-te-fw2-train-000000` | 5,670 | 4,758,086 | ind-te-fw2_part-00000_clean.parquet | 5,670 / 5,670 / 0 | `5a70a65df7d07063…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-te-sangraha-s-train-000000` | 4,419 | 4,781,160 | ind-te-sangraha-s_part-00000_clean.parquet | 4,419 / 4,419 / 0 | `fbc93236d63888dd…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `ind-te-sangraha-v-train-000000` | 8,593 | 5,326,404 | ind-te-sangraha-v_part-00000_clean.parquet | 8,594 / 8,593 / 1 | `1036ff48ca9f7143…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `math-finemath-train-000000` | 28,088 | 38,582,010 | math-finemath_part-00000_clean.parquet | 28,262 / 28,088 / 174 | `6e84f270a53bcdd2…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `math-megamath-train-000000` | 17,232 | 33,979,879 | math-megamath_part-00000_clean.parquet | 17,555 / 17,232 / 323 | `ff5a213f47981243…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |
| `sci-finepdfs-train-000000` | 5,993 | 39,470,275 | sci-finepdfs_part-00000_clean.parquet | 5,997 / 5,993 / 4 | `e95a44b141ec0431…` (yes) | 57 P / 1 F / 0 NC | PASS (20) | cleaning_pipeline records a dedup version (#503) |

Per-shard evidence (every check with expected/observed, all artifact hashes, decoded-document positions, IDs, counts and SHA-256 of decoded text, never text): `shard_check/<shard>.checks.json`. Reproduce with `shard_check/shard_check.py` (the checker `teams/01-data-a/audit/check_shard.py` is on TSAI main, #482).

## Dedup

`dedup: null` (#503): this bundle was written before dedup v1 ran. The dedup job (#255, results #547, 17 Nov) removes 1,345 documents; 227 of them are in parts these shards hold, and all 227 are still in the shards (largest: code-rust 58, ind-hi-sangraha-s 35, ind-hi-sangraha-v 20, en-nemotroncc 19). Exact duplicates by token IDs across all shards: 11 extra copies in 1,200,725 documents (10 groups, none across packs). The first training shards need to be written from the deduplicated parts and record the dedup version. Evidence: `shard_check/dedup_vs_shards.json`, `shard_check/exact_dups.json` (`shard_check/dupcheck.py`; `remove_list.csv` from `teams/01-data-a/jobs/results/2026-11-14-dedup/` on TSAI main).

## Coverage

Byte-level checks cover every document of every shard (token range, specials, EOS, index/metadata agreement, hashes vs manifest). Decode covers 20 evenly spread documents per shard, first and last included, checked for round-trip consistency, not read for cleaning quality. Original cleaned parts and F2 payload were not re-scanned; provenance references were checked for consistency.
