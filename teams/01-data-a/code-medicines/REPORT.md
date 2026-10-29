# Code medicines: results

This report covers the code-go, code-rust, code-js-ts, code-java and code-cpp packs. code-python is left out for now.

Every number is per pack, against that pack's own gold set. The gold sets are go 163, rust 78, js-ts 49, java 40 and cpp 120 docs, from `teams/01-data-a/gold/`. A pack passes if the gold docs changed plus dropped are at most 1% of its gold set.

The method, and why the results are 0, are in `HARM_TEST_METHODOLOGY.md`.

## Result of the whole sheet

The sheet has 25 rules and runs in sheet order.

| pack | rules on | gold changed | gold dropped | harm | result | pack fixed / dropped / untouched | sick rows treated |
|---|---|---|---|---|---|---|---|
| go | 23 | 0 / 163 | 0 / 163 | 0.00% | PASS | 243 / 83 / 174 | 326 / 337 |
| rust | 23 | 0 / 78 | 0 / 78 | 0.00% | PASS | 234 / 23 / 243 | 256 / 259 |
| js-ts | 24 | 0 / 49 | 0 / 49 | 0.00% | PASS | 268 / 23 / 209 | 284 / 296 |
| java | 23 | 0 / 40 | 0 / 40 | 0.00% | PASS | 319 / 23 / 158 | 342 / 366 |
| cpp | 22 | 0 / 120 | 0 / 120 | 0.00% | PASS | 348 / 9 / 143 | 358 / 378 |

Each rule also passes alone, at 0.00%, in every pack it runs on. The table at the top of `medicine_code.md` gives each rule's numbers for each language.

## Against each pack's own main medicine

Agreement is measured against the 500-row labels of the pack's main annotator.

| pack | rule set | fix rows treated | drop rows dropped | clean rows untouched |
|---|---|---|---|---|
| go | sheet | 244 / 254 | 79 / 83 | 163 / 163 |
| go | own (TEJASKUMAR-REDDY-J) | 244 / 254 | 79 / 83 | 163 / 163 |
| rust | sheet | 233 / 233 | 17 / 26 | 240 / 241 |
| rust | own (amukka) | 232 / 233 | 17 / 26 | 241 / 241 |
| js-ts | sheet | 259 / 267 | 16 / 23 | 197 / 210 |
| js-ts | own (varshith2000) | 258 / 267 | 16 / 23 | 204 / 210 |
| java | sheet | 340 / 360 | none labelled | 138 / 140 |
| java | own (curioustushar) | 334 / 360 | none labelled | 140 / 140 |
| cpp | sheet | 354 / 365 | 0 / 2 | 130 / 131 |
| cpp | own (TharunSivamani) | 325 / 365 | 0 / 2 | 131 / 131 |

## Rules per disease: how conflicts were resolved

There are 59 candidate rules:
- every code rule in `rules/registry.json`,
- AjaySnl's js-ts B3 rule (PR 117),
- riyaagrahari's java sheet (PR 123, not in the registry yet),
- the code-go sheet.

For each disease, the rule that fixes the most sick rows is kept. Another rule for the same disease is kept only if it fixes rows the kept ones miss.

| disease | candidates | kept | not kept, and why |
|---|---|---|---|
| A1 | 2 | `DA-A1-001` | `DA-A1-002`: the same 15 rows |
| A2 | 8 | `DA-A2-001` | 6 others fix the same 115 rows; `DA-A2-005` fixes none |
| A3 | 1 | - | `DA-A3-001` (python): no A3 rows in these packs |
| A4 | 2 | `DA-A4-001` (drop, 3 of 3 rows) | the code-go A4 rule (fix): 1 row, which is one of the same 3 |
| A6 | 1 | `DA-A6-001` | - |
| B1 | 1 | - | `DA-B1-001` (python): fixes 0 of the 2 B1 rows |
| B2 | 1 | `DA-B2-001` | - |
| B3 | 9 | `DA-B3-008` (1225 of 1225 rows) | 8 others: each fixes fewer rows and none that it misses |
| B4 | 7 | `DA-B4-005` | 5 fix the same rows or fewer; `DA-B4-004` only checks, so it would drop files that the ruling says to fix |
| C1 | 2 | `DA-C1-004`, `DA-C1-001` | - (each fixes a different row) |
| C2 | 1 | - | `DA-C2-001` (python): fixes 0 of the 4 rows |
| C3 | 1 | `DA-C3-002` (go only) | - |
| D3 | 1 | - | `DA-D3-001`: a check that leaves the text as it is; fixes 0 of the 28 rows |
| E1 | 6 | `DA-E1-005`, `DA-E1-004`, `DA-E1-001`, `DA-E1-002`, `DA-E1-006` | `DA-E1-003` (python): fixes none |
| E2 | 3 | `DA-E2-001` | the code-go E2 rule fixes fewer rows; `DA-E2-002` FAILS rust (1.28%) and fixes no extra row |
| E3 | 3 | `DA-E3-003`, `DA-E3-001` (not go) | `DA-E3-002` (python): fixes none |
| E4 | 7 | `DA-E4-004`, `DA-E4-007`, `DA-E4-005`, `DA-E4-002` (not go), `DA-E4-006` (go, js-ts, java) | `DA-E4-003`: the same rows as `DA-E4-002`; `DA-E4-001`: cannot run (needs a 2nd argument) |
| F1 | 1 | - | `DA-F1-001` (python): fixes 0 of the 6 rows |
| F2 | 1 | `DA-F2-001` (go, rust, js-ts) | - |
| H3 | 1 | `DA-H3-001` | - |

Five diseases have no rule in the sheet: A3, B1, C2, D3 and F1. Each has exactly 1 candidate, and that candidate fixes 0 rows in these packs. Four of them come from the python pack, and the D3 one only checks. No medicine was dropped for any other reason.

## Rules limited to some languages

A rule is turned off only in a pack where it touches gold.

| rule | go | rust | js-ts | java | cpp | runs on |
|---|---|---|---|---|---|---|
| `DA-C3-002` | 0.00% | **20.51%** (16/78) | 0.00% | 0.00% | 0.00% | go |
| `DA-F2-001` | 0.00% | 0.00% | 0.00% | **5.00%** (2/40) | **9.17%** (11/120) | go, rust, js-ts |
| `DA-E4-006` | 0.00% | **1.28%** (1/78) | 0.00% | 0.00% | 0.83% (1/120) | go, js-ts, java |
| `DA-E3-001` | 0.61% (1/163) | 0.00% | 0.00% | 0.00% | 0.00% | rust, js-ts, java, cpp |
| `DA-E4-002` | 0.61% (1/163) | 0.00% | 0.00% | 0.00% | 0.00% | rust, js-ts, java, cpp |

Bold marks a FAIL. Three cells are under the 1% limit (go 0.61% twice, cpp 0.83%), but the rule is still turned off there. The reason: with both `DA-E3-001` and `DA-E4-002` on, go fails at 1.23% (2 of 163).

## Sync with `tools/harm_test.py`

On this branch the team tool runs the sheet directly, one pack at a time:

```
python -I teams/01-data-a/tools/harm_test.py --pack <pack.parquet> --gold teams/01-data-a/gold/<pack>_gold.csv --rules teams/01-data-a/code-medicines/medicine_code.md --rule all
```

This gives the same result as `test_medicine_code.py`: 0.00% PASS for go, rust, js-ts, java and cpp. Three changes to `harm_test.py` made that possible, and its existing tests still pass:
1. Each `RULE_ID` block of a sheet runs in its own namespace.
2. True means drop and False means keep.
3. A rule whose first parameter is `doc` gets `url` and `lang_label` as well as the text.

`test_medicine_code.py` stays for checks the tool does not do: all packs in one run, and a second run over the output.

Still not runnable:
- `RaviNaik.py` and `curioustushar.py` need the rules files extracted again. The extractor now adds `import re`.
- `DA-E4-001` needs a second argument.

## Open points

1. **A4 policy.** `DA-A4-001` drops every file that holds U+FFFD. The code-go A4 rule fixes such a file instead (ruling 7). The A4 rule was kept for fixing the most rows (3 of 3), but which action is right is the team's call.
2. **Drop versus fix.** The E1 rules drop generated java and cpp files that those annotators labelled fix. `DA-E3-001` drops a file that has a secret, while `DA-E3-003` replaces the secret. These are also the team's call.
3. **Clean-labelled docs changed outside gold.** The sheet changes 13 such docs in js-ts and 2 in java. Check them.
4. **Second run.** cpp `a283a8943ca1d402` has two licence blocks one after the other, and `DA-E4-004` removes one per run. The pipeline should run until nothing changes, at most 3 times.
5. **New rule IDs.** These are not in the registry yet: `DA-E1-005`, `DA-E1-006`, `DA-E3-003`, `DA-E4-005`, `DA-E4-006`, `DA-E4-007`, `DA-H3-001`, `DA-C3-002`, `DA-F2-001`, `DA-A6-001`, `DA-C1-004`, `DA-B3-008`. Each takes the next free number.
