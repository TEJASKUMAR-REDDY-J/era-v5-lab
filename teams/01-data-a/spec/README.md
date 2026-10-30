# Spec v1: structure and requirements

Status: **DRAFT.** A proposal for how Data A's Spec v1 is laid out and what a rule must show before it is approved. It follows `spec_v1_TEMPLATE.md`. The code family is filled in as the worked example; other families can copy the form.

## Layout

```
teams/01-data-a/spec/
  README.md               this file
  spec_v1_<family>.md     scope, order, conflicts, open items, freeze state
  medicine_<family>.md    the runnable rules: one block per rule, in run order
  decisions_<family>.md   why each rule was picked or not, for each disease
  results/<pack>_harm.json   harm_test.py --report output: IDs and digests only
```

Families: `code`, `en`, `math`. Science and Indic follow when their owners are set.

**One source for each fact.** Rules live only in `medicine_<family>.md`. The registry of the template's §3 is the table at the top of that file, so it cannot drift from the code. Numbers come from `results/`, not from hand-typed tables.

`spec/spec_v1.md` stays the name that `build_spec_v1.py` writes and `run_harm_suite.py` reads. This folder does not use it for now: see "Decide" below.

## What every rule must have

A block in the sheet with these fields, and a `medicine(doc) -> (action, text)`. `harm_test.py --rule all` and `medicine_conflicts.py --sheet` already read this form.

| field | meaning |
|---|---|
| `RULE_ID` | Stable `DA-<code>-<nnn>`. Never reused. |
| `CODE` | Disease code from `DISEASES.md`. |
| `ACTION` | `fix`, `drop` or `fix+drop`. |
| `STAGE` | Stage below. The run order is section order. |
| `STATUS` | `CANDIDATE`, `APPROVED`, `FAILED`, `BLOCKED` or `DEFERRED`. |
| `LANGS` | Language tags it runs on. A row outside passes unchanged. |
| `ORIGIN` | Packs it runs on, comma separated. |
| `SOURCE` | Pack whose medicine it came from. |
| `AUTHOR` | Code field for `medicine_conflicts.py`. Not used in any text. |

Around the block: disease with counts and `doc_id` examples, medicine in words, action, harm test per pack, side effects. Examples give `doc_id` and offset only. E3 and F1 give type and offset only, never the value.

## Stages

| stage | what | why here |
|---|---|---|
| 00 guard | `LANGS` and the pack scope. | A rule must not touch a language it was not tested on. The language tag is taken as correct. |
| 10 characters | A1, A2, A4, A6. | Later patterns need clean characters. |
| 20 markup | B3. | Later rules expect the file to start at its real first line. |
| 30 source | Drops first (E1, E2, C3, C4), then strips (E4, C1). | A generated file with its banner inside the licence survives if the licence goes first. |
| 40 data safety | B4, E3, and F1 if approved. | A6 can turn an obfuscated address into plain text, so this runs after it. |
| 90 post-clean | A test, not a rule: no empty docs, no doc left with no code. | Catches what the gold test cannot. |

## When a rule is APPROVED

All of these, on every pack in `ORIGIN`. Anything else stays `CANDIDATE`, or `BLOCKED` when it waits on an answer.

1. **Within the limit,** alone and in the whole sheet: changed + dropped at most `max(1, floor(1% of gold))`. An empty gold set is NOT TESTABLE, never PASS. This is the limit in `harm_test.py`; §2.5 of the template still says 1.0% and needs updating.
2. **Treats real rows:** labelled rows treated out of labelled rows, per pack. A rule that does nothing also passes the limit.
3. **Does not damage what it keeps:** comment rules leave code unchanged, which is checked with comments stripped. Gold cannot show this. `DA-E4-004` passed gold and deleted `#include`.
4. **Idempotent:** a second run changes nothing.
5. **Not resting on a dispute:** it still passes with the disputed docs left in, or the reason is written down. A reader's own dispute must not be what makes their rule pass.
6. **Reviewed** by someone other than its author, with commit and digests recorded.

## Assumptions

- **Language tags are correct.** No detector runs. D1 rows wait for a language check at scale.
- **F2 is BLOCKED on the G9 fingerprints.** The word "leetcode" alone is not a leak (instructor, 30 Oct).
- **H3 has no rule.** A vendored copy is not a disease by itself. The same file twice in a pack is H1 or H2 on the second copy (instructor, 30 Oct).
- **A 0 result is a bound, not proof.** With n gold docs and 0 hits, the harm rate is only shown to be below about 3/n. Show this next to the result. About 300 docs are needed to show 1%.

## What to report per pack, never pooled

Gold size, limit, changed, dropped, affected IDs, pack fixed / dropped / untouched, labelled rows treated, and the stress result with disputed docs left in. Each pack passes or fails on its own.

## Run it

```
python -I teams/01-data-a/tools/harm_test.py --pack <pack>.parquet --gold teams/01-data-a/gold/<pack>_gold.csv \
  --rules teams/01-data-a/spec/medicine_code.md --rule all --report teams/01-data-a/spec/results/<pack>_harm.json
python -I teams/01-data-a/tools/medicine_conflicts.py --packs code- --sheet teams/01-data-a/spec/medicine_code.md --out <file>
```

These tools are on `g1-harm-test`, not on this base branch. Results here were made with them at `bae5163`.

## Decide

| question | proposal |
|---|---|
| Is the sheet the source for Spec v1? | Yes. `build_spec_v1.py` lists every submission as a non-executable draft (about 3,800 lines) and stays useful for inventory. The sheet is what runs. |
| Should `run_harm_suite.py` read sheets? | Yes. It now tests registry rules one at a time and never the combined sheet, so someone has to run `harm_test.py --rule all` as well. |
| Do `STAGE` and `STATUS` apply to the other sheets? | Yes, so all families have one form. |
| Freeze date: 31 Oct or Week 2? | The template says 31 Oct, and 24 code rules still need a reviewer. |
