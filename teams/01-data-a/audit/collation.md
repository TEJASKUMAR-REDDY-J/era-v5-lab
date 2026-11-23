# Audit collation: every finding, the rule behind it and its proposal

Week 4, tasks 4.4 and 5.1. 22 Nov 2026, second round 23 Nov. Collected by `TEJASKUMAR-REDDY-J` from `day_D3.md` and the audit PRs #68, #71, #72, #76, #78, #79, #81, #83 and #84 of patilvijay23/era-v5-lab. No cleaner rule is changed here.

**The medicines of these audits are put together in [`collated_medicine.md`](collated_medicine.md), with the conflicts between them resolved. What was used is listed under [Medicines used](#medicines-used).**

The audits read different cleaned outputs. So every labelled document was run again through the current `spec_v1_1/clean.py` of `g1-w4-pipeline` (sha256 `ce131217…`, with the F1 code-pack and Sanskrit `DB-B4-004` fixes of 23 Nov), rule by rule, to see which findings are still there and which rule causes each. The pipeline's own clean stage was also run end to end on a small copy of every part (see [End-to-end trial](#end-to-end-trial)).

| File | What it holds |
|---|---|
| [`collation_findings.csv`](collation_findings.csv) | 53 findings: audit, documents, disease, current rule, whether it is still there, proposal, its card in the collated medicine, next step |
| [`collation_docs.csv`](collation_docs.csv) | 553 labelled documents: label, what the current cleaner does, the rules that acted in order |
| [`collation_scope.csv`](collation_scope.csv) | Documents each rule fixes and drops on the English and math train parts |
| [`collation_replay.py`](collation_replay.py) | The script that writes `collation_docs.csv` and `collation_scope.csv` |
| [`collated_medicine.md`](collated_medicine.md) | 22 cards from #71, #72, #75, #76, #79 and #81 as one set that loads in `harm_test.py` |
| [`collated_medicine_docs.csv`](collated_medicine_docs.csv), [`collated_medicine_packs.csv`](collated_medicine_packs.csv) | What the set does on the 553 documents and on thirteen whole packs |
| [`collated_medicine_check.py`](collated_medicine_check.py) | The script that writes these two and checks the gold sets |

The files hold ids, rule ids and counts only: no document text and no personal data.

## What changed in the second round

- **New audits:** #68 en-nemotroncc (35), #72 code-java (35), #76 code-python (45), #81 en-fineweb-edu (35), #83 code-rust (35) and #84 code-cpp (35), and the Gujarati and Marathi supplement of `day_D3.md` (20): 240 more labelled documents. Every pack of the assignment now has an audit.
- **New medicines:** #72's four cards (`DA-A6-004`, `DA-E4-011`, `DA-E4-012`, and its `DA-C1-012`, which is `DA-C1-016` here) and #81's four (`DA-C1-015`, `DA-C3-009`, `DA-C5-008`, `DA-F1-010`). Seven are new cards; `DA-F1-010` is merged into the two phone cards.
- **Findings F18 and F19 now have cards** (#72's `DA-A6-004` and `DA-E4-011`), and **F06 too** (#81's `DA-C3-009` brings back both wrong drops of #68 on en-dclm).
- The rows of the first round are unchanged: the same 313 documents give the same current output.
- **New base:** `g1-w4-pipeline` and its cleaner `ce131217`. On the labelled documents it gives the same output as `6a57276c`; the two fixes act elsewhere (below).

## Coverage

| Audit | Pack | Labels | Current cleaner: fix / keep / drop |
|---|---|---:|---|
| `day_D3.md` | 29 label files | 71 | 10 / 17 / 44 |
| `day_D3.md` supplement | ind-gu-fw2, ind-mr-sangraha-v | 20 | 8 / 12 / 0 |
| #68 | en-dclm | 35 | 28 / 0 / 7 |
| #68 | en-nemotroncc | 35 | 23 / 0 / 12 |
| #71 | math-finemath, math-megamath | 35 | 28 / 0 / 7 |
| #72 | code-go | 45 | 37 / 0 / 8 |
| #72 | code-java | 35 | 35 / 0 / 0 |
| #76 | en-nemotroncc-synth | 76 | 75 / 0 / 1 |
| #76 | code-python | 45 | 41 / 0 / 4 |
| #78 | code-js-ts | 45 | 41 / 0 / 4 |
| #79 | sci-finepdfs | 6 of 35 | 6 / 0 / 0 |
| #81 | en-fineweb-edu | 35 | 23 / 0 / 12 |
| #83 | code-rust | 35 | 35 / 0 / 0 |
| #84 | code-cpp | 35 | 34 / 0 / 1 |
| **Total** | | **553** | **424 / 29 / 100** |

- **#79:** its label CSV lists only the 6 `fix` and `drop` documents, so the 29 `clean` ones are not here.
- **`day_D3.md` supplement:** the reviewer read the p1536 shards (spec v1). Spec v1.1 changes 3 documents labelled there as having no issue (`DB-C2-010`, `DB-C5-009`), and the 7 documents with an issue are still kept (F52, F53).
- **Code packs:** the cleaner changes 209 of the 213 code documents labelled `clean`, and the audits count those changes as right. In 136 of them the only change is the StarCoder metadata line (`DA-B3-001`); the rest are licence headers, `<NAME>` placeholders, IDE templates and control characters.
- **#76 code-python:** 4 documents labelled `clean` are dropped by the cleaner, spec v1 and spec v1.1 alike (F35).

## Main findings

1. **`DA-C3-003` drops good documents, and now has a proposal for three packs.** It drops a document whose last word is a word like `this`, `at` or `by`. On the four English packs it drops 3,019 documents, 1,959 of them over 2,000 characters. The audits found 9 wrong drops: 2 on en-dclm (#68), 2 on en-nemotroncc (#68), 4 on en-fineweb-edu (#81) and 1 on synth (#76).
   - #81's `DA-C3-009` counts curly quotes as an ending and trims a long prose document instead of dropping it. With it, 8 of the 9 come back; the ninth (`a12d77a8e0df9c60`, 1,729 characters) is under its 2,000-character bar. On synth #76's `DA-C3-008` withdraws the test instead. The team picks one policy for all four packs.
   - The endings of 40 of the 707 en-dclm drops were read in the first round (one reader, endings only). About 32 end in site chrome or in a link or contact that was already removed, about 6 are cut off, one ends in a curly quote, and one is a raw feed.
2. **The shared F1 rule never acted on a code pack** (#84, F45): every code row carries `lang_label` "code". **Fixed in `ce131217`:** F1 now takes the language from the pack. In the trial copy it adds 4 masks in 3 code documents and changes no labelled one. It needs `tree-sitter-language-pack` in the job image, as #84 said.
3. **The phone mask is wrong in both directions on the English packs.** It masks DOI digits, runs of years (#81), model numbers and a race name (#68 en-nemotroncc), and misses phones with more groups (#81). #81's exclusions for DOIs and years are merged into the phone cards; the others have no card (F39, F48).
4. **`DA-C7-002` drops 1,498 of 17,647 megamath documents (8.5%)** because the text mentions figures. Two of them are labelled `fix` in #71, one as good content.
5. **#71 read an older output.** In it the cleaner had dropped 13 megamath documents; the current cleaner drops 2,550. On finemath it is 600 and 2,609. Its labels hold for the documents still kept. **#79 too:** its report says the cleaner drops none of the 6,011 sci-finepdfs documents; the current cleaner drops 166.
6. **Short licence headers stay on every code pack.** #72 has cards for code-go and code-java (`DA-E4-011`, `DA-E4-012`); code-cpp, code-js-ts, code-python and code-rust have the same finding and no card (F20, F23, F42, F46). #84 also finds that `DA-E4-010` misses a header behind an editor modeline and can take the next comment with it.
7. **The rules #71 could not name:** the deleted reference and author lines are `DA-C5-006`, and the deleted formula lines are `DA-C2-001`.
8. **`day_D3.md` is partly out of date.** Of its 56 dropped documents, 12 (all Indic) are kept now and 44 are still dropped; `collation_docs.csv` names the rule for each. With the cards, 7 of its English drops by `DA-C3-003` are trimmed instead.

## Medicines used

Every executable proposal of the audits is used: 23 proposals, 22 cards.

| Source | Used | As | Not used |
|---|---|---|---|
| #75 (`2ecacf5f`) | all 5 | `DA-A2-010`, `DA-B3-012`, `DA-B4-016`, `DA-C2-009`, `DA-F1-007`; also one half of `DA-C2-010` and a third of `DA-F1-009` | |
| #76 (`e387d93e`) | all 6 | `DA-C1-013`, `DA-C3-008`, `DA-C5-007`, `DA-B4-015` as they are; the other half of `DA-C2-010` (its `DA-C2-008`) and a third of `DA-F1-009` (its `DA-F1-008`) | M7: a policy question, no code. Its code-python report has no card. |
| #71 (`4d17b696`) | both | `DA-C1-012`, `DA-C2-007`; on finemath `DA-C2-007` runs in the place of `DA-C2-001` | |
| #79 (`489593e9`) | both | `DA-C2-011` (Medicine 1), `DA-C1-014` (Medicine 2, part a) | Medicine 2, part (b): it changes documents labelled `clean` |
| #72 (`10cea824`) | all 4 | `DA-A6-004`, `DA-E4-011`, `DA-E4-012` as they are; its java `DA-C1-012` as `DA-C1-016` | |
| #81 (`8642da74`) | all 4 | `DA-C1-015`, `DA-C5-008` as they are; `DA-C3-009` on three packs (not synth); `DA-F1-010` merged into `DA-F1-007` and `DA-F1-009` | its proposals 6 and 7: no code |
| #68, #78, #83, #84, `day_D3.md` | findings only | | no executable medicine in them (#68's five en-dclm bugs are #75's cards) |

**Results of the whole set:** gold 0 changed and 0 dropped by every card on all thirteen packs, and the output of `clean()` is the same on all 1,969 gold documents with the cards in place. Of the 553 labelled documents 83 get another output, none labelled `clean`, none newly dropped; 9 drops that the audits call wrong are kept. On the whole packs 1,696 documents are recovered (464 en-dclm, 231 en-fineweb-edu, 943 en-nemotroncc, 57 synth, 1 finemath), almost all by `DA-C3-009`, and 3 are newly dropped (finemath, `DA-C7-001`). All five bugs of #68 on en-dclm are fixed, and all 25 wrong phone masks of #76's review are restored while its 8 ambiguous or private ones stay. Details are in [`collated_medicine.md`](collated_medicine.md).

## Conflicts and how they are resolved

- **Three PRs replace `DA-F1-005`:** #75 and #81 on the four English packs, #76 on synth. #81's one change (a DOI or a run of years is not a phone) does not touch the others, so it is added to both phone cards: `DA-F1-007` (en-dclm, en-fineweb-edu, en-nemotroncc) and `DA-F1-009` (synth).
- **#75 and #76 on synth** (`DA-C2-003` and `DA-F1-005`), as in the first round: merged into `DA-C2-010` and `DA-F1-009`.
  - `DA-C2-010`: a repeated line is left alone if either source leaves it alone.
  - `DA-F1-009`: #76 decides whether a line gives a reason to mask, #75 makes it one decision for each number. A number that looks public in one place and private in another is masked everywhere (privacy first).

  | doc_id | phone masks now | with #75 | with #76 | with `DA-F1-009` |
  |---|---:|---:|---:|---:|
  | `8aecb4bed3222e59` | 1 | 2 | 0 | 0 |
  | `417036b98dd9380a` | 1 | 2 | 0 | 0 |
  | `d6e8da1b50823198` | 1 | 2 | 1 | 2 |

  #76 judges the first two as public contacts and marks the third for review, so the merged card agrees with its labels on all three. **For the team lead to confirm:** privacy first, and masking the second copy in the third document.
- **Two PRs replace `DA-C3-003`:** #81's `DA-C3-009` (trim a long document) and #76's `DA-C3-008` (no last-word test, synth only). They are two policies for the same rule, so they are not merged: `DA-C3-008` stays on synth and `DA-C3-009` runs on the other three packs. **For the team:** one policy for all four packs.
- **One number, two cards:** #71 (math) and #72 (java) both use `DA-C1-012`. #71's keeps it; #72's is `DA-C1-016` here. #72 itself is not edited.
- **Rule IDs of #75:** `DA-A2-009`, `DA-B3-002`, `DA-B4-014` and `DA-C2-005` are already in `rules/registry.json`. In the collated medicine they are `DA-A2-010`, `DA-B3-012`, `DA-B4-016` and `DA-C2-009`; `DA-F1-007` is free and stays. #75 itself is not edited.
- **#71 `DA-C2-007` takes the place of `DA-C2-001`** on finemath: run last, it would let `DA-C7-001` and `DA-C9-003` drop 21 documents that are kept today. Retiring `DA-C2-001` is still a team decision.
- **`DA-E4-011` and `DA-E4-012`** share their shape test; #72 asks whether to merge them. They replace different rules, so they stay two cards, and the decision to adopt them should be one.

## #68: each finding and its medicine

| Finding in #68 | Current rule | Medicine |
|---|---|---|
| cp1252 quotes deleted | `DA-A2-008` | `DA-A2-010` (#75 `DA-A2-009`) |
| Lines cut inside code | `DA-C2-003` | `DA-C2-009` (#75 `DA-C2-005`); record fields (not on synth) and formula lines are still cut |
| Math removed inside dollar signs | `DA-B4-010` | `DA-B4-016` (#75 `DA-B4-014`); sets that start with a letter, minus or bracket are still cut (2 en-dclm documents, up to 3 synth) |
| Phone masked once | `DA-F1-005` | `DA-F1-007` (#75); a `+44` copy of the number is not matched |
| `<s>` and `</s>` kept | none | `DA-B3-012` (#75 `DA-B3-002`); also strips literal examples and code fences |
| Two wrong drops (en-dclm) | `DA-C3-003` | `DA-C3-009` (#81): both kept, trimmed |
| Two wrong drops (en-nemotroncc) | `DA-C3-003` | `DA-C3-009` (#81): one kept; the other is under 2,000 characters |
| Phone and address masks on non-personal numbers (en-nemotroncc) | `DA-F1-005` | **None** |
| Repeated poster names and ad lines (en-nemotroncc) | `DA-C2-003` | **None** |
| Wrong language, gutted | `DA-D3-003` | **None** |
| Boilerplate (C1): 25 en-dclm, 12 en-nemotroncc documents | `DA-C1-006`, `DA-C2-003` | **None for these packs** (#76 `DA-C1-013` is synth only, #71 `DA-C1-012` math only, #81 `DA-C1-015` fineweb only) |
| Joined pages (C4), PDF bullets (A3), SEO line (C5), spun and spam pages kept | none | **None** |

## How to reproduce

From the repository root, with the raw sample train parts in `<raw>`:

```bash
python -I teams/01-data-a/audit/collation_replay.py docs --raw <raw> --labels teams/01-data-a/audit/collation_docs.csv --out collation_docs.csv
python -I teams/01-data-a/audit/collation_replay.py scope --raw <raw> --out collation_scope.csv
```

`collated_medicine.md` has the commands for its own checks. `docs` takes its labels from the committed CSV and writes the same file again. Each replay is compared with `clean()` and the script stops on a difference. `clean.py` sha256 `ce131217cd5247a3…` (`g1-w4-pipeline`).

## End-to-end trial

The pipeline's clean stage (`pipeline/clean_job.py`, parallel since #85) on a trial copy of tokenizer sample v0: all 86 parts (48 train, 38 held-out), each with its first 150 rows plus the documents of the audit PRs and of the main `day_D3.md` audit in it, 12,145 rows, with a manifest of the copies.

| Check | Result |
|---|---|
| Clean stage, 4 workers and 1 worker | both complete, 0 errors: 3,176 fix, 397 drop, 8,572 keep; the 86 cleaned parts are byte-identical, the reports differ only in timings (75 s and 124 s) |
| Its output against the collation's rule-by-rule replay | 10,251 documents of packs with rules: 0 differ. 1,894 documents of the 7 packs with none: copied unchanged |
| The collated cards on the same documents | 119 changed, 26 kept that are dropped today, 0 newly dropped |
| `ce131217` against `6a57276c` on the same documents | 8 differ: 5 ind-sa-fw2 (verse numbers and years kept, `DB-B4-004`), 3 code (F1 masks in comments) |

The log is [`../jobs/logs/2026-11-23-collation-e2e-local.txt`](../jobs/logs/2026-11-23-collation-e2e-local.txt). The overlap, dedup, F2 and shards stages were not run: `overlap.py` needs Linux, and they do not read the cards.

## Tests and benchmark carried from #75

The five proposals are in the collated sheet, so their tests now load
`audit/collated_medicine.md` directly. No separate copy of `proposals_english.md`
is needed. Source: #75 commit `2ecacf5f`.

- `spec_v1_1/tests/test_proposals_english.py`: the 22 regression tests, using
  the renumbered cards. The synth-specific merges remain covered by
  `tests/audit/test_collated_medicine.py`.
- `spec_v1_1/tests/test_speed_equivalence_proposals_english.py`: the 9 speed-up
  checks, including 4,000 seeded random texts for each of A2, C2 and F1. The
  unoptimized F1 reference also applies #81's DOI/year exclusions, so these
  compare the same policy before and after the speed-up.
- `spec_v1_1/scripts/speed_proposals.py`: the benchmark now uses the collation's
  own pack scopes and replacement order. It times every applicable card and the
  whole pipeline, including the shared F1 rule. It verifies its baseline replay
  against `clean()` before timing. The default is the four English packs;
  `--pack` can select any of the thirteen collated packs.
- `tests/audit/test_speed_proposals.py`: command checks on synthetic Parquet
  packs, including the synth merges, changed-output counts, and an empty pack.

From the repository root:

```bash
python -m pytest -q teams/01-data-a/spec_v1_1/tests teams/01-data-a/tests/audit
python -I teams/01-data-a/spec_v1_1/scripts/speed_proposals.py --clean teams/01-data-a/spec_v1_1/clean.py --packs <sample-pack-folder>
```

Validation on Python 3.12: **2,014 passed, 1 skipped, 9 subtests passed** using
the command above, including the synthetic benchmark command checks.

The synthetic command checks do not establish corpus throughput. #75's reported
timings apply to its original five proposals; the full collated set still needs
timing on real sample packs before adoption. These files preserve the proposal
and validation work; the running cleaner and spec are unchanged.

## Limits

- The replay uses the raw tokenizer sample v0 train parts, not corpus-v1 and not the token shards.
- A finding marked "still there" means the same characters or the same drop are in the current output. It does not say how common the problem is. Audited documents were mostly picked from the ones the cleaner changed.
- The 40 endings were read by one person, and the wrong and right drops of `DA-C3-003` are not labelled pack-wide.
- No new medicine is written here: the cards are the audits' own, merged where they clash. The findings marked **None** still need a card and a harm test.
