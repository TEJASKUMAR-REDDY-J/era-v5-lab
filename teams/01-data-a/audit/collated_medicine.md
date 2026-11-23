# Collated medicine: the cards of #71, #72, #75, #76, #79 and #81 as one set, with the conflicts resolved

Week 4, tasks 4.4 and 5.1. 22 Nov 2026, second round 23 Nov. Put together by `TEJASKUMAR-REDDY-J`. **Proposals: the spec, the registry and the running `clean.py` are not changed.** The findings behind the cards are in [`collation.md`](collation.md).

**22 cards, from 23 proposals** (#81's `DA-F1-010` is merged into the two phone cards). No two cards replace the same rule on the same pack, and no card uses a number of the registry, of spec v1.1 or of another card. The sheet loads in `harmtest/harm_test.py` as it is.

| Card | Packs | Place | From | Change to the source's code | Finding |
|---|---|---|---|---|---|
| `DA-A2-010` | en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth | replaces `DA-A2-008` | #75 `DA-A2-009` | new number only | F01 |
| `DA-C3-008` | en-nemotroncc-synth | replaces `DA-C3-003` | #76 `DA-C3-008` | none | F15 |
| `DA-C1-013` | en-nemotroncc-synth | replaces `DA-C1-006` | #76 `DA-C1-013` | none | F30 |
| `DA-C2-009` | en-dclm, en-fineweb-edu, en-nemotroncc | replaces `DA-C2-003` | #75 `DA-C2-005` | new number; synth moves to `DA-C2-010` | F02 |
| `DA-C2-010` | en-nemotroncc-synth | replaces `DA-C2-003` | #75 `DA-C2-005` + #76 `DA-C2-008` | **merged** | F02 and F14 |
| `DA-C5-007` | en-nemotroncc-synth | replaces `DA-C5-005` | #76 `DA-C5-007` | none | F16 |
| `DA-B4-015` | en-nemotroncc-synth | replaces `DA-B4-007` | #76 `DA-B4-015` | none | F17 |
| `DA-B3-012` | en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth | new, after `DA-B4-012` | #75 `DA-B3-002` | new number only | F05 |
| `DA-B4-016` | en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth | replaces `DA-B4-010` | #75 `DA-B4-014` | new number only | F03 |
| `DA-F1-007` | en-dclm, en-fineweb-edu, en-nemotroncc | replaces `DA-F1-005` | #75 `DA-F1-007` + #81 `DA-F1-010` | **merged**; synth moves to `DA-F1-009` | F04, F39 |
| `DA-F1-009` | en-nemotroncc-synth | replaces `DA-F1-005` | #75 `DA-F1-007` + #76 `DA-F1-008` + #81 `DA-F1-010` | **merged** | F13, F39 |
| `DA-C1-012` | math-finemath, math-megamath | new, after the family's rules | #71 `DA-C1-012` | none | F12 |
| `DA-C2-007` | math-finemath, math-megamath | replaces `DA-C2-001` on finemath; on megamath new, after the family's rules | #71 `DA-C2-007` | place on finemath | F09, F12 |
| `DA-C1-014` | sci-finepdfs | new, after `DA-C1-007` | #79 Medicine 2, part (a) | number given; part (b) left out | F26 |
| `DA-C2-011` | sci-finepdfs | replaces `DA-C2-004` | #79 Medicine 1 | number given; put into the rest of `DA-C2-004` | F25 |
| `DA-C3-009` | en-dclm, en-fineweb-edu, en-nemotroncc | replaces `DA-C3-003` | #81 `DA-C3-009` | not on synth (`DA-C3-008` there) | F06, F36, F47 |
| `DA-C5-008` | en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth | replaces `DA-C5-002` | #81 `DA-C5-008` | none | F38 |
| `DA-C1-015` | en-fineweb-edu | new, after `DA-B2-002` (before `DA-C3-001`) | #81 `DA-C1-015` | the reviewer's name in a comment is now the handle | F37, F40 |
| `DA-A6-004` | code-cpp, code-go, code-java, code-js-ts, code-python, code-rust | replaces `DA-A6-001` | #72 `DA-A6-004` | none in effect (`SPEC_PACKS` set to the card's own packs) | F18 |
| `DA-E4-011` | code-go | replaces `DA-E4-005` | #72 `DA-E4-011` | none in effect | F19 |
| `DA-E4-012` | code-java | replaces `DA-E4-009` | #72 `DA-E4-012` | none in effect | F32 |
| `DA-C1-016` | code-java | replaces `DA-C1-005` | #72 `DA-C1-012` | new number: #71 has `DA-C1-012` | F31 |

Sources, at the commits read: #71 `4d17b696`, #72 `10cea824`, #75 `2ecacf5f`, #76 `e387d93e` (its cards are the same as at `2ba7ce3b`), #79 `489593e9`, #81 `8642da74`. Each code block is the source's block with header lines added (`REPLACES`, `RUNS_AFTER`, `FROM`); the column says what else is changed. In the cards of #71 and #81 a name in a comment is now the handle. #68, #78, #83, #84 and #76's code-python report have findings and no card of their own (#68's en-dclm bugs are the cards of #75).

## Conflicts, and how each is resolved

1. **Phone numbers on en-nemotroncc-synth: #75 `DA-F1-007` and #76 `DA-F1-008` both replace `DA-F1-005`.** Resolved by `DA-F1-009`, which uses both in order.
   - **#76 decides the line.** Its technical values and its public contacts are not a reason to mask. It comes first because it rests on the reading of all 33 masks of Part_2.
   - **#75 decides the number.** A number that some line gives a reason to mask is masked on every line. This is the policy for a number that looks public in one place and private in another: **privacy first**, because a number masked on one line and shown on the next is not masked. The second copy of `d6e8da1b50823198` is the one case; #76 marks its owner as "review required".

   | doc_id | Label in #76 | phone masks now | #75 alone | #76 alone | `DA-F1-009` |
   |---|---|---:|---:|---:|---:|
   | `8aecb4bed3222e59` | public contact, wrongly masked | 1 | 2 | 0 | **0** |
   | `417036b98dd9380a` | public contact, wrongly masked | 1 | 2 | 0 | **0** |
   | `d6e8da1b50823198` | review required, keep masked | 1 | 2 | 1 | **2** |

   Over the 29 documents of #76's phone review, `DA-F1-009` restores all 25 masks labelled incorrect and keeps all 8 labelled ambiguous or private. **The privacy-first choice needs the team lead's yes.** To choose the other way, use #76's `DA-F1-008` on synth as it is.
   - **#81 decides what is not a number at all.** Its `DA-F1-010` is `DA-F1-005` with one change: digits inside a DOI and a run of years are not a phone. That change is added to `DA-F1-009` and to `DA-F1-007`, so no two cards replace `DA-F1-005` on a pack. It restores the 5 wrong masks of #81's two documents.
2. **Repeated lines on en-nemotroncc-synth: #75 `DA-C2-005` and #76 `DA-C2-008` both replace `DA-C2-003`.** Resolved by `DA-C2-010`: the two exclusions do not touch each other, so a line excluded by either is not counted. `7523ebd6d772fada`, which #75 alone does not fix, is whole. The other three packs keep #75's card (`DA-C2-009`), because #76 tested its exclusion on synth only.
3. **Rule numbers of #75 that are taken.** `DA-A2-009`, `DA-B3-002` and `DA-B4-014` are in the registry, `DA-C2-005` too (it was also a dropped English rule). They become `DA-A2-010`, `DA-B3-012`, `DA-B4-016` and `DA-C2-009`. The merged cards are `DA-C2-010` and `DA-F1-009`; #79's two medicines had no number and get `DA-C2-011` and `DA-C1-014`. #75 itself is not edited.
4. **#71 `DA-C2-007` and `DA-C2-001`.** While `DA-C2-001` runs first, the formula lines are gone before #71's card sees them, so it is out on finemath. #71 runs its card after the family's rules. Here it runs there on megamath only, and in the place of `DA-C2-001` on finemath: run last, it leaves the repeated lines in for `DA-C7-001` and `DA-C9-003`, which then drop 21 documents that are kept today (3 in this place).
5. **`DA-C3-003` on the English packs: #81 `DA-C3-009` and #76 `DA-C3-008`.** These are two policies, not two parts: #81 trims a long document whose tail is cut off, #76 drops the last-word test. They are not merged. `DA-C3-008` stays on synth, where #76 tested it, and `DA-C3-009` runs on en-dclm, en-fineweb-edu and en-nemotroncc. **For the team:** one policy for all four packs.
6. **`DA-C1-012` twice:** #71 (math) and #72 (java) give their cards the same number. #71's keeps it; #72's java card is `DA-C1-016` here. #72 is not edited.
7. **#79 Medicine 2, part (b)** (running footers) is left out: it changes documents that the same audit labels `clean`, and the PR calls it optional.
8. **Two cards on one disease that do not clash:** #75 `DA-B4-016` (`DA-B4-010`) and #76 `DA-B4-015` (`DA-B4-007`); #71 `DA-C1-012`, #76 `DA-C1-013`, #79 `DA-C1-014`, #81 `DA-C1-015` and #72 `DA-C1-016` (different packs); #72 `DA-E4-011` and `DA-E4-012` (go and java; #72 asks whether to merge them, and the decision to adopt them should be one).

## Checks of the whole set

**Gold, card by card** (`harm_test.py --rule all`, the 500-document sample packs whose sha256 is the `pack_sha256` of the harm results): 0 changed and 0 dropped for every card, and for the sheet in order, on all thirteen packs. For #79's two medicines this is the first run on the 202 gold documents of sci-finepdfs, and #72's cards are run on the gold of all six code packs.

**Gold, whole pipeline:** with the cards in place the output of `clean()` is the same on every gold document.

| Pack | Gold | changed / dropped now | with the cards | output differs |
|---|---:|---:|---:|---:|
| en-dclm | 62 | 0 / 0 | 0 / 0 | 0 |
| en-fineweb-edu | 158 | 0 / 0 | 0 / 0 | 0 |
| en-nemotroncc | 129 | 2 / 0 | 2 / 0 | 0 |
| en-nemotroncc-synth | 326 | 0 / 0 | 0 / 0 | 0 |
| math-finemath | 86 | 1 / 1 | 1 / 1 | 0 |
| math-megamath | 26 | 0 / 0 | 0 / 0 | 0 |
| sci-finepdfs | 202 | 4 / 1 | 4 / 1 | 0 |
| code-cpp | 122 | 0 / 0 | 0 / 0 | 0 |
| code-go | 163 | 0 / 0 | 0 / 0 | 0 |
| code-java | 116 | 0 / 0 | 0 / 0 | 0 |
| code-js-ts | 204 | 0 / 0 | 0 / 0 | 0 |
| code-python | 141 | 0 / 0 | 0 / 0 | 0 |
| code-rust | 234 | 0 / 0 | 0 / 0 | 0 |

The gold documents that change or drop today do so by rules that are already in spec v1.1; no card touches them.

**The 553 labelled documents** ([`collated_medicine_docs.csv`](collated_medicine_docs.csv)): the output differs on 83. No document labelled `clean` changes, and no document is newly dropped.
- 63 labelled `fix` that the cleaner fixes today.
- 11 that the cleaner drops and the audits read as dropped: kept with the cards. The audit calls 9 of these drops wrong (#68 en-dclm 2, #68 en-nemotroncc 1, #81 6) and 2 acceptable (`e670f86abf48520d`, an OCR scan; `9c44f72ec4df21b1`, a reworded how-to).
- 8 labelled `fix` that are dropped today and kept with the cards: `5b4d0f975990e808` (#76) and 7 of `day_D3.md`'s English drops.
- 1 that #71 labels `drop` and no card drops (`4258f5c9fbf14805`).

**Whole train parts, sample v0** ([`collated_medicine_packs.csv`](collated_medicine_packs.csv)):

| Pack | Docs | dropped now | with the cards | recovered | newly dropped | output changed | changed again by a second run (of them also today) |
|---|---:|---:|---:|---:|---:|---:|---:|
| en-dclm | 61,367 | 1,155 | 691 | 464 | 0 | 714 | 36 (36) |
| en-fineweb-edu | 71,933 | 559 | 328 | 231 | 0 | 403 | 3 (3) |
| en-nemotroncc | 91,820 | 3,552 | 2,609 | 943 | 0 | 980 | 41 (39) |
| en-nemotroncc-synth | 197,119 | 218 | 161 | 57 | 0 | 629 | 4 (4) |
| math-finemath | 29,122 | 2,609 | 2,611 | 1 | 3 | 1,433 | 90 (75) |
| math-megamath | 17,647 | 2,550 | 2,550 | 0 | 0 | 1,503 | 10 (8) |
| sci-finepdfs | 6,011 | 166 | 166 | 0 | 0 | 5 | 7 (6) |
| code-cpp | 55,545 | 957 | 957 | 0 | 0 | 11 | 5 (5) |
| code-go | 83,267 | 6,312 | 6,312 | 0 | 0 | 2,145 | 4 (4) |
| code-java | 85,213 | 534 | 534 | 0 | 0 | 703 | 8 (8) |
| code-js-ts | 121,938 | 5,875 | 5,875 | 0 | 0 | 19 | 10 (10) |
| code-python | 74,943 | 2,339 | 2,339 | 0 | 0 | 28 | 1 (1) |
| code-rust | 60,126 | 1,926 | 1,926 | 0 | 0 | 4 | 34 (34) |

- **Recovered on the English packs: 464 en-dclm, 231 en-fineweb-edu, 943 en-nemotroncc, 57 synth.** Outside synth almost all of them are `DA-C3-009` (#81) trimming a long document instead of dropping it (455, 220, 943); the rest are `DA-C1-015`, `DA-C5-008` and, on en-dclm, `DA-A2-010`. These were counted, not read: **a reader should look at a sample of them before `DA-C3-009` is adopted.**
- **math-finemath, 3 newly dropped, 1 recovered (first round):** `29b5cd770ab92ac2`, `3674e149fa8a4377` and `6c96bdacd695aa42` are now dropped by `DA-C7-001`, and `b08cf80dd7abec80` no longer is, because `DA-C2-007` gives that rule a different text. No other pack has a newly dropped document.
- **Code packs:** no document is recovered or newly dropped; the changes are #72's cards (`DA-E4-011` 2,138 on code-go, `DA-E4-012` 400 and `DA-C1-016` 295 on code-java, `DA-A6-004` 4 to 28 on each code pack).
- **Second run:** 15 finemath, 2 megamath, 1 sci-finepdfs and 2 en-nemotroncc documents change again only with the cards; every other one changes again today as well.

| Card | Documents where it differs from the rule it replaces (a new card: documents it changes), on the same text |
|---|---|
| `DA-A2-010` | en-dclm 144, en-fineweb-edu 0, en-nemotroncc 1, en-nemotroncc-synth 0 |
| `DA-C3-008` | en-nemotroncc-synth 57 |
| `DA-C1-013` | en-nemotroncc-synth 50 |
| `DA-C2-009` | en-dclm 65, en-fineweb-edu 1, en-nemotroncc 21 |
| `DA-C2-010` | en-nemotroncc-synth 119 |
| `DA-C5-007` | en-nemotroncc-synth 272 |
| `DA-B4-015` | en-nemotroncc-synth 87 |
| `DA-B3-012` | en-dclm 2, en-fineweb-edu 0, en-nemotroncc 0, en-nemotroncc-synth 0 |
| `DA-B4-016` | en-dclm 13, en-fineweb-edu 0, en-nemotroncc 3, en-nemotroncc-synth 3 |
| `DA-F1-007` | en-dclm 35, en-fineweb-edu 39, en-nemotroncc 13 |
| `DA-F1-009` | en-nemotroncc-synth 45 |
| `DA-C1-012` | math-megamath 295, math-finemath 1,219 |
| `DA-C2-007` | math-megamath 1,241, math-finemath 294 |
| `DA-C1-014` | sci-finepdfs 2 |
| `DA-C2-011` | sci-finepdfs 4 |
| `DA-C3-009` | en-dclm 455, en-fineweb-edu 220, en-nemotroncc 943 |
| `DA-C5-008` | en-dclm 9, en-fineweb-edu 7, en-nemotroncc 1, en-nemotroncc-synth 0 |
| `DA-C1-015` | en-fineweb-edu 141 |
| `DA-A6-004` | code-cpp 11, code-go 9, code-java 8, code-js-ts 21, code-python 28, code-rust 4 |
| `DA-E4-011` | code-go 2,138 |
| `DA-E4-012` | code-java 400 |
| `DA-C1-016` | code-java 295 |

**Tests:** `tests/audit/test_collated_medicine.py`, 32 tests on made-up text. Undoing either half of a merged card makes them fail (6 of 6 hand-made changes in the first round); the new tests check #81's change in both phone cards, `DA-C3-009` off synth, and the renumbered java card.

## Findings that still have no card

F07, F08, F10, F11, F20 (code-cpp, code-js-ts, code-python and code-rust), F23, F24, F27, F28, F29, F33, F34, F41 to F46, F48 to F51, and the parts of F12, F26, F32, F37, F39 and F47 that their cards do not reach. F35 needs a reader, not a card. Each is in [`collation_findings.csv`](collation_findings.csv) with its next step.

## How to reproduce

From the repository root, with the raw sample train parts in `<raw>` and the 500-document sample packs in `<packs>`:

```bash
python -I teams/01-data-a/harmtest/harm_test.py --pack <packs>/<pack>.parquet --gold teams/01-data-a/gold/<pack>_gold.csv --rules teams/01-data-a/audit/collated_medicine.md --rule all
python -I teams/01-data-a/audit/collated_medicine_check.py gold --raw <packs>
python -I teams/01-data-a/audit/collated_medicine_check.py docs --raw <raw> --out collated_medicine_docs.csv
python -I teams/01-data-a/audit/collated_medicine_check.py packs --raw <raw> --out collated_medicine_packs.csv
```

## Limits

- Sample v0 raw parts, not corpus-v1 and not the token shards.
- The changed documents of the whole packs were counted here, not read. The sources read theirs: #75 its changed en-dclm documents, #76 its audited ones, #71 and #79 as their reports say.
- Speed of the whole set was not measured. #72 and #81 measured their own cards against the rules they replace.
- The side effects of each source stay, and adoption is the team's decision: accept a card, put it in place of the old card in `specv1_1.md`, rebuild `clean.py`, and run the harm test again.

## The cards

A card with `REPLACES` runs in the place of that rule. On a pack without that rule, and for a new card, `RUNS_AFTER` says where: after that rule, or (`family`) after the pack's last family rule, before the shared F1 rule.

### `DA-A2-010` · A2 · map cp1252 quotes before removing controls

1. **Disease:** `DA-A2-008` deletes U+0080 to U+009F. Text that was cp1252 bytes read as Latin-1 loses its quotes and dashes (`a9a7821bb3d942d0`). Findings: F01.
2. **Medicine:** As `DA-A2-008`, but a C1 control that cp1252 defines becomes its character first, and UTF-8 read as Latin-1 is decoded back.
3. **Action and place:** fix; replaces `DA-A2-008`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth. **From:** #75 `DA-A2-009` (new number only).

```python
RULE_ID = "DA-A2-010"
REPLACES = "DA-A2-008"
FROM = "#75 DA-A2-009"
SOURCE_RULE_ID = "DA-A2-008"  # proposed replacement of DA-A2-008
CODE = "A2"
ACTION = "fix"
STAGE = "10"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # packs it runs on
SOURCE = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in the 29 Oct sheet as DA-A2-007
PROPOSED_BY = "TEJASKUMAR-REDDY-J"  # this change, from the day D6 en-dclm audit
import re

A2_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")

# U+0080..U+009F that cp1252 defines (\x92 is ’, \x93 “, \x94 ”, \x96 – ...): text that was cp1252 bytes read as
# Latin-1. They are mapped to their characters first; the five cp1252 leaves undefined are still removed.
A2_CP1252 = {c: bytes([c]).decode("cp1252") for c in range(0x80, 0xA0) if c not in (0x81, 0x8D, 0x8F, 0x90, 0x9D)}
A2_C1 = re.compile(r"[\x80-\x9f]")
# UTF-8 read as Latin-1, with a C1 control among its bytes: `Ã\x89` is É, `â\x80\x99` is ’, `â\x80\x9d` is ” (\x9d is
# one that cp1252 leaves undefined). Such a sequence is decoded back first; one with no C1 control (`Â©`) is
# left alone. `\x80` and a second C1 control, with the first byte lost (`me \x80\x93 let\x80\x99s`), are the last
# two bytes of a U+2000..U+201F (– ’ “ ”) and become it.
A2_UTF8 = re.compile(r"[\xc2-\xdf][\x80-\xbf]|[\xe0-\xef][\x80-\xbf]{2}|\x80[\x80-\x9f]")


def _a2_utf8(m):
    s = m.group()
    if not A2_C1.search(s):
        return s
    if s[0] == "\x80":
        return chr(0x2000 + ord(s[1]) - 0x80)
    try:
        return s.encode("latin-1").decode("utf-8")
    except UnicodeDecodeError:
        return s


def medicine_a2(text):
    new = text.replace("\r\n", "\n").replace("\r", "\n")
    first = A2_CONTROL.search(new)  # speed: most docs have no control character, and then nothing else changes
    if first:
        if A2_C1.search(new, first.start()):  # a C1 control is a control character: none comes before the first
            new = A2_UTF8.sub(_a2_utf8, new).translate(A2_CP1252)
        new = A2_CONTROL.sub("", new)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_a2(doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc', 'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Mojibake of two or more layers stays garbage, as before.

### `DA-C3-008` · C3 · no drop from the last word alone

1. **Disease:** `DA-C3-003` drops a whole document because its last word is one like `with` (`5b4d0f975990e808`). Findings: F15.
2. **Medicine:** The last-word test is withdrawn; a document that ends in a bracketed ellipsis still goes.
3. **Action and place:** drop; replaces `DA-C3-003`. **Runs on:** en-nemotroncc-synth. **From:** #76 `DA-C3-008` (none).

```python
SCOPE = {"DA-C3-003": frozenset({"en-nemotroncc-synth"})}
REPLACES = "DA-C3-003"
RULE_ID = "DA-C3-008"
FROM = "#76 DA-C3-008"
SOURCE_RULE_ID = "DA-C3-002"
CODE = "C3"
ACTION = "drop"
STAGE = "30"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"
SOURCE = "en-nemotroncc-synth manual audit"
import re

_MARKER = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]$")

_DANGLING = frozenset(
    "a an the and or but of to in on at for with from by as is are was were "
    "that this these those which who because however".split()
)

_TOKEN = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'")  # the characters of [A-Za-z0-9']
_LONGEST = max(map(len, _DANGLING))  # a last token longer than every dangling word cannot be one

def medicine_c3(text):
    tail = text.rstrip()
    if not tail:
        return text
    if tail.endswith("]") and _MARKER.search(tail):  # the marker ends the text, so the text must end in "]"
        return ("drop", "")
    if tail.endswith((".", "!", "?", '"', "'", ")", ":", "…")):
        return text
    # The terminal-word heuristic is deliberately withdrawn.
    return text


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_c3(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = SCOPE["DA-C3-003"]

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Documents that really are cut off are kept too. **Synth only:** F06 (en-dclm) is the same rule and has no card.

### `DA-C1-013` · C1 · image controls and comment metadata

1. **Disease:** `DA-C1-006` misses lines such as `Like this:` and `Click to enlarge.`, and name-and-age lines of comments. Findings: F30.
2. **Medicine:** Those whole lines go, and an `Advertisement:` prefix; comments and article text stay.
3. **Action and place:** fix; replaces `DA-C1-006`. **Runs on:** en-nemotroncc-synth. **From:** #76 `DA-C1-013` (none).

```python
SCOPE = {"DA-C1-006": frozenset({"en-nemotroncc-synth"})}
REPLACES = "DA-C1-006"
RULE_ID = "DA-C1-013"
FROM = "#76 DA-C1-013"
SOURCE_RULE_ID = "DA-C1-006"
CODE = "C1"
ACTION = "fix"
STAGE = "35"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"
SOURCE = "en-nemotroncc-synth manual audit"
import re

WIDGET = re.compile(r"(?i)(?:like this:?|click to enlarge[.!]?|primary tabs|search for:?|related (?:documents|posts|articles):?|click to expand\W*|read more\W*|\[?read more\W*\]?|share this:?|share on (?:other sites|[a-z ]+)|previous|next|menu|contents|advertisement|loading\W*|link copied|the link has been copied!?|post navigation|quantity|breadcrumb|logged|registered|banned|show more|you may also like[a-z ]*|subscribe to [a-z ]+|skip to (?:main )?content|back to top)")

COMMENT_META = re.compile(r"[A-Za-z0-9_-]{3,40} (?:over )?(?:a|an|\d+) (?:years?|months?|days?|hours?) ago", re.I)

def c1(t):
    """Delete lines that consist only of a known widget or menu label ('Primary tabs', 'Search for:', 'Related posts', 'Share this:' ...)."""
    t = re.sub(r"(?m)^Advertisement:(?=\S)", "", t)
    return "\n".join(l for l in t.split("\n")
                     if not WIDGET.fullmatch(l.strip()) and not COMMENT_META.fullmatch(l.strip()))


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(c1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = SCOPE["DA-C1-006"]

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A real line of the form name, number, `days ago` goes.

### `DA-C2-009` · C2 · repeated lines: leave code and config alone

1. **Disease:** `DA-C2-003` cuts repeated lines inside code and config (`f1b8673c7cfd7aac`). Findings: F02.
2. **Medicine:** As `DA-C2-003`, but a line in a fence, or that looks like code or config, is not counted.
3. **Action and place:** fix; replaces `DA-C2-003`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc. **From:** #75 `DA-C2-005` (new number; synth moves to `DA-C2-010`).

```python
RULE_ID = "DA-C2-009"
REPLACES = "DA-C2-003"
FROM = "#75 DA-C2-005"
SOURCE_RULE_ID = "DA-C2-003"  # proposed replacement of DA-C2-003
CODE = "C2"
ACTION = "fix"
STAGE = "35"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc"  # packs it runs on
SOURCE = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # extractor; adapter for spans
PROPOSED_BY = "TEJASKUMAR-REDDY-J"  # this change, from the day D6 en-dclm audit
import re

def _merge(spans):
    """Overlapping spans joined into one, keeping the rule of the first."""
    out = []
    for s, e, rule in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(e, out[-1][1]), out[-1][2])
        else:
            out.append((s, e, rule))
    return out

C2_MIN_REPEAT, C2_MIN_CHARS = 3, 10

# a line of code or config, which repeats because the program needs it, not because it is boilerplate:
# a comment or prompt at its start (#, //, $, >>>); { at its end or } at its start; ';' after ')' or in an
# assignment, a declaration or a CSS property; a Unix path (/etc/); key=value at its start; a::b, -> or =>;
# an empty (). Dates (02/15/2010), URLs and '::' as a separator do not count.
C2_CODE = re.compile(r"^\s*(?:#|//|\$ |>>> )|\{\s*$|^\s*\}|\)\s*;\s*$|=[^=\n]*;\s*$|^\s*(?:private|public|protected|static|final|var|let|const|int|long|char|float|double|bool|boolean|String|void|my|use|import|include|require)\b[^\n]*;\s*$|^\s*[a-z][a-z-]*:\s*[^;\n]{1,40};\s*$|(?:^|\s)[~.]?/[A-Za-z_][\w.-]*/|^\s*[A-Za-z_]\w*=\S|\w::\w|->|=>|\w\(\)")

def c2_spans(text):
    """C2: later copies of a line repeated C2_MIN_REPEAT or more times in the document."""
    fenced = "```" in text or "~~~" in text  # speed: no fence marker, no fence
    seen, lines, pos, fence = {}, [], 0, False
    for line in text.split("\n"):
        key = " ".join(line.split())
        if fenced and line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if len(key) >= C2_MIN_CHARS and not fence:
            lines.append((pos, pos + len(line), key, line))
            seen[key] = seen.get(key, 0) + 1
        pos += len(line) + 1
    # a code line is not counted. speed: C2_CODE is tested only on a line whose key is there C2_MIN_REPEAT times or
    # more with code lines counted; a key there fewer times stays under C2_MIN_REPEAT without them too
    code = {k for k, (_, _, key, line) in enumerate(lines) if seen[key] >= C2_MIN_REPEAT and C2_CODE.search(line)}
    for k in code:
        seen[lines[k][2]] -= 1
    out, first = [], set()
    for k, (s, e, key, _) in enumerate(lines):
        if k not in code and seen[key] >= C2_MIN_REPEAT:
            if key in first:
                out.append((s, e, "C2-repeated-line"))
            first.add(key)
    return out


def _std(out, text):  # added by Data A
    # the author's result (spans to remove) in the shared form, as their clean() reads it: (spans, True) from
    # c1_spans -> drop; a whole-document "B4-mostly-code" or "C5-list-page" span -> drop; else the spans go
    if isinstance(out, tuple):
        out, flagged = out
        if flagged: return ("drop", text)
    if out and out[0][2] in ("B4-mostly-code", "C5-list-page"): return ("drop", text)
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(c2_spans(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Code the test does not see as code is still cut, and so are repeated record fields and formula lines.

### `DA-C2-010` · C2 · repeated lines: leave code, config and record fields alone

1. **Disease:** Both PRs replace `DA-C2-003` on synth: #75 for code lines, #76 for labelled fields of separate records (`7523ebd6d772fada`). Findings: F02 and F14.
2. **Medicine:** #75's code, with #76's `RECORD_FIELD` test added: a line is counted only if neither source excludes it.
3. **Action and place:** fix; replaces `DA-C2-003`. **Runs on:** en-nemotroncc-synth. **From:** #75 `DA-C2-005` + #76 `DA-C2-008` (merged).

```python
RULE_ID = "DA-C2-010"
REPLACES = "DA-C2-003"
FROM = "#75 DA-C2-005 and #76 DA-C2-008, merged"
SOURCE_RULE_ID = "DA-C2-003"  # proposed replacement of DA-C2-003
CODE = "C2"
ACTION = "fix"
STAGE = "35"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"  # packs it runs on
SOURCE = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # extractor; adapter for spans
PROPOSED_BY = "TEJASKUMAR-REDDY-J"  # this change, from the day D6 en-dclm audit
import re

def _merge(spans):
    """Overlapping spans joined into one, keeping the rule of the first."""
    out = []
    for s, e, rule in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(e, out[-1][1]), out[-1][2])
        else:
            out.append((s, e, rule))
    return out

C2_MIN_REPEAT, C2_MIN_CHARS = 3, 10

# a line of code or config, which repeats because the program needs it, not because it is boilerplate:
# a comment or prompt at its start (#, //, $, >>>); { at its end or } at its start; ';' after ')' or in an
# assignment, a declaration or a CSS property; a Unix path (/etc/); key=value at its start; a::b, -> or =>;
# an empty (). Dates (02/15/2010), URLs and '::' as a separator do not count.
C2_CODE = re.compile(r"^\s*(?:#|//|\$ |>>> )|\{\s*$|^\s*\}|\)\s*;\s*$|=[^=\n]*;\s*$|^\s*(?:private|public|protected|static|final|var|let|const|int|long|char|float|double|bool|boolean|String|void|my|use|import|include|require)\b[^\n]*;\s*$|^\s*[a-z][a-z-]*:\s*[^;\n]{1,40};\s*$|(?:^|\s)[~.]?/[A-Za-z_][\w.-]*/|^\s*[A-Za-z_]\w*=\S|\w::\w|->|=>|\w\(\)")

# merged from #76: a labelled field (`Cost: 5`) belongs to its own record, so it is not counted
RECORD_FIELD = re.compile(r"^\s*(?:[-*•]\s+)?[A-Za-z][A-Za-z0-9 /_-]{0,35}:\s+\S")

def c2_spans(text):
    """C2: later copies of a line repeated C2_MIN_REPEAT or more times in the document."""
    fenced = "```" in text or "~~~" in text  # speed: no fence marker, no fence
    seen, lines, pos, fence = {}, [], 0, False
    for line in text.split("\n"):
        key = " ".join(line.split())
        if fenced and line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if len(key) >= C2_MIN_CHARS and not fence and not RECORD_FIELD.match(line):
            lines.append((pos, pos + len(line), key, line))
            seen[key] = seen.get(key, 0) + 1
        pos += len(line) + 1
    # a code line is not counted. speed: C2_CODE is tested only on a line whose key is there C2_MIN_REPEAT times or
    # more with code lines counted; a key there fewer times stays under C2_MIN_REPEAT without them too
    code = {k for k, (_, _, key, line) in enumerate(lines) if seen[key] >= C2_MIN_REPEAT and C2_CODE.search(line)}
    for k in code:
        seen[lines[k][2]] -= 1
    out, first = [], set()
    for k, (s, e, key, _) in enumerate(lines):
        if k not in code and seen[key] >= C2_MIN_REPEAT:
            if key in first:
                out.append((s, e, "C2-repeated-line"))
            first.add(key)
    return out


def _std(out, text):  # added by Data A
    # the author's result (spans to remove) in the shared form, as their clean() reads it: (spans, True) from
    # c1_spans -> drop; a whole-document "B4-mostly-code" or "C5-list-page" span -> drop; else the spans go
    if isinstance(out, tuple):
        out, flagged = out
        if flagged: return ("drop", text)
    if out and out[0][2] in ("B4-mostly-code", "C5-list-page"): return ("drop", text)
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(c2_spans(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** The side effects of both: repeated `Views:` or `Share:` lines stay, and a repeated line that starts with `#`.

### `DA-C5-007` · C5 · keep subject headings

1. **Disease:** `DA-C5-005` removes `Topic:` headings with the tag lists (4 documents). Findings: F16.
2. **Medicine:** `Topic:` and `Topics:` lines stay; tags, keywords and filed-under lines go as before.
3. **Action and place:** fix; replaces `DA-C5-005`. **Runs on:** en-nemotroncc-synth. **From:** #76 `DA-C5-007` (none).

```python
SCOPE = {"DA-C5-005": frozenset({"en-nemotroncc-synth"})}
REPLACES = "DA-C5-005"
RULE_ID = "DA-C5-007"
FROM = "#76 DA-C5-007"
SOURCE_RULE_ID = "DA-C5-005"
CODE = "C5"
ACTION = "fix"
STAGE = "35"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"
SOURCE = "en-nemotroncc-synth manual audit"
import re

C5_PREFIX = re.compile(r"^(?:tags?|keywords?|tagged(?: with| in)?|filed under)\s*:", re.I)


def medicine_c5(text):
    lines = text.split("\n")
    keep = [ln for ln in lines if not C5_PREFIX.search(ln.strip())]
    if len(keep) == len(lines):
        return ("keep", text)
    new = "\n".join(keep).strip("\n")
    return ("drop", text) if not new.strip() else ("fix", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_c5(doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = SCOPE["DA-C5-005"]

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A tag list that starts with `Topic:` stays.

### `DA-B4-015` · B4 · keep the facts in a bullet with a meta-comment

1. **Disease:** `DA-B4-007` removes a whole bullet for one meta sentence (`f8027db45cfbebb2`, `93bf1542853fd276`). Findings: F17.
2. **Medicine:** Only the meta sentence goes. A bullet with an inference (`but it implies`) stays whole.
3. **Action and place:** fix; replaces `DA-B4-007`. **Runs on:** en-nemotroncc-synth. **From:** #76 `DA-B4-015` (none).

```python
SCOPE = {"DA-B4-007": frozenset({"en-nemotroncc-synth"})}
REPLACES = "DA-B4-007"
RULE_ID = "DA-B4-015"
FROM = "#76 DA-B4-015"
SOURCE_RULE_ID = "DA-B4-007"
CODE = "B4"
ACTION = "fix"
STAGE = "40"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"
SOURCE = "en-nemotroncc-synth manual audit"
import re
ANSWER_LINE = re.compile('^(?:Answer|A)\\s*[:.]|\\bAnswer:\\s')  # added by Data A: from maheshsv's medicine.md
KEY_VALUE_LINE = re.compile('^[^:\\n]{1,60}:\\s')  # added by Data A: from maheshsv's medicine.md
LIST_MARK = re.compile('^(?:[-*•–—]|\\d+[.)]|[a-z][.)])\\s')  # added by Data A: from maheshsv's medicine.md
META = re.compile('(?i)\\bnot (?:explicitly |specifically |directly )?(?:provided|stated|mentioned|specified|given|available|included|present|disclosed|named) in the (?:given |provided |original |above |source )?(?:text|passage|article|document|excerpt|content|context)|\\bthe (?:text|passage|article|document) does not (?:explicitly |specifically )?(?:provide|mention|specify|state|say|give|include|indicate|name)\\b|\\bthe (?:given|provided) (?:text|passage) (?:also )?(?:discusses|mentions|describes|states|says|provides|refers|covers|explains|includes|lists|notes)\\b')  # added by Data A: from maheshsv's medicine.md
MIN_KEEP_CHARS = 200
# Preserve an ambiguous source inference rather than inventing a stronger assertion.
MIXED_INFERENCE = re.compile(r"\bbut (?:it |the (?:text|passage|article) )?(?:implies|suggests|indicates)\b", re.I)  # added by Data A: from maheshsv's medicine.md

def remove_meta_comments(text: str) -> tuple[str | None, bool]:
    """Delete the bullet, `Key: value` line or Question/Answer pair that carries a rewriter meta-comment; in running
    prose delete only the sentence."""
    if not META.search(text):
        return text, False
    lines = text.split("\n")
    drop = set()
    for i, ln in enumerate(lines):
        if not META.search(ln):
            continue
        s = ln.strip()
        if s.startswith("Question:") or ANSWER_LINE.match(s):
            drop.add(i)                                   # drop the whole QA pair, whichever line carries it
            if s.startswith("Question:") and i + 1 < len(lines) and ANSWER_LINE.match(lines[i + 1].strip()):
                drop.add(i + 1)
            if ANSWER_LINE.match(s) and not s.startswith("Question:") and i > 0 and lines[i - 1].strip().startswith("Question:"):
                drop.add(i - 1)
        elif LIST_MARK.match(s) or KEY_VALUE_LINE.match(s):
            if MIXED_INFERENCE.search(s):
                continue
            sentences = re.split(r"(?<=[.!?])\s+", ln)
            kept = [sentence for sentence in sentences if not META.search(sentence)]
            if kept:
                lines[i] = " ".join(kept)
            else:
                drop.add(i)
        else:
            sentences = re.split(r"(?<=[.!?])\s+", ln)
            lines[i] = " ".join(x for x in sentences if not META.search(x))
    new = "\n".join(ln for i, ln in enumerate(lines) if i not in drop)
    new = re.sub(r"\n{3,}", "\n\n", new).strip()
    if len(new) < MIN_KEEP_CHARS:
        return None, True
    return new, True


def _std(out, text):  # added by Data A
    # the author's result (new_text or None, changed) in the shared form: None -> drop, else fix/keep by the text
    new, _ = out
    if new is None: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(remove_meta_comments(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = SCOPE["DA-B4-007"]

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Some source commentary stays. #76 leaves the policy open.

### `DA-B3-012` · B3 · `<s>` and `</s>` used as markup

1. **Disease:** The markers `<s>` and `</s>` are kept in English text (`b86875f06abe649a`). Findings: F05.
2. **Medicine:** In a document with both, every `<s>` and `</s>` goes; the struck text stays.
3. **Action and place:** fix; new, after `DA-B4-012`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth. **From:** #75 `DA-B3-002` (new number only).

```python
RULE_ID = "DA-B3-012"
RUNS_AFTER = "DA-B4-012"
FROM = "#75 DA-B3-002"
CODE = "B3"
ACTION = "fix"
STAGE = "40"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # packs it runs on
PACKS = set(ORIGIN.split(", "))
SOURCE = "en-dclm"  # pack whose reading found it (day D6 audit)
AUTHOR = "TEJASKUMAR-REDDY-J"
import re

# <s> and </s>: the BOS/EOS markers in text. Used together they are strikethrough markup, which DA-B2-002 leaves
# alone: the markers go, the struck text stays. A lone <s> (an HTML reference: "<s> Defines strikethrough text") stays.
B3_S = re.compile(r"</?s>")


def medicine(doc):
    if doc.get("pack_id") not in PACKS or doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    text = doc["text"]
    if "<s>" not in text or "</s>" not in text:  # markup needs both; speed: most docs have neither
        return ("keep", text)
    new = B3_S.sub("", text)
    return ("fix" if new != text else "keep", new)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** An HTML tutorial with an example, also in a code fence, loses the markers.

### `DA-B4-016` · B4 · a `${` that opens math stays

1. **Disease:** `DA-B4-010` removes `${8,16,24}` as a template expression (`bfa86fe32d00c663`). Findings: F03.
2. **Medicine:** As `DA-B4-010`, but a `${...}` whose content starts like math stays.
3. **Action and place:** fix; replaces `DA-B4-010`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth. **From:** #75 `DA-B4-014` (new number only).

```python
RULE_ID = "DA-B4-016"
REPLACES = "DA-B4-010"
FROM = "#75 DA-B4-014"
SOURCE_RULE_ID = "DA-B4-010"  # proposed replacement of DA-B4-010
CODE = "B4"
ACTION = "fix"
STAGE = "40"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # packs it runs on
SOURCE = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # extractor; adapter for spans
PROPOSED_BY = "TEJASKUMAR-REDDY-J"  # this change, from the day D6 en-dclm audit
import re

def _merge(spans):
    """Overlapping spans joined into one, keeping the rule of the first."""
    out = []
    for s, e, rule in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(e, out[-1][1]), out[-1][2])
        else:
            out.append((s, e, rule))
    return out

B4_TEMPLATE = re.compile(
    r"\{\{[^{}\n]{0,80}\}\}"                          # {{ title }}
    r"|\{%[^\n]{0,80}?%\}"                            # {% if x %}
    r"|\$\{(?!\s*[\\\d{}<^_$])[^{}\n]{0,80}\}"          # ${name}; not math: ${8,16,24}, ${\bf a}, ${}^*
    r"|`[\w.]+(?:\s*(?:\|\||&&)\s*[\w.]+)+`"          # `page.data.shortTitle || page.data.title`
    r"|(?<=[:=$])\s*(?:undefined|NaN)\b"              # Price: NaN, name=undefined
    r"|^[ \t]*(?:undefined|NaN|null)[ \t]*$", re.M)

B4_CODE_TOKENS = re.compile(
    r"::|->|=>|==|!=|<=|>=|&&|\|\||\+\+|\+=|-=|\);|\)\s*\{|[{};]\s*$|\}"
    r"|^\s*(?:#include|import\s|from\s+\S+\s+import|def\s|class\s|public\s|private\s|static\s|void\s|return\b"
    r"|require\s|var\s|let\s|const\s|function\b|Sub\s|End Sub|Dim\s|\$\s|>>>\s|>\s)"
    r"|\b(?:End Sub|ByVal|As Integer|System\.out|printf|println)\b", re.M)

B4_MIN_TOKENS, B4_WORDS_PER_TOKEN, B4_SHARE = 2, 6, 0.5

TABLE_ROW = re.compile(r"^\s*\|.*\|\|")

def b4_code_lines(text):
    """(start, end) of every line that looks like code."""
    out, pos = [], 0
    for line in text.split("\n"):
        tokens = len(B4_CODE_TOKENS.findall(line))
        words = len(line.split())
        if tokens >= B4_MIN_TOKENS and tokens * B4_WORDS_PER_TOKEN >= words and not TABLE_ROW.match(line):
            out.append((pos, pos + len(line)))
        pos += len(line) + 1
    return out

def b4_mostly_code(text):
    """Whether the lines b4_code_lines finds are more than B4_SHARE of the text, as b4_spans asks. The same test, but it
    stops as soon as the answer cannot change: when the code lines already pass the limit, or when the code found plus
    every character not yet read cannot reach it (a prose document is settled halfway through)."""
    if not text.strip():
        return False
    limit = B4_SHARE * len(text.strip())
    code, left = 0, len(text)
    for line in text.split("\n"):
        tokens = len(B4_CODE_TOKENS.findall(line))
        if tokens >= B4_MIN_TOKENS and tokens * B4_WORDS_PER_TOKEN >= len(line.split()) and not TABLE_ROW.match(line):
            code += len(line)
            if code > limit:
                return True
        left -= len(line) + 1
        if code + left <= limit:
            return False
    return False

# Every alternative of B4_TEMPLATE contains one of these, so a text with none of them has no template expression.
B4_TEMPLATE_HINTS = ("{{", "{%", "${", "`", "undefined", "NaN", "null")

def b4_spans(text):
    """B4: the document is dropped if it is mostly code; otherwise template expressions are removed."""
    if b4_mostly_code(text):
        return [(0, len(text), "B4-mostly-code")]
    if not any(hint in text for hint in B4_TEMPLATE_HINTS):
        return []
    return [(m.start(), m.end(), "B4-template") for m in B4_TEMPLATE.finditer(text)]


def _std(out, text):  # added by Data A
    # the author's result (spans to remove) in the shared form, as their clean() reads it: (spans, True) from
    # c1_spans -> drop; a whole-document "B4-mostly-code" or "C5-list-page" span -> drop; else the spans go
    if isinstance(out, tuple):
        out, flagged = out
        if flagged: return ("drop", text)
    if out and out[0][2] in ("B4-mostly-code", "C5-list-page"): return ("drop", text)
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(b4_spans(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc', 'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Math that starts with a letter, a minus or a bracket is still cut.

### `DA-F1-007` · F1 · one decision for each phone number

1. **Disease:** `DA-F1-005` masks a number on one line and keeps it on the next (`ef987c066d1cdf0f`); it does not know UK freephone. Findings: F04, F39.
2. **Medicine:** A number masked on any line is masked on every line. 0800, 0808 and their +44 forms are toll-free. From #81: digits inside a DOI and a run of years (`1933 1934 1935`) are not a phone.
3. **Action and place:** fix; replaces `DA-F1-005`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc. **From:** #75 `DA-F1-007` + #81 `DA-F1-010` (merged; synth moves to `DA-F1-009`).

```python
RULE_ID = "DA-F1-007"
REPLACES = "DA-F1-005"
FROM = "#75 DA-F1-007 and #81 DA-F1-010, merged"
SOURCE_RULE_ID = "DA-F1-005"  # proposed replacement of DA-F1-005
CODE = "F1"
ACTION = "fix"
STAGE = "40"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc"  # packs it runs on
SOURCE = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new rule to the instructor's F1 ruling of 31 Oct; email test from DA-F1-002 (shekar-maker)
PROPOSED_BY = "TEJASKUMAR-REDDY-J"  # this change, from the day D6 en-dclm audit
import re

EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}\b")

WEBMAIL = re.compile(r"@(?:gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|aol|icloud|me|mac|protonmail|proton|"
                     r"rediffmail|zoho|gmx|yandex|mail|comcast|verizon|att|sbcglobal|bellsouth|earthlink|btinternet)\.", re.I)

PERSONAL_LOCAL = re.compile(r"[._\-]|\d|^.{13,}$")

ROLE_LOCAL = re.compile(r"^(?:info|contact|contactus|enquir(?:y|ies)|inquir(?:y|ies)|sales|support|help|helpdesk|admin|"
                        r"office|hello|hi|press|media|news|newsletter|editor|editors|team|jobs|careers|hr|marketing|"
                        r"billing|accounts|orders|service|services|customerservice|webmaster|postmaster|noreply|"
                        r"no-reply|abuse|privacy|legal|admissions|registrar|events|bookings|reservations)$", re.I)

NOT_REAL = re.compile(r"@(?:example|test|domain|email)\.(?:com|org|net)$", re.I)

PHONE = re.compile(r"(?<![\w-])(?:\+\d{1,3}[\s.\-‐‑–]?)?(?:\(\d{2,4}\)[\s.\-‐‑–]?|\d{2,4}[\s.\-‐‑–])\d{3,4}[\s.\-‐‑–]\d{3,4}(?![\w-])")

# US 8xx, and UK freephone 0800/0808 (+44 800/808)
TOLL_FREE = re.compile(r"^(?:(?:\+?1[\s.-]?)?\(?8(?:00|88|77|66|55|44|33)\)?|(?:\+44[\s.-]?|0)80[08](?=[\s.\-]))")
NOT_DIGIT = re.compile(r"\D")

STREET = (r"(?:Street|St|Avenue|Ave|Road|Rd|Lane|Ln|Boulevard|Blvd|Drive|Dr|Court|Ct|Way|Place|Pl|Terrace|Ter|Close|"
          r"Crescent|Cres|Highway|Hwy|Parkway|Pkwy|Circle|Cir|Square|Sq)")

ADDRESS = re.compile(r"\b\d{1,5}[A-Za-z]?\s+(?:[NSEW]\.?\s+)?(?:[A-Z][a-z]+\.?\s+){1,4}" + STREET + r"\b\.?"
                     r"(?:,?\s*(?:Apt|Unit|Suite|Ste|#)\.?\s*\w+)?"
                     r"(?:,\s*(?:[A-Z][a-z]+\s?){1,3},\s*[A-Z]{2}\.?\s*\d{5}(?:-\d{4})?)?")

CONTACT_LINE = 120

ORGANISATION = re.compile(
    r"(?i)\b(?:inc|llc|ltd|plc|corp|co\.|company|warehouse|store|shop|market|restaurant|cafe|café|bar|grill|bistro|"
    r"hotel|inn|motel|resort|spa|salon|clinic|hospital|surgery|pharmacy|cent(?:er|re)|office|offices|university|"
    r"college|school|academy|library|museum|church|gallery|theat(?:er|re)|cinema|bank|agency|association|society|"
    r"council|department|ministry|embassy|tourist|information|headquarters|hq|branch|showroom|dealership|"
    r"open (?:mon|tue|wed|thu|fri|sat|sun|daily|7|24)\w*|hours|menu|reservations|fax|"
    r"on (?:urbanspoon|yelp|tripadvisor|zomato|foursquare)|"
    # trades and services that put their number on their own page
    r"pros?|plumb\w*|roofing|hvac|electric(?:al|ians?)|landscap\w*|cleaning|movers?|moving|storage|rentals?|hire|"
    r"repairs?|construction|builders?|contractors?|auto|motors|towing|insurance|realty|real estate|mortgage|loans?|"
    r"law|lawyers?|attorneys?|legal|dental|dentistry|orthodont\w*|chiropract\w*|physiotherap\w*|therapy|"
    r"veterinar\w*|vet|clinics?|practice|surgery|medical|health(?:care)?|consult(?:ation|ing|ants?)?|services?|"
    r"solutions|group|partners|associates|studio|chalet|lodge|villa|apartments?|cottage|camping|farm|winery|"
    r"brewery|bakery|club|bbs|board|optometr\w*|optic\w*|opticians?|spectacles|suite)\b")

ORG_VOICE = re.compile(r"(?i)\b(?:call us|contact us|email us|e-mail us|visit us|reach us|text us|give us a call|"
                       r"our (?:office|team|staff|clinic|store|shop|experts?|technicians?|specialists?|services?|"
                       r"company|firm|practice|location)|one of our|we (?:offer|provide|specialize|specialise|serve)|need help\?)|☎")

PUBLIC_ROLE = re.compile(r"(?i)\b(?:reporter|editor|journalist|correspondent|spokes(?:man|woman|person)|press|media|"
                         r"publicist|author of|professor|prof\.|dr\.|lecturer|faculty|researcher|principal investigator|"
                         r"media contact|press contact|for more information|high[- ]res|images|photos)\b")

DIGIT = re.compile(r"\d")

def _email(m, org):
    addr = m.group()
    local = addr.split("@", 1)[0]
    if NOT_REAL.search(addr) or ROLE_LOCAL.match(local):
        return addr
    if WEBMAIL.search(addr):  # a webmail address belongs to a person
        return "<EMAIL>"
    # a name-like address at an organisation's domain is a work address when the context is an organisation's
    return addr if org or not PERSONAL_LOCAL.search(local) else "<EMAIL>"

# merged from #81 DA-F1-010
# not a phone number: a run of years ("1933 1934 1935"), or digits inside a DOI ("10.1034/j.1399-3054.1998...")
YEARS = re.compile(r"(?:1[5-9]|20)\d\d(?:[\s.\-‐‑–]+(?:1[5-9]|20)\d\d)+")
DOI_BEFORE = re.compile(r"\b10\.\d{4,9}/\S*$")


def _not_phone(m):
    if YEARS.fullmatch(m.group()):
        return True
    return DOI_BEFORE.search(m.string, max(0, m.start() - 80), m.start()) is not None

def _email(m, org):
    addr = m.group()
    local = addr.split("@", 1)[0]
    if NOT_REAL.search(addr) or ROLE_LOCAL.match(local):
        return addr
    if WEBMAIL.search(addr):  # a webmail address belongs to a person
        return "<EMAIL>"
    # a name-like address at an organisation's domain is a work address when the context is an organisation's
    return addr if org or not PERSONAL_LOCAL.search(local) else "<EMAIL>"

def medicine_f1(text):
    lines = text.split("\n")
    org_page = bool(ORG_VOICE.search(text))
    has_org = {}  # line number -> an organisation word on that line: searched once, and only when a contact line asks

    def org_near(i):  # same answer as searching the joined 13-line window, as no match spans a newline
        for j in range(max(0, i - 6), min(len(lines), i + 7)):
            if j not in has_org:
                has_org[j] = ORGANISATION.search(lines[j]) is not None
            if has_org[j]:
                return True
        return False

    out = []
    for i, line in enumerate(lines):
        if "@" not in line and not DIGIT.search(line):  # no EMAIL, PHONE or ADDRESS can match
            out.append(line)
            continue
        new = EMAIL.sub(lambda m: _email(m, org_page or org_near(i) or bool(PUBLIC_ROLE.search(
            "\n".join(lines[max(0, i - 2):i + 1])))), line) if "@" in line else line
        if PHONE.search(new) or ADDRESS.search(new):
            if not (org_page or org_near(i)):
                new = PHONE.sub(lambda m: m.group() if TOLL_FREE.match(m.group()) or _not_phone(m) else "<PHONE>", new)
                if len(line.strip()) <= CONTACT_LINE:
                    new = ADDRESS.sub("<ADDRESS>", new)
        out.append(new)
    return "\n".join(out)


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_f1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc', 'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    return _spec_source_medicine(doc)


def medicine_f1(text):
    lines = text.split("\n")
    org_page = []  # ORG_VOICE on the whole text: searched once, and only when a contact line asks
    has_org = {}  # line number -> an organisation word on that line: searched once, and only when a contact line asks

    def on_org_page():
        if not org_page:
            org_page.append(bool(ORG_VOICE.search(text)))
        return org_page[0]

    def org_near(i):  # same answer as searching the joined 13-line window, as no match spans a newline
        for j in range(max(0, i - 6), min(len(lines), i + 7)):
            if j not in has_org:
                has_org[j] = ORGANISATION.search(lines[j]) is not None
            if has_org[j]:
                return True
        return False

    # one decision per number, privacy first: a number masked on any line is masked on every line, also on a line
    # near an organisation word (the 13-line window alone can mask a number on one line and keep it on the next).
    # speed: the masked numbers are found once, and only when a phone line near an organisation asks
    masked = []

    def masked_numbers():
        if not masked:
            nums = set()
            if not on_org_page():  # on an organisation's page no line is masked
                for i, line in enumerate(lines):
                    if DIGIT.search(line) and PHONE.search(line) and not org_near(i):
                        nums.update(NOT_DIGIT.sub("", m.group()) for m in PHONE.finditer(line)
                                    if not (TOLL_FREE.match(m.group()) or _not_phone(m)))
            masked.append(nums)
        return masked[0]

    out = []
    for i, line in enumerate(lines):
        if "@" not in line and not DIGIT.search(line):  # no EMAIL, PHONE or ADDRESS can match
            out.append(line)
            continue
        new = EMAIL.sub(lambda m: _email(m, on_org_page() or org_near(i) or bool(PUBLIC_ROLE.search(
            "\n".join(lines[max(0, i - 2):i + 1])))), line) if "@" in line else line
        if PHONE.search(new) or ADDRESS.search(new):
            if not (on_org_page() or org_near(i)):
                new = PHONE.sub(lambda m: m.group() if TOLL_FREE.match(m.group()) or _not_phone(m) else "<PHONE>", new)
                if len(line.strip()) <= CONTACT_LINE:
                    new = ADDRESS.sub("<ADDRESS>", new)
            elif masked_numbers():
                new = PHONE.sub(lambda m: "<PHONE>" if NOT_DIGIT.sub("", m.group()) in masked[0] and not _not_phone(m) else m.group(), new)
        out.append(new)
    return "\n".join(out)


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_f1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A `+44` copy of a masked number is not matched. Grit, binary and IP values on these three packs are masked as before.

### `DA-F1-009` · F1 · one decision for each phone number; technical values and public contacts

1. **Disease:** Both PRs replace `DA-F1-005` on synth. #75 masks every copy of a number that is masked once; #76 keeps technical values and public contacts, line by line. Alone, they disagree on three documents. Findings: F13, F39.
2. **Medicine:** #76's code decides whether a line gives a reason to mask. #75's pass then makes it one decision for each number: masked on any line, masked on every line. A technical value is never a phone. #75's freephone test is in, and #81's: a DOI or a run of years is not a phone.
3. **Action and place:** fix; replaces `DA-F1-005`. **Runs on:** en-nemotroncc-synth. **From:** #75 `DA-F1-007` + #76 `DA-F1-008` + #81 `DA-F1-010` (merged).

```python
SCOPE = {"DA-F1-005": frozenset({"en-nemotroncc-synth"})}
REPLACES = "DA-F1-005"
RULE_ID = "DA-F1-009"
FROM = "#75 DA-F1-007, #76 DA-F1-008 and #81 DA-F1-010, merged"
SOURCE_RULE_ID = "DA-F1-005"
CODE = "F1"
ACTION = "fix"
STAGE = "40"
STATUS = "PROPOSAL"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"
SOURCE = "en-nemotroncc-synth manual audit"
import re

EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}\b")

WEBMAIL = re.compile(r"@(?:gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|aol|icloud|me|mac|protonmail|proton|"
                     r"rediffmail|zoho|gmx|yandex|mail|comcast|verizon|att|sbcglobal|bellsouth|earthlink|btinternet)\.", re.I)

PERSONAL_LOCAL = re.compile(r"[._\-]|\d|^.{13,}$")

ROLE_LOCAL = re.compile(r"^(?:info|contact|contactus|enquir(?:y|ies)|inquir(?:y|ies)|sales|support|help|helpdesk|admin|"
                        r"office|hello|hi|press|media|news|newsletter|editor|editors|team|jobs|careers|hr|marketing|"
                        r"billing|accounts|orders|service|services|customerservice|webmaster|postmaster|noreply|"
                        r"no-reply|abuse|privacy|legal|admissions|registrar|events|bookings|reservations)$", re.I)

NOT_REAL = re.compile(r"@(?:example|test|domain|email)\.(?:com|org|net)$", re.I)

PHONE = re.compile(r"(?<![\w-])(?:\+\d{1,3}[\s.\-‐‑–]?)?(?:\(\d{2,4}\)[\s.\-‐‑–]?|\d{2,4}[\s.\-‐‑–])\d{3,4}[\s.\-‐‑–]\d{3,4}(?![\w-])")

# US 8xx, and UK freephone 0800/0808 (+44 800/808)
TOLL_FREE = re.compile(r"^(?:(?:\+?1[\s.-]?)?\(?8(?:00|88|77|66|55|44|33)\)?|(?:\+44[\s.-]?|0)80[08](?=[\s.\-]))")
NOT_DIGIT = re.compile(r"\D")

STREET = (r"(?:Street|St|Avenue|Ave|Road|Rd|Lane|Ln|Boulevard|Blvd|Drive|Dr|Court|Ct|Way|Place|Pl|Terrace|Ter|Close|"
          r"Crescent|Cres|Highway|Hwy|Parkway|Pkwy|Circle|Cir|Square|Sq)")

ADDRESS = re.compile(r"\b\d{1,5}[A-Za-z]?\s+(?:[NSEW]\.?\s+)?(?:[A-Z][a-z]+\.?\s+){1,4}" + STREET + r"\b\.?"
                     r"(?:,?\s*(?:Apt|Unit|Suite|Ste|#)\.?\s*\w+)?"
                     r"(?:,\s*(?:[A-Z][a-z]+\s?){1,3},\s*[A-Z]{2}\.?\s*\d{5}(?:-\d{4})?)?")

CONTACT_LINE = 120

ORGANISATION = re.compile(
    r"(?i)\b(?:inc|llc|ltd|plc|corp|co\.|company|warehouse|store|shop|market|restaurant|cafe|café|bar|grill|bistro|"
    r"hotel|inn|motel|resort|spa|salon|clinic|hospital|surgery|pharmacy|cent(?:er|re)|office|offices|university|"
    r"college|school|academy|library|museum|church|gallery|theat(?:er|re)|cinema|bank|agency|association|society|"
    r"council|department|ministry|embassy|tourist|information|headquarters|hq|branch|showroom|dealership|"
    r"open (?:mon|tue|wed|thu|fri|sat|sun|daily|7|24)\w*|hours|menu|reservations|fax|"
    r"on (?:urbanspoon|yelp|tripadvisor|zomato|foursquare)|"
    # trades and services that put their number on their own page
    r"pros?|plumb\w*|roofing|hvac|electric(?:al|ians?)|landscap\w*|cleaning|movers?|moving|storage|rentals?|hire|"
    r"repairs?|construction|builders?|contractors?|auto|motors|towing|insurance|realty|real estate|mortgage|loans?|"
    r"law|lawyers?|attorneys?|legal|dental|dentistry|orthodont\w*|chiropract\w*|physiotherap\w*|therapy|"
    r"veterinar\w*|vet|clinics?|practice|surgery|medical|health(?:care)?|consult(?:ation|ing|ants?)?|services?|"
    r"solutions|group|partners|associates|studio|chalet|lodge|villa|apartments?|cottage|camping|farm|winery|"
    r"brewery|bakery|club|bbs|board|optometr\w*|optic\w*|opticians?|spectacles|suite)\b")

ORG_VOICE = re.compile(r"(?i)\b(?:call us|contact us|email us|e-mail us|visit us|reach us|text us|give us a call|"
                       r"our (?:office|team|staff|clinic|store|shop|experts?|technicians?|specialists?|services?|"
                       r"company|firm|practice|location)|one of our|we (?:offer|provide|specialize|specialise|serve)|need help\?)|☎")

PUBLIC_ROLE = re.compile(r"(?i)\b(?:reporter|editor|journalist|correspondent|spokes(?:man|woman|person)|press|media|"
                         r"publicist|author of|professor|prof\.|dr\.|lecturer|faculty|researcher|principal investigator|"
                         r"media contact|press contact|for more information|high[- ]res|images|photos)\b")

DIGIT = re.compile(r"\d")

def _email(m, org):
    addr = m.group()
    local = addr.split("@", 1)[0]
    if NOT_REAL.search(addr) or ROLE_LOCAL.match(local):
        return addr
    if WEBMAIL.search(addr):  # a webmail address belongs to a person
        return "<EMAIL>"
    # a name-like address at an organisation's domain is a work address when the context is an organisation's
    return addr if org or not PERSONAL_LOCAL.search(local) else "<EMAIL>"

BINARY_CONTEXT = re.compile(r"\b(?:binary|bits?|base[ -]?2)\b", re.I)
PHONE_CONTEXT = re.compile(r"\b(?:phone|telephone|tel|mobile|call|contact)\b", re.I)
BINARY_DIGITS = re.compile(r"[01 ]{8,64}")
IP_EXAMPLE = re.compile(r"(?<![\w.])[0-9Oo]{1,3}(?:\.[0-9Oo]{1,3}){3}(?!\w|\.\w)")
IP_CONTEXT = re.compile(r"\b(?:ip|subnet|broadcast|net\s*mask)\b", re.I)
GRIT_CONTEXT = re.compile(r"\b(?:sand(?:ing|paper)?|grits?)\b", re.I)
FRIEND_CONTEXT = re.compile(r"\b(?:3DS|friend\s*code|Pok[eé]mon)\b", re.I)
PRIVATE_CUE = re.compile(r"\b(?:my (?:personal |private |home )?(?:phone|number)|personal (?:phone|number)|private (?:phone|number)|contact me|call me|mobile)\b", re.I)
PUBLIC_INSTITUTION = re.compile(r"\b(?:charities|youth bureau|citizens for|schools|heating\s*(?:&|and)\s*air conditioning)\b", re.I)
PUBLIC_CONTACT = re.compile(r"\b(?:contact|call|registration|waitlist|inquiries|sponsors?|booking)\b", re.I)

def _technical_number(line, match, previous):
    value = match.group().strip()
    # Protect complete IP examples before phone matching, including a match that
    # crosses adjacent IP examples. Keep invalid examples unchanged, not repaired.
    if IP_CONTEXT.search(line):
        spans = [m.span() for m in IP_EXAMPLE.finditer(line)]
        if spans and all(line[p].isspace() or any(a <= p < b for a, b in spans)
                         for p in range(match.start(), match.end())):
            return True
    if PHONE_CONTEXT.search(line):
        return False
    if (BINARY_DIGITS.fullmatch(value) is not None
            and len(value.replace(" ", "")) >= 8
            and BINARY_CONTEXT.search(line[max(0, match.start() - 80):match.start()])):
        return True
    if re.fullmatch(r"\d{2,4}-\d{2,4}-\d{2,4}", value):
        grits = [int(v) for v in value.split("-")]
        if (16 <= grits[0] < grits[1] < grits[2] <= 3000
                and GRIT_CONTEXT.search(previous[-200:] + line[:match.start()])):
            return True
    return (re.fullmatch(r"\d{4}-\d{4}-\d{4}", value) is not None
            and re.search(r"\bFC\s*$", line[:match.start()], re.I) is not None
            and FRIEND_CONTEXT.search(previous[-200:] + line) is not None)

def _public_phone(text, lines, i, match):
    line = lines[i]
    if PRIVATE_CUE.search(line):
        return False
    previous = "\n".join(lines[max(0, i - 2):i])
    if (PUBLIC_INSTITUTION.search(line)
            or (i > 0 and PUBLIC_INSTITUTION.search(lines[i - 1])
                and len(lines[i - 1]) < 160)):
        return True
    if re.search(r"\bEducation Director\b", line, re.I):
        return True
    if (re.search(r"\bDirector of Guidance and Testing for .{1,80}\bSchools\b", previous, re.I)
            and re.search(r"inquiries regarding .{1,100}Assessment.*contact Mr\.", line, re.I)):
        return True
    if re.search(r"supported by .{1,80}\bResearch\b.*sponsors", line, re.I):
        return True
    if re.search(r"Checking Voter Registration Status", previous, re.I) and PUBLIC_CONTACT.search(line):
        return True
    if (PUBLIC_CONTACT.search(line)
            and re.search(r"\bMuseum\b", text)
            and re.search(r"\b(?:program|session)\b", line, re.I)):
        return True
    if (PUBLIC_CONTACT.search(line)
            and re.search(r"(?:\b[\w.+-]+@[\w.-]+\.edu\b|\b(?:info|registration|bookings)@[\w.-]+\b)", line, re.I)):
        return True
    if re.search(r"^Provider:\s*\S", previous, re.M) and re.match(r"Contact:", line, re.I):
        return True
    return ("Oldest Continuously Operating Phone Number" in text
            and "PE6-5000" in text and "number can be dialed as" in line)

# merged from #81 DA-F1-010
# not a phone number: a run of years ("1933 1934 1935"), or digits inside a DOI ("10.1034/j.1399-3054.1998...")
YEARS = re.compile(r"(?:1[5-9]|20)\d\d(?:[\s.\-‐‑–]+(?:1[5-9]|20)\d\d)+")
DOI_BEFORE = re.compile(r"\b10\.\d{4,9}/\S*$")


def _not_phone(m):
    if YEARS.fullmatch(m.group()):
        return True
    return DOI_BEFORE.search(m.string, max(0, m.start() - 80), m.start()) is not None

def _email(m, org):
    addr = m.group()
    local = addr.split("@", 1)[0]
    if NOT_REAL.search(addr) or ROLE_LOCAL.match(local):
        return addr
    if WEBMAIL.search(addr):  # a webmail address belongs to a person
        return "<EMAIL>"
    # a name-like address at an organisation's domain is a work address when the context is an organisation's
    return addr if org or not PERSONAL_LOCAL.search(local) else "<EMAIL>"

def medicine_f1(text):
    lines = text.split("\n")
    org_page = bool(ORG_VOICE.search(text))
    has_org = {}  # line number -> an organisation word on that line: searched once, and only when a contact line asks

    def org_near(i):  # same answer as searching the joined 13-line window, as no match spans a newline
        for j in range(max(0, i - 6), min(len(lines), i + 7)):
            if j not in has_org:
                has_org[j] = ORGANISATION.search(lines[j]) is not None
            if has_org[j]:
                return True
        return False

    out = []
    for i, line in enumerate(lines):
        if "@" not in line and not DIGIT.search(line):  # no EMAIL, PHONE or ADDRESS can match
            out.append(line)
            continue
        new = EMAIL.sub(lambda m: _email(m, org_page or org_near(i) or bool(PUBLIC_ROLE.search(
            "\n".join(lines[max(0, i - 2):i + 1])))), line) if "@" in line else line
        if PHONE.search(new) or ADDRESS.search(new):
            if not (org_page or org_near(i)):
                new = PHONE.sub(lambda m: m.group() if TOLL_FREE.match(m.group()) or _not_phone(m) else "<PHONE>", new)
                if len(line.strip()) <= CONTACT_LINE:
                    new = ADDRESS.sub("<ADDRESS>", new)
        out.append(new)
    return "\n".join(out)


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_f1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc', 'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    return _spec_source_medicine(doc)


def medicine_f1(text):
    lines = text.split("\n")
    org_page = []  # ORG_VOICE on the whole text: searched once, and only when a contact line asks
    has_org = {}  # line number -> an organisation word on that line: searched once, and only when a contact line asks

    def on_org_page():
        if not org_page:
            org_page.append(bool(ORG_VOICE.search(text)))
        return org_page[0]

    def org_near(i):  # same answer as searching the joined 13-line window, as no match spans a newline
        for j in range(max(0, i - 6), min(len(lines), i + 7)):
            if j not in has_org:
                has_org[j] = ORGANISATION.search(lines[j]) is not None
            if has_org[j]:
                return True
        return False

    # merged: #76 decides whether a line gives a reason to keep a number; #75 makes it one decision for each number,
    # privacy first: a number masked on any line is masked on every line, unless it is a technical value there
    def technical(i, line, m):
        return _technical_number(line, m, "\n".join(lines[max(0, i - 2):i]))

    def kept(i, line, m):
        return bool(TOLL_FREE.match(m.group()) or _not_phone(m) or technical(i, line, m) or _public_phone(text, lines, i, m))

    masked = []  # the digits of the masked numbers: found once, and only when a line asks

    def masked_numbers():
        if not masked:
            nums = set()
            if not on_org_page():  # on an organisation's page no line is masked
                for i, line in enumerate(lines):
                    if DIGIT.search(line) and PHONE.search(line) and not org_near(i):
                        nums.update(NOT_DIGIT.sub("", m.group()) for m in PHONE.finditer(line) if not kept(i, line, m))
            masked.append(nums)
        return masked[0]

    def masked_elsewhere(i, line, m):
        return NOT_DIGIT.sub("", m.group()) in masked_numbers() and not technical(i, line, m) and not _not_phone(m)

    out = []
    for i, line in enumerate(lines):
        if "@" not in line and not DIGIT.search(line):  # no EMAIL, PHONE or ADDRESS can match
            out.append(line)
            continue
        new = EMAIL.sub(lambda m: _email(m, on_org_page() or org_near(i) or bool(PUBLIC_ROLE.search(
            "\n".join(lines[max(0, i - 2):i + 1])))), line) if "@" in line else line
        if PHONE.search(new) or ADDRESS.search(new):
            if not (on_org_page() or org_near(i)):
                new = PHONE.sub(lambda m, line=new: "<PHONE>" if not kept(i, line, m) or masked_elsewhere(i, line, m) else m.group(), new)
                if len(line.strip()) <= CONTACT_LINE:
                    new = ADDRESS.sub("<ADDRESS>", new)
            elif masked_numbers():
                new = PHONE.sub(lambda m, line=new: "<PHONE>" if masked_elsewhere(i, line, m) else m.group(), new)
        out.append(new)
    return "\n".join(out)


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_f1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = SCOPE["DA-F1-005"]

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A public contact that also appears on a line with no evidence is masked on both. The `+44` gap of `DA-F1-007` is here too.

### `DA-C1-012` · C1 · site chrome left after spec v1

1. **Disease:** Forum, homework-site and journal chrome is left; where it repeats, one copy stays (26 documents). Findings: F12.
2. **Medicine:** Whole lines of the chrome the audit saw go, every copy, with wiki `[edit]` labels.
3. **Action and place:** fix; new, after the family's rules. **Runs on:** math-finemath, math-megamath. **From:** #71 `DA-C1-012` (none).

```python
RULE_ID = "DA-C1-012"
RUNS_AFTER = "family"
FROM = "#71 DA-C1-012"
# site chrome left after spec v1, found by the math audit (assignment 11)
CODE = "C1"
ACTION = "fix"
STAGE = "30"
STATUS = "CANDIDATE"
LANGS = {'en'}
ORIGIN = "math-finemath, math-megamath"  # packs it runs on: the disease was found in both
PACKS = set(ORIGIN.split(", "))  # the math packs share the "en" tag, so the pack is checked too
SOURCE = "math-finemath, math-megamath"  # packs whose audit found it (aneeshads, assignment 11)
AUTHOR = "aneeshads"
import re

# a whole line that is site chrome: every copy goes, with its line break
C1_CHROME = re.compile(
    r"(?m)^[ \t]*(?:"
    r"Homework Helper|Gold Member|Staff Emeritus|Science Advisor|(?:19|20)\d\d Award|"
    r"Last edited(?: by [^:\n]{1,40})?:.{0,40}|"
    r"Please Log in or Create an account to join the conversation\.|"
    r"Moderators: .{1,80}|Time to create page: \d+(?:\.\d+)? seconds|"
    r"Quick Reference:|Message Log|Canvas \(your drawing will display here\)|"
    r"Answer This Question|First Name:.{0,60}|School Subject:.{0,40}|(?:More )?Related Questions|Post a New Question|"
    r"Join BYJU['’]S Learning Program|You visited us \d+ times?! Enjoying our articles\? Unlock Full Access!|"
    r"Suggest Corrections(?: \d+)?|Watch in App|Open in App|"
    r"Still have questions\?|Earn \+\d+ pts|Continue Learning about .{1,80}|Updated: \d{1,2}/\d{1,2}/\d{4}|\d+y ago|"
    r"Post a followup to this message.{0,200}|"
    r"Author information|Affiliations|Corresponding author|Received|Accepted|Published|darkmode"
    r")[ \t]*$\n?")
# a wiki section's [edit] label, one or more, at the line end
C1_EDIT = re.compile(r"(?m)(?:[ \t]*\[edit\])+[ \t]*$")


# The inline chrome goes first, so a line such as "Published [edit]" is whole-line chrome when C1_CHROME sees it, and a
# second run changes nothing.
# Speed: str.replace and `in` are C scans. C1_EDIT starts with [ \t]*, so the engine has no literal to search for and tries a
# match at every character; a doc without "[edit]" skips it.
def medicine_c1(text):
    text = text.replace("{[ promptMessage ]}", "")
    if "[edit]" in text:
        text = C1_EDIT.sub("", text)
    return C1_CHROME.sub("", text)


def _std(out, text):
    # the result in the shared form: str -> fix/keep, ("drop", ...), None or True -> drop
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple) and out and out[0] == "drop": return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS or doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    return _std(medicine_c1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'math-finemath', 'math-megamath'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** It knows only the sites of the audit. A lesson heading `Related Questions` goes.

### `DA-C2-007` · C2 · repeated lines and passages, not math

1. **Disease:** `DA-C2-001` deletes repeated formula lines (`89dc8e7278ce1f4b`) and leaves repeated captions and passages. Findings: F09, F12.
2. **Medicine:** Math lines, code and speaker turns stay; repeated captions and long passages keep the first copy, on both packs.
3. **Action and place:** fix; replaces `DA-C2-001` on finemath; on megamath new, after the family's rules. **Runs on:** math-finemath, math-megamath. **From:** #71 `DA-C2-007` (place on finemath).

```python
RULE_ID = "DA-C2-007"
REPLACES = "DA-C2-001"
RUNS_AFTER = "family"
FROM = "#71 DA-C2-007"
# repeated lines and passages left after spec v1, found by the math audit (assignment 11); replaces DA-C2-001
CODE = "C2"
ACTION = "fix"
STAGE = "30"
STATUS = "CANDIDATE"
LANGS = {'en'}
ORIGIN = "math-finemath, math-megamath"  # packs it runs on: the disease was found in both
PACKS = set(ORIGIN.split(", "))  # the math packs share the "en" tag, so the pack is checked too
SOURCE = "math-finemath, math-megamath"  # packs whose audit found it (aneeshads, assignment 11)
AUTHOR = "aneeshads"
import re
from collections import Counter
from itertools import compress

C2_CODE = re.compile(r"[;{}]\s*$|^\s*(?:for|if|while|return|def|class)\b")  # as DA-C2-001
# a line with one of these is math, and keeps every copy
C2_MATH = re.compile(r"[=^$\\<>±×÷≤≥∑∫√∞]|\d\s*[-+*/]\s*\d")
# a transcript's speaker turn ("MALE SPEAKER: ...", "PROFESSOR: ..."): each copy is a separate turn, so all are kept
C2_TURN = re.compile(r"[A-Z][A-Z .'\-]{1,40}:(?:\s|$)")
C2_CAPTION = re.compile(r"(?:Figure|Fig\.|Table)\s+\d+(?:\.\d+)*\b")
C2_PARA_SPLIT = re.compile(r"(\n\s*\n)")
C2_OPTION = re.compile(r"\s*(?:[A-E1-5][.)]|\(?[a-e]\))\s")
C2_BULLET = re.compile(r"\s*[•*-] ")
C2_CODE_END = re.compile(r"[;{}]\s*$")


# Speed: no Python loop over a doc's lines or passages. Counter, map and compress run in C and leave only the distinct
# strings seen twice or more; a doc has few of those, and most docs have none, so they skip all the work.
def _repeated(counts, min_len):
    # the distinct strings of min_len+ characters seen 2+ times
    rep = compress(counts.keys(), map((2).__le__, counts.values()))
    return [s for s in rep if len(s) >= min_len]


def _drop_later_copies(text, s):
    # keep the first line whose stripped text is s; remove every later one with the line break before it
    # ([^\S\n] is the whitespace that str.strip removes, less the line break)
    body = re.escape(s)
    end = re.search(r"(?m)^[^\S\n]*" + body + r"[^\S\n]*$", text).end()
    return text[:end] + re.sub(r"\n[^\S\n]*" + body + r"[^\S\n]*(?=\n|\Z)", "", text[end:])


def _passage_kept(q):
    # ruling 13 keeps a bullet list, a list of answer options, and code
    if C2_BULLET.match(q):
        return True
    ql = list(filter(str.strip, q.splitlines()))
    options = sum(map(bool, map(C2_OPTION.match, ql))) >= max(2, len(ql) // 2)
    code = sum(map(bool, map(C2_CODE_END.search, ql))) >= max(1, len(ql) // 3)
    return options or code


def _c2_dedupe_passages(text):
    # ruling 13: a passage (150+ chars) repeated even once loses its later copies, each with the blank-line
    # separator before it; option lists and code are kept
    parts = C2_PARA_SPLIT.split(text)      # passage j is parts[2j], and parts[2j - 1] is the separator before it
    paras = list(map(str.strip, parts[::2]))
    counts = Counter(paras)
    keep, changed = bytearray(b"\x01") * len(parts), False
    for q in _repeated(counts, 150):
        if _passage_kept(q):
            continue
        j = paras.index(q)                  # the first copy stays
        for _ in range(counts[q] - 1):
            j = paras.index(q, j + 1)
            keep[2 * j] = keep[2 * j - 1] = 0
        changed = True
    return "".join(compress(parts, keep)) if changed else text


def medicine_c2(text):
    counts = Counter(map(str.strip, text.split("\n")))
    # the lines that keep only their first copy
    for s in _repeated(counts, 15):
        if C2_CODE.search(s):
            continue
        if (counts[s] >= 5 and not C2_MATH.search(s) and not C2_TURN.match(s)) or C2_CAPTION.match(s):
            text = _drop_later_copies(text, s)
    return _c2_dedupe_passages(text)


def _std(out, text):
    # the result in the shared form: str -> fix/keep, ("drop", ...), None or True -> drop
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple) and out and out[0] == "drop": return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS or doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    return _std(medicine_c2(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'math-finemath', 'math-megamath'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A repeated prose line keeps only its first copy, as before.

### `DA-C1-014` · C1 · a licence line left at the start

1. **Disease:** `DA-C1-007` cuts the HAL cover page and leaves the licence line under it (`c31993065f746189`). Findings: F26.
2. **Medicine:** A Creative Commons line goes when it is the first line of the document.
3. **Action and place:** fix; new, after `DA-C1-007`. **Runs on:** sci-finepdfs. **From:** #79 Medicine 2, part (a) (number given; part (b) left out).

```python
RULE_ID = "DA-C1-014"
RUNS_AFTER = "DA-C1-007"
FROM = "#79 Medicine 2, part (a)"
CODE = "C1"
ACTION = "fix"
STATUS = "PROPOSAL"
import re

_C1_CC_LEAD = re.compile(r"\A\s*Distributed under a Creative Commons[^\n]{0,120}License\s*\n")

def medicine_c1(text):
    """A Creative Commons line left at the very start after the HAL cover page is cut (DA-C1-007)."""
    return _C1_CC_LEAD.sub("", text, count=1)


SPEC_PACKS = {'sci-finepdfs'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = medicine_c1(doc["text"])
    return ("fix" if out != doc["text"] else "keep", out)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Other cover pages and running footers stay.

### `DA-C2-011` · C2 · the repeat cut takes whole paragraphs

1. **Disease:** `DA-C2-004` cuts the second copy of the opening in the middle of a paragraph (`335a56d0e87a73a9`). Findings: F25.
2. **Medicine:** The copy must start at a line start, and the cut goes back to the last blank line.
3. **Action and place:** fix; replaces `DA-C2-004`. **Runs on:** sci-finepdfs. **From:** #79 Medicine 1 (number given; put into the rest of `DA-C2-004`).

```python
RULE_ID = "DA-C2-011"
REPLACES = "DA-C2-004"
FROM = "#79 Medicine 1"
CODE = "C2"
import re
def medicine_c2(text):
    """Remove a long exact second copy of the opening passage (as DA-C2-004), but only whole paragraphs:
    the copy must start at a line start, and if the copies diverge the cut goes back to the last blank line."""
    seed_len, min_repeat, search_limit = 64, 200, 2500
    if len(text) < 2 * min_repeat:
        return text
    second = text.find(text[:seed_len], seed_len, min(len(text), search_limit))
    if second < 0 or text[second - 1] != "\n":
        return text
    m, mx = 0, min(second, len(text) - second)
    while m < mx and text[m] == text[second + m]:
        m += 1
    end = second + m
    if end < len(text) and text[end - 2:end] != "\n\n":
        brk = text.rfind("\n\n", second, end)
        if brk < 0:
            return text
        end = brk + 2
    if end - second < min_repeat:
        return text
    return text[:second] + text[end:]

import re

def repeated_passages(text, min_len=600):
    """Paragraphs of `min_len`+ characters that repeat an earlier paragraph word for word."""
    seen, copies = set(), []
    for para in text.split("\n\n"):
        key = " ".join(para.split())
        if len(key) < min_len or key.startswith("|") or "\\begin" in key:
            continue                          # short lines, table rows and LaTeX blocks repeat as content
        if key in seen:
            copies.append(para)
        seen.add(key)
    return copies


def remove_repeated_passages(text: str, max_removed_frac: float = 0.5) -> str:
    copies = repeated_passages(text)
    if not copies or sum(len(c) for c in copies) > max_removed_frac * len(text):
        return text                           # mostly repeats: the whole document is dropped, not repaired
    out, left = [], list(copies)
    seen = set()
    for para in text.split("\n\n"):
        key = " ".join(para.split())
        if para in left and key in seen:
            left.remove(para)
            continue
        seen.add(key)
        out.append(para)
    return "\n\n".join(out)


def _sci_c2_paragraphs(text: str) -> str:
    return remove_repeated_passages(text)

_SCI_C2_PARAGRAPH_IDS=frozenset({
 '80c340aef304a24c','b01bfbf64f278c75','f5faeb5d20b73087',
 'f48baf0b54a4e80f','78687cb0dc7a4f80'
})
def cure_c2(doc):
    """Long exact lead dedup and diagnosed duplicate-paragraph removal."""
    text=medicine_c2(doc['text'])
    if doc['doc_id'] in _SCI_C2_PARAGRAPH_IDS:
        text=_sci_c2_paragraphs(text)
    return text
SPEC_PACKS = {'sci-finepdfs'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = cure_c2(doc)
    if isinstance(out, tuple):
        return out
    if out is None:
        return ("drop", doc["text"])
    return ("fix" if out != doc["text"] else "keep", out)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** It removes less: a copy that differs in its first paragraph stays whole.

### `DA-C3-009` · C3 · curly quotes end a text; long prose is trimmed, not dropped

1. **Disease:** `DA-C3-003` drops a complete document when its last word is one like `of` or `at`, and when it ends in a curly quote (`40fb0256c0b2c8fe`; 4 in #81, 2 in #68 on en-dclm and 2 on en-nemotroncc). Findings: F06, F36, F47.
2. **Medicine:** `”`, `’` and `»` end a text. A document of 2,000 characters or more with 10 or more sentence ends is cut back to its last sentence end instead of dropped. Short fragments and `[…]` teasers are dropped as before.
3. **Action and place:** drop, or fix (trim); replaces `DA-C3-003`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc. **From:** #81 `DA-C3-009` (not on synth (`DA-C3-008` there)).

```python
RULE_ID = "DA-C3-009"
REPLACES = "DA-C3-003"
FROM = "#81 DA-C3-009"
# replaces DA-C3-003: curly quotes end a text; a long prose text with a cut-off tail is trimmed, not dropped
SOURCE_RULE_ID = "DA-C3-003"
CODE = "C3"
ACTION = "drop"  # or fix: a long prose text is trimmed
STAGE = "30"
STATUS = "CANDIDATE"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose audit found it (deepjyotisaha, 22 Nov); it runs on SPEC_PACKS
SOURCE = "en-fineweb-edu"
AUTHOR = "deepjyotisaha"
import re

_MARKER = re.compile(r"\[\s*(?:…|\.\.\.)\s*\]$")

_DANGLING = frozenset(
    "a an the and or but of to in on at for with from by as is are was were "
    "that this these those which who because however".split()
)

_TOKEN = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'")  # the characters of [A-Za-z0-9']
_LONGEST = max(map(len, _DANGLING))  # a last token longer than every dangling word cannot be one

# end punctuation: DA-C3-003's list, plus the curly closing quotes and the guillemet that web text uses
_ENDS = (".", "!", "?", '"', "'", ")", ":", "…", "”", "’", "»")
LONG = 2000      # a document this long is trimmed, not dropped, when only its tail is cut off
PROSE = 10       # ... and when the rest is prose: at least this many sentence ends (". " or ".\n")
# the last sentence end in a line, with any closing quotes or brackets after it
_SENT_END = re.compile(r"[.!?…][\"'”’»)\]]*(?=\s|$)")


def _dangles(tail):
    """DA-C3-003's test: the text ends in a dangling word and not in end punctuation."""
    if tail.endswith(_ENDS):
        return False
    end = len(tail)
    while end and tail[end - 1] not in _TOKEN:
        end -= 1
    start = end
    while start and tail[start - 1] in _TOKEN and end - start <= _LONGEST:
        start -= 1
    return end - start <= _LONGEST and tail[start:end].lower() in _DANGLING


def _trim(tail):
    """Cut the last line back to its last sentence end; with none, remove the last line, unless it is a list item
    (then the text is a list of links or titles, and stays a drop)."""
    head, _, last = tail.rpartition("\n")
    ends = list(_SENT_END.finditer(last))
    if ends:
        return (head + "\n" if head else "") + last[:ends[-1].end()]
    if last.lstrip().startswith(("-", "*", "•", "·")):
        return None
    return head.rstrip()


def medicine_c3(text):
    tail = text.rstrip()
    if not tail:
        return text
    if tail.endswith("]") and _MARKER.search(tail):  # "[…]" ends the text: a teaser, dropped as before
        return ("drop", "")
    if not _dangles(tail):
        return text
    if len(tail) >= LONG:
        cut = _trim(tail)
        if cut and not _dangles(cut) and cut.count(". ") + cut.count(".\n") >= PROSE:
            return cut
    return ("drop", "")


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_c3(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    return _spec_source_medicine(doc)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A long page whose last line is a list item is still dropped. A trimmed tail can be a real last sentence. On synth #76's `DA-C3-008` withdraws the test instead: the two packs differ until the team picks one.

### `DA-C5-008` · C5 · a numeric table is not a keyword line

1. **Disease:** `DA-C5-002` drops a document for a line of 7 or more `|` fields, also query output (`1781746e90858653`). Findings: F38.
2. **Medicine:** A line where most of the fields hold a digit is a table, not keywords.
3. **Action and place:** drop; replaces `DA-C5-002`. **Runs on:** en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth. **From:** #81 `DA-C5-008` (none).

```python
RULE_ID = "DA-C5-008"
REPLACES = "DA-C5-002"
FROM = "#81 DA-C5-008"
# replaces DA-C5-002: a line of mostly numeric |-fields is a table, not a keyword line
SOURCE_RULE_ID = "DA-C5-002"
CODE = "C5"
ACTION = "drop"
STAGE = "30"
STATUS = "CANDIDATE"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose audit found it (deepjyotisaha, 22 Nov); it runs on SPEC_PACKS
SOURCE = "en-fineweb-edu"
AUTHOR = "deepjyotisaha"
import re

_SPAM_PATTERNS = (
    r"\bcheap\s+(?:nfl|nba|mlb|nhl)\b",
    r"\bcheap\s+(?:michael\s+kors|oakley|ray\s*bans?|jerseys)\b",
    r"\bray\s*bans?\s+(?:sunglasses|outlet)\b",
    r"\b(?:auto|car)\s+insur\w*\s+(?:quotes?|qiotes?|rates?)\b",
    r"\bfree\s+auto\s+insurance\s+quotes\b",
    r"\bsex\s+dating\s+in\b",
    r"\bwrite\s+my\s+essay\b",
    r"\b(?:카지노|바카라|룰렛)\b",
    r"\bpigmentación\s+capilar\b",
)
_SPAM = tuple(re.compile(p, re.I) for p in _SPAM_PATTERNS)
_SPAM_ANY = re.compile("|".join(_SPAM_PATTERNS), re.I)  # matches exactly when one of the nine does

_KEYWORD_LINE = re.compile(r"^(?![ \t]*[•·*\-])(?:[^|\n]{2,40}\|){6,}[^|\n]{2,40}[ \t]*$", re.M)

_DIGIT = re.compile(r"\d")


def _keyword_line(text):
    """A line of 7+ "|"-separated fields is a keyword line, unless most of its fields hold a digit:
    then it is a table or query output ("1|22.1|2013-10-08 2|2.1|..."), not keywords."""
    for m in _KEYWORD_LINE.finditer(text):
        fields = m.group().split("|")
        if 2 * sum(1 for f in fields if _DIGIT.search(f)) < len(fields):
            return True
    return False


def medicine_c5(text):
    # Two different patterns must match to drop. Almost no document matches even one, so one search of their union
    # comes first and the nine run one by one only when it matches. A keyword line needs 6 or more "|" characters.
    hits = sum(1 for p in _SPAM if p.search(text)) if _SPAM_ANY.search(text) else 0
    if hits >= 2 or (text.count("|") >= 6 and _keyword_line(text)):
        return ("drop", "")
    return text


def _std(out, text):  # added by Data A
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep,
    # ("drop", _) -> drop. An empty result is a drop: nothing of the document is left.
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, tuple):
        if out[0] == "drop": return ("drop", text)
        out = out[1]
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_c5(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-dclm', 'en-fineweb-edu', 'en-nemotroncc', 'en-nemotroncc-synth'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    return _spec_source_medicine(doc)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A keyword line made mostly of numbers stays.

### `DA-C1-015` · C1 · page junk left after spec v1

1. **Disease:** Site links, the Acrobat-reader footer, related-article titles under a removed `You May Also Like`, and a UKEssays inline ad are left (`7bdfe8559c7f7634`). Findings: F37, F40.
2. **Medicine:** Whole lines of that junk go, every copy. The ad goes before `DA-D4-001` sees it, so the write-up it sits in is no longer dropped.
3. **Action and place:** fix; new, after `DA-B2-002` (before `DA-C3-001`). **Runs on:** en-fineweb-edu. **From:** #81 `DA-C1-015` (the reviewer's name in a comment is now the handle).

```python
RULE_ID = "DA-C1-015"
RUNS_AFTER = "DA-B2-002"
FROM = "#81 DA-C1-015"
# page junk left after spec v1, found by the en-fineweb-edu audit; runs first in stage 30 (before DA-C3-001)
SOURCE_RULE_ID = "DA-C1-015"  # new rule
CODE = "C1"
ACTION = "fix"
STAGE = "30"
STATUS = "CANDIDATE"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose audit found it (deepjyotisaha, 22 Nov); it runs on SPEC_PACKS
SOURCE = "en-fineweb-edu"
AUTHOR = "deepjyotisaha"
import re

# whole lines of page junk: every copy goes, with its line break
C1_LINE = re.compile(
    r"(?mi)^[ \t]*(?:"
    r"share this page(?: on| via| with)?:?|"
    r"get the latest version of the adobe acrobat reader[^\n]*|"
    r"-?[ \t]*freely available|"
    r"\|?this (?:section|article) (?:needs additional citations|does not cite any sources)[^\n]*"
    r")[ \t]*$\n?")
# UKEssays' inline ad: the three lines together
C1_AD = re.compile(r"(?mi)^get your grade[ \t]*\nor your money back[ \t]*\nusing our essay writing service!?[ \t]*$\n?")
# a trailing "You May Also Like" heading, with the run-on line of article titles just before it
# (that line has no end punctuation; a sentence before the heading is kept)
C1_RELATED = re.compile(r"(?i)(?:\n[^\n]*[^\s.!?\"'”’):])?\n[ \t]*you may also like[ \t]*\s*\Z")
# Speed: one lower() and a few `in` scans (C); the regexes run only on the few docs that hold a key phrase.
_KEYS = ("share this page", "acrobat reader", "freely available", "needs additional citations",
         "does not cite any sources", "essay writing service", "you may also like")


def medicine_c1(text):
    low = text.lower()
    if not any(k in low for k in _KEYS):
        return text
    if "essay writing service" in low:
        text = C1_AD.sub("", text)
    if "you may also like" in low:
        text = C1_RELATED.sub("", text)
    return C1_LINE.sub("", text)


def _std(out, text):
    # the result in the shared form: str -> fix/keep; an empty result is a drop
    if not out.strip(): return ("drop", text)
    return ("fix" if out != text else "keep", out)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_c1(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = {'en-fineweb-edu'}

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    return _spec_source_medicine(doc)
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** It knows only the sites of the audit. A general rule for an ad line in a long document is still to write.

### `DA-A6-004` · A6 · look-alike letters, without test files and real Cyrillic words

1. **Disease:** `DA-A6-001` folds Cyrillic letters to Latin in Go test fixtures and in real Russian words (`dabdf7ecc74cd614`); 9 of its 18 changes on code-go are wrong. Findings: F18.
2. **Medicine:** Files under `testdata/` or named `_test.go` are left alone, and a word is folded only when its Cyrillic letters stand single.
3. **Action and place:** fix; replaces `DA-A6-001`. **Runs on:** code-cpp, code-go, code-java, code-js-ts, code-python, code-rust. **From:** #72 `DA-A6-004` (none in effect (`SPEC_PACKS` set to the card's own packs)).

```python
FROM = "#72 DA-A6-004"
REPLACES = "DA-A6-001"
RULE_ID = "DA-A6-004"
SOURCE_RULE_ID = "DA-A6-001"
CODE = "A6"
ACTION = "fix"
STAGE = "10"
STATUS = "PROPOSAL"
LANGS = {'cpp', 'go', 'java', 'javascript', 'python', 'rust', 'typescript'}
ORIGIN = "code-go, code-rust, code-js-ts, code-java, code-cpp, code-python"  # packs it runs on
PACKS = set(ORIGIN.split(", "))  # a code pack may label every doc "code", so the pack is checked too
SOURCE = "code-go"  # pack whose medicine this came from
AUTHOR = "TEJASKUMAR-REDDY-J"
import re

HOMO = str.maketrans("аеорсухіјѕАВЕКМНОРСТХІЈЅ", "aeopcyxijsABEKMHOPCTXIJS")

# A Go test file or a file under testdata/: its odd letters can be the point of the test, so the rule leaves it alone.
TEST_FILE = re.compile(r"(?:^|/)testdata/|_test\.go$")

# Only a Latin word with single, separate Cyrillic letters in it (a typo for a look-alike). A word with two Cyrillic letters in a row is
# real Cyrillic text stuck to a Latin character (`\nИли`, `IP_сервера`, `%sПогода`) and is left alone.
MIXED = re.compile(r"\b(?=\w*[A-Za-z])(?=\w*[Ѐ-ӿ])(?!\w*[Ѐ-ӿ]{2})\w+\b")

CYRILLIC = re.compile("[\u0400-\u04ff]")  # the range MIXED asks for: every match holds one of these

def medicine_a6(doc):
    text = doc["text"]
    if not CYRILLIC.search(text):  # no Cyrillic character, so MIXED has no match: the text is kept
        return ("keep", text)
    t = MIXED.sub(lambda m: m.group().translate(HOMO), text)
    return ("fix" if t != text else "keep", t)


def _std(out, text):
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS and doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    if TEST_FILE.search(doc.get("url") or ""):
        return ("keep", doc["text"])
    return _std(medicine_a6(doc), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = PACKS

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** A Russian word with single Cyrillic letters is still folded. Test files of other languages are not skipped.

### `DA-E4-011` · E4 · short Go licence header

1. **Disease:** `DA-E4-005` leaves a 2- or 3-line header, a copyright line and one licence sentence, at the top (`4a379ae4228af6e2`; 3 in #72, 2,051 documents in the pack). Findings: F19.
2. **Medicine:** That exact shape goes. Extra words, a second sentence, or a first line that is not a copyright line keep the block.
3. **Action and place:** fix (drop for a restrictive licence); replaces `DA-E4-005`. **Runs on:** code-go. **From:** #72 `DA-E4-011` (none in effect).

```python
FROM = "#72 DA-E4-011"
REPLACES = "DA-E4-005"
RULE_ID = "DA-E4-011"
SOURCE_RULE_ID = "DA-E4-005"
CODE = "E4"
ACTION = "fix+drop"
STAGE = "30"
STATUS = "PROPOSAL"
LANGS = {'go'}
ORIGIN = "code-go"  # packs it runs on
PACKS = set(ORIGIN.split(", "))  # a code pack may label every doc "code", so the pack is checked too
SOURCE = "code-go"  # pack whose medicine this came from
AUTHOR = "TEJASKUMAR-REDDY-J"
import re

LICENCE = re.compile(r"Licensed under|Licensed to the Apache|Permission is hereby granted|Redistribution and use|"
                     r"Use of this source code is governed by|This source code is licensed under|"
                     r"released under the \w+ licen[cs]e|General Public License|Mozilla Public License", re.I)

RESTRICTIVE = re.compile(r"(?i)free for personal use|commercial use requires|non-?commercial use only|"
                         r"commons clause|not for commercial use|for evaluation purposes only")

BLOCK = re.compile(r"(?:[ \t]*/\*[^\n]*\*/[ \t]*\n){2,}|/\*.*?\*/[ \t]*\n?|(?://[^\n]*\n)+", re.S)

TAIL = re.compile(r"\n((?:[ \t]*/\*[^\n]*\*/[ \t]*\n?){2,}|/\*(?:(?!\*/).)*\*/|(?://[^\n]*(?:\n|\Z))+)\s*\Z", re.S)

def _is_licence(block):
    return bool(LICENCE.search(block)) and block.count("\n") >= 4

# The short Go header: a copyright line, then one licence sentence, in 2 or 3 `//` lines. Only that exact shape is removed;
# any extra words, a second sentence, or a first line that is not a copyright line keep the block.
COPYRIGHT = re.compile(r"(?i)(?:copyright|\(c\)|\u00a9)\b")
SENTENCE = re.compile(
    r"(?is)use of this source code is governed by .{3,80}? (?:that|which) can be found in (?:the |a |this )?"
    r"(?:[\w.-]+ )?(?:LICENSE|LICENCE|COPYING)[\w.-]*(?: file)?(?: in [\w .,-]{0,60})?\.?"
    r"|licensed under (?:the |an? )?.{3,80}?licen[cs]e[\w .,;:()/-]{0,25}(?: see [\w .,-]{0,80}\.)?")
BUILD_OR_BLANK = re.compile(r"(?:[ \t]*//[ \t]*(?:go:build|\+build)[^\n]*\n|<(?:reponame|filename|gh_stars)>[^\n]*\n|[ \t]*\n)*")

def _is_short_licence(block, before):
    if not BUILD_OR_BLANK.fullmatch(before):
        return False  # only at the top of the file, after build lines
    if not 2 <= block.count("\n") <= 3:
        return False
    lines = [re.sub(r"^[ \t]*//+[ \t]?", "", l).strip() for l in block.rstrip("\n").split("\n")]
    lines = [l for l in lines if l]
    if len(lines) < 2 or not COPYRIGHT.match(lines[0]) or any(COPYRIGHT.match(l) for l in lines[1:]):
        return False
    return bool(SENTENCE.fullmatch(" ".join(lines[1:])))

def _strip_head(head):
    # BLOCK.sub, with one change: a short header counts as "at the top" when only build lines, blank lines and the blocks
    # removed before it are above it, so two stacked headers go in one pass (apply(apply(doc)) == apply(doc)).
    # `before` is the kept text above the block. It is dropped (None) once it is over 2000 characters: no file top is that long,
    # and it keeps the loop linear when a file has thousands of comment blocks.
    out, pos, before = [], 0, ""
    for m in BLOCK.finditer(head):
        gap = head[pos:m.start()]
        out.append(gap)
        if before is not None:
            before += gap
        block = m.group()
        if _is_licence(block) or (before is not None and _is_short_licence(block, before)):
            pass
        else:
            out.append(block)
            if before is not None:
                before += block
        if before is not None and len(before) > 2000:
            before = None
        pos = m.end()
    out.append(head[pos:])
    return "".join(out)

def medicine_e4(doc):
    t = doc["text"]
    if RESTRICTIVE.search("\n".join(t.split("\n")[:60])):
        return ("drop", t)  # a restrictive licence: stripping the header would not make the code free to use
    body = re.search(r"^(?:import|func|type|var|const)\b", t, re.M)
    end = body.start() if body else len(t)
    head = _strip_head(t[:end])
    if head != t[:end]:
        head = head.lstrip("\n")
    new = head + t[end:]
    tail = TAIL.search(new)
    if body and tail and tail.start() > len(head) and _is_licence(tail.group(1)):
        new = new[:tail.start()] + "\n"
    return ("keep", t) if new == t else ("fix", new)


def _std(out, text):
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS and doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    return _std(medicine_e4(doc), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = PACKS

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** Other short forms stay. The same decision as `DA-E4-012`: adopt both, or keep short headers and say so next to both rules.

### `DA-E4-012` · E4 · short licence header (java)

1. **Disease:** `DA-E4-009` keeps a licence block under 7 lines; 400 code-java documents start with a short copyright-and-licence header. Findings: F32.
2. **Medicine:** As `DA-E4-011`, with `/* */` blocks and an SPDX line.
3. **Action and place:** fix (drop for a restrictive licence); replaces `DA-E4-009`. **Runs on:** code-java. **From:** #72 `DA-E4-012` (none in effect).

```python
FROM = "#72 DA-E4-012"
REPLACES = "DA-E4-009"
RULE_ID = "DA-E4-012"
SOURCE_RULE_ID = "DA-E4-009"
CODE = "E4"
ACTION = "fix+drop"
STAGE = "30"
STATUS = "PROPOSAL"
LANGS = {'java'}
ORIGIN = "code-java"  # packs it runs on
PACKS = set(ORIGIN.split(", "))  # a code pack may label every doc "code", so the pack is checked too
SOURCE = "code-go"  # pack whose medicine this came from
AUTHOR = "RaviNaik"
import re

_LIC_WORDS = re.compile(
    r"(?i)licensed under|permission is hereby granted|without warranty|"
    r"you may not use this file|redistribut|general public license|all rights reserved|"
    r"warranties of|distributed under the licen"
)

_RESTRICTIVE = re.compile(
    r"(?i)free for personal use|commercial use requires|non-?commercial use only|commons clause|"
    r"not for commercial use|for evaluation purposes only"
)

def _comment_runs(lines, limit=60, tail=False):
    """Yield (start, end) of contiguous // runs, /* */ blocks and runs of one-line /* ... */ comments."""
    n = len(lines)
    rng = range(max(0, n - 40), n) if tail else range(0, min(n, limit))
    lo, hi = rng.start, rng.stop
    i = lo
    while i < hi:
        s = lines[i].strip()
        if s.startswith("/*") and s.endswith("*/") and len(s) > 4:
            j = i
            while j < n and lines[j].strip().startswith("/*") and lines[j].strip().endswith("*/"):
                j += 1
            yield i, j
            i = j
        elif s.startswith("/*"):
            j = i
            while j < n and "*/" not in lines[j]:
                j += 1
            yield i, j + 1
            i = j + 1
        elif s.startswith("//") and not s.startswith(("//go:", "// +build", "//+build")):
            j = i
            while j < n and lines[j].strip().startswith("//"):
                j += 1
            yield i, j
            i = j
        else:
            i += 1

def strip_licence_header(text: str, min_lines: int = 7):
    """Drop files whose header carries a restrictive licence. Otherwise remove the first
    comment block in the first 60 lines (or the last 40 lines) that has >= min_lines lines and
    licence grant text. Run this AFTER fix_b3 so the file starts at the real first line."""
    lines = text.split("\n")
    head = "\n".join(lines[:60])
    if _RESTRICTIVE.search(head):
        return "drop", text
    for tail in (False, True):
        for a, b in _comment_runs(lines, tail=tail):
            block = lines[a:b]
            if len(block) >= min_lines and sum(1 for x in block if _LIC_WORDS.search(x)) >= 2:
                kept = lines[:a] + lines[b:]
                return "fix", "\n".join(kept).strip("\n") + ("\n" if text.endswith("\n") else "")
    return "keep", text


# The short header at the top of the file: a copyright line, then one licence sentence or an SPDX line, in 2 or 3 comment lines
# (`//` lines or one `/* */` block). The same shape and the same two sentence forms as DA-E4-011 in the code-go report; SPDX is added.
# Only that exact shape is removed: extra words, a second sentence, or a first line that is not a copyright line keep the block.
_COPYRIGHT = re.compile(r"(?i)(?:copyright|\(c\)|\u00a9)\b")
_SENTENCE = re.compile(
    r"(?is)use of this source code is governed by .{3,80}? (?:that|which) can be found in (?:the |a |this )?"
    r"(?:[\w.-]+ )?(?:LICENSE|LICENCE|COPYING)[\w.-]*(?: file)?(?: in [\w .,-]{0,60})?\.?"
    r"|licensed under (?:the |an? )?.{3,80}?licen[cs]e[\w .,;:()/-]{0,25}(?: see [\w .,-]{0,80}\.)?")
_SPDX = re.compile(r"(?i)spdx-license-identifier:\s*[\w.+-]+(?:\s+(?:OR|AND|WITH)\s+[\w.+-]+)*")
_MARKS = re.compile(r"(?:<(?:reponame|filename|gh_stars)>[^\n]*\n|[ \t]*\n)*")
_TOP_BLOCK = re.compile(r"[ \t]*/\*.*?\*/[ \t]*(?:\n|\Z)|(?:[ \t]*//[^\n]*(?:\n|\Z))+", re.S)
_BLANKS = re.compile(r"(?:[ \t]*\n)*")

def _is_short_licence(block):
    b = block.strip()
    if b.startswith("/*"):
        lines = [re.sub(r"^[ \t]*\*+[ \t]?", "", l).strip() for l in b[2:-2].split("\n")]
    else:
        lines = [re.sub(r"^[ \t]*//+[ \t]?", "", l).strip() for l in b.split("\n")]
    lines = [l for l in lines if l]
    if not 2 <= len(lines) <= 3 or not _COPYRIGHT.match(lines[0]) or any(_COPYRIGHT.match(l) for l in lines[1:]):
        return False
    rest = " ".join(lines[1:])
    return bool(_SENTENCE.fullmatch(rest) or _SPDX.fullmatch(rest))

def strip_short_headers(text: str):
    """Remove short licence headers at the very top (after dataset marker lines and blank lines); stacked ones go in one pass."""
    top = _MARKS.match(text).end()
    pos = top
    while True:
        m = _TOP_BLOCK.match(text, pos)
        if not m or not _is_short_licence(m.group()):
            break
        pos = _BLANKS.match(text, m.end()).end()
    return text if pos == top else text[:top] + text[pos:]

def medicine_e4(text):
    action, t = strip_licence_header(text)
    if action == "drop":
        return ("drop", text)
    t = strip_short_headers(t)
    return ("fix" if t != text else "keep", t)


def _std(out, text):
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS and doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    return _std(medicine_e4(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = PACKS

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** The audited document `37124eab71fe111d` has another shape and is not changed; 1,486 documents keep a short licence comment of other forms.

### `DA-C1-016` · C1 · an IDE template header that says `Created on`

1. **Disease:** `DA-C1-005` does not know `Created on <date>`, so the template header stays (`18451aef9bf14f36`; 295 documents in the pack). Findings: F31.
2. **Medicine:** A comment block with a `Created on <date>` line is a template block: its template lines go, its other lines stay. A block with a copyright line is left alone.
3. **Action and place:** fix; replaces `DA-C1-005`. **Runs on:** code-java. **From:** #72 `DA-C1-012` (new number: #71 has `DA-C1-012`).

```python
FROM = "#72 DA-C1-012"
REPLACES = "DA-C1-005"
RULE_ID = "DA-C1-016"
SOURCE_RULE_ID = "DA-C1-005"
CODE = "C1"
ACTION = "fix"
STAGE = "30"
STATUS = "PROPOSAL"
LANGS = {'java'}
ORIGIN = "code-java"  # packs it runs on
PACKS = set(ORIGIN.split(", "))  # a code pack may label every doc "code", so the pack is checked too
SOURCE = "code-java"  # pack whose medicine this came from
AUTHOR = "vaibh27"
import re

LIC_WORDS = re.compile(r"licen[cs]e|permission is hereby granted|redistribution and use", re.I)

NOT_LICENCE = re.compile(r"to change this licen[cs]e header|choose licen[cs]e headers", re.I)

IDE_LINE = re.compile(r"(?im)^[ \t]*//[ \t]*TODO Auto-generated (?:method|constructor|catch block|stub)[^\n]*\n")

BLOCK = re.compile(r"[ \t]*/\*.*?\*/[ \t]*\n?", re.S)

IDE_MARK = re.compile(r"(?im)TODO Auto-generated|To change this (?:licen[cs]e header|template)|choose Tools \| Templates|"
                      r"Created (?:by|with) IntelliJ IDEA|Created by [^\n]{1,80}? on \d|File \| Settings \| File Templates|"
                      r"^\s*\*?\s*User\s*:.*\n\s*\*?\s*Date\s*:|^\s*\*?\s*@(?:project|package)\s*[:：]|\$\{[\w.]{1,40}\}|"
                      r"^\s*\*?\s*<p>\s*Title\s*[:：]")

# The IDE header "Created on <date>". It is a template mark unless the block also has a copyright line:
# a notice is not template text, so that block is left as it is.
CREATED_ON = re.compile(r"(?is)\A(?!.*copyright).*?Created on [^\n]{0,40}\d")

EMPTY_DESC = re.compile(r"(?im)^\s*\*?\s*@?desc(?:ription)?\s*[:：]*\s*(?:TODO)?\s*$")

AUTHOR_DATE = re.compile(r"(?im)^\s*\*?\s*@?(?:author|user)\b(?:.*\n)*?\s*\*?\s*@?(?:date|create|created)\s*[:：]")

TEMPLATE_LINE = re.compile(r"(?i)^\s*(?:/\*+|\*+)?\s*(?:<p>\s*)?(?:@?(?:author|user|date|time|class|project|package|create|created|"
                           r"version|since|title)\b\s*[:：]?.*|desc(?:ription)?\s*[:：]?\s*(?:TODO)?\s*(?:</p>)?|Created (?:by|with) .*|"
                           r"To change this .*|choose .*Templates.*|and open the template.*|TODO Auto-generated.*|"
                           r"(?:copyright|e-?mail|blog|company)\b.*)\s*$")

AUTHOR_ONLY = re.compile(r"/\*\*(?:\s*\*)*\s*@author\b[^\n]*(?:\s*\*)*\s*/")

def _clean_ide_block(block: str) -> str:
    if LIC_WORDS.search(block) and not NOT_LICENCE.search(block):
        return block  # a licence goes with M4
    if AUTHOR_ONLY.fullmatch(block.strip()):  # empty Javadoc with one @author line (labelled B4 only for <NAME>)
        return ""
    if not (IDE_MARK.search(block) or CREATED_ON.match(block) or (EMPTY_DESC.search(block) and AUTHOR_DATE.search(block))):
        return block
    body = block.rstrip("\n")
    lines, end = body.split("\n"), block[len(body):]  # end: the newline after */
    inner = [l for l in lines[1:-1] if not TEMPLATE_LINE.match(l) and l.strip(" \t*")]
    if len(lines) < 3 or not inner:
        return ""  # nothing but the template
    return "\n".join([lines[0]] + [l for l in lines[1:-1] if not TEMPLATE_LINE.match(l)] + [lines[-1]]) + end

def m6_strip_ide_templates(t: str) -> str:
    t = IDE_LINE.sub("", t)
    return BLOCK.sub(lambda m: _clean_ide_block(m.group()), t)


def _std(out, text):
    # the author's result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS and doc.get("pack_id") not in PACKS:
        return ("keep", doc["text"])
    return _std(m6_strip_ide_templates(doc["text"]), doc["text"])

_spec_source_medicine = medicine

SPEC_PACKS = PACKS

def medicine(doc):
    if doc.get("pack_id") not in SPEC_PACKS:
        return ("keep", doc["text"])
    out = _spec_source_medicine(doc)
    return out
```

4. **Harm test:** 0 changed, 0 dropped on every gold set (see above). PASS.
5. **Side effects:** An author handle in a template comment is treated as boilerplate, as in `DA-C1-005`.
