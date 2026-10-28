# Code medicines: one standard sheet for five code packs

Each code pack is tested separately against its own gold set. All numbers below are per pack. Nothing is added up across languages.

| pack | languages (`lang_label`) | gold docs |
|---|---|---|
| code-go | go | 163 |
| code-rust | rust | 78 |
| code-js-ts | javascript, typescript | 49 |
| code-java | java | 40 |
| code-cpp | cpp | 120 |

code-python is left out for now. The gold sets are `teams/01-data-a/gold/<pack>_gold.csv`. A pack passes when changed + dropped gold docs are 1% or less of that pack's own gold set.

The 54 candidate rules are:
- every code-pack rule in `rules/registry.json`,
- AjaySnl's js-ts B3 rule,
- the code-go sheet's rules.

## Files

| file | what it is |
|---|---|
| `medicine_code.md` | 23 picked rules in one form: `RULE_ID`, `CODE`, `ACTION`, `LANGS`, `ORIGIN` and `medicine(doc) -> (action, text)`. The source code is copied unchanged and only a wrapper is added. The summary table gives, for each rule and each language, the gold harm % and the sick rows fixed. |
| `test_medicine_code.py` | Harm test, one pack at a time: each rule alone, the whole sheet in run order, then a second pass over the output. |

Run it from the repo root:

```
python -I teams/01-data-a/code-medicines/test_medicine_code.py --pack code-go=<code-go.parquet> --pack code-rust=<...> --pack code-js-ts=<...> --pack code-java=<...> --pack code-cpp=<...>
```

## How the rules were picked

A rule is picked only when it fixes sick rows that the rules already picked do not. Rows count as sick when an annotator of that pack labelled them with the rule's code.

A rule must also touch 0 gold docs in every pack it runs on. A rule that touches gold docs in some packs is limited, through `LANGS`, to the packs where it touches none.

## Result per pack (whole sheet, in run order)

| pack | rules on | gold changed | gold dropped | harm % | result | pack fixed / dropped / untouched | sick rows treated |
|---|---|---|---|---|---|---|---|
| go | 21 | 0 / 163 | 0 / 163 | 0.00 | PASS | 244 / 82 / 174 | 326 / 337 (97%) |
| rust | 21 | 0 / 78 | 0 / 78 | 0.00 | PASS | 234 / 23 / 243 | 256 / 259 (99%) |
| js-ts | 22 | 0 / 49 | 0 / 49 | 0.00 | PASS | 268 / 23 / 209 | 280 / 292 (96%) |
| java | 21 | 0 / 40 | 0 / 40 | 0.00 | PASS | 324 / 17 / 159 | 340 / 360 (94%) |
| cpp | 20 | 0 / 120 | 0 / 120 | 0.00 | PASS | 348 / 9 / 143 | 358 / 378 (95%) |

Every rule also passes on its own, in every pack it runs on, at 0.00%. The per-rule, per-language numbers are in the table at the top of `medicine_code.md`.

The sheet's copy of each rule gives the same result as the original rule on every doc of every pack in its `LANGS`.

## Per pack: this sheet compared with that pack's own medicine

Agreement is measured against the 500-row `labels.csv` of the pack's main annotator:

| pack | main annotator |
|---|---|
| go | TEJASKUMAR-REDDY-J |
| rust | amukka |
| js-ts | varshith2000 |
| java | curioustushar |
| cpp | TharunSivamani |

| pack | rule set | harm % | fix rows treated | drop rows dropped | clean rows untouched |
|---|---|---|---|---|---|
| go | this sheet | 0.00 | 244 / 254 (96%) | 79 / 83 (95%) | 163 / 163 (100%) |
| go | own medicine | 0.00 | 244 / 254 (96%) | 79 / 83 (95%) | 163 / 163 (100%) |
| rust | this sheet | 0.00 | 233 / 233 (100%) | 17 / 26 (65%) | 240 / 241 (99.6%) |
| rust | own medicine | 0.00 | 232 / 233 (99.6%) | 17 / 26 (65%) | 241 / 241 (100%) |
| js-ts | this sheet | 0.00 | 259 / 267 (97%) | 16 / 23 (70%) | 197 / 210 (94%) |
| js-ts | own medicine | 0.00 | 258 / 267 (97%) | 16 / 23 (70%) | 204 / 210 (97%) |
| java | this sheet | 0.00 | 340 / 360 (94%) | none labelled drop | 139 / 140 (99%) |
| java | own medicine | 0.00 | 334 / 360 (93%) | none labelled drop | 140 / 140 (100%) |
| cpp | this sheet | 0.00 | 354 / 365 (97%) | 0 / 2 | 130 / 131 (99%) |
| cpp | own medicine | 0.00 | 325 / 365 (89%) | 0 / 2 | 131 / 131 (100%) |

The biggest gain is in cpp, at +29 fix rows, from the B3, B4 and E4 rules of other packs. Java gains +6.

The cost is a few clean-labelled docs that the sheet now changes. Only the ones outside the gold set are affected:

| pack | clean-labelled docs changed |
|---|---|
| rust | 1 |
| js-ts | 7 more than the own medicine |
| java | 1 |
| cpp | 1 |

## Rules limited to some languages

Harm % is per pack. A rule is left out of every pack where it touches any gold doc.

| rule | go | rust | js-ts | java | cpp | runs on |
|---|---|---|---|---|---|---|
| `DA-C3-002` Go lexer, drop | 0.00% | **20.51%** (16/78) | 0.00% | 0.00% | 0.00% | go only |
| `DA-F2-001` contest path, drop | 0.00% | 0.00% | 0.00% | **5.00%** (2/40) | **9.17%** (11/120) | go, rust, js-ts |
| `DA-E4-006` licence block, fix | 0.00% | **1.28%** (1/78) | 0.00% | 0.00% | 0.83% (1/120) | go, js-ts, java |
| `DA-E3-001` secret assignment, drop | 0.61% (1/163) | 0.00% | 0.00% | 0.00% | 0.00% | rust, js-ts, java, cpp |
| `DA-E4-002` licence before `package`/`import`, fix | 0.61% (1/163) | 0.00% | 0.00% | 0.00% | 0.00% | rust, js-ts, java, cpp |

Bold marks a FAIL. 0.61% and 0.83% would still PASS, but those packs are left out anyway so that the sheet keeps 0 gold harm in every pack.

Why each rule is limited:
- **`DA-C3-002`** is a Go-only check. It also fires on clean non-gold docs in other languages.
- **`DA-F2-001`**: the java and cpp gold sets hold contest solutions labelled clean, and this rule drops them.
- **`DA-E3-001`** and **`DA-E4-002`** add new rows: 4 E3 rows in js-ts, and 5 E4 rows in js-ts and java.

## Not picked (31 of 54)

| reason | rules | leave out? |
|---|---|---|
| Fixes the same rows as a picked rule, nothing more (18) | A1-002; A4-001 (and it touches 1 clean doc); A2-002, 003, 004, 006 and the code-go A2 rule; B3-001, 002, 003, 004, 005, 007 (each misses 6 B3 rows that `DA-B3-008` fixes); B4-001, 002, 003 and the code-go B4 rule; the code-go E2 rule (fixes 6 E2 rows, where `DA-E2-001` fixes 8) | Yes. Each one is a duplicate. |
| Fixes 0 rows in all five packs (9) | Python-pack rules A2-005, A3-001, B1-001, B3-006, C2-001, E1-003, E3-002 and F1-001; `DA-D3-001` (0 D3 rows; it only checks) | Yes for now. Test them again when code-python is added. |
| Touches gold and adds nothing (2) | `DA-E2-002`: rust 1.28%, FAIL, and its rows are already covered. `DA-E4-003`: go 0.61%, same rows as `DA-E4-002`. | Yes. |
| Detector only (1) | `DA-B4-004` returns True or False, so it would drop B4 files that the ruling says to fix. | Yes. `DA-B4-005` fixes the same rows. |
| Cannot run (1) | `DA-E4-001` needs a second `header` argument and has no detection logic. | Its author needs to fix it. |

## Sync with `tools/harm_test.py`

`test_medicine_code.py` imports the team's `tools/harm_test.py` and uses its `read_gold`, `classify` and `harm_percent`. The gold file, the counting and the 1% limit are therefore the same in both scripts. Only reading the pack stays here, for two reasons:
- The shared tool reads `doc_id` and `text` only, and calls `fn(text)`. The H3 and F2 rules need `url`, and `LANGS` needs `lang_label`.
- The shared tool gives the same numbers for the registry rules that it can run, for example `DA-E4-004` on rust and `DA-B4-005` on cpp: 0 changed, 0 dropped, PASS.

Some code rules do not run under the shared tool yet. `medicine_code.md` gets around each problem with its wrapper:

| rules file | under `tools/harm_test.py` | why | how `medicine_code.md` handles it |
|---|---|---|---|
| `code-go/RaviNaik.py`, `code-java/curioustushar.py` | the file does not load | `import re` was lost in extraction (NameError) | the copied code carries its own `import re` |
| `code-js-ts/varshith2000.py`: `DA-E1-002`, `DA-E3-001`, `DA-B4-004` | ERROR on every doc | detectors return True/False, while the shared `classify` takes only a str or `(action, text)` | True becomes drop and False becomes keep |
| `code-go/TEJASKUMAR-REDDY-J.py`: `DA-B3-003` | ERROR on every doc | the rule is `medicine(doc)` and gets a dict, not the text | the rules in the sheet take `doc` |
| `code-cpp/TharunSivamani.py`: `DA-E4-001` | ERROR | it needs a second `header` argument | not used |

To end up with one harm test, `tools/harm_test.py` would need three changes:
1. Accept True/False results: True means drop.
2. Pass `url` and `lang_label` to the rule, for example with an optional `doc` argument.
3. Skip a rule on rows outside its `LANGS`.

With those, this sheet runs on the shared tool directly.

## Open points

1. **Two docs change again on a second run of the sheet.** Neither is a gold doc.
   - java `2111dfa57dfd75e8` is a generated SDK file. The drop rules run first and miss it. Once its licence header is removed, `DA-E1-005` drops it.
   - cpp `a283a8943ca1d402` has two licence blocks one after the other. `DA-E4-004` removes one block per run.

   Fix: the pipeline should run the sheet again until nothing changes, at most 3 runs. This touches no gold doc in any pack, because no gold doc changes on the first run.
2. **js-ts changes 13 clean-labelled non-gold docs; the own medicine changes 6.** Check these before the js-ts gold set grows.
3. **Some rules drop files that a label sheet marks as fix.**
   - The E1 rules drop generated java and cpp files that those annotators labelled fix.
   - `DA-E3-001` drops a file with a secret, while `DA-E3-003` replaces the secret.

   This is a policy question for the team, not a harm-test failure.
4. **New rule IDs.** `DA-E1-005`, `DA-E3-003`, `DA-E4-005`, `DA-E4-006`, `DA-H3-001`, `DA-C3-002`, `DA-F2-001`, `DA-A4-002`, `DA-A6-001`, `DA-C1-004` and `DA-B3-008` are not in the registry yet. Each takes the next free number in `registry.json` on this branch. Registering them may change the numbers.
5. **The gold sets are interim and small:** java has 40 docs and js-ts has 49, so a single doc is 2.5% or 2.0% of the set. Run the test again when the gold sets are regenerated.
