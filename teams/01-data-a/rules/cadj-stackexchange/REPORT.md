# Rule report: cadj-stackexchange

- Pack file: cadj-stackexchange.parquet (500 documents)
- Gold set: cadj-stackexchange_gold_DUMMY.csv (200 documents), limit 1%
- Label sheets: smitasasindran (152 rows), tanmays369 (150 rows)
- Rules in this report: 2 active

## Rules

| ID | Code | Annotator | Action: written / seen | Gold changed | Gold dropped | % of gold | Harm test | Sick rows | Hit | Extra | Unlabelled | Missed | Errors |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DB-B3-001 | B3 | smitasasindran | fix / fix | 200 | 0 | 100.00% | FAIL | 152 | 152 | 0 | 348 | 0 | 0 |
| DB-B4-001 | B4 | smitasasindran | fix / fix | 23 | 0 | 11.50% | FAIL | 19 | 19 | 0 | 34 | 0 | 0 |

Sick rows: labelled with the code (verdict fix or drop), by any annotator. Hit: sick rows the rule changes or drops. Extra: rows labelled with something else that it changes or drops. Unlabelled: rows nobody has labelled that it changes or drops. Missed: sick rows it leaves alone. A hit is not a check that the new text is right.

## Rules with the same code

No code has more than one rule.

## Flags

- B2: 17 sick rows in the labels and no rule for it
- C4: 51 sick rows in the labels and no rule for it
- H2: 51 sick rows in the labels and no rule for it
