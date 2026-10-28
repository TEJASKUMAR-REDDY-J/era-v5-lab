# Harm test methodology: code medicines

This document covers the code-go, code-rust, code-js-ts, code-java and code-cpp packs. Each pack is tested against its own gold set: go 163, rust 78, js-ts 49, java 40 and cpp 120 docs. No numbers are pooled across packs.

## 1. Process

| step | what was done |
|---|---|
| 1. Collect | 59 candidate rules from the registry, AjaySnl (PR 117), riyaagrahari (PR 123) and the code-go sheet. Each rule's code is used as written. |
| 2. Run | Each rule was run on all 500 docs of every pack. For each pack this records the gold docs changed or dropped, and the sick rows fixed. |
| 3. Resolve conflicts | For each disease, the rule that fixes the most sick rows is kept. A second rule for the same disease is kept only if it fixes rows the first misses. |
| 4. Harm gate | A rule is turned off (through `LANGS`) in any pack where it touches a gold doc. This applies to 5 rules. |
| 5. Standardise | The kept rules are copied into `medicine_code.md`. The copies give the same result as the source code on all 57,500 rule-and-doc checks. |
| 6. Test | `test_medicine_code.py` tests each pack, using the team's `tools/harm_test.py` for counting and the 1% limit. |

## 2. Checks that the test works

These are fake rules, run on each pack's gold set. They show that the test can fail.

| canary rule | go | rust | js-ts | java | cpp |
|---|---|---|---|---|---|
| change nothing | 0% PASS | 0% PASS | 0% PASS | 0% PASS | 0% PASS |
| drop everything | 100% FAIL | 100% FAIL | 100% FAIL | 100% FAIL | 100% FAIL |
| add one space | 100% FAIL | 100% FAIL | 100% FAIL | 100% FAIL | 100% FAIL |

Each gold file was also checked. Every gold id is present in its pack, and no id appears twice.

## 3. Why the final result is 0.00%: shown as is

The same harm test was run at three stages, on each pack's gold set:

| pack | (a) all 58 runnable rules | (b) 25 kept rules, run on every pack | (c) final sheet (25 rules with `LANGS`) |
|---|---|---|---|
| go | 2 / 163 = **1.23% FAIL** | 2 / 163 = **1.23% FAIL** | 0 / 163 = 0.00% PASS |
| rust | 18 / 78 = **23.08% FAIL** | 17 / 78 = **21.79% FAIL** | 0 / 78 = 0.00% PASS |
| js-ts | 0 / 49 = 0.00% PASS | 0 / 49 = 0.00% PASS | 0 / 49 = 0.00% PASS |
| java | 2 / 40 = **5.00% FAIL** | 2 / 40 = **5.00% FAIL** | 0 / 40 = 0.00% PASS |
| cpp | 12 / 120 = **10.00% FAIL** | 12 / 120 = **10.00% FAIL** | 0 / 120 = 0.00% PASS |

The step from (b) to (c) is the harm gate. It turns 5 rules off in the packs where they touch gold:

| pack | gold docs touched in (b) | rule turned off there |
|---|---|---|
| rust | 16 | `DA-C3-002` (Go lexer: not valid on Rust) |
| rust | 1 | `DA-E4-006` |
| java | 2 | `DA-F2-001` (contest paths in gold) |
| cpp | 11 | `DA-F2-001` (contest paths in gold) |
| cpp | 1 | `DA-E4-006` |
| go | 1 | `DA-E3-001` |
| go | 1 | `DA-E4-002` |

No rule was removed from the sheet, no gold doc was changed, and no label was changed. The 0% comes from these 5 per-language switches.

Most rules touch no gold doc at all, because the gold docs do not contain what those rules look for. A gold doc is one that 2 readers marked clean, with no fix or drop:

| what the rule looks for | go | rust | js-ts | java | cpp |
|---|---|---|---|---|---|
| `<reponame>` line (B2/B3): gold / other docs | 0 / 247 | 0 / 225 | 0 / 245 | 0 / 250 | 0 / 245 |
| `<NAME>`, `<EMAIL>` (B4): gold / other docs | 0 / 43 | 0 / 18 | 0 / 30 | 0 / 82 | 0 / 121 |
| CR line endings (A2): gold / other docs | 0 / 1 | 0 / 6 | 0 / 17 | 0 / 44 | 0 / 47 |
| `vendor/` path (H3): gold / other docs | 0 / 38 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| licence word in the first 30 lines (E4): gold / other docs | 5 / 85 | 2 / 35 | 1 / 20 | 0 / 110 | 8 / 195 |

## 4. Limits

- **The gold sets that judged the harm gate also picked the rules.** A rule turned off for touching 1 gold doc might also touch docs outside gold. Rerun on new or bigger gold sets: that is the independent test.
- **The gold sets are small.** In java, 1 doc is 2.5% of the set, and in js-ts 1 doc is 2.0%.
- **The test counts whether a gold doc was touched, not whether a fix is correct.** Some docs labelled clean outside gold are changed: 13 in js-ts and 2 in java.
- **Some rules run in a pack where they touch 1 gold doc and still pass.** `DA-E4-006` in cpp touches 1 of 120 (0.83%). `DA-E3-001` and `DA-E4-002` in go each touch 1 of 163 (0.61%). All three are turned off anyway: together, E3-001 and E4-002 make go fail at 1.23%. This is the one place where the process is stricter than the spec, which allows up to 1% per rule.

## 5. Reproduce

```
python -I teams/01-data-a/code-medicines/test_medicine_code.py --pack code-go=<code-go.parquet> --pack code-rust=<...> --pack code-js-ts=<...> --pack code-java=<...> --pack code-cpp=<...>
```
