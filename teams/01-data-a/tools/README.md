# Data A tools: medicine checks

Tools to test the cleaning rules (medicines) from the annotators' `medicine.md` files. All three need `pip install pyarrow`. Run them from the repo root with `python -I`.

## The scripts

Run them in this order. Steps 2 and 3 both use the rules and IDs that step 1 makes.

| Step | Script | Input | Output |
|---|---|---|---|
| 1 | `medicine_extract.py` | one `medicine.md` | the rules as a Python file, and a rule ID for each rule |
| 2 | `harm_test.py` | one pack, one gold file, one rule ID | documents changed, documents dropped, the percent, PASS or FAIL at 1% |
| 3 | `rule_report.py` | one pack, its gold file, all its rules | `REPORT.md`: harm test of every rule for the pack, and advice on which rules to keep |

## 1. Extract the rules: `medicine_extract.py`

```
python -I teams/01-data-a/tools/medicine_extract.py diagnosis/submissions/<pack_id>/<handle>/medicine.md
```

Reads the `medicine.md` (it does not run it). Each `**Disease:** <code>` line starts a section, and the Python in that section is its rule. It writes:

- `teams/01-data-a/rules/<pack_id>/<handle>.py`: the rules as one Python file
- `teams/01-data-a/rules/registry.json`: one entry per rule, with its ID

The extractor finds the function for a code in this order: the `RULES = {"B3": fn}` dict, a function named `cure_b3`, the only function in the section. If none fits, it says so and writes nothing for that rule.

**Rule IDs** look like `DA-B3-001`: team (`DA` for the Data A packs, `DB` for all others), disease code, number. A rule keeps its ID when you run the extractor again. A rule removed from a `medicine.md` is marked `withdrawn`, and its ID is not reused.

## 2. Harm test: `harm_test.py`

```
python -I teams/01-data-a/tools/harm_test.py --pack <pack.parquet> --gold <pack_gold.csv> --rule DA-B3-001
```

Runs one rule on the gold set. Prints documents changed, documents dropped, the percent, and PASS or FAIL (changed + dropped must be 1% or less of the gold set). The exit code is 0 for PASS, 1 for FAIL and 2 if the test could not run.

To test code that is not in the registry, use `--rules <rules.py or medicine.md> --rule B3`.

## 3. Report: `rule_report.py`

```
python -I teams/01-data-a/tools/rule_report.py --pack-id <pack_id> --pack-file <pack.parquet> --gold <pack_gold.csv>
```

Runs every rule of the pack and writes `teams/01-data-a/rules/<pack_id>/REPORT.md`:

- the harm test result of each rule
- how many of the labelled-sick rows each rule fixes (from the pack's `labels.csv` files)
- for a code with more than one rule: advice to KEEP or DROP each, and why. A rule that does nothing also passes the harm test, so a rule is kept only if it fixes sick rows that the other kept rules do not.
- flags for problems

The advice is for a person to check. Nothing records the decision yet.

## The registry and Spec v1

`teams/01-data-a/rules/registry.json` has one entry for every rule that the extractor found:

| Field | Meaning |
|---|---|
| `id` | the rule ID, for example `DA-B3-001` |
| `pack`, `handle` | where the rule came from |
| `code`, `n` | the disease code, and which medicine of that code in the annotator's file (1, 2, ...) |
| `action` | `fix` or `drop`, as the annotator wrote it |
| `file` | the rules file that holds the code, relative to the registry |
| `withdrawn` | `true` if the rule is no longer in the `medicine.md` |

To build `spec_v1.md` from it:

1. Run the extractor on every `medicine.md`, then `rule_report.py` for every pack.
2. Take the rules that are not withdrawn, PASS the harm test, and that the report advises to KEEP.
3. For each one, write the ID, the code, the action (from the registry), the rule in words (the **Medicine** text in that annotator's `medicine.md`), the rule in code (the function in `file`), and the harm test result (from the report).
4. Add the Indic rules from G2.
5. Decide the order the rules run. The registry does not hold an order, so the team decides it.

Nothing writes `spec_v1.md` automatically yet.

## Writing a medicine.md so the extractor can read it

- Put `**Disease:** <code>` and `**Action:** fix` (or `drop`) in each section.
- Put the Python in a ```` ```python ```` block in that section.
- Name the function `cure_<code>` (for example `cure_b3`). It takes the text and returns the new text.
- To drop a document, return `("drop", "")`. To fix, return a string, or `("fix", new_text)`.
- A second medicine for the same code goes in its own section, with a function that has its own name.

## Notes

- The tools **run the annotators' code** (`harm_test.py`, `rule_report.py`). Read it first.
- Gold files go in `teams/01-data-a/gold/<pack_id>_gold.csv`: doc-ids only, no text. A `_DUMMY` gold file is for testing.
- The pack Parquet files are not in the repo.
- Tests: `python -I teams/01-data-a/tools/test_harm_test.py` (and `test_medicine_extract.py`, `test_rule_report.py`).
- `registry.json` is shared. Decide who runs the extractor and commits it, to avoid merge conflicts.
