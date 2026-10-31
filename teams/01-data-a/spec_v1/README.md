# Spec v1: how to run it and how to add to it

`clean.py` is the cleaner. It is generated from the medicine sheets in `../spec/`, so **add rules to a sheet, never to `clean.py`**.

| where | what | who changes it |
|---|---|---|
| `../spec/medicine_<family>.md` | The rules of one family: `code`, `en`, `math`, `sci` | The PR for that family |
| `../spec/decisions_<family>.md` | Why each rule was picked or not | The same PR |
| `tools/f1_rule.py` | The one F1 rule, shared by all families | A PR that names the family it adds |
| `clean.py`, `harm_tests.md`, `harm_results/` | Generated | Only the rebuild step, after a merge |

## Run it

```
pip install pyarrow pytest tree-sitter-language-pack ftfy
python spec_v1/tools/build_clean.py
python -m pytest spec_v1/tests
python spec_v1/run_clean.py --pack <pack>.parquet --out out
python spec_v1/tools/make_harm_tests.py <g1-harm-test checkout> <folder with the packs>
```

Paths start at `teams/01-data-a/`. `ftfy` is needed once the English A3 rule is in. `make_harm_tests.py` uses `harm_test.py`, which is on `g1-harm-test` until PR 140 merges. The packs are not in the repo, so get your link from the lab plan sheet.

## Add your medicines without double work

1. **Check first.** Look at the open PRs to `g1-specv1`. If a PR already covers your family and code, comment there instead of starting again.
2. **Claim it.** Open a draft PR to `g1-specv1` early, titled `medicine_<family>: <codes>`. Only one open PR per family sheet at a time, so sheets do not conflict.
3. **Put each rule in your family's sheet, in the form of `../spec/medicine_code.md`,** at the place its stage says. Copy the sheet into `../spec/` if your family has none yet:
   - **English:** the sheet is on `g1-en-medicines`. Move it to `../spec/medicine_en.md`.
   - **Math:** make `../spec/medicine_math.md`. The finemath sheet has code fragments and no functions, so each needs writing as a `medicine(doc)`.
   - **Science:** make `../spec/medicine_sci.md`: one medicine from all 500 rows, as TSAI ruled. The 5 diagnosis PRs stay as they are.
   - **Code:** add to `../spec/medicine_code.md`. Sheets that came after it still need checking against it.
4. **Resolve conflicts before you ask for review.** Run `medicine_conflicts.py --packs <family prefix> --sheet <your sheet>`, then for each code with more than one rule:

   | what you find | what to do |
   |---|---|
   | Same text on every doc | Keep one. Say so in the decisions file. |
   | They fix different rows | Keep both, as two blocks. |
   | They disagree on the same rows | Keep the one that treats the most labelled rows within the limit. On a tie, read the code. |
   | One passes only because its supporter's dispute took docs out of gold | Hold it as `BLOCKED`. |
   | It needs an answer from TSAI | Hold it as `BLOCKED`, with the question. |

5. **Do not edit someone else's rule to change what it does.** Add a new block and say why in the decisions file.
6. **In your PR, change only your sheet, your decisions file and your tests.** Leave `clean.py` and `harm_results/` out: two PRs regenerating them will always conflict. Paste your harm results in the PR text.
7. **After a merge,** whoever merges reruns the steps in "Run it" and commits the generated files.

Each rule needs `RULE_ID`, `CODE`, `ACTION`, `STAGE`, `STATUS`, `LANGS`, `ORIGIN`, `SOURCE`, `AUTHOR` and `medicine(doc) -> (action, text)`. `../spec/README.md` has what each one means and the bar for `APPROVED`.

**Rule IDs:** an ID only has to be unique inside its sheet. `clean.py` adds the family, so `DA-A2-007` in two families does not clash. Registry IDs get renumbered, so a sheet's ID is a label and not a link to the registry.

## Regex: which diseases, and how

| use | diseases | how |
|---|---|---|
| Regex alone is enough | A1, A2, A4, A5, A6, B1, B3 | A fixed character or token. Replace only that. |
| Regex, with care | B2, B4, E1, E2, E4, C2 | Anchor it to the header or to a known marker. Check it does not touch valid code or markup. |
| Regex plus tree-sitter, in code | F1, and anything that should only touch comments or strings | The regex finds the value and the tree says where it sits. Leave it alone if it is in code. |
| Regex finds some, not all | C1, C3, C5, E3 | Phrase lists and shapes fit the sites seen so far. Report what is left. |
| Library | A3 | `ftfy`, as the English sheet does. |
| Regex does not work | C4, D1, D3, D4, D5, F3, H1, H2, H3 | Label it. These need a whole-pack check, a language model or a classifier. |
| Needs G9 | F2 | Blocked on the benchmark fingerprints. |

Try a pattern before you write the rule. This prints counts and doc_ids, never text:

```
python spec_v1/tools/regex_check.py --pack <pack>.parquet --gold <gold>.csv --labels <diagnosis/submissions/pack> --code E4 --regex "(?i)copyright"
python spec_v1/tools/regex_check.py --pack <pack>.parquet --gold <gold>.csv --labels <diagnosis/submissions/pack> --code E3 --regex "AKIA" --where string
```

Then:
1. **Read the misses, not only the hits.** A rule can match every labelled row and still delete real code. `DA-E4-004` passed gold and removed `#include`.
2. **Keep the match narrow.** Anchor it, set `LANGS`, and change only the bad part.
3. **Check it is idempotent.** A second run must change nothing.
4. **Add a unit test** with made-up values in `tests/`: one sick case and one look-alike that must stay.
5. **Run the harm test.** The limit is `max(1 document, 1%)` of the pack's gold, per pack, never pooled. An empty gold set is not testable.

## F1

`tools/f1_rule.py` follows the TSAI decision: `<PHONE>`, `<EMAIL>` and `<ADDRESS>` for a private person, drop a personal listing, keep organisations and public offices.

- **Where it runs:** code only for now, because only code has had the harm test. To add a family, put its language tags in `_F1_LANGS`, run the harm test, and put the results in your PR. Prose has no tree, so it runs on regex alone.
- **Never write a private value** in a commit, a PR or chat. Use doc_ids and offsets, as `regex_check.py` does.
- **Known limits:** it misses lower-case addresses, and it reads "8 Bit Drive" as an address. An email at a company domain counts as personal unless it is a role address like `support@`. Names are not in the TSAI list, so it leaves them.
- **B4:** in `clean.py`, the code B4 rule leaves `<EMAIL>` alone, because it is now the F1 tag, and still replaces `<NAME>`, `<KEY>` and `<PASSWORD>`. Before this, a second run turned the tag into `user@example.com`. `tools/build_clean.py` makes this change, and `../spec/medicine_code.md` still has the old rule until the team agrees. 26 docs labelled B4 hold only `<EMAIL>`, so they keep the token.
