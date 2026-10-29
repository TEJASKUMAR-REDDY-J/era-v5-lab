# G1 Data A — Spec v1: Parent Medicine (DRAFT)

> **Status:** NOT APPROVED / NOT FROZEN. All `medicine.md` submissions below
> are inputs, not automatically executable or independently certified rules.
> **G2 Indic:** PENDING team handoff; not implicitly integrated.

## 1. Scope and source provenance

- Source directory: `teams/01-data-a/medicines/submissions` (recursive discovery).
- Found **21 medicine files**, **109 proposed sections**, **93 pack/disease groups**.
- Every source is listed below, including unfilled templates and unstructured sheets.
- The original Python examples are shown as non-executable text fences, never run by this builder.
- Re-run harm tests on regenerated gold sets; historic and proxy PASS claims are not current approval.
- Source excerpts are defensively redacted for obvious emails, phone numbers and token patterns;
  reviewers must still check E3/F1 and other sensitive strings before publishing.

| Pack | Contributor | Medicine sections | State | Source SHA-256 |
|---|---|---:|---|---|
| cadj-commits | kunal2016 | 0 | TEMPLATE | `f510a79661eef2f51c5ff122db3d8e3ab9ee7af77da713ed53cc4140f600eb9a` |
| cadj-commits | pradeep-kumar-gs | 1 | MEDICINES | `0e2d8f052d6a31fe7b70ffd28cb5318c713c50fff430b79b4cc7a981adc3b941` |
| cadj-commits | sureshmantha | 1 | MEDICINES | `1ed7c99b4963b94e844256497f1e7b893f7891cc717d4681c42dac618790f4fd` |
| cadj-stackexchange | smitasasindran | 2 | MEDICINES | `e78f856f5c8390f9304092da7a7d63cedff3fef9e8f1ae15e4092dbae5fa027f` |
| code-cpp | TharunSivamani | 5 | MEDICINES | `4aa2677fcb0e4d2d8786fe323fafeeda351d2bb3af22f629694c906f7fd97674` |
| code-go | RaviNaik | 5 | MEDICINES | `90e6acbc972e77cd517d9a7b2900f01ed89655f8a73ee6b6fe243fc825ad578b` |
| code-go | TEJASKUMAR-REDDY-J | 14 | MEDICINES | `fbfd3562bbf9432560b5e3934292c8e608c389939de22c1d188a1ebdf64be271` |
| code-java | curioustushar | 5 | MEDICINES | `ba7526cb282842b3cb7b2b67a16783b1fd8c53c61159bc3438362573a4974573` |
| code-java | vaibh27 | 4 | MEDICINES | `748af8d5a06ffd7cd342eedf2cf0817ab3c71c572e7c4c2288af387c9769cf5d` |
| code-js-ts | AjaySnl | 1 | MEDICINES | `508e59c856ab87d2e9036ba6232460ac104e7d52852cff1e699e898ab33dfc29` |
| code-js-ts | varshith2000 | 7 | MEDICINES | `4250eb8f593c583e3236810dcf12c25e311b0e76758ede9eeefac037602e08b9` |
| code-python | saitej123 | 11 | MEDICINES | `edfd817f22e91f36ac970e3392952732bbca4cbdfcfea7761ea7379fef9808e4` |
| code-rust | amukka | 5 | MEDICINES | `c638ff36e3662f231aa938efa42ec9fc5a9a82da111eba5e0a5a53cd30feb9cf` |
| en-dclm | mittalutkarsh | 0 | TEMPLATE | `f510a79661eef2f51c5ff122db3d8e3ab9ee7af77da713ed53cc4140f600eb9a` |
| en-dclm | shekar-maker | 8 | MEDICINES | `15131138f6df6e2b10953de4729f1440c93520a758bf03457dec7626cad8e356` |
| en-fineweb-edu | deepjyotisaha | 5 | MEDICINES | `cdf5a2aee7c2cba4640dfc7e95af91efa0b8e29dba5edce22c3ae02849261342` |
| en-nemotroncc-synth | AJJAPUSIVA | 5 | MEDICINES | `a5f09cd74f63548585abfccb095837082b7400c30276bad0afc17b1d4d051726` |
| en-nemotroncc-synth | maheshsv | 7 | MEDICINES | `f321f1120b3502f736bc9a8a8b0cce61c4adb7b5bcf6ba569d747870362e69d7` |
| en-nemotroncc | HariniJasti | 0 | TEMPLATE | `f510a79661eef2f51c5ff122db3d8e3ab9ee7af77da713ed53cc4140f600eb9a` |
| math-finemath | SomaKorada07 | 15 | MEDICINES | `89ea2898e6fa37f408e62d1f4e0ce4c3061044ab2bceac5cc9fb4d9fb8df284b` |
| sci-finepdfs | jssunil | 8 | MEDICINES | `9d8ffee19ac42232be3d5cbb3d65fbadc551dcd63510d5495d30af65cd36a3a3` |

## 2. Conflict resolution and execution decisions

**Safety resolution:** two or more distinct proposals for the same `(pack, disease)`
are **BLOCKED** from executable consolidation until a human selects/combines
an implementation and validates it against every applicable refreshed gold set.
Equivalent wording is only marked DUPLICATE, not automatically approved.
No rule is promoted to an approved pipeline by this generator.

| Pack | Disease | Proposals | Decision | Resolution |
|---|---|---:|---|---|
| cadj-commits | F1 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-go | B3 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-go | B4 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-go | E1 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-go | E2 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-go | E4 | 3 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-java | A2 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-java | B3 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-java | B4 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| code-java | E4 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| en-nemotroncc-synth | B4 | 3 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| en-nemotroncc-synth | C3 | 2 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |
| en-nemotroncc-synth | C4 | 3 | BLOCKED | Different or incomplete medicines: no executable rule selected until independent adjudication |

## 3. Five-field medicine records (source-based, not yet certified)

### Medicine 1: cadj-commits / F1 · pradeep-kumar-gs

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: F1.
> **Source:** [teams/01-data-a/medicines/submissions/cadj-commits/pradeep-kumar-gs/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/cadj-commits/pradeep-kumar-gs/medicine.md)

1. **Disease:** F1, 26 documents in this pack. Examples: `e0c1e30626b9b1ff` (at line 31; at line 60); `6454d40260da86f0` (at line 23; at lines 48-49; at lines 22-23); `49b151d5092e2af4` (at lines 25-26; at lines 63-64; at lines 62-63).

2. **Medicine:** Replace real-looking email addresses with <EMAIL>; example.com/test/localhost stay.

   ```text
   def fix_emails(text: str) -> str:
       """F1: replace real-looking email addresses with a placeholder (example.com and test addresses stay)."""
       email = re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}(?![\w-])")
       keep = re.compile(r"(?i)@(?:[\w-]+\.)*(?:example\.(?:com|org|net)|test|invalid|localhost)$")
       return email.sub(lambda m: m.group(0) if keep.search(m.group(0)) else "<EMAIL>", text)
   ```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   _not run: no gold set given (`--gold`)._ Proxy on this pack: it changes or drops 2 of the 124 documents you labelled clean.

5. **Side effects:** - Email-parsing tests lose their sample addresses.
   - Organisation addresses (a project's security or support mailbox) are replaced too.
   - Misses 2 of the 26 documents you labelled F1 (e.g. `d6617dadff45989c`, `1ed9b4ca0577b614`): those need a hand fix or a better rule.
   - Also changes 2 labelled document(s) you did not mark F1 (e.g. `47bb35e905ade74d`, `bb55c9242d2f7e4f`): check them.

### Medicine 2: cadj-commits / F1 · sureshmantha

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1 — F1: potential personal email addresses in code/commit records.
> **Source:** [teams/01-data-a/medicines/submissions/cadj-commits/sureshmantha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/cadj-commits/sureshmantha/medicine.md)

1. **Disease:** **40 candidate records** with named author, signer, reviewer or copyright contact information. Three examples: row 9 (`e0c1e30626b9b1ff`): email at offset 518; row 10 (`6454d40260da86f0`): email at offset 480; row 12 (`49b151d5092e2af4`): email at offset 742. The offsets are zero-based Unicode-character positions in the original `text` field. Public source availability does not by itself establish permission to train on personal contact information.

2. **Medicine:** Inspect each code record, identify email-address spans, and **confirm that the mailbox belongs to a private person** rather than a corporate contact or a clearly fictional fixture. Only redact confirmed private-person addresses. Preserve source-code punctuation and quotation syntax. Do not change the original pack in this assignment; provide the cleaning rule for approval.

   ```text
   import re
   EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])")

   def candidate_offsets(text: str) -> list[tuple[int, int]]:
       """Positions only. Do not emit the raw matched values to public logs."""
       return [(m.start(), m.end()) for m in EMAIL.finditer(text)]

   def redact_approved_spans(text: str, approved_spans: list[tuple[int, int]]) -> str:
       """Only use spans explicitly approved by privacy review."""
       for start, end in sorted(approved_spans, reverse=True):
           if not (0 <= start < end <= len(text)):
               raise ValueError("Invalid span")
           text = text[:start] + "[REDACTED_EMAIL]" + text[end:]
       return text
   ```

3. **Action:** `fix` confirmed personal addresses using a syntactically safe placeholder; escalate/drop the record if the change breaks code semantics. Do **not** automatically remove an organization’s designated package-maintainer address, anonymous placeholders, or synthetic seeded test values.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   **NOT EXECUTED — official code-language gold set not supplied.** Gold `N`: unknown; changed: unmeasured; dropped: unmeasured; affected fraction: unmeasured; **result: PENDING**. For the final approved *automatic* rule, compare original versus transformed text for every official gold record; count every changed or dropped record once and reject when `affected/N > 0.01`. A nonautomatic human approval step is not a substitute for testing a proposed scaled-up cleaning rule.

5. **Side effects:** Package metadata and copyright attribution may be meaningful; replacing email literals can modify intended test fixtures; publicly named reviewers can have official rather than personal addresses; regexes may flag syntactically incomplete email fragments. False positives must be tested with privacy-preserving evidence.

### Medicine 3: cadj-stackexchange / B3 · smitasasindran

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1 (unnumbered heading).
> **Source:** [teams/01-data-a/medicines/submissions/cadj-stackexchange/smitasasindran/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/cadj-stackexchange/smitasasindran/medicine.md)

1. **Disease:** B3, ghost chat markers
- **Count:** 500 of 500 documents, 1,966 occurrences in total: 500 `<issue_start>` and 1,466 `<issue_comment>`.
- **Examples:**
     - `87116d4f6facd13b`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 302 and 495.
     - `c9e11c8baa07c6e0`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 944, 1367 and 4657.
     - `d78b5eeab23e7a55`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 1120 and 302.

2. **Medicine:** Replace `<issue_start>` with `[issue_start]`   
Replace each `<issue_comment>` with `[issue_comment]`   

```text
import re

def cure_b3(text: str) -> str:
    text = text.replace("<issue_start>", "[issue_start]")
    text = text.replace("<issue_comment>", "[issue_comment]")
    return text
```

3. **Action:** fix the text. No document is dropped.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   PENDING. 
   
      | Gold set | Documents | Changed | Dropped | Result |
      |---|---|---|---|---|
      | _to fill_ | _to fill_ | _to fill_ | 0 | _pass if changed is 1% or less_ |
   
      The expected result is 0 changed for a gold set of source files, because they should contain none of these markers. If a gold set does contain `<issue_start>` or `<issue_comment>` text, those documents were not really clean, and that is worth reporting to the gold-set owners.

5. **Side effects:** Simple replace rule on exact match, should have no side effects

### Medicine 4: cadj-stackexchange / B4 · smitasasindran

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2.
> **Source:** [teams/01-data-a/medicines/submissions/cadj-stackexchange/smitasasindran/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/cadj-stackexchange/smitasasindran/medicine.md)

1. **Disease:** B4, redaction placeholders that look like HTML tags.
- **Count:** 162 occurrences in 53 documents: `<NAME>` 90 (24 docs), `<EMAIL>` 44 (13 docs), `<PASSWORD>` 27 (17 docs), `<KEY>` 1 (1 doc). About 130 of them are inside code snippets.
- **Examples:**
     - `a06ac825948fcdf1`: `@<NAME>,` at offset 1239.
     - `b79c9269b393f7ee`: `"email": "<EMAIL>",` at offset 119.
     - `32407cff5d9572ab`: `$password="<PASSWORD>";` at offset 410.

2. **Medicine:** Replace the exact tags `<NAME>`, `<EMAIL>`, `<PASSWORD>` and `<KEY>` with `[NAME]`, `[EMAIL]`, `[PASSWORD]` and `[KEY]`.  
Leave the `username_N:` labels in place.  
Other tags (`<br>`, `<image>`, `<div>`) are left alone.

```text
import re

def cure_b4(text: str) -> str:
    return re.sub(r"<(NAME|EMAIL|PASSWORD|KEY)>", r"[\1]", text)
```

3. **Action:** fix the text. No document is dropped.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   PENDING. Run `cure_b4` on the gold set with the sample check below.
   
      | Gold set | Documents | Changed | Dropped | Result |
      |---|---|---|---|---|
      | _to fill_ | _to fill_ | _to fill_ | 0 | _pass if changed is 1% or less_ |

5. **Side effects:** - In other code, `<NAME>` or `<KEY>` can be real syntax, for example a generic type `Map<KEY>` or a template. Replacing it would change the code. The gold-set test should show whether it happens in other languages.

### Medicine 5: code-cpp / A1 · TharunSivamani

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: A1.
> **Source:** [teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md)

1. **Disease:** A1, 12 rows. All current A1 evidence in the CSV is U+FEFF (BOM).
   - `782bc9665f0acdf7`: U+FEFF at offset 0.
   - `de12a2fd152768d6`: U+FEFF at offset 0.
   - `f63ec57866305825`: U+FEFF at offset 0.

2. **Medicine:** Remove U+FEFF only. Preserve other format characters, especially characters that may be meaningful in source text.

   ```text
   def remove_bom_characters(text: str) -> str:
       return text.replace("\ufeff", "")
   ```

3. **Action:** Fix the training-text copy by removing U+FEFF.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not run. No code-cpp gold set is present in the workspace. Test the change against the code-language gold set before release; the medicine fails if it changes more than 1% of that set.

5. **Side effects:** A U+FEFF used intentionally inside a document would be removed. Review its position and encoding role before applying the rule.

### Medicine 6: code-cpp / A2 · TharunSivamani

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: A2.
> **Source:** [teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md)

1. **Disease:** A2, 43 rows. All current A2 evidence in the CSV is carriage returns at line endings.
   - `09b5f5db05cc311d`: carriage return at offset 61; 29 affected lines.
   - `d5e1b337f212f4e2`: carriage return at offset 105; 386 affected lines.
   - `11edb16ce89987d8`: carriage return at offset 32; 111 affected lines.

2. **Medicine:** Normalize carriage-return line endings to LF. Do not remove tabs or ordinary LF newlines.

   ```text
   def normalize_line_endings(text: str) -> str:
       return text.replace("\r\n", "\n").replace("\r", "\n")
   ```

3. **Action:** Fix the training-text copy by normalizing line endings.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not run. No code-cpp gold set is present in the workspace. Test the change against the code-language gold set before release; the medicine fails if it changes more than 1% of that set.

5. **Side effects:** A literal carriage return embedded inside a string could be changed. Confirm matches occur as line endings before applying the rule.

### Medicine 7: code-cpp / B3 · TharunSivamani

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: B3.
> **Source:** [teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md)

1. **Disease:** B3, 243 rows. Important taxonomy caveat: all 243 CSV evidence entries point to `<reponame>`, `<filename>`, or `<gh_stars>` metadata prefixes. The disease guide defines B3 as ghost chat markers, and a full-pack scan found no examples of those markers. This proposal follows the current CSV labels, but the B3 classification should be reconciled with the guide before this medicine is approved.
   - `83dc5d60eaef6288`: `<reponame>` at offset 0.
   - `3a7b03b626595019`: `<filename>` at offset 0.
   - `a800be93ce443cb5`: `<gh_stars>` at offset 0.

2. **Medicine:** Remove the first line only when it begins with one of the observed metadata markers. The validation pass found that all 243 B3-labeled rows begin with one of these markers. Keep the metadata in structured fields; do not remove later source lines or rubric-defined chat markers under this rule.

   ```text
   import re

   METADATA_PREFIX = re.compile(
       r"\A<(?:reponame|filename|gh_stars)>[^\r\n]*(?:\r?\n|\Z)",
       re.IGNORECASE,
   )

   def remove_metadata_prefix(text: str) -> str:
       return METADATA_PREFIX.sub("", text, count=1)
   ```

3. **Action:** Fix the model-input copy by removing the dataset metadata line; retain the metadata outside the training text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not run. No code-cpp gold set is present in the workspace. Run this against the code-language gold set before release; the medicine fails if it changes more than 1% of that set.

5. **Side effects:** A genuine source line beginning with one of these tags could be removed. Limit the rule to the first line, review the matched line format, and preserve the original source.

### Medicine 8: code-cpp / B4 · TharunSivamani

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: B4.
> **Source:** [teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md)

1. **Disease:** B4, 119 rows. The most frequent recorded examples are redaction/template placeholders.
   - `ab726af7ee73aa3b`: `<NAME>` at offset 25.
   - `a800be93ce443cb5`: `<NAME>` at offset 29.
   - `0797d20110e8ab9b`: `<EMAIL>` at offset 13499 (3 occurrences).

2. **Medicine:** Remove only the known redaction placeholders observed in the CSV. Do not remove arbitrary angle-bracketed text, C++ templates, or strings such as `undefined`/`NaN` without context.

   ```text
   import re

   REDACTION_PLACEHOLDER = re.compile(
       r"<(?:NAME|EMAIL|PASSWORD|AUTHOR|YEAR)>", re.IGNORECASE
   )

   def remove_redaction_placeholders(text: str) -> str:
       return REDACTION_PLACEHOLDER.sub("", text)
   ```

3. **Action:** Fix the training-text copy by removing only exact redaction placeholders; preserve the original in the source archive.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not run. No code-cpp gold set is present in the workspace. Test the exact allowlist against the code-language gold set before release; the medicine fails if it changes more than 1% of that set.

5. **Side effects:** A placeholder may be part of an illustrative example or generated documentation. Exact-token matching avoids consuming surrounding code, but context review is still required.

### Medicine 9: code-cpp / E4 · TharunSivamani

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: E4.
> **Source:** [teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-cpp/TharunSivamani/medicine.md)

1. **Disease:** E4, 153 rows.
   - `83dc5d60eaef6288`: copyright header at offset 36; CSV evidence says the same text occurs in three documents.
   - `9f6e4e65e41f69c4`: `MIT License` header at offset 0, spanning 17 lines.
   - `9195ba155f4ee31e`: copyright header at offset 0, spanning 10 lines.

2. **Medicine:** Remove only an audited, exact license header that is confirmed to recur across documents. Keep a hash allowlist of the reviewed header text; do not delete arbitrary first comments containing the word "license".

   ```text
   def strip_verified_header(text: str, header: str) -> str:
       if header and text.startswith(header):
           return text[len(header):]
       return text
   ```

3. **Action:** Fix the training-text copy only after confirming that the identical header is repeated. Keep license and provenance information in metadata or a separate legal record.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not run. No code-cpp gold set is present in the workspace. Test each allowlisted header against the code-language gold set before release; the medicine fails if it changes more than 1% of that set.

5. **Side effects:** Removing a required attribution or a header that is not actually duplicated can violate license requirements or remove useful source context. Never apply a broad regex to all comments.

### Medicine 10: code-go / A2 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7: `DA-A2-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** A2, invisible control characters. Count: 1 of 500. Example:
   - `34133f5414afff81`: 409 carriage returns (U+000D), the first at offset 2, from Windows CRLF line endings

2. **Medicine:** Turn CRLF and lone CR into LF, and delete the other C0 control characters and DEL. Keep tab (U+0009),
   newline (U+000A) and form feed (U+000C), which source code uses.
   ```text
   RULE_ID = "DA-A2-001"
   LANGS = {"go"}
   import re
   CTRL = re.compile(r"[\x00-\x08\x0b\x0e-\x1f\x7f]")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = CTRL.sub("", doc["text"].replace("\r\n", "\n").replace("\r", "\n"))
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** all programming languages. Raw control characters in
   source are almost always line-ending debris. A language must pass its own harm test first, because some code has
   raw escape characters inside string literals.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 1 document,
      the one labelled A2.

5. **Side effects:** A raw control character that the code needs (for example a literal ESC byte inside a Go
   string) is deleted. None was seen in the pack. Go source should write `\x1b` instead.

### Medicine 11: code-go / A4 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 11: `DA-A4-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** A4, lost bytes shown as U+FFFD. Count: 1 of 500, plus the E5 debris next to them. Example:
   - `2a92a9a8489c5ea2`: `// ��ȸ` at offset 17258, a comment that holds only two U+FFFD and one leftover letter
     (U+0238, E5)
   - Not a case: `1dbf03039c9ea15c` has `// Replacement character �.` at offset 2384. The author quotes the character
     on purpose, so it is content, not A4 (ruling 7), and the rule must keep it.

2. **Medicine:** Delete a `//` comment that holds U+FFFD and no ASCII letter or digit. Such a comment is only
   debris. A comment that has real words around the U+FFFD, like the quoted one, is kept (ruling 7). The code itself
   is never touched.
   ```text
   RULE_ID = "DA-A4-001"
   LANGS = {"go"}
   import re
   LOST = re.compile(r"[ \t]*//[^\n\w]*�[^\nA-Za-z0-9]*$", re.M)

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = LOST.sub("", doc["text"])
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** C-family languages with `//` comments. Python and shell
   need the `#` form.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 1 document,
      the labelled A4/E5 file. The author-quoted U+FFFD file is not touched.

5. **Side effects:** U+FFFD inside a string literal, or inside a comment with words, is not repaired. The lost
   original bytes cannot be recovered, so the rule removes the debris but cannot restore the text.

### Medicine 12: code-go / A6 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 10: `DA-A6-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** A6, Cyrillic look-alike letters inside Latin words. Count: 2 of 500. Examples:
   - `64ed179e7e5c3d21`: `intс` at offset 1324, where the last letter is Cyrillic с (U+0441), in a command name
   - `48b3b124a7aaa5fc`: Cyrillic а (U+0430) and о (U+043E) inside a Latin word at offset 61 (type and position only:
     the word is part of personal data, F1)

2. **Medicine:** Find words that mix Latin letters with Cyrillic letters, and map the Cyrillic look-alikes in those
   words to their Latin twins (а→a, е→e, о→o, р→p, с→c, у→y, х→x, and the capitals). Words that are fully Cyrillic,
   such as Russian comments, are not touched.
   ```text
   RULE_ID = "DA-A6-001"
   LANGS = {"go"}
   import re
   HOMO = str.maketrans("аеорсухіјѕАВЕКМНОРСТХІЈЅ", "aeopcyxijsABEKMHOPCTXIJS")
   MIXED = re.compile(r"\b(?=\w*[A-Za-z])(?=\w*[Ѐ-ӿ])\w+\b")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = MIXED.sub(lambda m: m.group().translate(HOMO), doc["text"])
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** all programming languages. Greek look-alikes (ο, α) can
   be added the same way.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 2 documents,
      both labelled A6.

5. **Side effects:** In `48b3b124a7aaa5fc`, the look-alike letters were hiding a personal e-mail address from the
   earlier PII pass. The fix turns it back into a plain address, so **the PII pass must run again after this rule**.
   That is a benefit, because the address can then be redacted (F1). A real mixed word, such as a transliteration with
   one Cyrillic letter on purpose, would be changed. None was seen in the pack.

### Medicine 13: code-go / B3 · RaviNaik

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: B3, StarCoder metadata markers at the start of the file.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md)

1. **Disease:** B3, 247 of 500 documents (75 in the first 150). Examples: `c3e759376a153e83` has `<reponame>` at offset 0; `a7f76871d23b1bb2` has `<gh_stars>` at offset 26 (after `<reponame>`); `9b21eb8ec24619c6` has `<filename>` at offset 0. Some files carry two or three markers joined on line 1 (for example `<reponame>..<filename>..<gh_stars>..`). In the whole pack the markers always sit on the first line.

2. **Medicine:** the dataset builder prepended the repo name, the file path and the star count as plain text. Delete the marker line at the top (any of the three, in order). If a marker is found anywhere else in the file, drop the document, because the fix cannot be trusted.
```text
_B3_HEAD = re.compile(
    r"\A(?:<reponame>[^\n<]*)?(?:<filename>[^\n<]*)?(?:<gh_stars>[^\n<]*)?(?:\n|\Z)"
)
_B3_ANY = re.compile(r"<(?:reponame|filename|gh_stars)>")


def fix_b3(text: str):
    """Strip the marker line(s) at the top. Drop if a marker is left anywhere else."""
    m = _B3_HEAD.match(text)
    if not m or not _B3_ANY.match(text):
        return ("keep", text) if not _B3_ANY.search(text) else ("drop", text)
    new = text[m.end():]
    if _B3_ANY.search(new):
        return "drop", text
    return "fix", new
```

3. **Action:** fix (strip the first line). Drop only when a marker remains after the strip.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   on the 193-document proxy gold set it changes 0 and drops 0 (0.0%, limit 1%). On the 500 labelled rows it matches all 247 B3 labels with 0 false positives and 0 misses. After the fix no marker remains in any of the 217 documents it fixes, and every fixed document is still at least 207 characters and still contains a `package` line.

5. **Side effects:** the repo name and star count are lost. If the training team wants them as conditioning signals, they should be converted to real special tokens before training (team 10 and team 3 decide), not kept as plain text. A Go file that really discusses these marker strings in a comment would be flagged only if the marker is at offset 0, so this is very unlikely to hit real code. A fix of a leading marker does not repair other damage in the same file.

### Medicine 14: code-go / B3 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 14: `DA-B3-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** B3, StarCoder metadata markers (ruling 1). Count: 247 of 500. Examples:
   - `2f6d4b8c8e3fcbd5`: `<reponame>polaris-slo-cloud/polaris-scheduler` at offset 0
   - `2bdf36ae14fd90fa`: `<gh_stars>1-10` at offset 0
   - `b0eed26ac2f6a1a7`: `<filename>utils/convert.go` at offset 0

2. **Medicine:** In this pack the markers only ever appear as one run at the very start of the file, followed by a
   newline: `<reponame>`, `<filename>` and `<gh_stars>`, each followed by its value. Remove that run and the newline.
   It runs last, after the other rules, which read the `url` column and do not need the markers.
   ```text
   RULE_ID = "DA-B3-001"
   LANGS = {"go"}
   import re
   MARKERS = re.compile(r"^(?:<(?:reponame|filename|gh_stars)>[^<\n]*)+\n?")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = MARKERS.sub("", doc["text"])
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** every StarCoder language, since the markers come from the
   dataset, not from the code.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 247 documents, which are all 247 labelled B3 and nothing else.

5. **Side effects:** A file whose first line is a real string that starts with `<filename>` would lose that line.
   None is in the pack. A marker in the middle of a file is missed, and none was seen. The other StarCoder markers
   (`<issue_start>`, `<jupyter_...>`) are not in Go files and are not handled.

### Medicine 15: code-go / B4 · RaviNaik

> **Status:** BLOCKED; not approved. **Original section:** Medicine 5: B4, redaction placeholders (`<EMAIL>`, `<NAME>`, `<KEY>`, `<PASSWORD>`).
> **Source:** [teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md)

1. **Disease:** coded B4, as ruled by TSAI on 25 Oct (placeholders from earlier PII cleaning: B4, verdict fix, note PII placeholder). The dataset's PII scrubber replaced real values with the tokens `<EMAIL>`, `<NAME>`, `<KEY>`, `<PASSWORD>`. 43 of 500 documents contain one. Examples: `0f4121b3b47fc3e0` (`<NAME>` in a copyright line, offset 316), `d09425b871a43e73` (`Password: <PASSWORD>,` in code position, so the file no longer compiles), `e095932243abe03b` (`<KEY>` where a valid bech32 address is required, so the test cannot pass).

2. **Medicine:** in a comment, delete the token. In a string literal, replace `<EMAIL>` with `[REDACTED_EMAIL]` and `<NAME>` with `Jane Doe`. If the token is `<KEY>` or `<PASSWORD>`, or it sits in code position, the code is damaged: drop the document.
```text
_PH = re.compile(r"<(?:EMAIL|NAME|KEY|PASSWORD|IP_ADDRESS|USERNAME)>")
_SYNTH = {"<EMAIL>": "[REDACTED_EMAIL]", "<NAME>": "Jane Doe"}


def _context(line: str, col: int) -> str:
    """'comment', 'string' or 'code' for position col of a single line (line-local heuristic)."""
    pre = line[:col]
    s = line.lstrip()
    if s.startswith(("//", "*", "/*")) or "//" in pre:
        return "comment"
    if pre.count("`") % 2 == 1 or pre.replace('\\"', "").count('"') % 2 == 1:
        return "string"
    return "code"


def fix_placeholders(text: str):
    """Comment or string use of <EMAIL>/<NAME>: replace with a synthetic value (comments: delete).
    Any <KEY>/<PASSWORD>, or any placeholder in code position, broke the code: drop the file."""
    if not _PH.search(text):
        return "keep", text
    out = []
    for line in text.split("\n"):
        new, last = [], 0
        for mm in _PH.finditer(line):
            ctx = _context(line, mm.start())
            if mm.group() in ("<KEY>", "<PASSWORD>") or ctx == "code":
                return "drop", text
            new.append(line[last:mm.start()])
            new.append("" if ctx == "comment" else _SYNTH[mm.group()])
            last = mm.end()
        new.append(line[last:])
        out.append("".join(new))
    return "fix", "\n".join(out)
```

3. **Action:** fix for comments and strings; drop when the code is damaged or the token is `<KEY>`/`<PASSWORD>`.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   0 changed and 0 dropped on the 193-document proxy gold set (0.0%). On the 500 labelled rows it hits 34 of the 43 directly; the other 9 have the token inside a licence header, which Medicine 4 removes first, so the token is gone either way.

5. **Side effects:** the line-local context test is a heuristic. A token inside a multi-line string or a block comment may be seen as code and the file dropped (safe but lossy). The synthetic values look like personal data but use the reserved `example.com` domain. The rule is cautious on purpose with `<KEY>` and `<PASSWORD>`: three documents where I judged the file fixable by hand (`71c23854dac98b68`, `a3f10c54d87ce1fd`, `634696dba0edcbb7`: the placeholder stands alone in a string constant) are dropped by the rule. The opposite case is `8c13a363011078ca`: `<EMAIL>` swallowed parts of test strings, which the rule "fixes" by inserting an address, although the test inputs stay garbled.

### Medicine 16: code-go / B4 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 8: `DA-B4-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** B4, placeholders left by earlier PII cleaning (ruling 2). Count: 45 of 500. Examples:
   - `f08e1abfa9c2ebdc`: `<EMAIL>` at offset 138
   - `c05ecf8c28dd8d51`: `<NAME> <<EMAIL>>` at offset 20
   - `312d930b2b41cf89`: `<NAME> (<EMAIL>)` at offset 696

2. **Medicine:** Replace each of the four placeholders with a fixed neutral word, so that the model does not learn the
   `<NAME>` token and the Go string literals stay valid. `example.com` is a domain reserved for examples.
   ```text
   RULE_ID = "DA-B4-001"
   LANGS = {"go"}
   import re
   NEUTRAL = {"<NAME>": "AUTHOR", "<EMAIL>": "[REDACTED_EMAIL]", "<KEY>": "EXAMPLE_KEY", "<PASSWORD>": "EXAMPLE_PASSWORD"}
   PLACEHOLDER = re.compile("|".join(map(re.escape, NEUTRAL)))

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = PLACEHOLDER.sub(lambda m: NEUTRAL[m.group()], doc["text"])
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** every StarCoder language, since the same PII pass made
   the placeholders. 9 of the B4 documents are labelled `drop` for other reasons and are dropped by the drop rules
   (E1, H3, C3), except the F3 file.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 43 documents, all labelled B4.

5. **Side effects:** It cannot repair code that the redaction broke (`DA-C3-001` drops that file). Two kinds of B4
   are not handled. The PII pool swapped real IP addresses for other real-looking addresses (2 files), and the medicine
   cannot see that. A cobra template header has the words `NAME HERE <EMAIL ADDRESS>` (1 file), which is not one of
   the four placeholders. The neutral word turns a copyright line into "Copyright 2016 AUTHOR", which is still not
   the true author.

### Medicine 17: code-go / C1 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 12: `DA-C1-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** C1, template boilerplate left from a code generator's scaffold. Count: 1 of 500 labelled. Examples:
   - `45ac5026eac81b39`: `EDIT THIS FILE!  THIS IS SCAFFOLDING FOR YOU TO OWN!` at offset 628
   - `45ac5026eac81b39`: `NOTE: json tags are required.` at offset 684
   - `fd10104d4b8b5721`: `NOTE: json tags are required.` at offset 664 (the same kubebuilder note, not labelled C1)

2. **Medicine:** Delete the kubebuilder and operator-sdk scaffold notes. These are `//` comment lines with fixed
   wording that the tool writes into every new API type. Real doc comments are kept.
   ```text
   RULE_ID = "DA-C1-001"
   LANGS = {"go"}
   import re
   SCAFFOLD = re.compile(r'^[ \t]*//[ \t]*(?:EDIT THIS FILE!.*|NOTE: json tags are required\..*|'
                         r'Important: Run "make" to regenerate code after modifying this file.*|'
                         r'INSERT ADDITIONAL (?:SPEC|STATUS) FIELDS?.*)\n', re.M)

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = SCAFFOLD.sub("", doc["text"])
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** none. The scaffold is Go-only (kubebuilder and
   operator-sdk).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 2 documents:
      the one labelled C1, and `fd10104d4b8b5721`, which has the same scaffold note but was labelled for its licence
      only. That second file is a missed C1 label, not harm.

5. **Side effects:** A developer who copies one of these lines into their own comment loses it. Other generators'
   scaffold notes are not covered.

### Medicine 18: code-go / C3 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: `DA-C3-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** C3, a file that is no longer valid code. Count: 1 of 500. Example:
   - `a27e1273db746e7d`: `key := fmt.Sprintf("<KEY>` at offset 8404. The PII redaction cut the rest of the line,
     so the string is never closed and the file no longer parses.

2. **Medicine:** Run a small Go lexical check. Skip comments, strings (`"..."`, `` `...` ``) and runes (`'...'`), and
   count brackets. The file fails when a string, rune or block comment is not closed, when a `"` string runs into a
   newline, or when the brackets do not balance. A failed file is dropped.
   ```text
   RULE_ID = "DA-C3-001"
   LANGS = {"go"}

   def go_lexes(t):
       i, n, depth = 0, len(t), 0
       while i < n:
           c = t[i]
           if t.startswith("//", i):
               j = t.find("\n", i)
               i = n if j < 0 else j
           elif t.startswith("/*", i):
               j = t.find("*/", i + 2)
               if j < 0:
                   return False
               i = j + 2
           elif c in "\"'":
               i += 1
               while i < n and t[i] != c:
                   if t[i] == "\n":
                       return False
                   i += 2 if t[i] == "\\" else 1
               if i >= n:
                   return False
               i += 1
           elif c == "`":
               j = t.find("`", i + 1)
               if j < 0:
                   return False
               i = j + 1
           else:
               depth += (c in "{([") - (c in "})]")
               if depth < 0:
                   return False
               i += 1
       return depth == 0

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       return ("keep" if go_lexes(doc["text"]) else "drop", doc["text"])
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** none as it is. Every language has its own string and
   comment syntax, so each needs its own check. The best version for Go is the real parser (`gofmt -e` or `go/parser`).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 1 document, the one labelled C3. The other 499 files pass the check.

5. **Side effects:** It is a lexical check, not a full parser, so code with valid brackets but broken grammar is
   missed. A file cut off by a size limit in the middle of a function fails the check and is dropped, which is
   correct for training.

### Medicine 19: code-go / E1 · RaviNaik

> **Status:** BLOCKED; not approved. **Original section:** Medicine 2: E1, generated code.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md)

1. **Disease:** E1, 42 of 500 documents (15 in the first 150). Examples: `723e8d86cd1796ba` (`Code generated by skv2. DO NOT EDIT.` at offset 3), `8ce0877ba42fd4c9` (`Code generated by go-swagger; DO NOT EDIT.`, a go-swagger client), `4ae0cd8c3b8c9cf0` (`This file was autogenerated by deepcopy-gen. Do not edit it manually!` at offset 101, a vendored Kubernetes deepcopy file). Other generators seen: protoc-gen-go `.pb.go`, MockGen, AutoRest, Swagger Codegen, OpenAPI Generator, Kubeform `client-gen`/`lister-gen`, ffjson, controller-gen, FlatBuffers, the Pulumi SDK generator, the AWS SDK `gen-api`.

2. **Medicine:** look for a generated-code marker in the header only, that is before the `package` clause and in the 1500 characters after it. Markers deeper in the file, for example inside a string literal that a code generator prints, do not count (`5b33ed1435ccaccf` is a generator tool and stays). The pattern also accepts the wordings "this file was/is (automatically) generated", "automatically generated by", and two fingerprints for generators that print no marker: Kiota's hashed import alias and the goformation comment "specification version that this resource was generated from".
```text
_GEN = re.compile(
    r"(?im)^\s*(?://|/\*|\*)?\s*(?:"
    r"code generated\b|"
    r"auto-?generated|"
    r"由\w*自动生成|"
    r"\(re-\)?generated by\b.*|"
    r"generated by:?\s*(?:swagger|go-swagger|protoc|mockgen|microsoft|openapi)|"
    r"do not (?:edit|change) this file|"
    r"(?:\*{3}\s*warning:\s*)?this file (?:was|is|has been) (?:automatically |auto-?)?(?:generated|autogenerated)\b|"
    r"(?:this file )?(?:was )?automatically generated\b|"
    r"this file was generated by\b)"
)
# generator fingerprints that carry no marker line
_GEN_FINGERPRINT = re.compile(
    r"(?m)^\s*i[0-9a-f]{40,}\s+\"github\.com/microsoft/kiota|"
    r"AWSCloudFormationSpecificationVersion returns the AWS Specification Version that this resource was generated from"
)
_PKG = re.compile(r"(?m)^package\s+\w+")


def drop_generated(text: str):
    """Drop the file if a generated-code marker sits in the header (before `package`
    or within the first 40 lines). Markers inside string literals further down do not count."""
    m = _PKG.search(text)
    head = text[: m.end()] if m else text[:2000]
    head = "\n".join(head.split("\n")[:40]) if len(head) > 4000 else head
    # also allow the Go convention of the marker directly after the package clause (go-swagger)
    tail_probe = text[m.end(): m.end() + 1500] if m else ""
    if _GEN.search(head) or _GEN.search(tail_probe) or _GEN_FINGERPRINT.search(text[:3000]):
        return "drop", text
    return "keep", text
```

3. **Action:** drop the document. Generated files repeat the same boilerplate per endpoint or per message and teach little about writing Go.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   0 changed and 0 dropped on the 193-document proxy gold set (0.0%). On the 500 labelled rows: 41 of 42 found, 1 false positive, 1 miss (both below). The first version of the pattern found only 34 of 42; the 7 extra came from the wordings listed above.

5. **Side effects:** false positive `83381a2f882bdce3` (a swagger server stub that has a `Generated by` line but was heavily edited by hand; I labelled it E4 only). Miss `46f55367265bf0f0` (Cisco YANG model bindings): machine-generated but no marker, so it needs a structural rule (for example many near-identical `GetEntityData` methods). Dropping all generated code also removes examples of real API shapes (gRPC, protobuf); if the team wants a small sample, keep one file per generator.

### Medicine 20: code-go / E1 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: `DA-E1-002`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** E1, generated code (ruling 3: only when the code itself is generated). Count: 40 of 500. Examples:
   - `3c4db0c3d41b7673`: `// Code generated by MockGen. DO NOT EDIT.` at offset 0
   - `637118880fa53f2f`: `// Code generated by protoc-gen-go. DO NOT EDIT.` at offset 38
   - `3dc96675632ddcff`: `Code generated by Microsoft (R) AutoRest Code Generator.` at offset 196

2. **Medicine:** In the first 1500 characters, find a **comment line** (starting with `//`, `/*` or `*`) that holds
   a generator note: "Code generated", "generated by", "auto-generated", "automatically generated", or the Chinese
   "自动生成". The note has to be in a comment. A generator program that *prints* this line from a Go string
   (`fmt.Fprintln(out, "// Code generated ...")`) is hand-written code and is kept.
   Two generators print no marker line, so they are found by a fingerprint in the first 3000 characters: Kiota's
   hashed import alias for `github.com/microsoft/kiota...`, and goformation's comment "Specification Version that
   this resource was generated from". Both fingerprints come from RaviNaik's code-go sheet (PR #36).
   ```text
   RULE_ID = "DA-E1-002"
   LANGS = {"go"}
   import re
   GENERATED = re.compile(r"^[ \t]*(?://|/\*|\*)[^\n]*?(?:Code generated|generated by|auto-?generated|"
                          r"automatically generated|AutoRest Code Generator|自动生成)", re.I | re.M)
   FINGERPRINT = re.compile(r"(?m)^\s*i[0-9a-f]{40,}\s+\"github\.com/microsoft/kiota|"
                            r"Specification Version that this resource was generated from")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = doc["text"]
       return ("drop" if GENERATED.search(t[:1500]) or FINGERPRINT.search(t[:3000]) else "keep", t)
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** C, C++, Java, JavaScript/TypeScript, Rust and C#, which
   use the same comment markers. Python, Ruby and shell use `#` comments and need a new version.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 41 documents: all 40 labelled E1, and one goformation file labelled H3 (dropped anyway).
      A first version that also matched string literals dropped
      one hand-written generator program (`5b33ed1435ccaccf`). The comment-line rule fixed that.

5. **Side effects:** It misses generated code that has neither a header nor a known fingerprint. The earlier version
   `DA-E1-001`, which had no fingerprints, missed the Kiota file `352589a9ac5405c4`; `DA-E1-002` catches it.
   RaviNaik's wider pattern also matches `83381a2f882bdce3`, a server stub that was edited by hand. That match is a
   false positive, so that part of the pattern was not taken. Ruling 3 also covers the opposite case, a hand-written
   file that carries a "generated" header. That file would be dropped wrongly. None was seen in the pack.
   A comment such as "// the ID generated by the server" in the first 1500 characters would also match, so watch for
   this when the rule runs at scale.

### Medicine 21: code-go / E2 · RaviNaik

> **Status:** BLOCKED; not approved. **Original section:** Medicine 3: E2, embedded data blobs.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md)

1. **Disease:** E2, 7 of 500 documents. All are protoc-gen-go `.pb.go` files whose `rawDesc` or `fileDescriptor` is a long list of `0x..` bytes. Examples: `8c1931d1524ec642` (61% of the file is the byte array, first bytes `0x0a, 0x13` at offset 916), `dd9421d5a42adf64` (54%, `0x0a, 0x10` at offset 859), `023d4d7c1524277f` (37%, a gzipped descriptor starting `0x1f, 0x8b` at offset 1495). Hex strings that are test fixtures (for example a 500-character transaction in `c157efe0ccbf343f`) are not blobs.

2. **Medicine:** measure how much of the file is covered by byte-array literals (24 or more `0x..` items in a row) or by long base64-looking runs. Drop the document when byte arrays cover 10% or more, or base64 runs cover 40% or more. Removing the array would break the Go code, so there is no fix.
```text
_BYTES = re.compile(r"(?:0x[0-9a-fA-F]{2},\s*){24,}(?:0x[0-9a-fA-F]{2},?)?")
_B64 = re.compile(r"[A-Za-z0-9+/]{200,}={0,2}")


def drop_blob(text: str, share: float = 0.10, b64_share: float = 0.4):
    """Drop the file when byte-array literals cover at least `share` of it, or when base64-looking
    runs cover at least `b64_share`. Removing the array would break the Go code, so there is no fix."""
    if not text:
        return "keep", text
    n = len(text)
    if sum(len(m.group()) for m in _BYTES.finditer(text)) / n >= share:
        return "drop", text
    if sum(len(m.group()) for m in _B64.finditer(text)) / n >= b64_share:
        return "drop", text
    return "keep", text
```

3. **Action:** drop the document.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   0 changed and 0 dropped on the 193-document proxy gold set (0.0%). On the 500 labelled rows it finds all 7 E2 labels with 0 false positives. All 7 are also caught by Medicine 2, so in this pack the rule adds no extra drops; it is there for blobs without a generator marker.

5. **Side effects:** the 10% threshold is set from seven examples (their shares are 17% to 61%), so it is a guess for other packs. Generated files with smaller tables are caught by Medicine 2 only. A hand-written lookup table (for example a CRC table) with many `0x..` items could be dropped if it dominates a small file.

### Medicine 22: code-go / E2 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 4: `DA-E2-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** E2, a large binary blob embedded in the source as a byte array. Count: 3 of 500. Examples:
   - `637118880fa53f2f`: `0x1f, 0x8b, 0x08` at offset 5772 (a gzipped protobuf descriptor)
   - `91bf17319ac11223`: `file_dictybase_api_jsonapi_request_proto_rawDesc = []byte{` at offset 23934
   - `e673cf85cd68c71d`: `0x1f, 0x8b, 0x08` at offset 24790

2. **Medicine:** Drop the file when it holds 300 or more two-digit hex byte literals (`0x1f,`). A table of 256 bytes,
   such as a CRC or S-box table, stays below the limit. A file with more is mostly data, not code.
   ```text
   RULE_ID = "DA-E2-001"
   LANGS = {"go"}
   import re
   BYTE = re.compile(r"0x[0-9a-fA-F]{2}\s*,")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       return ("drop" if len(BYTE.findall(doc["text"])) >= 300 else "keep", doc["text"])
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** C, C++, Rust, Java and C#, which write byte arrays the
   same way.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 5 documents: the 3 labelled E2, and 2 more protobuf outputs with the same descriptor
      arrays (`dd9421d5a42adf64`, `8c1931d1524ec642`). Those two are labelled E1 and are dropped by `DA-E1-002` anyway.

5. **Side effects:** A hand-written file with a large lookup table (more than 300 bytes) would be dropped. A blob
   written as a string (`"\x1f\x8b..."`) or in base64 is missed.

### Medicine 23: code-go / E3 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 9: `DA-E3-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** E3, a hard-coded secret. Count: 1 of 500. Example (type and position only, never the value):
   - `98e4c493f32c8bfa`: TOTP secret seed (base32, 64 characters) in a string constant at offset 87

2. **Medicine:** Replace secrets with the word `EXAMPLE_SECRET`. Two kinds are covered. The first is well-known key
   formats: AWS access key, GitHub token, `sk-` API key, Slack token and PEM private key. The second is a base32 string
   of 16 or more characters assigned to a name that contains `secret`, `seed`, `totp` or `otp`. The code still
   compiles, because only the string content changes.
   ```text
   RULE_ID = "DA-E3-001"
   LANGS = {"go"}
   import re
   KEYS = [re.compile(p) for p in (r"AKIA[0-9A-Z]{16}", r"gh[pousr]_[A-Za-z0-9]{30,}", r"\bsk-[A-Za-z0-9_-]{20,}",
           r"xox[baprs]-[A-Za-z0-9-]{10,}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")]
   SEED = re.compile(r'(?i)((?:secret|seed|totp|otp)\w*\s*:?=\s*")[A-Z2-7]{16,}(")')

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = doc["text"]
       for rx in KEYS:
           t = rx.sub("EXAMPLE_SECRET", t)
       t = SEED.sub(r"\1EXAMPLE_SECRET\2", t)
       return ("fix" if t != doc["text"] else "keep", t)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** all programming languages for the key formats. The `:=`
   and `=` assignment pattern fits Go, Python, JavaScript and most C-family languages.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 1 document,
      the one labelled E3.

5. **Side effects:** Secrets with no known format and no telling variable name are missed. A full secret scanner
   (gitleaks or trufflehog rules) should run at scale. A public test vector (for example the RFC 6238 TOTP seed in a
   test) would be replaced too, which breaks that test.

### Medicine 24: code-go / E4 · RaviNaik

> **Status:** BLOCKED; not approved. **Original section:** Medicine 4: E4, long licence header.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/RaviNaik/medicine.md)

1. **Disease:** E4, 53 of 500 documents (20 in the first 150). Examples: `43950f6543ffa8ee` (13-line Apache header from offset 0), `24a7be0ee133443b` (15-line Apache header drawn as one-line `/* ... */` comments), `a1c8a3831a37b7e7` (13-line Apache block at the end of the file, offset 5695). Other holders seen: GPL-3.0 (`20331b3adb6eeb61`), AGPL-3.0 (`83d8307ca8489972`), and one restrictive header, `ab877ddc979bdd7d`: free for personal use and commercial trial, commercial use needs a paid licence.

2. **Medicine:** find the first comment block (a `//` run, a `/* */` block, or a run of one-line `/* ... */` comments) in the first 60 lines, or in the last 40 lines, that has at least 7 lines and at least 2 lines with licence-grant words ("Licensed under", "Permission is hereby granted", "WITHOUT WARRANTY", ...). Remove that block. If the header carries a restrictive licence phrase, drop the whole document instead. Short notices (an SPDX line, "see LICENSE", a 3-line MPL notice) are kept.
```text
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
```

3. **Action:** fix (remove the header); drop for restrictive licences.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   0 changed and 0 dropped on the 193-document proxy gold set (0.0%). On the 500 labelled rows it matches all 53 E4 labels with 0 false positives and 0 misses. Raising the minimum from 6 to 7 lines and adding the boxed and trailing cases were the changes made after the first 150 rows.

5. **Side effects:** the licence text is legal information, so the licence id and the copyright holder must be recorded in the shard manifest before the text is removed (this connects to the team 10 licence table). GPL and AGPL files are copyleft: stripping the header does not change their licence, so keep their licence id in the manifest and let team 10 decide whether to train on them at all. A block shorter than 7 lines, or a licence block in the middle of the file, is not found. The restrictive-phrase list is short and will miss other wordings.

### Medicine 25: code-go / E4 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 6: `DA-E4-003`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** E4, a licence header that does not allow the code to be used freely. Count: 1 of 500. Example:
   - `ab877ddc979bdd7d`: `Free for personal use and commercial trial` at offset 64, followed by "Commercial use requires per-user
     licenses"

2. **Medicine:** Look in the first 60 lines for a restrictive licence phrase ("free for personal use", "commercial use
   requires", "non-commercial use only", "Commons Clause", "not for commercial use", "for evaluation purposes only").
   If one is found, drop the file. Removing the header would not change the licence, so the file cannot be used for
   training. The phrase list comes from RaviNaik's code-go sheet (PR #36).
   ```text
   RULE_ID = "DA-E4-003"
   LANGS = {"go"}
   import re
   RESTRICTIVE = re.compile(r"(?i)free for personal use|commercial use requires|non-?commercial use only|"
                            r"commons clause|not for commercial use|for evaluation purposes only")

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       head = "\n".join(doc["text"].split("\n")[:60])
       return ("drop" if RESTRICTIVE.search(head) else "keep", doc["text"])
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** all programming languages. It reads only licence wording.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** On the pack it fires on 1 document,
      which `labels.csv` labels E4/fix. This sheet now proposes drop for it, because a header strip cannot make a
      restrictive licence free to use.

5. **Side effects:** The phrase list is short and misses other wordings. A file that only *mentions* such a licence in
   a comment, for example a licence checker, would be dropped. None was seen in the pack.

### Medicine 26: code-go / E4 · TEJASKUMAR-REDDY-J

> **Status:** BLOCKED; not approved. **Original section:** Medicine 13: `DA-E4-002`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** E4, licence text in the file header. Count: 76 of 500. Examples:
   - `2bdf36ae14fd90fa`: `Licensed under the Apache License` at offset 122
   - `3dc96675632ddcff`: `Licensed under the MIT License.` at offset 100
   - `83381a2f882bdce3`: `Permission is hereby granted, free of charge` at offset 95

2. **Medicine:** The header is the part of the file before the first `import`, `func`, `type`, `var` or `const` line.
   In the header, remove each comment block (a `/* ... */` block or a run of `//` lines) that has licence wording
   **and is at least four lines long**. Keep everything else: the package clause, build tags, package docs and
   generator notes. Short one- to three-line notes such as "Use of this source code is governed by a BSD-style
   license that can be found in the LICENSE file" are kept, because the harm test showed that removing them changes
   gold documents (see 4).
   Two more shapes are handled, both seen in RaviNaik's code-go sheet (PR #36). The first is a "boxed" header made of
   one-line `/* ... */` comments, one per line. The second is the same licence block placed at the very end of the
   file, after the code.
   ```text
   RULE_ID = "DA-E4-002"
   LANGS = {"go"}
   import re
   LICENCE = re.compile(r"Licensed under|Licensed to the Apache|Permission is hereby granted|Redistribution and use|"
                        r"Use of this source code is governed by|This source code is licensed under|"
                        r"released under the \w+ licen[cs]e|General Public License|Mozilla Public License", re.I)
   BLOCK = re.compile(r"(?:[ \t]*/\*[^\n]*\*/[ \t]*\n){2,}|/\*.*?\*/[ \t]*\n?|(?://[^\n]*\n)+", re.S)
   TAIL = re.compile(r"\n((?:[ \t]*/\*[^\n]*\*/[ \t]*\n?){2,}|/\*(?:(?!\*/).)*\*/|(?://[^\n]*(?:\n|\Z))+)\s*\Z", re.S)

   def is_licence(block):
       return bool(LICENCE.search(block)) and block.count("\n") >= 4

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       t = doc["text"]
       body = re.search(r"^(?:import|func|type|var|const)\b", t, re.M)
       end = body.start() if body else len(t)
       head = BLOCK.sub(lambda m: "" if is_licence(m.group()) else m.group(), t[:end])
       if head != t[:end]:
           head = head.lstrip("\n")
       new = head + t[end:]
       tail = TAIL.search(new)
       if body and tail and tail.start() > len(head) and is_licence(tail.group(1)):
           new = new[:tail.start()] + "\n"
       return ("keep", t) if new == t else ("fix", new)
   ```

3. **Action:** fix. **Applies to:** `go`. **Portable to:** C-family languages after a new header rule (the first
   `import`/`func` line is Go syntax). The licence wording list works for every language.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.** A first version without the four-line
      minimum also removed two-line "governed by a BSD/MIT-style license" notes. On the stand-in set it changed 3
      documents (1.8%) and failed, so the four-line minimum was added.
      On the pack it fires on 55 documents, all labelled E4.

5. **Side effects:** It leaves the short "governed by" notes untouched, on purpose (see 4). The earlier version
   `DA-E4-001` also missed the boxed header in `24a7be0ee133443b` and the licence at the end of `a1c8a3831a37b7e7`
   (offset 5695); `DA-E4-002` removes both. The restrictive licence in `ab877ddc979bdd7d` is handled by `DA-E4-003`. Removing the header also removes the copyright and licence notice that the licence asks to
   keep with the code. The licence of the source repository should be recorded in metadata before the text is
   removed. A licence block that sits right on top of the package doc comment, with no blank line between them, is
   one comment block, so the package doc goes with it.

### Medicine 27: code-go / F2 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: `DA-F2-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** F2, solutions to competitive-programming problems (benchmark leak risk). Count: 7 of 500. Examples:
   - `b44b171be56ec0f4`: `leetcode/1-100/0020.Valid-Parentheses` at offset 10
   - `da27b96957304886`: `leetcode/solutions/0119.PascalsTriangleII` at offset 39
   - `c33cef44b04d2df4`: path `.../leetcode/solutions/__114_path_sum.go`

2. **Medicine:** Drop the file when the repository name or the path names LeetCode, Codeforces or AtCoder.
   Code benchmarks such as HumanEval, MBPP and LiveCodeBench are built from problems like these.
   ```text
   RULE_ID = "DA-F2-001"
   LANGS = {"go"}
   import re
   CONTEST = re.compile(r"leetcode|codeforces|atcoder", re.I)

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       return ("drop" if CONTEST.search(doc["url"]) else "keep", doc["text"])
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** all programming languages. It reads only the path,
   so the code is the same for every language. Each language still needs its own harm test before it is added to
   `LANGS`.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS.**
      On the pack it fires on 6 documents, all labelled F2.

5. **Side effects:** It misses repositories that name the site in another way (`egregors/leetgo`, 1 file) and
   problem files that have no site name in the path. It drops every solution from those sites, including problems
   that are not in any benchmark. For a final list, the benchmark problem IDs should be matched against the problem
   number in the path.

### Medicine 28: code-go / H3 · TEJASKUMAR-REDDY-J

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: `DA-H3-001`.
> **Source:** [teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-go/TEJASKUMAR-REDDY-J/medicine.md)

1. **Disease:** H3, a vendored copy of another repository (the same code exists in its own repository). Count: 38
   of 500. Examples (from the `url` column):
   - `a976ed522ec7ab10`: `.../vendor/github.com/hashicorp/terraform/terraform/interpolate.go`
   - `2ca23804af7259a9`: `.../vendor/github.com/juruen/rmapi/filetree/treeutil.go`
   - `535f703c48d38087`: `.../vendor/github.com/aliyun/alibaba-cloud-sdk-go/services/...`

2. **Medicine:** Drop the file when its repository path has a `vendor/` folder. Go's `vendor/` holds copies of other
   modules.
   ```text
   RULE_ID = "DA-H3-001"
   LANGS = {"go"}
   import re

   def medicine(doc):
       if doc.get("lang_label") not in LANGS:
           return ("keep", doc["text"])
       return ("drop" if re.search(r"(?:^|/)vendor/", doc["url"]) else "keep", doc["text"])
   ```

3. **Action:** drop. **Applies to:** `go`. **Portable to:** PHP (Composer also uses `vendor/`) and Ruby
   (`vendor/bundle`). JavaScript needs `node_modules/` instead.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   163 gold documents: 0 changed, 0 dropped (0.0%). **PASS, with a note.** The medicine matches the
      labels exactly (38 fired, the same 38 labelled). The pass depends on the gold builder's dispute rule. Six vendored
      files have two `clean` votes (RaviNaik and udisinghania), but this sheet labelled them H3/drop, so the builder
      leaves them out of the gold set as disputed. If the team builds the gold set with `--allow-disputed` (two clean
      votes win), the rule drops those 6 (3.5%) and FAILS. So this is a disagreement between readers about whether a
      vendored copy is a disease. Under the 27 Oct answer, it should be settled by the lead, not by the rule.
      **Status: candidate, blocked on that decision.** The fallback route is **exact deduplication** at corpus level: drop a
      vendored file only when a byte-identical copy (the original in its own repository) is also in the corpus. That
      keeps every vendored file whose original is missing. It cannot be measured inside one pack: the pack has no exact
      duplicates, so the rule would fire on 0 documents here. Open question for the lead and the Data A lead.

5. **Side effects:** A project folder that is named `vendor/` but is not Go vendoring would be dropped. Vendored
   code that sits in other folders (`third_party/`, `external/`) is missed. Dropping a vendored file loses nothing
   only when the original repository is also in the corpus.

### Medicine 29: code-java / A2 · curioustushar

> **Status:** BLOCKED; not approved. **Original section:** Medicine 3: CRLF line endings (A2).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md)

1. **Disease:** A2. Count: **44** of 500 labelled; **44** of 500 in the pack.
   - `e0ebe203093970dc`: U+000D (CRLF) at offsets 17, 19, 45
   - `7fc99d2b6e1e3d08`: U+000D (CRLF) at offsets 2, 38, 63
   - `1a1a1d7ab0bf9188`: U+000D (CRLF) at offsets 2, 56, 60

2. **Medicine:** ```text
def m3_normalise_newlines(t: str) -> str:
    return t.replace("\r\n", "\n").replace("\r", "\n")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of 140 `clean` documents, drops 0.

5. **Side effects:** Does not change escaped \"\\r\\n\" inside string literals.

### Medicine 30: code-java / A2 · vaibh27

> **Status:** BLOCKED; not approved. **Original section:** Medicine 3: CRLF line endings (A2).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md)

1. **Disease:** A2, control character U+000D (CR) as Windows line endings (`0D 0A`). Count: 21 of 150 labelled;
   **44 of 500** in the pack. No lone CR and no other control characters in the pack.
   - `e0ebe203093970dc`: U+000D x38, first at offset 17
   - `7fc99d2b6e1e3d08`: U+000D x330, first at offset 2
   - `b584f0fe9264ce70`: U+000D x24, first at offset 47

2. **Medicine:** turn every CRLF into LF, then any lone CR into LF.
   ```text
   def m3_normalise_newlines(t: str) -> str:
       return t.replace("\r\n", "\n").replace("\r", "\n")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of my 10 `clean` documents, drops 0.

5. **Side effects:** Java treats CR and LF the same, so the program does not change. The escaped text `"\r\n"`
   inside a string is two ASCII characters, not U+000D, so it is not touched. A raw CR inside a Java text block
   (`"""`) would change the string value. I found none in the pack.

### Medicine 31: code-java / B3 · curioustushar

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: StarCoder metadata header (B3).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md)

1. **Disease:** B3. Count: **250** of 500 labelled; **250** of 500 in the pack.
   - `d0947d80d45f7ce3`: <filename> at offset 0
   - `c9eb2d8e4f9cacde`: <reponame> at offset 0
   - `a8a876672781cd58`: <reponame> at offset 0

2. **Medicine:** ```text
META_HEAD = re.compile(r"\A(?:<reponame>[^<\n]*|<filename>[^<\n]*|<gh_stars>[^<\n]*)+\n")

def m1_strip_meta_header(t: str) -> str:
    return META_HEAD.sub("", t, count=1)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of 140 `clean` documents, drops 0.

5. **Side effects:** Repo path metadata is removed; anchor is line 0 only.

### Medicine 32: code-java / B3 · vaibh27

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: StarCoder metadata header (B3).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md)

1. **Disease:** B3, ghost dataset tokens `<reponame>`, `<filename>`, `<gh_stars>` on the first line.
   Count: 73 of 150 labelled; **250 of 500** in the pack. These tokens never appear after the first line in this pack.
   - `d0947d80d45f7ce3`: `<filename>src/test/java/problems/RangeSumOfBSTTest.java` at offset 0
   - `7590b32d671f36c9`: `<reponame>88t6/vwkit-matrix<gh_stars>1-10` at offset 0
   - `073b348caf645018`: `<reponame>DezByte/multiverse<filename>multiverse-core/...RetryError.java<gh_stars>0` at offset 0

2. **Medicine:** if the document starts with one or more of these tokens, delete that whole first line. Touch nothing
   after it.
   ```text
   import re
   META_HEAD = re.compile(r"\A(?:<reponame>[^<\n]*|<filename>[^<\n]*|<gh_stars>[^<\n]*)+\n")

   def m1_strip_meta_header(t: str) -> str:
       return META_HEAD.sub("", t, count=1)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of my 10 `clean` documents, drops 0.

5. **Side effects:** the repo name and file path are lost. If we want them as metadata, copy them into a separate
   column before stripping. The rule is anchored at offset 0, so a `<filename>` string inside real code cannot match.
   After stripping, every one of the 250 documents starts with `package`, `import`, `public` or a comment. One
   document (`beae2c42d8a34ccc`) then starts with a BOM (A1), which needs its own fix.

### Medicine 33: code-java / B4 · curioustushar

> **Status:** BLOCKED; not approved. **Original section:** Medicine 2: PII redaction placeholders (B4).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md)

1. **Disease:** B4. Count: **83** of 500 labelled; **82** of 500 in the pack.
   - `13a397d8bedc6210`: <NAME> at offset 159 + <EMAIL> at offset 167
   - `8c9a9aa845f91a2c`: <EMAIL> at offset 284 + <PASSWORD> at offset 321
   - `4b761af28be90423`: <filename> at offset 0 + <gh_stars> at offset 35

2. **Medicine:** ```text
SURROGATE = {"<EMAIL>": "[REDACTED_EMAIL]", "<NAME>": "Author Name", "<PASSWORD>": "password"}

def m2_surrogate_placeholders(t: str) -> str:
    for k, v in SURROGATE.items():
        t = t.replace(k, v)
    return t
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of 140 `clean` documents, drops 0.

5. **Side effects:** Placeholder tokens in pack: 54 `EMAIL`, 1 `KEY`, 118 `NAME`, 21 `PASSWORD`. Does not fix unredacted phones (F1).

### Medicine 34: code-java / B4 · vaibh27

> **Status:** BLOCKED; not approved. **Original section:** Medicine 2: PII redaction placeholders (B4).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md)

1. **Disease:** B4 (ruling of 25 Oct: placeholders from earlier PII cleaning are B4, note `PII placeholder`; they
   are not personal data), the upstream PII-redaction placeholders `<NAME>`, `<EMAIL>`, `<PASSWORD>` and `<KEY>` left as
   plain text. A model trained on them learns to write these tokens. Count: 24 of 150 labelled; **82 of 500** in the
   pack (118 `<NAME>`, 54 `<EMAIL>`, 21 `<PASSWORD>`, 1 `<KEY>`).
   - `13a397d8bedc6210`: `@author <NAME> <<EMAIL>>`, `<NAME>` at offset 159
   - `8c9a9aa845f91a2c`: `String passWord = "<PASSWORD>";`, `<PASSWORD>` at offset 321
   - `4fce1af748c757ed`: `<NAME> (<EMAIL>)` 11 times (copyright line and `@author` tags), first `<NAME>` at offset 109

2. **Medicine:** replace each placeholder with a fixed, neutral surrogate. Do not delete it: in string literals,
   deleting it would leave `""` or broken code. Replace `<KEY>` only inside quotes, because a bare `<KEY>` is a legal
   Java generic type parameter (`class Cache<KEY>`).
   ```text
   SURROGATE = {"<EMAIL>": "[REDACTED_EMAIL]", "<NAME>": "Author Name",
                "<PASSWORD>": "password", '"<KEY>"': '"key"'}
   REDACT = re.compile("|".join(map(re.escape, SURROGATE)))

   def m2_surrogate_placeholders(t: str) -> str:
       return REDACT.sub(lambda m: SURROGATE[m.group()], t)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of my 10 `clean` documents, drops 0.

5. **Side effects:** - A real XML/HTML tag `<NAME>` inside a string would be changed. There are no `</NAME>`, `</EMAIL>` or
     `</PASSWORD>` closing tags in the pack, so I found no such case.
   - Every author becomes the same "Author Name". This is a small bias, but it is better than the special token.
   - The redaction was not complete. `1a1a1d7ab0bf9188` still has a real phone number (F1, offsets 40 and 1499) and a
     garbled `<EMAIL>H<EMAIL>`. M2 does not find unredacted PII. F1 needs its own rule.

### Medicine 35: code-java / C1 · curioustushar

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: IDE and generator boilerplate (C1).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md)

1. **Disease:** C1. Count: **69** of 500 labelled; **69** of 500 in the pack.
   - `e0ebe203093970dc`: 3-line IntelliJ template comment at offset 108
   - `c9eb2d8e4f9cacde`: 3-line IntelliJ template comment at offset 437
   - `50e06974390e57ea`: 5-line NetBeans template comment at offset 0 + empty Javadoc with only @author at offset 332

2. **Medicine:** ```text
NETBEANS = re.compile(
    r"\A\s*/\*\s*\n\s*\*\s*To change this license header.*?\*/\s*\n",
    re.S | re.I)
INTELLIJ = re.compile(
    r"\A\s*/\*\*?\s*\r?\n\s*\*\s*Created by [^\n]+\r?\n\s*\*/\s*\n",
    re.M)

def m5_strip_ide_boilerplate(t: str) -> str:
    for rx in (NETBEANS, INTELLIJ):
        t = rx.sub("", t, count=1)
    return t
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of 140 `clean` documents, drops 0.

5. **Side effects:** Does not remove class Javadoc or real documentation. Empty @author-only blocks inside classes need a separate rule.

### Medicine 36: code-java / E4 · curioustushar

> **Status:** BLOCKED; not approved. **Original section:** Medicine 4: Licence headers (E4).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/curioustushar/medicine.md)

1. **Disease:** E4. Count: **99** of 500 labelled; **99** of 500 in the pack.
   - `5655154f71365c63`: 18-line licence header at offset 0
   - `7fc99d2b6e1e3d08`: 4-line licence header at offset 0
   - `86534a30f79557fb`: 13-line licence header at offset 0

2. **Medicine:** ```text
LIC_HEAD = re.compile(r"\A(\s*)/\*.*?\*/[ \t]*\n", re.S)
LIC_WORDS = re.compile(r"licen[cs]e|permission is hereby granted", re.I)

def m4_strip_licence_header(t: str) -> str:
    m = LIC_HEAD.match(t)
    if not m or not LIC_WORDS.search(m.group()):
        return t
    if not re.match(r"\s*(package|import)\b", t[m.end():]):
        return t
    return t[m.end():].lstrip("\n")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of 140 `clean` documents, drops 0.

5. **Side effects:** Skips NetBeans template comments (C1). Misses some //-line and short copyright-only headers; see labels.

### Medicine 37: code-java / E4 · vaibh27

> **Status:** BLOCKED; not approved. **Original section:** Medicine 4: Licence headers (E4).
> **Source:** [teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-java/vaibh27/medicine.md)

1. **Disease:** E4, the same licence text at the top of many files (Apache-2.0 ASF, Apache-2.0 short form, MIT,
   BSD). Count: 24 of 150 labelled; **87 of 500** in the pack.
   - `5655154f71365c63`: 18-line ASF Apache-2.0 header, offsets 0 to 825
   - `4fce1af748c757ed`: 23-line MIT header, offsets 0 to 1205
   - `86534a30f79557fb`: 13-line Apache-2.0 short-form header, offsets 0 to 562; the same text is in 35 other documents

2. **Medicine:** if the document starts with a block comment that contains "license"/"licence" or "Permission is
   hereby granted", and the next code is `package` or `import`, delete that comment.
   ```text
   LIC_HEAD = re.compile(r"\A(\s*)/\*.*?\*/[ \t]*\n", re.S)
   LIC_WORDS = re.compile(r"licen[cs]e|permission is hereby granted", re.I)

   def m4_strip_licence_header(t: str) -> str:
       m = LIC_HEAD.match(t)
       if not m or not LIC_WORDS.search(m.group()):
           return t
       if not re.match(r"\s*(package|import)\b", t[m.end():]):
           return t  # may be a class Javadoc, not a file header
       return t[m.end():].lstrip("\n")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold set pending. Stand-in: changes 0 of my 10 `clean` documents, drops 0. On my 50 labelled rows
      On my 150 labelled rows it does not match my E4 labels yet (to fix by 31 Oct):
      - it fires on 2 NetBeans "To change this license header" templates (`50e06974390e57ea`, `6e3090899a74fa03`).
        They say "license" but hold no licence; I label them C1. M4 needs a guard for this template.
      - it misses 5 E4 headers: 4 written as `//` line comments (`2b64b0726c469c39`, `d1e50dcbfa47a388`,
        `f8d11746cccf1c17`, `73e175e90e6e37da`) and a BSD header without the word "license" (`fea61dd1f1c92f61`).

5. **Side effects:** - Short copyright-only headers without the word "license" (for example `7fc99d2b6e1e3d08`,
     "Copyright (c) 2010, tamacat.org. All rights reserved.") are kept. I did not label them E4 either.
   - A file in the default package (no `package` line) keeps its header. This is a miss, not harm.
   - The licence notice is removed from the training text. If the release team needs licence information, keep the
     header in a metadata column. Another option is to keep it once per repository instead of once per file. I need
     a decision from the lead on this.
   - A header that also holds real documentation (a file description inside the licence block) loses it.

### Medicine 38: code-js-ts / A2 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5 — A2 control characters.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** A2, 17 documents. Examples: `76882c7f242de544` (CR at offset 62),
   `7ae3bbd66580bde3` (CR at offset 51), `a7529f5930280cff` (CR characters at
   offsets 62, 64, and 126).

2. **Medicine:** Convert carriage returns used as CRLF line endings to LF. Preserve
   tabs and newlines; remove other control characters only after confirming they are
   not required by the source format.

   ```text
   def normalize_line_endings(text):
       return text.replace("\r\n", "\n").replace("\r", "\n")
   ```

3. **Action:** Fix line endings. Do not drop a document solely for CRLF.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** Blind removal can alter terminal-control examples, serialized
   data, or strings where a control character is intentional. Apply only to actual
   line-ending controls.

### Medicine 39: code-js-ts / B2 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1 — B2 source metadata leakage.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** B2, 244 documents. Examples: `c38890881e99e48e` (`<filename>` at
   offset 0 and `<gh_stars>` at offset 34), `c09dabc135210035` (`<reponame>` at
   offset 0), `7ffff923de0354f6` (`<reponame>` at offset 0 and `<filename>` at
   offset 76).

2. **Medicine:** Remove only leading dataset metadata fields `<reponame>...`,
   `<filename>...`, and `<gh_stars>...`. Do not remove ordinary JSX/HTML tags or
   TypeScript generic syntax.

   ```text
   import re

   SOURCE_META = re.compile(
       r"\A(?:<(?:reponame|filename|gh_stars)>[^\r\n]*)+(?:\r?\n)?"
   )

   def remove_source_metadata(text):
       return SOURCE_META.sub("", text, count=1)
   ```

3. **Action:** Fix the text by removing the metadata prefix. Drop only when B2 is
   part of a generated artifact that independently meets the E1 rule.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** A broad tag-removal regex would damage JSX, HTML template
   strings, XML-like examples, and TypeScript generics. The rule must be anchored at
   the document start and limited to the three dataset fields.

### Medicine 40: code-js-ts / B3 · AjaySnl

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1 — B3: StarCoder ghost tokens.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/AjaySnl/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/AjaySnl/medicine.md)

1. **Disease:** **Code:** B3  
**Count in pack:** 258 documents out of 500  
**Description:** Documents from `bigcode/starcoderdata` carry StarCoder preprocessing tokens embedded in their text. These tokens were inserted by StarCoder's data pipeline to mark metadata (repository name, filename, star count) and to anonymise personal data (email addresses and author names). They are not part of the original source code. Training V5 on text containing these tokens would teach the model to generate them as plain text.

The tokens observed:

| Token | Docs containing token | Total occurrences |
|---|---|---|
| `<gh_stars>` | 107 | 107 |
| `<filename>` | 105 | 105 |
| `<reponame>` | 101 | 101 |
| `<NAME>` | 14 | 25 |
| `<EMAIL>` | 10 | 29 |

`<filename>`, `<reponame>`, and `<gh_stars>` each appear at most once per document (always as a prefix block). `<EMAIL>` and `<NAME>` may appear multiple times per document (once for each anonymised value).

**Four examples:**

**Example A — `<filename>` and `<gh_stars>` prefix block:**
- `doc_id=c38890881e99e48e`
- Text starts: `<filename>src/extended-repeater.js<gh_stars>0\nimport { NotImplementedError }...`
- `'<filename>'` at offset 0; `'<gh_stars>'` at offset 34

**Example B — `<reponame>` prefix:**
- `doc_id=c09dabc135210035`
- Text starts: `<reponame>heminjohnson/Node-Chat-App-With-Socket.io\nvar expect = require('expect')`
- `'<reponame>'` at offset 0

**Example C — `<EMAIL>` anonymisation token in test code:**
- `doc_id=ec27a58ce8941db1`
- Text contains: `...rule.passes('<EMAIL>', { primary_email: '<EMAIL>' })...`
- `'<EMAIL>'` at offsets 202, 230, 328 (multiple occurrences; 29 total across 10 documents)

**Example D — `<NAME>` author anonymisation token in licence header:**
- `doc_id=ac23df9698407bac`
- Text starts: `/** * Copyright (c) 2020 <NAME> * Licensed under the Apache License...`
- `'<NAME>'` at offset 32

---

2. **Medicine:** **Rule in words:**

1. Strip the StarCoder prefix block from the **absolute beginning** of the document. The block consists of one to five consecutive lines, each starting with `<reponame>`, `<filename>`, or `<gh_stars>` (in any order), followed by their value on the same line. The match must begin at character position 0.
2. Replace any remaining `<EMAIL>` tokens in the document body with `[REDACTED_EMAIL]`.
3. Replace any remaining `<NAME>` tokens with `[AUTHOR]`.
4. Remove any other ghost-marker tokens (chat template tokens) if present.

**Rule in code:**

```text
import re

# \A anchors to the absolute start of the string.
# This prevents the regex from matching a <filename>-like line in the middle
# of a document body. Using ^ with re.MULTILINE would incorrectly match
# any line starting with the token, not only the document's first line.
_STARCODER_LINE = r'<(?:reponame|filename|gh_stars)>[^\n]*\n?'
STARCODER_PREFIX_RE = re.compile(r'\A(?:' + _STARCODER_LINE + r'){1,5}')

# Replace <EMAIL> anonymisation tokens.
# [REDACTED_EMAIL] uses the IANA-reserved example.com domain (RFC 2606)
# and is a syntactically valid RFC 5321 email address.
# The old placeholder [email protected] was NOT RFC 5321 valid.
EMAIL_TOKEN_RE = re.compile(r'<EMAIL>')

# Replace <NAME> anonymisation tokens.
NAME_TOKEN_RE = re.compile(r'<NAME>')

# Remove other ghost markers (chat-template tokens) if present.
OTHER_GHOST_RE = re.compile(
    r'<\|im_start\|>|<\|im_end\|>|<\|endoftext\|>'
    r'|\[INST\]|\[/INST\]|<<SYS>>|<</SYS>>'
    r'|<think>|</think>'
)

def fix_b3(text: str) -> str:
    """Strip StarCoder prefix and replace anonymisation tokens."""
    text = STARCODER_PREFIX_RE.sub('', text, count=1)
    text = EMAIL_TOKEN_RE.sub('[REDACTED_EMAIL]', text)
    text = NAME_TOKEN_RE.sub('[AUTHOR]', text)
    text = OTHER_GHOST_RE.sub('', text)
    return text
```

---

3. **Action:** **Fix the text.** The underlying code is valid; only the StarCoder metadata prefix and anonymisation tokens need to be removed or replaced. Dropping the whole document would be wasteful for 258 otherwise-clean files.

Exception: if B3 co-occurs with E1 (compiled/generated code) or E3 (embedded secrets), the verdict is `drop` regardless of this medicine, because the other disease takes precedence.

---

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   #### 4a. Regression tests (automated, pass/fail)
   
   20 unit tests covering:
   
   | Test group | Cases covered | Result |
   |---|---|---|
   | Anchor correctness | Valid prefix stripped; body token NOT stripped; no-prefix doc unchanged; trailing blank after prefix | 6/6 pass |
   | Token-like strings in code | `<filename>` in `//` comment; in string literal; in object value; in JSX attr (with whitespace); at non-zero line start | 5/5 pass |
   | EMAIL replacement | String-literal context; known test-literal regression; EMAIL inside prefix block | 3/3 pass |
   | NAME replacement | Copyright header; doc without token | 2/2 pass |
   | OTHER_GHOST_RE | Chat token stripped from body; `<s>` HTML tag preserved; chat token in string literal removed; chat token in comment removed | 4/4 pass |
   
   **Total: 20/20 pass.**
   
   Key result for the anchor fix: test `1c` confirms that a `<filename>` line in the document body is **not** stripped with the `\A` anchor. The old `re.MULTILINE` version incorrectly stripped it (test `1d` documents the bug).
   
   Tests `5c` and `5d` document that `OTHER_GHOST_RE` removes ghost tokens globally — including from inside string literals and comments. This is the intended behaviour (see side effect 8 below) and is tested, not assumed.
   
   #### 4b. Proxy harm test (informative, not definitive)
   
   **Official gold set status: BLOCKED — gold set unavailable.**
   
   The official JavaScript/TypeScript gold set (≥ 200 documents reviewed by two readers and marked `clean`) has not yet been released by the Data A team. The following proxy result is non-definitive and is provided for orientation only.
   
   | Metric | Value |
   |---|---|
   | Proxy set | 66 documents labelled `clean` in the corrected first-150 diagnosis |
   | Docs changed by `fix_b3()` | 0 |
   | Docs dropped by `fix_b3()` | 0 |
   | Percentage affected | 0.00% |
   | Passes 1% threshold? | Yes (informatively) |
   
   **What this proxy test does and does not cover:**
   
   The 66 proxy documents were labelled `clean` by automated scanning (every character checked by the detection functions). Per DISEASES.md, `read=partial` applies only when the reviewer does not read the language well; JavaScript and TypeScript impose no such barrier. All 66 proxy documents are marked `read=full`.
   
   The proxy test does **not** verify:
   - Whether `fix_b3()` correctly strips prefixes from the 258 B3 documents (the regression tests in §4a cover this).
   - Whether `fix_b3()` would alter any document in the official gold set (that set has not been released).
   - Whether the `<EMAIL>` → `[REDACTED_EMAIL]` substitution changes the correctness of email-validation tests in the gold set.
   
   **Procedure for the official gold-set test:**
   
   ```text
   def run_harm_test(gold_docs, fix_fn):
       """
       gold_docs: list of {'doc_id': str, 'text': str} from the gold set.
       Returns True if the medicine passes the 1% threshold.
       """
       changed = dropped = 0
       for d in gold_docs:
           fixed = fix_fn(d['text'])
           if fixed == '':
               dropped += 1
           elif fixed != d['text']:
               changed += 1
       total = len(gold_docs)
       pct = (changed + dropped) / total * 100 if total else 0
       print(f"Gold set: {total}  changed: {changed}  dropped: {dropped}  affected: {pct:.2f}%")
       return pct <= 1.0
   ```
   
   ---

5. **Side effects:** **1. `re.MULTILINE` anchor bug (fixed in this version).**  
The previous version used `re.compile(r'^...', re.MULTILINE)`. With that flag, `^` matches at the start of any line, not only at position 0. A document whose body contained a line starting with `<filename>…` would have had that line stripped. The fixed regex uses `\A`, which anchors exclusively to position 0 regardless of flags.

**2. StarCoder token in a string literal or comment at the document's first line.**  
If a document's very first line is a JavaScript string or comment that begins with the token text — for example, if a file starts with `const marker = '<filename>'` — the prefix regex would NOT match (the line starts with `const`, not `<filename>`). The medicine is safe in this respect. However, if a file starts with a bare `<filename>src/utils.js` line for reasons other than StarCoder preprocessing, that line would be stripped. This is considered benign: such a line would not be valid JavaScript.

**3. `<EMAIL>` in a test that validates the literal string `<EMAIL>`.**  
Document `ec27a58ce8941db1` uses `<EMAIL>` as an argument to a "Different" rule validator:  
`rule.passes('<EMAIL>', { primary_email: '<EMAIL>' })`  
After applying `fix_b3()`, both occurrences become `[REDACTED_EMAIL]`. For this specific test, the semantics are preserved: the "Different" rule compares input against `primary_email`; when both are the same value, the rule fails and `toBeFalsy()` still passes. However, for any test that checks whether the input is a **valid email address**, the replacement changes the outcome: `<EMAIL>` is not a valid email (so a validator would reject it), while `[REDACTED_EMAIL]` is a valid RFC 5321 address (so a validator would accept it). Such tests would change from passing to failing after the fix. This is a **known side effect** that cannot be avoided without knowing the full semantics of the test.

**4. `<EMAIL>` placeholder choice.**  
The old placeholder `[email protected]` was **not** RFC 5321 valid: the local part `[email protected]` contains brackets that are only valid inside a quoted string. The replacement `[REDACTED_EMAIL]` uses the IANA-reserved `example.com` domain (RFC 2606) and is syntactically valid. This reduces the risk of the placeholder being rejected by email-format validators.

**5. `<NAME>` in JSX-like angle-bracket syntax.**  
`<NAME>` could in theory be interpreted as a JSX element. However, JSX component names must begin with an uppercase letter; `<name>` would be a native DOM element, and `<NAME>` in all-uppercase does not correspond to any standard HTML tag or common JSX convention. The replacement `[AUTHOR]` introduces square brackets that are not valid JSX syntax, but since the surrounding context is a JSDoc comment block (`/** Copyright (c) 2020 <NAME> */`), this is acceptable: the comment is not parsed as JSX.

**6. Loss of file-path and star-count context.**  
The `<filename>` and `<gh_stars>` prefixes encode the original file path and GitHub star count. Stripping them removes this context. This is intentional: the signals were not part of the original file content, and V5 should not learn to generate them.

**7. Prefix quantifier limit.**  
The regex allows up to five consecutive metadata lines (`{1,5}`). If a rare document has more than five such lines, the sixth and beyond are preserved. Adjust the quantifier if a higher-count prefix format is observed in the full dataset.

**8. `OTHER_GHOST_RE` removes chat-template tokens globally, including from string literals and comments.**  
`OTHER_GHOST_RE` does not check whether a ghost token appears inside a JavaScript string literal, template string, or comment. Code that stores or documents chat-template token names as string values — for example, a library that parses or formats LLM prompts — will have those strings altered. This is intentional: DISEASES.md states that "a ghost marker in pre-training text teaches the model to write our special tokens as plain text", with no exception for string or comment contexts. No documents in the first-150 pack sample contained `<|im_start|>` or other chat-template tokens in any context; this side effect is low-risk for the `code-js-ts` pack.

---

*Medicine sheet complete for pack `code-js-ts`. Only B3 qualifies (258 > 5 occurrences). E1 has 4 occurrences in the first-150 diagnosis; E3 has 1. Neither reaches the 5-occurrence threshold for medicine in this slice. Full-pack E1 and E3 counts will be recalculated in the Oct 31 submission.*

---

### Medicine 41: code-js-ts / B4 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3 — B4 template and scrubber junk.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** B4, 25 documents. Examples: `cc42702a51d8a8ee` (`<question>` and
   `<KEY>` placeholders), `ec27a58ce8941db1` (`<EMAIL>` placeholders),
   `a2c50d532fb9d07a` (`<PASSWORD>` inserted into UI hint text).

2. **Medicine:** Treat placeholders as junk only when they are demonstrably injected
   into a value or prose field by a scrubber/template. Never replace a placeholder
   with a guessed value. Prefer restoring the original source; otherwise remove the
   affected fixture or document when its meaning is broken.

   ```text
   import re

   SCRUBBER_TOKEN = re.compile(r"<(?:EMAIL|NAME|PASSWORD|KEY|TOKEN|QUESTION)>")

   def has_scrubber_token(text):
       return bool(SCRUBBER_TOKEN.search(text))
   ```

3. **Action:** Fix when the original value can be safely restored; otherwise drop a
   broken generated fixture. Do not expose the replaced value.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** This pattern also appears legitimately in documentation,
   template examples, tests, and UI hints. Context review is mandatory; the regex is
   a detector, not a blind replacement rule.

### Medicine 42: code-js-ts / D3 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2 — D3 mixed-language code text.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** D3, 27 documents. Examples: `e2deacf4ecd2030b` (Chinese comments),
   `d5c3a1b4e003ed61` (Spanish UI strings), `0d3bff117f465b99` (Persian UI strings).

2. **Medicine:** No automatic translation or language normalization. Record the
   language in review metadata while preserving valid identifiers, comments, strings,
   and UI text.

   ```text
   def preserve_mixed_language(text):
       return text
   ```

3. **Action:** Keep the code unchanged. D3 is informational when the text is natural
   multilingual code content.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** Translation can corrupt identifiers, user-facing wording,
   comments, and tests. It can also incorrectly label natural multilingual software
   as defective.

### Medicine 43: code-js-ts / E1 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4 — E1 generated, minified, or build artifacts.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** E1, 19 documents. Examples: `7edec6fc57a3a792` (bundled UMD file),
   `82661aa7e8fdfc1f` (Doxygen search index), `991e567591fcf611` (autogenerated
   contract bindings).

2. **Medicine:** Drop generated artifacts when they have a strong generation marker
   or are clearly a minified/search-index/build output. Do not drop ordinary long
   source files merely because they are large.

   ```text
   import re

   GENERATED = re.compile(
       r"(?i)(auto[- ]?generated|autogenerated|do not edit|"
       r"var searchData\s*=|code generated by|sourceMappingURL=)"
   )

   def is_generated_artifact(text, filename=""):
       minified = text.count("\n") <= 2 and len(text) > 10000
       return bool(GENERATED.search(text)) or minified
   ```

3. **Action:** Drop the document or replace it with the original hand-written source
   file when available.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** Generated code can still be useful for reproducibility, and
   some legitimate source files contain “do not edit” comments. Require a strong
   marker or corroborating artifact evidence.

### Medicine 44: code-js-ts / E3 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6 — E3 secrets and credential assignments.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** E3, 9 documents. Examples: `0d3bff117f465b99` (Pusher client key at
   offset 8571), `8302c459b07901ca` (Google API key at offset 189),
   `6d3b68ef0b39f910` (passwords at offsets 1782, 2538, 3099, and 3661). Values are
   intentionally not reproduced.

2. **Medicine:** Detect secret-shaped assignments and redact the value without
   logging or copying it. If a real secret is present, quarantine/drop the document
   and rotate the credential outside this repository.

   ```text
   import re

   SECRET_ASSIGNMENT = re.compile(
       r"(?i)\b(api[_-]?key|token|password|passwd|secret|auth[_-]?token)\b"
       r"\s*[:=]\s*([\"'])(?:(?!\2).){8,}\2"
   )

   def contains_secret_assignment(text):
       return bool(SECRET_ASSIGNMENT.search(text))
   ```

3. **Action:** Redact or drop; never publish the value. Scrubbed placeholders alone
   are evidence of contamination but are not themselves secrets.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** API documentation, interface fields such as `API_SECRET`, test
   fixtures, and already-scrubbed placeholders can trigger the detector. Context and
   value inspection must be done privately.

### Medicine 45: code-js-ts / E4 · varshith2000

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7 — E4 repeated licence headers.
> **Source:** [teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-js-ts/varshith2000/medicine.md)

1. **Disease:** E4, 8 documents. Examples: `ac23df9698407bac` (Apache header),
   `1e918efcbd1c6f4b` (Apache header), `877058bd3cb250e3` (AGPL header). Short
   copyright notices were intentionally not counted as E4.

2. **Medicine:** Detect long repeated licence blocks at file starts. Retain one
   canonical licence notice when legally required; remove only duplicate copies or
   drop generated artifacts whose only content is a repeated licence/build header.

   ```text
   import re

   LICENSE_BLOCK = re.compile(
       r"(?is)\A(?:\s*(?:/\*+|//|#).*?"
       r"(?:apache license|gnu general public license|mit license|"
       r"all rights reserved|permission is hereby granted).*?"
       r"(?:\*/|\n))"
   )
   ```

3. **Action:** Fix duplicate headers while preserving required legal attribution.
   Do not remove a single legally required licence notice automatically.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Gold set unavailable locally; changes/drops N/A; pending run.

5. **Side effects:** Removing licence text can create legal/compliance problems, and
   short copyright notices are not the E4 disease. Review licence type and whether
   the header is duplicated before editing.

### Medicine 46: code-python / A1 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `A1` (Invisible junk characters), count `309` in pack (`218,079` documents scanned). Examples: `1024` (`⟦BOM⟧ U+FEFF at offset 0`), `2926` (`⟦BOM⟧ U+FEFF at offset 0`), `5537` (`⟦ZWSP⟧ U+200B at offset 28456`).

2. **Medicine:** strip only the A1 invisible junk characters from `diagnosis/tools/view_pack.py` (`VISIBLE` excluding `\t`, `U+FFFD`, `U+200C` ZWNJ, and `U+200D` ZWJ per `diagnosis/DISEASES.md`).
```text
from diagnosis.tools.view_pack import VISIBLE

DROP_A1 = {ch for ch in VISIBLE if ch not in ("\t", "\ufffd", "\u200c", "\u200d")}

def medicine_a1(text: str) -> str:
    return "".join(ch for ch in text if ch not in DROP_A1)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** a unit test that intentionally asserts the presence of a byte-order mark (`\ufeff`) or zero-width space (`\u200b`) literal loses that character. Preserving `U+200C` (ZWNJ) and `U+200D` (ZWJ) avoids corrupting Indic script conjuncts or composite emoji sequences.

### Medicine 47: code-python / A2 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `A2` (Control characters), count `39` in pack. Examples: `1935` (`⟦U+0008⟧ BACKSPACE at offset 3891`), `6672` (`⟦U+0010⟧ DATA LINK ESCAPE at offset 29013`), `6917` (`⟦U+008A⟧ CONTROL U+008A at offset 1238`).

2. **Medicine:** delete accidental C0/C1 control characters (`U+0000..U+0008`, `U+000B`, `U+000E..U+001A`, `U+001C..U+001F`, `U+007F..U+009F`) shown as `⟦U+XXXX⟧` by `diagnosis/tools/view_pack.py`, while preserving tab (`\t`), newline (`\n`), CR (`\r`), form-feed page breaks (`\x0c`), and ANSI escape sequences (`\x1b`).
```text
import re

RE_A2 = re.compile(r"[\x00-\x08\x0b\x0e-\x1a\x1c-\x1f\x7f-\x9f]")

def medicine_a2(text: str) -> str:
    return RE_A2.sub("", text)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** binary protocol tests that embed raw unescaped control bytes instead of `\xNN` escapes will have those bytes removed.

### Medicine 48: code-python / A3 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `A3` (Mojibake), count `11` in pack. Examples: `10401` (`mojibake 'Ã¡' at offset 7377 (3x)`), `14278` (`mojibake 'Ã¼' at offset 16999 (4x)`), `26910` (`mojibake 'Ã¥' at offset 2675`).

2. **Medicine:** repair double-decoded UTF-8 sequences (`Ã[\x80-\xbf]`, `â€™`, `â€œ`, `â€\x9d`, `â€“`, `â€”`) by re-encoding from CP1252/Latin-1 and decoding as UTF-8.
```text
import re

MOJIBAKE = re.compile(r"(?:Ã[\x80-\xbf]|â€™|â€œ|â€\x9d|â€“|â€”)")

def medicine_a3(text: str) -> str:
    def fix(m: re.Match[str]) -> str:
        s = m.group(0)
        try:
            return s.encode("cp1252").decode("utf-8")
        except UnicodeError:
            return s
    return MOJIBAKE.sub(fix, text)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** encoding unit tests that intentionally store mojibake fixtures would be normalized if not excluded.

### Medicine 49: code-python / A4 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `A4` (Replacement characters), count `21` in pack. Examples: `13867` (`⟦U+FFFD⟧ at offset 221`), `19500` (`⟦U+FFFD⟧ at offset 11816`), `20650` (`⟦U+FFFD⟧ at offset 2888 (12x)`).

2. **Medicine:** drop any document containing `U+FFFD` (``, shown as `⟦U+FFFD⟧` in `diagnosis/tools/view_pack.py`), unless the file is explicitly documenting `0xFFFD`, because the original bytes were already lost before release.
```text
def medicine_a4(text: str) -> str | None:
    return None if ("\ufffd" in text and "0xfffd" not in text.lower()) else text
```

3. **Action:** drop the document.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** drops files that intentionally include literal `` in a regex character class without mentioning `0xFFFD`.

### Medicine 50: code-python / B1 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `B1` (HTML entities), count `41` in pack. Examples: `4928` (`HTML entity &amp; at offset 6689`), `10770` (`HTML entity &amp; at offset 847`), `12051` (`HTML entity &quot; at offset 21672`).

2. **Medicine:** unescape HTML entities (`&amp;`, `&nbsp;`, `&lt;`, `&gt;`, `&quot;`, `&copy;`, `&reg;`, `&#NNN;`) only when they appear inside `#` comment lines, leaving Python string literals in HTML builders and web templates untouched.
```text
import html, re

RE_B1_COMMENT = re.compile(r"(?m)^\s*#[^\n]*?(&(?:amp|nbsp|lt|gt|quot|copy|reg);|&#\d{2,5};)")

def medicine_b1(text: str) -> str:
    def fix_line(line: str) -> str:
        if line.lstrip().startswith("#") and RE_B1_COMMENT.match(line):
            return html.unescape(line)
        return line
    return "".join(fix_line(ln) for ln in text.splitlines(keepends=True))
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** a comment that intentionally illustrates raw HTML entity syntax (e.g. `# use &amp; for ampersand`) is unescaped to `&`.

### Medicine 51: code-python / B3 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `B3` (Ghost chat markers), count `15` in pack. Examples: `4263` (`ghost marker <|endoftext|> at offset 3647`), `10143` (`ghost marker <|endoftext|> at offset 5864`), `19182` (`ghost marker <|endoftext|> at offset 2887`).

2. **Medicine:** strip `<|im_start|>`, `<|im_end|>`, `<|endoftext|>`, `[INST]`, `[/INST]`, `### Assistant:`, `<think>`, and `</think>` from pre-training text while preserving `<s>` and `</s>` (which are valid HTML strikethrough tags or NLP tokenizer literals in Python code).
```text
import re

GHOST = re.compile(r"<\|im_start\|>|<\|im_end\|>|<\|endoftext\|>|\[INST\]|\[/INST\]|### Assistant:|<think>|</think>")

def medicine_b3(text: str) -> str:
    return GHOST.sub("", text)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** tokenizer or stop-sequence scripts that reference literal `'<|endoftext|>'` lose that string literal.

### Medicine 52: code-python / C2 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `C2` (Repeated lines), count `34` in pack. Examples: `2418` (`line repeated 32 times consecutively at offset 1323`), `20636` (`line repeated 12 times consecutively at offset 3296`), `21766` (`line repeated 30 times consecutively at offset 2921`).

2. **Medicine:** when the exact same non-trivial line (`>= 20` stripped characters) is repeated `>= 12` times **consecutively**, cap that consecutive run at 3 lines; leave non-consecutive repeated lines across unit tests untouched.
```text
def medicine_c2(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out = []
    prev = None
    run = 0
    changed = False
    for line in lines:
        s = line.strip()
        if len(s) >= 20 and s == prev:
            run += 1
            if run >= 12:
                changed = True
            if run > 3:
                continue
        else:
            prev = s if len(s) >= 20 else None
            run = 1 if prev else 0
        out.append(line)
    return "".join(out) if changed else text
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** static lookup tables with 12+ identical consecutive rows are shortened to 3 rows.

### Medicine 53: code-python / E1 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 8.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `E1` (Minified or generated code), count `60` in `labels.csv` (`4,271` across the full `218,079`-document shard). Examples: `21` (`auto-generated header at offset 101`), `190` (`auto-generated header at offset 36`), `239` (`auto-generated header at offset 0`).

2. **Medicine:** drop any file that has a single line of `>= 2000` characters or an explicit auto-generated header (`# AUTOGENERATED! DO NOT EDIT`, `# Generated by the protocol buffer compiler`, `# Generated by Django`, `PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED`) in the first 1000 characters.
```text
import re

AUTOGEN = re.compile(
    r"(?i)(# *auto-?generated[^\n]{0,60}do not edit|"
    r"please do not edit this file, it is generated|"
    r"# *generated by the protocol buffer compiler|"
    r"# *generated by django)"
)

def medicine_e1(text: str) -> str | None:
    lines = text.splitlines()
    if lines and max(len(line) for line in lines) >= 2000:
        return None
    if AUTOGEN.search(text[:1000]):
        return None
    return text
```

3. **Action:** drop the document.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** drops notebook-exported modules (`nbdev`) and compiled protobuf stubs (`_pb2.py`).

### Medicine 54: code-python / E2 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 9.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `E2` (Data blobs), count `28` in pack. Examples: `2418` (`hex/number array of 6906 chars at offset 1275`), `13204` (`hex/number array of 1710 chars at offset 1027`), `26303` (`hex/number array of 2875 chars at offset 414`).

2. **Medicine:** replace embedded base64 payloads (`b64decode(...)`, `data:image/...;base64,...`, or padded base64 strings `>= 400` chars) and long hardcoded hex lookup arrays (`>= 64` consecutive `0x...` literals) with an empty placeholder.
```text
import re

BLOB = re.compile(
    r"(?:b64decode\s*\(\s*b?['\"][A-Za-z0-9+/=\s]{300,}['\"]|"
    r"data:image/[a-z]+;base64,[A-Za-z0-9+/=]{200,}|"
    r"['\"][A-Za-z0-9+/]{400,}={1,2}['\"]|"
    r"(?:\b0x[0-9a-fA-F]{2,8}\s*,\s*){64,})"
)

def medicine_e2(text: str) -> str:
    return BLOB.sub('""', text)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** hardware driver scripts or cryptographic S-box modules that inline 64+ hex constants lose the array contents unless imported from a data file.

### Medicine 55: code-python / E3 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 10.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `E3` (Secrets), count `13` in pack. Examples: `635` (`private key at offset 41541`), `8178` (`github token at offset 257`), `8802` (`private key at offset 5478`).

2. **Medicine:** drop any document matching a private key block, AWS access key ID, API key, or GitHub token.
```text
import re

SECRET = re.compile(
    r"AKIA[0-9A-Z]{16}|"
    r"BEGIN [A-Z ]*PRIVATE KEY|"
    r"\bsk-[A-Za-z0-9]{20,}|"
    r"\bgh[pousr]_[A-Za-z0-9]{30,}"
)

def medicine_e3(text: str) -> str | None:
    return None if SECRET.search(text) else text
```

3. **Action:** drop the document.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** drops unit tests that embed a full synthetic PEM private key fixture.

### Medicine 56: code-python / F1 · saitej123

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 11.
> **Source:** [teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-python/saitej123/medicine.md)

1. **Disease:** `F1` (Personal data), count `11` in pack. Examples: `37226` (`email at offset 648`), `47333` (`email at offset 4021`), `52535` (`email at offset 238`).

2. **Medicine:** replace personal email addresses in comment/docstring/`__email__`/`author_email`/`maintainer_email` metadata with `<EMAIL>`, leaving service/placeholder domains (`users.noreply.github.com`, `example.com`, `localhost`), decorators (`@app.route`), filenames (`@2x.png`), and matrix multiplication (`@`) untouched.
```text
import re

RE_F1_META = re.compile(
    r"(?im)^(?:\s*#|\s*\"\"\"|\s*'''|\s*__email__\s*=|\s*author_email\s*=|\s*maintainer_email\s*=)"
    r"[^\n]{0,80}?([A-Za-z][A-Za-z0-9._%+-]{1,40}@([A-Za-z][A-Za-z0-9.-]*\.[A-Za-z]{2,8}))\b"
)

def medicine_f1(text: str) -> str:
    return RE_F1_META.sub(lambda m: m.group(0)[:m.group(0).rfind(m.group(1))] + "<EMAIL>", text)
```

3. **Action:** fix the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   200 clean Python documents — `0` changed (`0.0%`), `0` dropped (`0.0%`). Pass (`<= 1%`).

5. **Side effects:** replaces author contact email strings in package setup headers with `<EMAIL>`.

### Medicine 57: code-rust / A2 · amukka

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: A2, control characters (CRLF).
> **Source:** [teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md)

1. **Disease:** A2, 6 documents. Examples: `2f34546793ed7faf` (227 CR U+000D, first at offset 36),
   `182c2cf59a3fa4f1` (38 CR, first at offset 12), `d185a07e3d515a8e` (29 CR, first at offset 94; hex `0d 0a`).
   No other control character was found in the pack.

2. **Medicine:** replace `\r\n` with `\n`, then delete any remaining U+0000-U+001F (except tab and newline) and U+007F.
   ```text
   text = text.replace("\r\n", "\n"); text = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", text)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold documents changed: PENDING / dropped: 0. Hit rate on my labels: 6 of 6, 0 extra.

5. **Side effects:** CR is U+000D, so the DISEASES.md definition counts CRLF as A2. But CRLF is valid in Rust source
   and normal for files written on Windows. About 1.2% of my pack (6 of 500) has it, so if two readers marked
   CRLF files as clean, this rule can reach the 1% limit by itself. If the gold set shows that, I would suggest
   treating A2 as "CRLF only, normalise" and moving it to a global preprocessing step instead of a disease.

### Medicine 58: code-rust / B3 · amukka

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: B3, StarCoder dataset markers.
> **Source:** [teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md)

1. **Disease:** B3, 225 documents. Examples: `e016447055203614` (`<gh_stars>1-10` at offset 0),
   `d1e5237063713aba` (`<filename>` at offset 0), `a500c6c5ef2132b5` (`<filename>` at offset 0). The pack has
   `<reponame>`, `<filename>` and `<gh_stars>` only, always on line 1. Per the 25 Oct ruling: label B3, verdict fix.

2. **Medicine:** if line 1 starts with `<reponame>`, `<filename>` or `<gh_stars>`, delete the whole line. Also delete
   `<issue_start>`, `<issue_comment>`, `<issue_closed>`, `<jupyter_*>` and `<empty_output>` anywhere (none in this pack).
   ```text
   MARKER_LINE = re.compile(r"^(?:<(?:reponame|filename|gh_stars)>[^\n]*)\n?")
   text = MARKER_LINE.sub("", text, count=1)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold documents changed: PENDING / dropped: 0 (this rule never drops). Hit rate on my labels: 225 of 225, 0 extra.

5. **Side effects:** the repo name and file path in the removed line are lost (the path is not needed). A real
   `<filename>` string in code at offset 0 would be removed too, which is very unlikely in Rust.

### Medicine 59: code-rust / B4 · amukka

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: B4, PII placeholders.
> **Source:** [teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md)

1. **Disease:** B4, 18 documents. Examples: `7dcf53c66a82f309` (`<NAME>` at offset 22, in a copyright line),
   `1a9f57255400a662` (`<EMAIL>` at offset 280), `ffbe67b8e7db9078` (`<KEY>` at offset 2381). The tokens are
   `<NAME>`, `<EMAIL>`, `<KEY>` and `<PASSWORD>`. They come from earlier PII cleaning and are not personal data.
   Per the ruling: label B4, verdict fix, note "PII placeholder".

2. **Medicine:** delete the token when it is in a comment or inside a string literal, otherwise (code position)
   replace it with `""`. A token is in a string when an odd number of `"` come before it on the line.
   ```text
   PII_PLACEHOLDER = re.compile(r"<(?:NAME|EMAIL|KEY|PASSWORD)>")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold documents changed: PENDING / dropped: 0. Hit rate on my labels: 18 of 18, 0 extra.

5. **Side effects:** it changes meaning in code: `author = "<NAME> <<EMAIL>>"` becomes `author = " <>"`. The one
   code-position case (`password: Some(<PASSWORD>.to_string())`) becomes `Some("".to_string())`, which still
   compiles. If the clean gold set also contains
   these tokens, this rule will fail the 1% limit, and then the better action is to leave them (they are harmless).

### Medicine 60: code-rust / E1 · amukka

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: E1, generated code.
> **Source:** [teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md)

1. **Disease:** E1, 23 documents. Examples: `920d344679eb3387` (`Generated by: openapi-generator.tech` in header),
   `9773497d0c18080b` (`Code generated ... DO NOT EDIT` at line 2), `462324dfcdae2d44` (openapi-generator output).
   Per the ruling, a header alone is not enough if the code below is hand-written. For example `8e7aa276c383727b` has a
   long generated-looking string interface but is hand-written, so it is clean.

2. **Medicine:** drop the document if (a) a banner matching `auto-generated | automatically generated | code
   generated | generated by | @generated | do not (directly) edit | this file is generated` appears in the first
   15 lines (after removing the B3 line), or (b) 20 or more lines contain `#[doc = "` (svd2rust register blocks).
   ```text
   if GENERATED.search("\n".join(body[:15])) or sum('#[doc = "' in l for l in body) >= 20: drop
   ```

3. **Action:** drop.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold documents changed: 0 by design / dropped: PENDING. Hit rate on my labels: 17 of 23, 0 extra.

5. **Side effects:** misses 6 generated files that have no banner (instruction test vectors with very long lines, an
   icon component with one 933-character SVG path, a pattern-built FHIR builder). A hand-written file that
   mentions "generated by" in its first 15 lines, for example a comment about a code generator it uses, would be
   dropped wrongly. This is the rule most likely to touch the gold set.

### Medicine 61: code-rust / E4 · amukka

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: E4, licence header.
> **Source:** [teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/code-rust/amukka/medicine.md)

1. **Disease:** E4, 22 documents. Examples: `b0a1eeeb782fea8c` (MIT licence, lines 2-19), `17e695a1c0fee084` (13-line
   Apache-2.0 header), `132f133c3df2dd7d` (about 42-line Apache + MIT header).

2. **Medicine:** after removing the B3 line, take the leading comment block. It is either one `/* ... */` or a run
   of `//` lines with single blank lines allowed. `//!`, `///`, `/*!` and `/**` doc comments are never part of it.
   Delete the block if it has 5 or more lines, at least 3 licence lines, and at least 40% of its non-blank lines are
   licence text (copyright, licensed, warranty, Apache, MIT, GPL, public domain, and similar).
   ```text
   if n >= 5 and hits >= 3 and hits * 10 >= len(lines) * 4: remove the block
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   gold documents changed: PENDING / dropped: 0. Hit rate on my labels: 21 of 22, 0 extra.

5. **Side effects:** a short 1-4 line header such as `// Copyright 2021 X` or SPDX is kept on purpose (the rule
   needs 5 or more lines). The one miss is `f4beb9cf72f11461`, a generated protobuf file that the E1 rule drops anyway. A hand-written
   explanatory comment that quotes licence terms for 5 or more lines would be removed. Removing the header also
   removes the copyright notice, which is a legal question for the data team, not a quality one.

### Medicine 62: en-dclm / A1 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: A1 invisible junk characters.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** A1, 12 documents. Examples: `4a22b0cbca7869fc` BOM `U+FEFF` at offset 0; `9f004914c20a592b` three
   BOMs `U+FEFF U+FEFF U+FEFF` at offset 0; `855032b92c2b8d25` soft hyphens `U+00AD` at offsets 161, 185, 527, 550
   (`ge­sprochen`); `f4e27249dc2787fc` LRE `U+202A` at offset 90; `11c3cd0e50856c3e` ZWSP `U+200B` at offset 0.

2. **Medicine:** delete ZWSP, BOM, soft hyphen and the bidi embedding/isolate marks. Keep ZWJ/ZWNJ.
   ```text
   A1_RE = re.compile("[​﻿­‪-‮⁦-⁩]")
   def m_a1(text): return A1_RE.sub("", text), False
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 10 changed, 0 dropped.

5. **Side effects:** a soft hyphen that a typesetter placed on purpose is deleted too, which joins the word
   correctly (`never­ending` → `neverending`), so no damage. Bidi marks in genuinely mixed-direction text (Arabic
   or Hebrew quotes inside English) would be lost; none in this pack. The medicine does not touch U+200C/U+200D.

### Medicine 63: en-dclm / A3 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: A3 mojibake.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** A3, 7 documents. Examples: `7b1d879aa4e04769` `â€”` for an em dash at offset 554 (52 hits, with
   `U+009D` controls); `94f537dcf85f69f8` `â€œ`-style quotes from offset 2494 to the end (57 C1-control bytes);
   `816e5ec1fb368590` `NoÂ waste` (`U+00C2 U+00A0`) at offset 596 and `Ã…` for `Å` at 3092; `5d1fd12b101321f0`
   `artistÂ\x92s` at 12598.

2. **Medicine:** detect the double-decoding signatures, repair with `ftfy.fix_text`, and drop the document only
   if the signature is still dense after repair (the bytes are gone, not just mis-decoded).
   ```text
   A3_RE = re.compile(r"â€[\x80-\xbf‘-™]?|Ã[\x80-\xbf\u0080-ÿ]|Â[\xa0-\xbf]|[\x80-\x9f]")
   def m_a3(text):
       if not A3_RE.search(text): return text, False
       new = ftfy.fix_text(text)
       return new, len(A3_RE.findall(new)) * 1000 / max(len(new), 1) > 1.0
   ```

3. **Action:** fix; drop when unrepairable.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 4 changed, 0 dropped.

5. **Side effects:** the signature regex misses mojibake that went through a non-UTF-8 round trip, for example
   Cyrillic `й` standing in for `é` (`Pokйmon` in `68575a61a90990d5`, `Diffйrents` in `467b5c0aa1d13de8`) and
   symbol-font gibberish (`3dc93ffbd87ba839`): 3 of the 7 labelled documents are not touched. `ftfy` can in rare
   cases "repair" legitimate text that happens to look like mojibake (`Ã` followed by a letter in Portuguese); the
   gold run will show whether that happens in English.

### Medicine 64: en-dclm / B4 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: B4 template and code junk in prose.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** B4, 23 documents. Examples: `e3fba14beec00b2b` tracking JS `fbq('track', 'ViewContent');` at offset
   0; `6da64e1f3aa0f61c` image alt residue `dougball.gif - 0.95 K` 18 times from offset 40315; `b0b8c0fe32cb4bee`
   filename `bigstock--191940913.jpg` glued to the first word at offset 126; `6d42edb6050b961a` template bug
   `WRITTEN BY Home Upgrades That Can Save You Money` at offset 39.

2. **Medicine:** delete the residue tokens, not the document.
   ```text
   B4_RES = [re.compile(r"\b[\w-]+\.(?:jpe?g|png|gif|webp)(?:\s*-\s*[\d.]+\s*K)?\b", re.I),
             re.compile(r"\bfbq\([^)]*\);?|\bgtag\([^)]*\);?|\bga\('send'[^)]*\);?"),
             re.compile(r"\{\{\s*[\w.]+\s*\}\}|\$\{[^}]{1,40}\}"),
             re.compile(r"^(?:undefined|NaN|null)\s*$", re.M)]
   def m_b4(text):
       new = text
       for rx in B4_RES: new = rx.sub("", new)
       return re.sub(r"[ \t]{2,}", " ", new) if new != text else text, False
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 8 changed, 0 dropped.

5. **Side effects:** recall is low (2 of 23 labelled documents): most B4 in this pack is placeholder text glued
   into words (`holder maleChase`, `Lance-Earl-Ladn-C-trucsLance`) or an unrendered theme string, which no regex can
   separate from prose. A tutorial that legitimately names `image.png` loses that filename.

### Medicine 65: en-dclm / C1 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: C1 boilerplate.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** C1, 386 documents (the most common disease: 77% of the pack). Examples: `a6673336e37d2ca9`
   breadcrumb `You are here: Home >` at offset 0 and `Related Links:` at 10208; `0864734353e1b73e` `YOU ARE HERE:
   LAT HomeCollections` at 0 and `Los Angeles Times Articles` at 4980; `80c9139ec8b57301` `Post a Comment` 9 times
   and `No comments :` 6 times; `401400b4e5ef2ee8` `Skip to: Site Menu | Main content` at 63.

2. **Medicine:** remove a line when it is short (8 words or fewer) and starts with a site-chrome phrase.
   ```text
   C1_RE = re.compile(r"^(?:share (?:on|this|via)|tweet|follow (?:us|me|@)|like us|related (?:posts?|articles?|links?|games?)"
       r"|read more|click (?:here|to)|leave a (?:comment|reply)|post(?:ed)? (?:a )?comment|no comments?|\d+ comments?"
       r"|posted (?:by|on|in)|filed under|tags?:|categor(?:y|ies):?|labels?:|skip to|you are here|home\s*[>»|]"
       r"|log ?in|sign (?:in|up)|register|subscribe|newsletter|all rights reserved|copyright|©|privacy policy"
       r"|terms of (?:use|service)|powered by|back to top|print this|email this|previous post|next post|older post"
       r"|newer post|view (?:all|profile)|contact us|advertisement|sponsored|links to this post|<< home)", re.I)
   def m_c1(text):
       keep = [ln for ln in text.split("\n") if not (ln.strip() and len(ln.split()) <= 8 and C1_RE.search(ln.strip()))]
       return re.sub(r"\n{3,}", "\n\n", "\n".join(keep)), False
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 117 changed, 0 dropped.

5. **Side effects:** the rule only matches a line that *starts* with a chrome phrase, so it reaches 117 of the 386
   labelled documents; the rest are repeated titles, nav bars like `Contents | < Browse | Browse >`, forum
   headers `Author Topic: ... (Read 289 times)` and comment chrome glued to prose with NBSP. A line of real prose
   that starts with "Register" or "Subscribe" (an instruction in an article) is deleted. A sentence that happens to
   start with "Copyright" in a legal article is deleted. These are the cases to check on the gold run.

### Medicine 66: en-dclm / C2 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: C2 repeated lines.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** C2, 30 documents. Examples: `50d363e8b8340b11` `never quiet, never soft.....` 21 times from offset
   2715; `8fa9168e8da3a2d4` `Individual Eyelashes Extensions` as a line 4 times at 180; `a874cd0a1d145148` title
   `Maintenance Bond` 3 times at 14/141/194; `e2f62269aa2a0900` caption `borrowed with permission from ...` 3 times.

2. **Medicine:** a line of 20+ characters that appears 3 or more times is kept once; if the repeated lines are more
   than 30% of the non-empty lines the document is dropped.
   ```text
   def m_c2(text, min_len=20, min_rep=3, drop_ratio=0.3):
       lines = text.split("\n")
       counts = Counter(ln.strip() for ln in lines if len(ln.strip()) >= min_len)
       rep = {ln for ln, c in counts.items() if c >= min_rep}
       if not rep: return text, False
       if sum(counts[ln] for ln in rep) / max(sum(1 for ln in lines if ln.strip()), 1) > drop_ratio: return text, True
       seen, out = set(), []
       for ln in lines:
           s = ln.strip()
           if s in rep:
               if s in seen: continue
               seen.add(s)
           out.append(ln)
       return "\n".join(out), False
   ```

3. **Action:** fix; drop when the document is mostly repetition.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 8 changed, 0 dropped.

5. **Side effects:** a refrain in a poem or song, a repeated stage direction in a play, or a repeated table header
   is collapsed to one copy. Short repeated lines (under 20 characters, e.g. `Post a Comment`) are left to Medicine 4.

### Medicine 67: en-dclm / C3 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6: C3 truncated document.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** C3, 98 documents. Examples: `cd0ef2540a4ee803` teaser cut with `...` at offset 317; `8b697f9f7d91de38`
   ends mid-sentence `I think that you will be` at 2680; `a1b97fd910707a8d` sentence cut where link text was stripped
   `I can't even find a link from` at 4095; `089fde49e557cc5d` ends with the heading `Female Problems` and no body.

2. **Medicine:** only the *stub* form is treated. A document of at most 600 characters whose last word is one no
   sentence ends on (`from`, `the`, `and`, ...) or that ends with a teaser `...` is dropped (the dangling-word test only applies when the text has no
   terminal punctuation).
   ```text
   DANGLING = set("a an the and or but of to in on at by for from with as that which who will would can could is are was were be been being has have had this these those its their his her my our your".split())
   def m_c3(text, max_len=600):
       body = text.rstrip()
       if len(body) > max_len: return text, False
       last = (re.findall(r"[A-Za-z']+", body) or [""])[-1].lower()
       teaser = body.endswith(("...", "…", "[...]", "[…]", "(more)", "Read more"))
       unfinished = body[-1] not in ".!?\"')]}»”’:;" and last in DANGLING
       return text, bool(teaser or unfinished)
   ```

3. **Action:** drop (stubs only); longer truncated documents are labelled, not cut.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 0 changed, 1 dropped.

5. **Side effects:** my first version trimmed any last line without terminal punctuation; it changed 5 of the 28
   documents then in the proxy set (complete sentences that simply lack a full stop), so it was withdrawn. The
   stub rule's dangling-word test then dropped a clean 560-character document ending `...what research impact is.`,
   which failed the 1% limit on the 65-document proxy; it now applies only when the text has no terminal
   punctuation. The rule catches 1 of the 98 labelled documents, because in this pack C3 is mostly mid-text gaps
   where a link, a citation, a quote or an image was stripped by an earlier cleaner (the readers' notes say most C3 rows are of this kind, not end-of-document cuts).
   There is no safe regex for that; it is the main finding of this slice for the pipeline team: the
   HTML-to-text step drops anchor text and embedded content.

### Medicine 68: en-dclm / C5 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7: C5 keyword lists and SEO spam.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** C5, 61 documents. Examples: `c64a732a64b1ce8b` `teknik forex tf h1` injected
   at offsets 44, 6858 and throughout random textbook sentences; `d7d9f2c89773b700` Korean casino keywords
   `온라인카지노` injected mid-sentence at 2801, 5424, 8201; `a381d9217f39570e` `cheap michael kors handbags` at 93;
   `ba893cf355e53633` spun word salad `be sure to seems to cost` from offset 147.

2. **Medicine:** drop when (a) a 4-word phrase made of 3+ content words repeats 6+ times at a density of at least
   8 per 1000 words, or (b) a CJK/Hangul/Cyrillic run sits between Latin words on the same line at least twice.
   ```text
   STOP = set("the a an of and or to in on for with at by from is are was were be as it this that these those its".split())
   FOREIGN = "가-힯一-鿿぀-ヿЀ-ӿ"
   INJECT_RE = re.compile(rf"[A-Za-z]{{3,}}[ ,.]+[{FOREIGN}]{{2,}}[ ,.]+[A-Za-z]{{3,}}")
   def m_c5(text, min_rep=6, min_density=0.008):
       words = re.findall(r"[a-z0-9']+", text.lower())
       if len(words) < 60: return text, False
       grams = Counter(" ".join(words[i:i+4]) for i in range(len(words) - 3))
       phrase, n = max(grams.items(), key=lambda kv: kv[1])
       content = [w for w in phrase.split() if w not in STOP]
       spam = n >= min_rep and len(content) >= 3 and n / len(words) >= min_density
       return text, bool(spam or len(INJECT_RE.findall(text)) >= 2)
   ```

3. **Action:** drop.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 0 changed, 8 dropped.

5. **Side effects:** precision was bought with recall. A looser version (4 repeats, 2 content words, any
   non-Latin share under 5%) dropped 44 documents in the pack but also a clean student-union article (`a U-Pass
   program` 5 times) and a legitimate bilingual Chinese-English dictionary page, so it was tightened. The tight
   rule catches 7 of the 61 labelled documents: most C5 here is *spun* English (`be sure to seems to cost`) or
   glued textbook sentences, which read as ordinary words to a regex. Those need a language-model perplexity or
   a repetition-of-rare-n-grams filter at the pipeline level, not a line rule. A product review that names the
   product in four content words six or more times (`sony alpha 7 iii`) would be dropped.

### Medicine 69: en-dclm / F1 · shekar-maker

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 8: F1 personal data.
> **Source:** [teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-dclm/shekar-maker/medicine.md)

1. **Disease:** F1, 8 documents. Examples (type and position only): `71f25549c2c4200d` email at offset 2436;
   `416e12ac72df0b07` emails at offsets 669, 964, 2192; `e5d949484740fff3` PO box at 8031, email at 8120, phone at
   8155; `c3ff48f35f98745c` phone at offset 8567.

2. **Medicine:** replace with a placeholder. An email is redacted when its shape is personal (first.last, digits,
   a long local part, or a webmail domain); a single-word mailbox at an organisation's own domain is kept. Phone
   numbers in national or international format are always redacted.
   ```text
   EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
   PHONE_RE = re.compile(r"(?<![\d\w-])(?:\+\d{1,3}[\s.-]?)?(?:\(\d{3}\)|\d{3})[\s.-]\d{3}[\s.-]\d{4}(?![\d\w-])")
   WEBMAIL_RE = re.compile(r"@(?:gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|aol|icloud|me|protonmail|proton|rediffmail|zoho|gmx|yandex|mail)\.", re.I)
   PERSONAL_LOCAL_RE = re.compile(r"[._\-]|\d|^.{13,}$")
   def _private(addr): return bool(WEBMAIL_RE.search(addr) or PERSONAL_LOCAL_RE.search(addr.split("@", 1)[0]))
   def m_f1(text):
       new = EMAIL_RE.sub(lambda m: "[EMAIL]" if _private(m.group()) else m.group(), text)
       return PHONE_RE.sub("[PHONE]", new), False
   ```

3. **Action:** fix (redact in place).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold 0/65 changed, 0 dropped. Whole pack: 13 changed, 0 dropped.

5. **Side effects:** the shape rule is a guess about who is private: a person with a one-word mailbox at their own
   domain is not redacted, and a company address like `sales.team@...` is. Business phone numbers (restaurants,
   banks, a shop) are redacted although they are public; the readers chose not to label those F1. The phone
   regex matches 10-digit groups only; UK/EU formats and numbers written without separators pass through. Postal
   addresses and PO boxes are not handled.

### Medicine 70: en-fineweb-edu / B4 · deepjyotisaha

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: B4 template and code junk.
> **Source:** [teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md)

1. **Disease:** B4, in 8 of the 500 labelled documents (16 labelled cases). Three examples:
   - `3e44df6a7ddb0098` (document 43): "`page.data.shortTitle || page.data.title`"
   - `4af5022aceeaf8b2` (document 256): "require 'nokogiri' require 'open-uri' # Get a Nokogiri::HTML:Document for the page"
   - `ef54fd4d35956893` (document 421): "> take :: Integer -> [Integer] -> [Integer] take _  =  take n xs"

2. **Medicine:** Two parts.
   - template junk (fix): remove what a web page left unfilled: "{{ title }}", "{% if … %}", "${name}", a code expression in backticks such as "`page.data.shortTitle || page.data.title`", "NaN" or "undefined" right after ":", "=" or "$", and a line that is only "undefined", "NaN" or "null";
   - mostly code (drop): a line is a code line when it has at least two code tokens ("::", "->", "==", "&&", "{", "}", a line ending in ";", a line starting with "import", "def", "return", "public", "$ ", "Sub", …) and at least one for every six words; a table row "|cell||cell|" is never a code line. A document whose code lines hold more than half of its characters is dropped;
   - code snippets inside an article are kept on purpose (decided 27 Oct): tutorials and manual pages with a few lines of code are good training text, and cutting them risks removing real content.

   In code: the function `b4_spans(text)` in **Runnable code** at the end of this sheet.

3. **Action:** fix for template junk (the expression is removed); drop for a document that is mostly code.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold set = the 202 rows of `labels.csv` with verdict `clean` (each read in full, no disease found). The medicine changes or drops **0 of 202** of them (0.00%): **pass** against the 1% bar. On the whole pack it changes 1 of 500 documents and removes 41 of 2,442,877 characters (0.00%). The official gold set for English (owned by Data A) is not published yet; this test will be repeated on it when it is.

5. **Side effects:** the medicine finds 1 of the 16 labelled cases. On the whole pack it changes 1 document. The mostly-code part drops no document of this pack: the most code-like one (document 10) has code in only 3% of its text. The other B4 documents are articles with a code snippet (a Visual Basic or Java listing, a Ruby example, a command manual page, a Haskell mailing-list post), kept on purpose; the readers' labels remain the record of them. Code flattened into a prose line by the original crawl is hard to tell from prose with symbols, which is why the drop needs more than half of the document to be code.

### Medicine 71: en-fineweb-edu / C1 · deepjyotisaha

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: C1 boilerplate.
> **Source:** [teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md)

1. **Disease:** C1, in 277 of the 500 labelled documents (592 labelled cases). Three examples:
   - `74ea30694d60f739` (document 13): "© 1995-2017 Bible History Online"
   - `f6393483c601faf0` (document 22): "View all Kids Bikes"
   - `1e5e295e77f6c38e` (document 45): "By Kevin Schargen"

2. **Medicine:** Remove a line, or the end of a line, when it is website text rather than article text. Five kinds, each with its own pattern (all case-insensitive, lines under 120 characters unless stated):
   - teaser and action links: a line that starts with "Read more", "Continue reading", "Explore further", "Click here", "Learn more about", "To learn more about", "Find out more", "For further information", "View all", "View larger map", "Show summary details", "Share this", "Choose a citation style" or "Call now"; and a teaser such as "[...] Read more", "Continue reading →" or "Read more »" at the end of a longer line (only the teaser is removed);
   - bylines and dates: in the first three lines, a line that is "By <Name>", "From: …", "Posted …", "Updated …", "Published …", "Contributed by …", "Written by …", "Latest revision …" or only a date; anywhere, a line that is only "By <Name>";
   - credits, sources and footers: a line that starts with "©", "Copyright", "Source:", "Article source:", "Website:", "Courtesy:", "Photo:", "Image:", "Editor's note:", "Editor:" or "Correction";
   - navigation: a breadcrumb or menu line of four or more items joined by " | ", " : " or " » " (under 160 characters), and link boxes such as "|… »||… »|";
   - shop and promotion text (under 220 characters): book details ("Paperback:", "Publisher:", "ISBN-13:", "Product dimensions:"), order confirmations, "Help support … and get …", "Don't forget to check out …", "click on the … to follow me", "Subscribe to our newsletter".
   - line scorer: every line also gets a score from 0 to 1 from a logistic regression trained on the labels (positive: the labelled C1 lines; negative: every line of the documents labelled clean). Its features are what boilerplate lines share whatever their words: length, a full stop at the end, position (first or last three lines), link words, web address, ©, date, separators, share of capitalised words, digits, whether a paragraph follows, and how many other documents repeat the line. A line scoring 0.97 or more is removed, but only if it is at most 200 characters and carries an explicit boilerplate signal (link word, web address, ©, date, byline or separator; from 27 Oct also a line found in 3 or more documents of the pack, and "Back to …", "Photo credit", "Contributors:", "Last reviewed", "Article ID:", "community guidelines", "customer reviews"), so an article title or an ordinary sentence is never removed on its score alone. A lower threshold for the first and last three lines was tested on 27 Oct and rejected: it changed more clean documents (a dateline, a closing reference);
   - block expansion: a line next to a removed line is removed too if it is short, has no full stop, scores at least half the threshold, and is signalled or a "Key: value" line (the rest of a byline or of a book-details block);
   - a teaser glued to the end of a sentence ("…can be prescribed.Learn more about …") removes only the teaser, never the sentence;
   - guard: if all of this would remove more than 20% of a document and more than 300 characters, nothing is cut and the document is flagged for drop (so a normal footer on a short page is cut, not turned into a drop). The threshold 0.97 is the one that catches the most labelled lines while changing at most 1% of the clean documents, in a five-fold test on documents the scorer did not see during training (`c1tune.py`).

   In code: the function `c1_spans(text)` in **Runnable code** at the end of this sheet.

3. **Action:** fix. The matched text is removed; the rest of the document is kept. A document the guard flags is dropped.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold set = the 202 rows of `labels.csv` with verdict `clean` (each read in full, no disease found). The medicine changes or drops **2 of 202** of them (0.99%, each tested by a scorer that had not seen it): **pass** against the 1% bar. On the whole pack it changes 153 of 500 documents and removes 16,704 of 2,442,877 characters (0.68%). The official gold set for English (owned by Data A) is not published yet; this test will be repeated on it when it is.

5. **Side effects:** on documents the scorer had not seen, the medicine finds 229 of the 540 labelled C1 lines (42%; the phrase rules alone find 117). It misses C1 that has no fixed wording and no boilerplate signal: one-off site headings ("Programs for children", "Chapter 02 Worksheet"), reference lists and citations, catalogue records and promotion inside a long paragraph. These are left to the readers. Article titles are kept on purpose: the first version of the scorer removed titles and sentences such as "By the end of 1992, …" from clean documents, which is why the scorer may only remove signalled lines. Remaining risks: a "Source:" line under a chart, and a short line with a date or a link word that belongs to the article.

### Medicine 72: en-fineweb-edu / C3 · deepjyotisaha

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: C3 truncated document.
> **Source:** [teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md)

1. **Disease:** C3, in 13 of the 500 labelled documents (14 labelled cases). Three examples:
   - `2067313a5e000336` (document 5): "He writes in the Guardian on Tuesday:"
   - `8620d74ba9ae6cdc` (document 24): "For more information about the collection, visit"
   - `d9cf118c7cae38e0` (document 42): "week we celebrate the holiday of Chanuka."

2. **Medicine:** Remove the last line of a document when it is an unfinished sentence: the last non-empty line has at least six words and ends on a word no complete sentence ends on (for example "the", "of", "to", "visit", "they") or on ":" or ",", and the C1 medicine does not already remove it. The document then ends at its last complete line. Run after the C1 medicine. Two broader rules were tested and rejected (25 Oct): "the last line ends with any lower-case letter" also removed titles and author notes at the end of good documents, and "the text starts with a lower-case letter" also removed dictionary entries that start in lower case. Those cases stay with the readers.

   In code: the function `c3_spans(text)` in **Runnable code** at the end of this sheet.

3. **Action:** fix. The matched text is removed; the rest of the document is kept.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold set = the 202 rows of `labels.csv` with verdict `clean` (each read in full, no disease found). The medicine changes or drops **0 of 202** of them (0.00%): **pass** against the 1% bar. On the whole pack it changes 4 of 500 documents and removes 346 of 2,442,877 characters (0.01%). The official gold set for English (owned by Data A) is not published yet; this test will be repeated on it when it is.

5. **Side effects:** the medicine finds 2 of the 14 labelled cases. It misses cut-offs that do not end on a dangling word or a colon (for example a teaser ending in "..."), and documents that start in the middle of a sentence. Some labelled cut-offs are removed by the C1 medicine first, because their last line is also a link ("…For more information about the collection, visit"). On the whole pack it changes 4 documents; checked on 25 Oct, one of them is a title ending in "On" ("The Saga Lives On"), which is a wrong removal.

### Medicine 73: en-fineweb-edu / D3 · deepjyotisaha

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: D3 mixed language.
> **Source:** [teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md)

1. **Disease:** D3, in 6 of the 500 labelled documents (27 labelled cases). Three examples:
   - `f9c53a41965da2a5` (document 164): "Да ти се чува името само за добро"
   - `c7a02c529ace1f12` (document 380): "ἄνθρωπος :: ἄνθρωποι, πρῶτος :: πρῶτοι"
   - `00909b0fd14585fc` (document 237): "el caramelo se le deshizo / se le disolvió en la boca"

2. **Medicine:** Keep: nothing is removed. DISEASES.md says mixed language can be natural and is to be labelled, not judged, and every labelled case in this pack is on purpose (proverbs with their translation, Greek grammar, Spanish example phrases, Indonesian course slides, Chinese calendar names in an infobox). The medicine only flags passages for a reader:
   - a run of at least three words in one alphabet other than Latin (Cyrillic, Greek, Arabic, Devanagari, …);
   - for alphabets written without spaces (Chinese, Japanese, Thai), a run of at least four characters;
   - a word that mixes alphabets ("α-helix") is not flagged: that is A6, not D3.

   In code: the function `d3_flags(text)` in **Runnable code** at the end of this sheet.

3. **Action:** keep. Nothing is removed; the flags are for a reader.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold set = the 202 rows of `labels.csv` with verdict `clean` (each read in full, no disease found). The medicine changes or drops **0 of 202** of them (0.00%): **pass** against the 1% bar. On the whole pack it changes 0 of 500 documents and removes 0 of 2,442,877 characters (0.00%). The official gold set for English (owned by Data A) is not published yet; this test will be repeated on it when it is.

5. **Side effects:** the medicine flags 25 of the 27 labelled cases. It cannot see mixed language in the Latin alphabet (the Spanish and Indonesian cases), which only reading finds. Removing nothing is deliberate: every labelled case is part of its article. It also flags document 356, which is not labelled D3 (in document 356 the flag is invisible Hangul filler characters, A1 junk, not language).

### Medicine 74: en-fineweb-edu / F1 · deepjyotisaha

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: F1 personal data.
> **Source:** [teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-fineweb-edu/deepjyotisaha/medicine.md)

1. **Disease:** F1, in 8 of the 500 labelled documents (13 labelled cases). Three examples:
   - `841da1d7e68b3ab8` (document 135): "phone number at offset 1597"
   - `6a515f44bd213b3d` (document 155): "phone number after a Tel: label at offset 7182"
   - `e202cef6da70c403` (document 450): "phone number after a Tel: label at offset 3943"

2. **Medicine:** Remove every email address, phone number and ID number, together with a label in front of it ("Tel:", "Fax:", "Phone:"). Nothing is put in its place: a placeholder such as "[phone]" would teach the model to write our own made-up token (decided 27 Oct). The patterns are the scanner's F1 patterns:
   - emails, except FineWeb's own example.com replacements;
   - phone numbers: international ("+44 …"), US ("[REDACTED_PHONE]", "[REDACTED_PHONE]"), UK and Indian numbers that start with 0, and any number after a Tel, Fax, Phone or Mobile label;
   - ID numbers: US social security numbers, PAN numbers, and card and Aadhaar numbers only when their check digit is valid (the Luhn test for cards, the Verhoeff test for Aadhaar), so a run of years or a product code is not taken for one;
   - not personal data: a match inside a journal reference, an ISBN, a DOI or a run of years is left alone;
   - a line with no letter or digit left after the removal ("Tel: … / Fax: …") is removed whole.

   In code: the function `f1_spans(text)` in **Runnable code** at the end of this sheet.

3. **Action:** fix. The matched text is removed; the rest of the document is kept.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy gold set = the 202 rows of `labels.csv` with verdict `clean` (each read in full, no disease found). The medicine changes or drops **0 of 202** of them (0.00%): **pass** against the 1% bar. On the whole pack it changes 8 of 500 documents and removes 200 of 2,442,877 characters (0.01%). The official gold set for English (owned by Data A) is not published yet; this test will be repeated on it when it is.

5. **Side effects:** the medicine finds 13 of the 13 labelled cases. On the whole pack it changes 8 documents, all of them labelled F1. It misses personal data with no fixed shape: names, home addresses, and numbers written in words or grouped in an unusual way. Every phone number counts, also an organisation's (decided 24 Oct). After the removal a sentence such as "call … for details" can read oddly.

### Medicine 75: en-nemotroncc-synth / B4 · AJJAPUSIVA

> **Status:** BLOCKED; not approved. **Original section:** Row 81: B4 placeholder medicine.
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md)

1. **Disease:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

2. **Medicine:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

3. **Action:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

5. **Side effects:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

### Medicine 76: en-nemotroncc-synth / B4 · maheshsv

> **Status:** BLOCKED; not approved. **Original section:** Medicine 3: B4 rewriter meta-comments (8 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** B4 (closest code: junk from the generation pipeline in prose; the list has no code for rewriter
   artefacts). The rewriting model leaked its instruction context into the output: it tells the reader what the
   source page did *not* say.
   - `47f4f5107ac9aece`: `The provided text also discusses` ("The provided text also discusses …")
   - `6a2017ab99292d5b`: `Not specified in the given text` as a whole bullet
   - `d896f8ca6a2beae1`: `The text does not provide` as a QA answer
   8 documents, 5 of them `knowledge_list`. Plain "The text discusses …" openers of
   `distill` summaries are not counted: they are the summary frame, not a failed extraction.

2. **Medicine:** match the negated phrase (`not … in the (given|provided) text/passage/document`, `the text does
   not provide/mention/…`) or `the given/provided text`. Delete the bullet, `Key: value` line or QA pair that
   carries it; in running prose delete only the sentence.
```text
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
            drop.add(i)
        else:
            sentences = re.split(r"(?<=[.!?])\s+", ln)
            lines[i] = " ".join(x for x in sentences if not META.search(x))
    new = "\n".join(ln for i, ln in enumerate(lines) if i not in drop)
    new = re.sub(r"\n{3,}", "\n\n", new).strip()
    if len(new) < MIN_KEEP_CHARS:
        return None, True
    return new, True
```
   `META` (case-insensitive):
```
(?i)\bnot (?:explicitly |specifically |directly )?(?:provided|stated|mentioned|specified|given|available|included|present|disclosed|named) in the (?:given |provided |original |above |source )?(?:text|passage|article|document|excerpt|content|context)|\bthe (?:text|passage|article|document) does not (?:explicitly |specifically )?(?:provide|mention|specify|state|say|give|include|indicate|name)\b|\bthe (?:given|provided) (?:text|passage) (?:also )?(?:discusses|mentions|describes|states|says|provides|refers|covers|explains|includes|lists|notes)\b
```

3. **Action:** fix. Drop if fewer than 200 characters remain (`4fc487e14eab5961` is a 458-character list in which
   the country and the coup are never named; it drops).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **0 changed, 0 dropped (0.0%)**. Passes the 1% rule. On the whole pack the rule touches 8 of 500 documents, 8 of the 36 documents labelled B4. **This test is circular:** the label sheet applied this same regular expression when
      labelling, so every matching document is already `fix`, never `clean`, and the 0 cannot fail. What the data does
      show: all 8 hits were inspected individually and every one is a genuine artefact
      (precision 8/8). The real harm test needs the independent gold set.

5. **Side effects:** the pattern deliberately does **not** match plain "in the text" (QA questions such as "Who is
   the main character in this text?" are the normal format of `diverse_qa_pairs`), nor "The text discusses …" and
   "The text mentions that …" (the summary frame of `distill` and `knowledge_list` rewrites, present in several
   clean rows), nor "the original text", which two `wrap_medium` documents use legitimately as product copy about
   paraphrasing tools. Constructed sentences such as `Read the given passage carefully and answer the questions that follow.`; `Applicants must sign the provided document before the deadline.` are
   no longer matched, because the `given/provided text`
   branch now requires a reporting verb. A Question line that carries the phrase takes its Answer line with it and
   vice versa, so no orphan line is left. A genuine essay that writes "the provided text also discusses" would lose
   that sentence.

### Medicine 77: en-nemotroncc-synth / B4 · maheshsv

> **Status:** BLOCKED; not approved. **Original section:** Medicine 4: B4 detokenisation glitch, missing space before an opening quote (18 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** B4 (closest code). A systematic generation artefact: the space before an opening single quote is
   missing, so the quote glues to the previous word.
   - `536547e07d7d65ca`: `n. The'resources(-Count)' re`
   - `c1a354c76d5c4586`: `ds for'remember' and 'forget` (five times in one document)
   - `7e2cbd39bf39635f`: `called'silth/seeth'. Upon re`
   18 documents, 23 occurrences, in all five rewrite kinds. A sibling variant, the
   missing space before a dot-extension (`e.g.,.tar`, `like.yaml or.txt` in `03ad0f392751ba37`), is labelled B4
   but not fixed by this rule.

2. **Medicine:** when a letter is directly followed by `'`, the quote opens a word that starts with `s`, `r` or
   `m`, and the phrase is closed by another `'` on the same line, insert a space before the quote. The `s/r/m`
   restriction comes from the data: every one of the 23 glitches opens such a word, which fits a detokeniser that
   treated the quote as the start of a contraction (`'s`, `'re`, `'m`) and glued it to the previous word.
   Contractions, possessives and poetic elisions (`it's`, `don't`, `we're`, `o'clock`, `y'all`, `rock'n'roll`,
   `ne'er`) are excluded by the look-ahead; Python string prefixes (`f'…'`, `r'…'`, `b'…'`, `rb'…'`) by the
   look-behind.
```text
def fix_detok_quotes(text: str) -> tuple[str | None, bool]:
    new = DETOK.sub(" '", text)
    return new, new != text
```
   `DETOK` (compiled with `re.M`):
```
(?<=[A-Za-z])(?<![^A-Za-z][frbuFRBU])(?<![^A-Za-z][rR][bB])(?<![^A-Za-z][bB][rR])'(?!s\b|t\b|re\b|ll\b|ve\b|d\b|m\b|em\b|n'|er\b|clock\b|all\b|am\b)(?=[srmSRM][A-Za-z][^'\n]{0,40}'(?:[\s,.;:)!?]|$))
```

3. **Action:** fix (insert one space).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **0 changed, 0 dropped (0.0%)**. Passes the 1% rule. On the whole pack the rule touches 18 of 500 documents, 17 of the 36 documents labelled B4. **This test is circular** in the same way as medicine 3: the labelling applied the
      same expression. All 18 hits were inspected individually and every one is a genuine glitch
      (precision 18/18); one of them carries the instance under B5 (`6c9e38f009ea3806`), hence
      17 of 18 are labelled B4.

5. **Side effects:** a possessive directly followed by a quoted phrase that closes on the same line (`the boys'bikes'`)
   would get a spurious space; not seen in 500 documents. Constructed code and verse inputs (`print(f'hello world')`; `pattern = re.compile(r'sample')`; `payload = b'raw'`; `I ne'er saw such a thing,' she said`; `the boys' bikes were new`)
   are left alone. False negatives: a
   quoted phrase longer than 40 characters, a glitch with no closing quote on the line, the sibling variant with a
   dot-extension (`e.g.,.tar`, `like.yaml`, `the.NET`: 2 documents, labelled B4, not fixed by this rule). Curly quotes (’) are
   not handled; none occur in this pack.

The B4 total (36 documents) is larger than the two rules together because B4 was also used, as the
closest code, for other pipeline junk in 11 documents: `d2fb665c40af5edb` (`-DATE-` placeholder left in a bill description); `ea0ecda1c2f25dd1` (OCR glyph junk `e~ \` inside prose); `6011e88c8cc9c77d` (missing space before dot-extensions (`in.jpg,.png`)); `12693fe362d15d0d` (Cloudflare `[email protected]` placeholder); `373e0f0dd5699ac0` (e-learning template demo content under a real course title, dropped); `57922931d471745c` (epoch-bug date `January 17, 1970` and midnight time copied from the CMS); `0c03a4c096276336` (forum thread recast as an AI/user exchange); `d4f559ee86104b5b` (missing space before `.NET`); `68924f97019edabb` (`https://www.example.com/…` placeholder link); `e472a2fcc0df3984` (SEO-writing prompt leaked into the prose, dropped); `03ad0f392751ba37` (missing space before dot-extensions (`e.g.,.tar`)).
The most training-relevant of these is the leaked SEO-writing prompt in `e472a2fcc0df3984` ("vary your verbs …"),
dropped, and the chat-role recasting in `0c03a4c096276336` ("The AI advises the user …"), which teaches the
assistant/user frame as plain text and sits next to B3 in danger.

### Medicine 78: en-nemotroncc-synth / B5 · maheshsv

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6: B5 broken Markdown in code (12 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** B5, 12 documents. The rewriter emitted identifiers inside code as Markdown, and the
   underscores were eaten as italics markers (`add_filter` became `addfilter`, `load_word2vec_format` became
   `loadword2vecformat`); in other documents the announced code examples were dropped and only the prose around
   them survived, or a LaTeX formula lost its subscripts. Examples:
   - `42d8419d13115795`: `addfilter('intermediateimagesizesadvanced','myintermediateimage_sizes');`
   - `ac2d7bac43b4a937`: `setllCUSTNO ORDHDRL1;` (space eaten between RPG opcode and operand)
   - `b63a5e89acfb14e3`: `$\sigmax\sigmap \geq \frac{h}{4\pi}$`

2. **Medicine:** no safe automatic fix: restoring an eaten underscore needs knowledge of the API (`add_filter`
   versus `addfilter`), and a dropped code example cannot be recovered. A detector is possible and is tested here:
```text
def flag_eaten_identifiers(text: str) -> tuple[str, bool]:
    """Flag code (fenced or backticked) that contains a lower-case identifier of 12+ letters, no underscore, that is
    not a dictionary word: the signature of `add_filter` -> `addfilter` damage."""
    words = _dictionary()
    for span in CODE_SPAN.findall(text):
        for tok in LONG_LOWER.findall(span):
            if tok not in words:
                return text, True
    return text, False
```
   using the system word list (`/usr/share/dict/words`) to exclude real words.

3. **Action:** route flagged documents to a manual fix. Fix by hand where the identifier is known
   (`42d8419d13115795`, `f160996522775c21`, `ac2d7bac43b4a937`, `713e88c96cefef1a`, `6c9e38f009ea3806`,
   `6df80446baf7b672`); where an announced code example is simply gone (`03ad0f392751ba37`, `7ee6cdea68d597b0`,
   `52731a50fbea41cb`, `f5d81aaad46e50f8`) keep the prose; `wrap_medium` and `extract_knowledge` rewrites that
   contain code fences should not feed the code mix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **0 changed, 0 dropped (0.0%)**. Passes the 1% rule. On the whole pack the rule touches 3 of 500 documents, 3 of the 12 documents labelled B5. The detector cannot see dropped examples, mangled spaces in RPG
      (`setllCUSTNO`) or a broken formula, hence the partial recall.

5. **Side effects:** a legitimate long lower-case identifier that is not an English word (`stringbuilder`,
   `getelementbyid` written in lower case) would be flagged for review; the action is a review, not a change.

### Medicine 79: en-nemotroncc-synth / C1 · maheshsv

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: C1 boilerplate (76 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** C1, 76 documents. Two shapes. (a) Whole boilerplate lines left by the scraper:
   - `d7ece2193f620b9b`: `[Share on other sites]` (three times)
   - `7e33ae5e96e36516`: `Word Count: 2498`
   - `b61d4ab44f34bce1`: `RELATED STORIES` followed by `6 mins read`
   (b) Advertising or call-to-action sentences that the rewriter wove into the prose, for example a closing
   "consider contacting <vendor> on <number> for further information" (`922e32f45f63d013`), a law firm's "How We
   Can Help" section (`fa6afecb771ef379`), a download-button instruction (`d4700fb9b804516b`), a treatment centre's
   closing paragraph (`2819f558ee6c1e7e`). Contact lines are labelled C1 whether or not a person is named; business
   and institution phone numbers are not F1.

2. **Medicine:** delete a line when the whole line, trimmed, matches a navigation, sharing, metadata
   or footer pattern.
```text
def strip_boilerplate_lines(text: str) -> tuple[str | None, bool]:
    kept = [ln for ln in text.split("\n") if not BOILERPLATE_LINE.match(ln.strip())]
    changed = len(kept) != text.count("\n") + 1
    new = "\n".join(kept).strip()
    if changed and len(new) < MIN_KEEP_CHARS:
        return None, True
    return (new if changed else text), changed
```
   `BOILERPLATE_LINE` (case-insensitive, applied to the trimmed line) matches whole lines such as `Share …`,
   `Read more …`, `Related posts …`, `Posted by …`, `Word Count: 2498`, `Tags: …`, `3 Comments`, `Subscribe …`,
   `© …`, `Previous`, `Next`, `Home`, `Menu`, `Search`:
```
^(?![^\n]*[^\s.][.!?]$)(?:\[?(?:share (?:on|this|via)\b|share:|tweet(?: this)?\b|pin it\b|email this\b|print this\b)[^\n]{0,40}\]?|(?:read|learn|see|view) more\b[^\n]{0,30}|related (?:posts?|stories|articles|questions|links|content)\b[^\n]{0,40}|(?:posted|published|updated|last updated|written) (?:by|on)\b[^\n]{0,50}|(?:posted|published|updated|last updated):[^\n]{0,40}|word count:?\s*\d+\s*|tags?:[^\n]{0,200}|(?:\d+ )?comments?(?: \(\d+\))?:?|leave a (?:comment|reply)\b[^\n]{0,30}|(?:subscribe|sign up|log ?in|register)(?: now| here| today| to our newsletter| for (?:free|updates))?\s*[»›>]?|click here\b[^\n]{0,40}|(?:©|copyright ©?\s*(?:19|20)\d\d|all rights reserved\b)[^\n]{0,80}|(?:previous|next)(?: (?:post|article|page))?\s*[»›>]?|[«‹<]?\s*(?:previous|next)(?: (?:post|article|page))?|home|menu|search|skip to (?:main )?content)$
```

3. **Action:** fix (delete the line). Drop if fewer than 200 characters remain.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **0 changed, 0 dropped (0.0%)**. Passes the 1% rule. On the whole pack the rule touches 5 of 500 documents, 4 of the 76 documents labelled C1. Not circular: the regular expression was not used in labelling.

5. **Side effects:** the line rule is safe but weak: 72 of the
   76 C1 documents are shape (b), in-prose advertising, which no regular expression can remove without
   damaging real sentences. For spec v1 I propose: treat shape (b) by document-level verdict (the labelled
   `doc_id`s are the fix/drop list for this pack) and ask for a classifier rule trained on these labels.
   Constructed ordinary sentences that an earlier version deleted and this version keeps (the rule now refuses any
   line that ends like a sentence, and the `share`, `login`, `register`, `published` and `copyright` branches are
   anchored to their boilerplate forms): `Share prices fell 5% today after the earnings report.`; `Login to the server using SSH with the command below:`; `Register your vehicle within 30 days of moving.`; `Published by Penguin in 1999, it became a bestseller.`; `Written by Shakespeare around 1600.`; `See more examples in the next section.`; `Copyright infringement occurs when a work is used without th`
   (0 of 7 still deleted). What still goes: any line that starts
   with `Tags:` and has no sentence punctuation, a bare `Search` or `Home` line, a `Register` line of up to a few
   words. The proxy gold set contains almost no legal, finance or tutorial prose of the kind at risk, and every
   whole-line boilerplate the reader saw is already outside it, so the 0% says little about those genres.

### Medicine 80: en-nemotroncc-synth / C3 · AJJAPUSIVA

> **Status:** BLOCKED; not approved. **Original section:** Rows 75-76: manual list reconstruction (C3 provisional).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md)

1. **Disease:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

2. **Medicine:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

3. **Action:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

5. **Side effects:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

### Medicine 81: en-nemotroncc-synth / C3 · maheshsv

> **Status:** BLOCKED; not approved. **Original section:** Medicine 1: C3 truncated document (47 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** C3, 47 documents. 61 documents of this pack are consecutive chunks of one OCR'd book
   (Upton's *Nibelungs*, one URL); the chunking cut the passage mid-sentence and the rewriter then appended
   `Question: … Answer: …` pairs after the cut, so the fragment sits at the end of the passage, not at the end of the
   document. Where the cut sits in the 47 documents: 18 start mid-sentence, 24 end
   the passage with a fragment (several of them a short line: an orphan heading such as `The Festival`, a line of
   verse), 5 are cut inside the passage (page turns, a dropped line of speech). Examples (exact trailing
   characters of the passage):
   - `d896f8ca6a2beae1`: `…company. Leading e-commerce platforms in 2020`
   - `fdd2b470571c5e4d`: `…ly with all leading business systems such as:`
   - `593cf027a182e228`: `…ed. Other useful information about this game:`

2. **Medicine:** take the passage before the first `Question:` line. (a) If its last line is a prose line (20
   characters or more, not a bullet, not a `Key: value` line, not an `Answer:` line) and does not end with sentence
   punctuation or a closing bracket, cut that line back to its last sentence end, or remove the line if it has
   none. (b) If its first line starts with a lower-case letter and is 40 characters or more, cut it up to its first
   sentence end. Keep the QA block.
```text
def _split_qa(text: str) -> tuple[str, str]:
    m = QA_START.search(text)
    return (text[: m.start()], text[m.start():]) if m else (text, "")

def _finish(lines: list[str], tail: str) -> tuple[str | None, bool]:
    new_body = "\n".join(lines).rstrip()
    if len(new_body) < MIN_KEEP_CHARS:
        return None, True
    return (new_body + ("\n\n" + tail.strip() if tail.strip() else "")), True

def trim_truncation(text: str) -> tuple[str | None, bool]:
    """Cut a sentence fragment at the end of the passage (before any Question/Answer block). Drop if little is left.
    A trailing line that ends in sentence punctuation, a closing bracket or quote, a bullet, a `Key: value` line or an
    Answer line is left alone."""
    body, tail = _split_qa(text)
    lines = body.rstrip().split("\n")
    last = lines[-1].strip()
    if not (len(last) >= MIN_PROSE_LINE and not LIST_MARK.match(last) and not KEY_VALUE_LINE.match(last)
            and not ANSWER_LINE.search(last) and not TERMINAL.search(last)):
        return text, False
    ends = list(SENTENCE_END.finditer(last + " "))
    lines[-1] = last[: ends[-1].end()].rstrip() if ends else ""
    return _finish(lines, tail)

def trim_leading_fragment(text: str) -> tuple[str | None, bool]:
    """Cut a leading fragment: a long first prose line that starts with a lower-case letter and does not look like code."""
    body, tail = _split_qa(text)
    lines = body.lstrip().split("\n")
    first = lines[0].strip()
    if not (first and first[0].islower() and len(first) >= MIN_LEAD_LINE and not CODE_LIKE.search(first)):
        return text, False
    e = SENTENCE_END.search(first + " ")
    lines[0] = first[e.end():].lstrip() if e else ""
    return _finish(lines, tail)

def trim_truncation_both_ends(text: str) -> tuple[str | None, bool]:
    new, ch1 = trim_truncation(text)
    if new is None:
        return None, True
    new2, ch2 = trim_leading_fragment(new)
    return new2, ch1 or ch2
```
   with `MIN_PROSE_LINE = 20`, `MIN_LEAD_LINE = 40`, `MIN_KEEP_CHARS = 200` and the patterns
   `QA_START = '^\\s*Question:'` (multiline), `TERMINAL = '[.!?…]+[\\"\'”’)\\]]*$|[)\\]]$|[\\"”’]$'`,
   `LIST_MARK = '^(?:[-*•–—]|\\d+[.)]|[a-z][.)])\\s'`, `KEY_VALUE_LINE = '^[^:\\n]{1,60}:\\s'`,
   `ANSWER_LINE = '^(?:Answer|A)\\s*[:.]|\\bAnswer:\\s'`, `SENTENCE_END = '[.!?…][\\"\'”’)\\]]*\\s'`,
   `CODE_LIKE = '[$/\\\\=(){}<>|]|--|\\bnpm\\b|\\bpip\\b|\\bgit\\b'`.

3. **Action:** fix (trim the fragment). Drop the document if fewer than 200 characters remain.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **0 changed, 0 dropped (0.0%)**. Passes the 1% rule. On the whole pack the rule touches 26 of 500 documents, 24 of the 47 documents labelled C3. This test is not circular: the C3 labels come from reading, not from this rule.

5. **Side effects:** 23 of the 47 labelled documents are out
   of reach: cuts inside the passage and the shortest orphan lines (`The Festival`, 12 characters) need a
   rejoin of consecutive chunks from the same URL, not a trim. Convention: a chunk that ends on a bare heading whose
   body sits in the next chunk is labelled C3 (orphan heading); the blind second reader called those complete, so
   expect disagreement on exactly those rows. False positives, constructed and confirmed: a first line that starts
   with a lower-case brand name (`iPhone …`, `eBay …`) and runs 40 characters or more loses its first sentence; a
   complete last line of 20 characters or more without a full stop (a line of verse, a slogan, a heading such as
   `Frequently Asked Questions About Taxes`, a line ending in an emoji) is removed, which for a heading is the intended
   orphan-heading behaviour; a roman-numeral or abbreviated item (`ii. Keep the soil moist`, `Dr.`, `e.g.`) can be cut
   back to the abbreviation because `SENTENCE_END` treats it as a sentence end. False negatives: a fragment on a
   `Key: value` line (`Note: the company said that it would`), a capitalised start fragment, a fragment that happens
   to end with a full stop. Lines ending in a closing quote or bracket and en-dash bullets are now accepted as
   complete, and a code-like first line (`npm install …`) is never trimmed; an earlier version trimmed a complete
   parenthetical (`35ebd1eaea214130`). None of the false positives occurred in the proxy gold set.

### Medicine 82: en-nemotroncc-synth / C4 · AJJAPUSIVA

> **Status:** BLOCKED; not approved. **Original section:** Row 16: manual C4 medicine.
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md)

1. **Disease:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

2. **Medicine:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

3. **Action:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

5. **Side effects:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

### Medicine 83: en-nemotroncc-synth / C4 · AJJAPUSIVA

> **Status:** BLOCKED; not approved. **Original section:** Row 34: manual C4 medicine.
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md)

1. **Disease:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

2. **Medicine:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

3. **Action:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

5. **Side effects:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

### Medicine 84: en-nemotroncc-synth / C4 · maheshsv

> **Status:** BLOCKED; not approved. **Original section:** Medicine 5: C4 two documents joined (9 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** C4, 9 documents: SEO aggregator or "people also ask" pages whose unrelated snippets the
   rewriter stitched into one text. Examples: `7b8ffe6ce68a4411` (Chicago housing market interleaved with RESPA
   kickback law), `650be7c8d64f5efd` (five unrelated essay snippets plus a dangling graded outline),
   `a14eaa5e58baf3c3` (Q&A aggregator). Verdicts: 5 drop, 4 fix
   (fix where the joined part is a short tail that can be cut: a reader comment, appended related-post teasers, a
   second forum question).

2. **Medicine:** the obvious lexical rule, as code, so that its failure is on record:
```text
def flag_topic_shift(text: str) -> tuple[str, bool]:
    """Flag a document of four or more paragraphs in which two adjacent paragraphs share no content words."""
    paras = [p for p in re.split(r"\n\s*\n|\n", text) if len(p.split()) >= MIN_PARA_WORDS]
    if len(paras) < MIN_PARAS:
        return text, False
    words = [{w for w in WORD_RE.findall(p.lower()) if w not in STOP} for p in paras]
    return text, any(not (a & b) for a, b in zip(words, words[1:]))
```
   with `MIN_PARAS = 4`, `MIN_PARA_WORDS = 25`. The boundary is semantic; an
   embedding-based topic-shift score may work but needs the gold set to set its threshold. For this pack the
   medicine is the list of labelled `doc_id`s.

3. **Action:** drop; fix where the joined part is a short tail that can be cut.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Run on the proxy gold set (339 documents of this pack marked `clean`): **57 changed, 0 dropped (16.81%)**. Fails the 1% rule. On the whole pack the rule touches 109 of 500 documents, 5 of the 9 documents labelled C4. **Fails**: forum threads, tag archives, course grids and knowledge lists are
      legitimately multi-topic. The drop list by construction touches 0 of 339 proxy gold documents. No
      automatic rule is proposed for spec v1.

5. **Side effects:** any automatic rule will also flag legitimate multi-topic pages that the label sheet
   deliberately kept as page structure; the threshold must be set on those.

### Medicine 85: en-nemotroncc-synth / C5 · maheshsv

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7: C5 lists of titles or links (7 documents).
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/maheshsv/medicine.md)

1. **Disease:** C5, 7 documents: pages that are mostly a list of teaser titles, related-story headlines
   or a series table of contents, with little or no prose. Examples: `affc40538cb81c3e` (a series table of contents
   of about 30 question titles), `beb73cd7cb9e50fd` (a list of related magazine stories), `f27860217811cf33` (an SEO
   aggregator's list of essay topics).

2. **Medicine:** none that passes a test yet. I tried "flag a document in which at least half of the non-QA lines are
   short title-case lines without sentence punctuation, with at least eight such lines": at thresholds that keep the
   harm under 1% it catches 0 of the 7 documents, because the rewriter turned most of these lists into
   run-on lines or glued titles together. For this pack the medicine is the list of labelled `doc_id`s.

3. **Action:** drop when the list is the whole document; fix (cut the list) when it is a tail after a real article
   (`b61d4ab44f34bce1`).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   the drop list by construction touches 0 of 339 proxy gold documents. No automatic rule is
      proposed.

5. **Side effects:** none for a manual list.

### Medicine 86: en-nemotroncc-synth / UNCLASSIFIED · AJJAPUSIVA

> **Status:** CANDIDATE; not approved. **Original section:** Rows 109-110: join article bodies and preserve Q&A separately.
> **Source:** [teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/en-nemotroncc-synth/AJJAPUSIVA/medicine.md)

1. **Disease:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

2. **Medicine:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

3. **Action:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

5. **Side effects:** Not supplied in a standard five-field format; inspect source. No automatic executable decision is permitted.

### Medicine 87: math-finemath / A1 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: A1 invisible characters.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** A1, 15 documents. `064d8dd19536d1d8` U+200E LRM @9 (x2); `8f09ea36d06abaef` U+00AD soft hyphen @3180 (x4); `263a5308b96d2e4a` U+200B @6754.

2. **Medicine:** delete U+200B, U+FEFF, U+00AD, U+200E, U+200F, U+2060, U+202A–U+202E, U+2066–U+2069. ZWJ/ZWNJ are never touched (ruling 12).
   ```text
   A1_RX = re.compile(r'[​﻿­‎‏⁠‪-‮⁦-⁩]')
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** a ZWSP used as the only word separator joins two words. LRM/RLM matter in RTL text (safe in this English pack; do not run on RTL packs). U+2062 INVISIBLE TIMES in MathML text (1 document) is not removed.

### Medicine 88: math-finemath / A3 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 8: A3 mojibake.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** A3, 11 documents. `c9e5d27233084b62` "â€™" @178 (x24; U+00E2 U+20AC U+2122); `ab295000bded241a` "ðŸ˜€" @118; `f79e6aeb5ebb6a5c` "тАЩ" @4628 (UTF-8 read as cp866).

2. **Medicine:** a short run starting with a UTF-8 lead byte seen as cp1252 (`Â Ã â ð Ð Ñ à á ä`) is re-encoded as cp1252 and decoded as UTF-8; kept only if that succeeds and is shorter. Same for cp866 `т[АБ].`.

3. **Action:** fix. All 10 repairs checked by hand (`Ben’s`, `statistics…`, `plano–convex`, `Here’s`, 😀).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** the first version accepted any Latin-1 lead and turned `×`+NBSP into Hebrew `נ` in 2 clean documents; the lead set is now restricted. Real Latin-1 text could still be "repaired" when the run happens to decode as UTF-8 (rare).

### Medicine 89: math-finemath / A5 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 14: A5 compatibility forms (PDF ligatures, fullwidth punctuation).
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** A5, 6 documents. `c16db13d63739369` "ﬀ" @313 (x91 ligatures: ﬀ ﬁ ﬂ ﬃ, U+FB00 U+FB01 U+FB02 U+FB03); `ce9b0d519779eba2` "ﬀ" @68 (x17); `addb07a0a886743c` fullwidth comma "，" @2666 (x2, U+FF0C) in English text translated from Chinese.

2. **Medicine:** replace the ligatures U+FB00–U+FB06 by their NFKC letters (ﬁ → fi, ﬀ → ff); replace fullwidth ASCII punctuation U+FF01–U+FF5E by the ASCII character, but only in documents where CJK characters are under 1% of the letters (real Chinese/Japanese text keeps its punctuation).
   ```text
   out = LIG_RX.sub(lambda m: unicodedata.normalize('NFKC', m.group()), t)
   if cjk_share(out) < 0.01: out = FULLWIDTH_RX.sub(lambda m: chr(ord(m.group()) - 0xFEE0), out)
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   see the table (proxy and gold columns). Gold: _pending_.

5. **Side effects:** a document that quotes a ligature as a character (a typography page) would lose it. Fullwidth digits in English text become ASCII digits, which is wanted here. Full NFKC is not applied: it would also change superscripts (x² → x2) and other maths symbols.

### Medicine 90: math-finemath / A6 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 10: A6 symbol-font private-use glyphs and look-alikes.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** A6, 9 documents. `9be631b8d8a8b294` U+F0C5 @6107 (should be ⊕); `c46f9ecdfac73e93` U+F0D8 @875 (x9); `f2746fa01fbc3cf4` "fɑstidious" @4992 (U+0251 U+0455 U+0461).

2. **Medicine:** map U+F000+code to the Symbol-font character for 46 codes (`(`, `)`, `=`, `⊕`, `∂`, Greek, brackets, …); leave other private-use characters.

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** Wingdings uses the same code points: U+F0D8 as an arrow bullet becomes `¬`. Look-alike letters in spam (`fɑstidious`) and the Armenian apostrophe in `Math՚s` are not fixed (recall 5 / 9).

### Medicine 91: math-finemath / B2 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 9: B2 HTML tags.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** B2, 8 documents. `bf73e54bda1aabdb` "<br />" @367 (x18); `addb07a0a886743c` "<ul>" @6030; `951a4c150e019bd5` "</Math>" @22663.

2. **Medicine:** `<br>` → newline; remove simple formatting tags (`p div span a ul ol li sup sub strong em font b i center`); skip documents with a code fence or `<script>`.

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** `x<sup>2</sup>` becomes `x2`. Recall 3 / 8: tags inside documents that also contain code, and broken fragments like `strong> Option`, are left.

### Medicine 92: math-finemath / B4 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6: B4 template junk.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** B4, 18 documents. `2d9c3add6852f806` "{{ 'ml-label-loading-course' | message }}" @0 (x14); `56027551326bb040` "{[ snackBarMessage ]}" @1482; `e967e3352605755f` "[TheoryMissing]" @102.

2. **Medicine:** delete `{[ name ]}`, `{{ name.attr | filter }}` (spaces inside, so LaTeX `{{x}}` is not hit), `{% … %}`, `[TheoryMissing]`, `document.write(…)`.
   ```text
   B4_RX = re.compile(r"\{\[\s*\w+\s*\]\}|\{\{\s+['\w][\w'.| :-]*\s+\}\}|\{%.*?%\}|\[TheoryMissing\]|document\.write\([^)]*\);?")
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** a tutorial that teaches Angular/Jinja templates would lose its examples. Recall 9 / 18: AsciiMath leftovers such as `color(blue)(` are not covered.

### Medicine 93: math-finemath / B5 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7: B5 broken LaTeX / markdown.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** B5, 28 documents. `e73db44e20a89b36` "$$$where" @241 (x4); `951a4c150e019bd5` "[itex]" @23031; `3a2ccc88dfcd67c9` unclosed ``` fence @12634.

2. **Medicine:** exactly `$$$` → `$$`; forum BBCode `[itex] [/itex] [tex] [/tex] [math]` → `$`; an odd number of ``` fences gets a closing fence at the end.

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** found while testing: `$$$$` is two adjacent display blocks and is valid (`3e136806c369dfbc`), so only exactly three dollars are changed. A literal `[math]` in prose becomes `$`. Recall 5 / 28: stray `$$` inside inline math (`3f15fccd9f76020b`) and LaTeX with stripped backslashes (`$mathbb`) cannot be repaired by rule.

### Medicine 94: math-finemath / C1 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: C1 boilerplate.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** C1, 328 documents (most web pages keep some site chrome). `72f073c36305b095` "posted by gamer chick" @13; `de1b08a158de9ae9` "This preview shows page" @95; `92bef36fe0c0fc40` "Replies / Views" related-thread blocks @9487.

2. **Medicine:** delete a line that is a known chrome phrase (`C1`), or that contains a site-chrome phrase (`C1_SITE`, ~70 phrases seen in this pack: GMAT Club headers, "View Full Document", OEIS footer, "My Personal Notes arrow_drop_up", …) and is at most 120 characters; delete `Replies\n<n>\nViews\n<n>` blocks.
   ```text
   keep = [l for l in t.split('\n') if not (C1.fullmatch(l) or (C1_SITE.search(l) and len(l) <= 120))]
   ```

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 changed / 0 dropped. Gold: _pending_.

5. **Side effects:** recall is only 109 / 328: the phrase list is fitted to sites seen here, so new sites' menus and footers are missed. A forum title ending in `[#permalink]` is removed (the question usually repeats in the post). A real line that is only "Share", "Views" or "Tags:" would be removed. Found and fixed while testing: "The time now is" deleted the problem statement "If the time now is 9 o'clock" (now needs hh:mm).

### Medicine 95: math-finemath / C2 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: C2 repeated lines and passages.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** C2, 187 documents. `92bef36fe0c0fc40` "• Introductory Physics Homework Help" @9487 (x10); `98e5be6db6c1c81e` "Mathematical Practice 3: Construct viable…" @2979 (x2); `e9bc93d8821adcec` the same reading passage before each question (x4–5).

2. **Medicine:** (a) a non-code line of 15+ characters that appears 5+ times keeps only its first copy; (b) a passage (blank-line block, 150+ characters, not a bullet list, not answer options, not code) that appears more than once keeps only its first copy (ruling 13).

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 1 changed / 0 dropped (0.85%). Gold: _pending_.

5. **Side effects:** the proxy change is natural restatement: an author repeats a sentence on purpose (`5ee756dbf1307a6f`) and the copy is lost. Repeated per-question passages (`e9bc93d8821adcec`) lose their later copies, so later questions lose their context. Recall 40 / 187: short repeated titles and quoted questions under 150 characters are kept.

### Medicine 96: math-finemath / C3 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: C3 truncated documents.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** C3, 49 documents. `de1b08a158de9ae9` Course Hero preview cut at "s[R2(Cgs" @3238; `9d26c83f14d2087f` "We hav" @772 (paywall); `4e1e6a7902a4435e` teaser ending "deeper unders..." @6566.

2. **Medicine:** drop a document that carries a preview/paywall banner (`This preview shows|Sign up to view the full|View Full Document|intentionally blurred sections`); if a document ends in a teaser cut (`word...` or `word…`), trim back to the last full sentence.
   ```text
   if PREVIEW_RX.search(t): return None
   if re.search(r'\w(?:\.\.\.|…)$', t.rstrip()): t = t[:last_full_stop + 1]
   ```

3. **Action:** drop (previews) / fix (teasers).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** a good document that merely quotes "View Full Document" would be dropped. Recall 15 / 49: a document that stops mid-solution with no marker (`b6a1ee1fa12a6d5e` code cut at @4908) cannot be detected by a rule. A first version that trimmed every last line without end punctuation changed 6 of 117 clean documents (headings, signatures, answer lists) and was replaced.

### Medicine 97: math-finemath / C4 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 12: C4 two documents joined.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** C4, 7 documents. `dcaa196cc9b2af15` "A COVID-19 Prophecy" headline inside a units page @2843; `4d57615e33e7997e` "What mammal most abhors physical violence?" @573; `e68f196ec97b88a5` "What is Kanka?" @1865.

2. **Medicine:** none that is safe. A tested rule (cut a trailing block with no maths after a maths document) caught 0 of the labelled cases and changed 2 clean documents, so it is not proposed.

3. **Action:** drop by verdict. 4 of the 7 are also spam pages (C5) and are already `drop`; `e68f196ec97b88a5`, `c55fa2fcaeafd041` and `f6c1776061f622c6` (19 exam papers joined into one document) need the parts split or cut by hand or by a better splitter.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   not applicable (no automatic rule).

5. **Side effects:** none from automation; the cost is that C4 stays in documents nobody reviews.

### Medicine 98: math-finemath / C5 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: C5 keyword / link lists.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** C5, 50 documents. `25901665fc855b35` "See more: What Did Greg Giraldo…" @3568; `b124803aff87e2d9` "Domain And Range Notes Teachers Pay Teachers…" @5708; `1eff00a48b3b10a0` SEO FAQ farm.

2. **Medicine:** delete lines starting `See more:` and lines made of 5+ comma-separated Title-Case phrases of 2–8 words.
   ```text
   SEO = re.compile(r"(?m)^(?:See more: .*|(?:[A-Z][\w’'&.-]*(?: [\w’'&.-]+){1,7}, ){5,}.*)$")
   ```

3. **Action:** fix; a page that is mostly SEO is dropped by its verdict (most of the 46 are `drop`).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** recall is 5 / 50: most C5 here is whole spun/SEO pages, which only a drop decision handles. A real comma list of Title-Case names (bibliography, theorem names) would be deleted.

### Medicine 99: math-finemath / D3 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 11: D3 mixed-in foreign script.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** D3, 10 documents. `b605c8aa5c37f266` Japanese title "ベクトル…" @23; `f2746fa01fbc3cf4` Ukrainian ad lines "Дивитися фільми…" @10238 (x4); `8210e5fa65c2f665` Marathi intro "पाईये" @144.

2. **Medicine:** delete a line when more than half of its letters are Cyrillic, Indic, CJK, kana, Hangul or Arabic; if such lines hold more than 30% of the document's letters, drop the document (that is D1).

3. **Action:** fix (drop when mostly foreign).

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 0 / 0. Gold: _pending_.

5. **Side effects:** a legitimate quotation or title in another language is removed (DISEASES.md says D3 can be natural). Greek is excluded on purpose, since Greek letters are maths.

### Medicine 100: math-finemath / D4 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 13: D4 machine-translated or machine-spun text.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** D4, 22 documents. Most are SEO pages rewritten by a paraphrasing tool ("spun"): `4bbc06d580844d70` "optimistic integers that are only separating" @367 (for "positive integers that are only divisible"); `d3dc5a9f14a9a35a` "sine regulation" @658 (for "sine rule"); `a5d6914aacebfa97` "6 inches equals 3 thumbs up" @4121. A few are machine translations: `2b0dcb71433030d5` (German Wikipedia, LaTeX broken by the translator), `7fec63b917700801` "Because the byte unit inside the computer to represent the number are fixed-length" @478.

2. **Medicine:** no safe rule. Spun text is grammatical word by word; the signal is synonyms that make no sense in maths ("sine regulation", "optimistic integers"). A rule-based detector cannot see that without a language model. Proposed for later (not built, not tested): score each document with a small reference LM and a list of known spin substitutions ("sine regulation", "thumbs up" for inches, "optimistic" for positive), and send high scores to review.

3. **Action:** drop by verdict. 16 of the 22 are already `drop` (whole pages of spun SEO text); the 6 `fix` rows have one spun or translated paragraph inside an otherwise good page and need that paragraph cut by hand.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   not applicable (no automatic rule).

5. **Side effects:** none from automation. Ruling 11: ordinary spelling and grammar mistakes by people are not D4, so a future LM detector must be tuned not to flag forum posts by non-native writers.

### Medicine 101: math-finemath / F1 · SomaKorada07

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 15: F1 personal data.
> **Source:** [teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/math-finemath/SomaKorada07/medicine.md)

1. **Disease:** F1, 7 documents (values never copied). `02c235b035b38798` email at offset 82 (x2); `ace41f52d349ca6b` email at offset 1447 (x2); `4477acbfa8e1a6da` phone number at offset 2074. Company numbers and business emails are not F1 (ruling 6).

2. **Medicine:** emails → `[email removed]`; NNN-NNN-NNNN phone numbers → `[phone removed]` when no digit is within 3 characters (skips number tables).

3. **Action:** fix.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   proxy 1 changed (0.85%). Gold: _pending_.

5. **Side effects:** business contacts are masked too (harmless for privacy; that is the proxy change). Recall 2 / 7: IP addresses (`0306000512344150`), obfuscated emails and messenger IDs are not matched.

---

### Found five times or fewer (no medicine required)
E1 code collapsed into one line by extraction, or generated code (5, `af9d1316d085d805` MATLAB program on one 3712-char line), E2 hash blobs and data arrays (5), B1 entities (4, `ab0dcfdea8b8f728` "&#40;1-2x&#41;"), D2 romanised Hindi (2, `c5b36a86af256f62` "Apne doubts clear karein"), A4 U+FFFD (3, `7c6df0c4a23c902b` "M�bius"), A2 control characters (3, `c16db13d63739369` U+0004), F2 competition problems from known contests (4: `296ba0775d5f6cca` IMO 2009 Q5, `b65447202cb074c9` AMC 8 2012, `8f09ea36d06abaef` IMO 1959 problem, `b22b5d72708d7f26` IMO 1964 problem), H2 (2), D1 (1, `ce878294b69f1b20` Chinese). No F3, E3, B3 or G-group cases.

### Not in the disease list
25 documents lost their formulas when the page was extracted (e.g. `161a7643db59ce25`, `8e9e5b4d6166454e`): the text says "the slope of the line tangent to the graph of at the point is". This is recorded in `note` only; it may deserve its own code.

### Medicine 102: sci-finepdfs / A6 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 6: A6 Mixed Script Within a Word (Cyrillic/Latin OCR Homoglyphs).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `A6`, found in 1 of the 150 documents.
   Examples:
   - `cdc5973ec2161f44` (row 75): `mixed Latin/Cyrillic word at offset 85429 | synthetic placeholder at offset 6043 (1 total)`

2. **Medicine:** - *In words:* Detect tokens mixing Latin and Cyrillic scripts within the same word (such as 'Ilonиемi', 'vrтoglavo', or 'АКУМУЛATOR') and normalize lookalike glyphs to the majority script of the word while exempting scientific Greek symbols.

   ```text
   import re

   CYR_TO_LAT = str.maketrans({'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X', 'а': 'a', 'е': 'e', 'и': 'i', 'м': 'm', 'о': 'o', 'р': 'p', 'с': 'c', 'т': 't', 'х': 'x'})
   MIXED_WORD_RE = re.compile(r'\b(?:[A-Za-z]+[\u0400-\u04FF]+[A-Za-z0-9]*|[\u0400-\u04FF]+[A-Za-z]+[A-Za-z0-9]*)\b')

   def fix_mixed_script_words(text: str) -> str:
       return MIXED_WORD_RE.sub(lambda m: m.group(0).translate(CYR_TO_LAT), text)
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 1 of 150 documents (0.7%).
        - Removes/modifies < 0.001% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Pure Cyrillic words and standard Greek math/physics symbols remain untouched.

---

### Medicine 103: sci-finepdfs / B2 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 5: B2 HTML Tags (Scientific Subscripts & Line Breaks).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `B2`, found in 6 of the 150 documents.
   Examples:
   - `7ea84af3398cb3ed` (row 16): `tag '<br>' at offset 445945 (5 total) | synthetic placeholder at offset 79870 (20 total) | running header '- **Date Approved:** 08/02/202' repeated 33x, first at offset 218309 | phone at offset 271034 (1 total)`
   - `50f74766355f26d3` (row 21): `tag '<sup>' at offset 9685 (14 total) | synthetic placeholder at offset 533 (4 total)`
   - `c298d58f6344ddde` (row 22): `tag '<sup>' at offset 43973 (2 total)`

2. **Medicine:** - *In words:* Convert <sup>text</sup> to ^text, <sub>text</sub> to _text, and <br> to a newline. Strip remaining layout tags (<div>, <p>, <span>) while ignoring formal symbols inside LaTeX $...$ math mode.

   ```text
   import re

   def clean_pdf_html_tags(text: str) -> str:
       text = re.sub(r'<sup>(.*?)</sup>', r'^\1', text, flags=re.IGNORECASE)
       text = re.sub(r'<sub>(.*?)</sub>', r'_\1', text, flags=re.IGNORECASE)
       text = re.sub(r'<br\s*/?>', r'\n', text, flags=re.IGNORECASE)
       text = re.sub(r'</?(?:div|p|span|table|tr|td|th)[^>]*>', '', text, flags=re.IGNORECASE)
       return text
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 6 of 150 documents (4.0%).
        - Removes/modifies 0.002% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Converting tags to ^ and _ preserves scientific gene superscripts and chemical subscripts.

---

### Medicine 104: sci-finepdfs / B4 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 3: B4 Placeholders (Upstream Synthetic Redaction & Template Parameters).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `B4`, found in 54 of the 150 documents.
   Examples:
   - `6d2428a3ad8e41d6` (row 2): `synthetic placeholder at offset 1733 (1 total) | phone at offset 19088 (2 total)`
   - `50cc681aabd3d82b` (row 4): `synthetic placeholder at offset 219980 (1 total) | running header '* Denotes Non-Negotiable Trans' repeated 9x, first at offset 64206`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`

2. **Medicine:** - *In words:* Replace synthetic placeholders ([REDACTED_EMAIL] / [REDACTED_EMAIL]) with the standard <EMAIL> token. Remove unrendered parameter placeholders (<parameter 1>, <function name>, <typename T>).

   ```text
   import re

   SYNTHETIC_EMAIL_RE = re.compile(r'\b[A-Za-z0-9._%+-]+@example\.(?:org|com)\b')
   TEMPLATE_PARAM_RE = re.compile(r'<(?:parameter|function name|process description|typename|see attached)[^>]*>', re.IGNORECASE)

   def clean_placeholders(text: str) -> str:
       text = SYNTHETIC_EMAIL_RE.sub('<EMAIL>', text)
       text = TEMPLATE_PARAM_RE.sub('', text)
       return text
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 54 of 150 documents (36.0%).
        - Removes/modifies 0.057% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - A tutorial specifically explaining how to use example.com would have the domain replaced by <EMAIL>.

---

### Medicine 105: sci-finepdfs / C1 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 1: C1 Boilerplate (Running Page Headers & Footers).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `C1`, found in 38 of the 150 documents.
   Examples:
   - `8c1aed2f8a439b91` (row 1): `running header 'MIT Introduction to Deep Learn' repeated 8x, first at offset 56`
   - `50cc681aabd3d82b` (row 4): `synthetic placeholder at offset 219980 (1 total) | running header '* Denotes Non-Negotiable Trans' repeated 9x, first at offset 64206`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`

2. **Medicine:** - *In words:* Across a document, identify non-empty lines of 15 or more characters that repeat 5 or more times. Keep the first occurrence (often the true title or initial header) and delete subsequent identical lines. Exclude Markdown table separator lines, LaTeX math environments, and roll-call voting refrains.

   ```text
   import re
   from collections import Counter

   TABLE_BORDER = re.compile(r'^[\s|:\-]+$')
   MATH_ENV = re.compile(r'\\(begin|end)\{(?:cases|align\*?|equation\*?)\}|\\hline')

   def remove_running_headers(text: str, min_len: int = 15, min_repeats: int = 5) -> str:
       lines = text.split('\n')
       counts = Counter(l.strip() for l in lines)
       header_candidates = {
           s for s, c in counts.items()
           if len(s) >= min_len and c >= min_repeats
           and not TABLE_BORDER.match(s) and not MATH_ENV.search(s) and 'Motion Carried.' not in s
       }
       if not header_candidates:
           return text
       kept, seen = [], set()
       for line in lines:
           s = line.strip()
           if s in header_candidates:
               if s in seen:
                   continue
               seen.add(s)
           kept.append(line)
       return '\n'.join(kept)
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 38 of 150 documents (25.3%).
        - Removes/modifies 0.934% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - In slide decks, retaining the first instance keeps the title on slide 1, but strips it from later slides as intended.

---

### Medicine 106: sci-finepdfs / C3 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 4: C3 Truncated Documents (Broken Trailing Tables & Mid-Phrase Cutoffs).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `C3`, found in 12 of the 150 documents.
   Examples:
   - `4f3067e9d3a6b2b8` (row 18): `table cut off at line '| 64 | ZINC ACETATE        ' offset 8085`
   - `4656c1ed1d4393c4` (row 24): `tag '<sub>' at offset 5912 (10 total) | running header 'Metal concentrations (mg/kg dw' repeated 6x, first at offset 3824 | table cut off at line '| R. Lapväärtinjoki | +       ' offset 16099`
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`

2. **Medicine:** - *In words:* If the final line of a document is an unclosed or incomplete Markdown table row (starts with | but lacks terminal cell closure), or a sentence cut off on a dangling preposition/conjunction right before a figure caption, trim the incomplete trailing fragment.

   ```text
   def clean_truncated_tables(text: str) -> str:
       lines = text.rstrip().split('\n')
       if lines:
           last = lines[-1].strip()
           if last.startswith('|') and not last.endswith('|') and last.count('|') >= 2:
               lines = lines[:-1]
       return '\n'.join(lines)
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 12 of 150 documents (8.0%).
        - Removes/modifies 0.012% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Removes the last partial table row or dangling phrase when cut off at end of PDF.

---

### Medicine 107: sci-finepdfs / C4 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 8: C4 Two Documents Joined (Multi-Article Journal Pages).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `C4`, found in 2 of the 150 documents.
   Examples:
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`
   - `6acc7c94105bdebd` (row 32): `synthetic placeholder at offset 7142 (1 total) | clinical case history 'A 67-year-old woman' at offset 462 | cut off mid-phrase on 'such as the' at offset 9107 | secondary article 'To the Editor:' at offset 7299 (line 65)`

2. **Medicine:** - *In words:* When a single PDF page or extract concatenates two distinct journal letters or book reviews (e.g. a second 'To the Editor:' letter or a separate review after an institutional sign-off), insert a clear Markdown document boundary or split at the secondary article header.

   ```text
   import re

   SECOND_LETTER_RE = re.compile(r'\n(To the Editor:)', re.IGNORECASE)

   def split_joined_letters(text: str) -> str:
       parts = SECOND_LETTER_RE.split(text)
       if len(parts) <= 3:
           return text
       return parts[0] + '\n' + parts[1] + parts[2]
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 2 of 150 documents (1.3%).
        - Removes/modifies 0.015% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Preserves the primary article while cleanly separating concatenated secondary correspondence.

---

### Medicine 108: sci-finepdfs / D1 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 7: D1/D3 Full-Document Language Verification & Bilingual Filtering.
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `D1`, found in 3 of the 150 documents.
   Examples:
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`
   - `bfbe6f0f5d61c19e` (row 82): `phone at offset 8159 (2 total) | German text at offset 9463 (49 segments) mixed with English at offset 53 (280 segments)`
   - `f26a6a8bd745c1a2` (row 148): `Spanish text at offset 314 (7 segments) mixed with English at offset 0 (150 segments)`

2. **Medicine:** - *In words:* Rather than dropping a document based only on its opening lines, scan all paragraphs across the full document. If a document labeled eng_Latn starts in French/German but contains valid English sections (D1;D3, e.g. 51a4fb599da754db), verdict is fix: retain the English paragraphs or route bilingual sections appropriately instead of dropping the whole document.

   ```text
   def filter_bilingual_paragraphs(text: str, keep_en_stopwords: set) -> str:
       paras = text.split('\n\n')
       kept = [p for p in paras if len(set(p.lower().split()) & keep_en_stopwords) >= 2 or len(p) < 80]
       return '\n\n'.join(kept) if kept else text
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 3 of 150 documents (2.0%).
        - Removes/modifies 0.045% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Preserves English abstracts, citations, and bilingual passages in multi-language academic PDFs.

---

### Medicine 109: sci-finepdfs / F1 · jssunil

> **Status:** CANDIDATE; not approved. **Original section:** Medicine 2: F1 Personal Data (Unredacted Telephone Numbers & Clinical Case Histories).
> **Source:** [teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md](https://github.com/patilvijay23/era-v5-lab/blob/g1-harm-test/teams/01-data-a/medicines/submissions/sci-finepdfs/jssunil/medicine.md)

1. **Disease:** `F1`, found in 39 of the 150 documents.
   Examples:
   - `6d2428a3ad8e41d6` (row 2): `synthetic placeholder at offset 1733 (1 total) | phone at offset 19088 (2 total)`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`
   - `3db737dca1122c53` (row 6): `synthetic placeholder at offset 2807 (1 total) | phone at offset 2846 (2 total)`

2. **Medicine:** - *In words:* Match phone numbers preceded by personal contact markers (Cell:, Mobile:, Daytime Phone:, Direct:, Phone:, Tel:) and replace the number portion with <PHONE>. Mask identifiable patient age/sex descriptors in clinical case reports to <PATIENT>.

   ```text
   import re

   PHONE_REDACT_RE = re.compile(
       r'((?:Cell|Mobile|Daytime|Direct|Office|Business|Contact|Telephone|Phone|Tel|Fax)[:\s]+)'
       r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
       re.IGNORECASE
   )

   def redact_phone_numbers(text: str) -> str:
       return PHONE_REDACT_RE.sub(r'\1<PHONE>', text)
   ```

3. **Action:** `fix` the text.

4. **Harm test:** **NOT_EVALUATED on regenerated gold.** Any numbers below are source-reported/historical, not a fresh certification.

   - Tested across all 150 documents:
        - Changes 39 of 150 documents (26.0%).
        - Removes/modifies 0.006% of total text (passing the < 1% threshold).
        - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **Side effects:** - Business contact numbers labeled 'Office Phone:' are redacted to <PHONE>, which is preferred for pre-training privacy.

---

## 4. Pending and excluded inputs

- **G2 Indic:** not integrated; team handoff pending.
- **Harm evidence:** each candidate and the final ordered combined pipeline
  must pass each applicable official gold set at 1% or below.
- **Conflict selection:** BLOCKED groups need explicit owner/reviewer decisions and fixtures.
- **Previously documented code precedence:** E3 drop before E3 masking to avoid hiding secrets;
  revalidate before enabling. Do not infer executable ordering from raw contributor markdown.
- **Previously reviewed English candidates:** C1/C5/F1 overlap was curated in separate
  code/English summary sheets; those historical choices are not automatically carried over to
  raw submission implementations without an explicit mapping and fresh harm tests.
- **Unstructured and template submissions:** retained in the inventory but are not executable.
- **G9 F2:** fingerprint dependency not assumed complete.
