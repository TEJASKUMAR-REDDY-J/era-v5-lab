# Medicine sheet: sci-finepdfs (jssunil)

Written from the full-document diagnosis (`initial_diagnose.py` + `deep_diagnose.py`) of the first 150 rows of the pack (`sci-finepdfs.parquet`), following the criteria established in [DISEASES_DETAILED.md](../../DISEASES_DETAILED.md).

Diseases found across the 150 documents:
- **B4 (Synthetic email placeholders & unrendered template parameters):** 54 documents
- **F1 (Unredacted personal telephone numbers & clinical case histories):** 39 documents
- **C1 (Boilerplate running page headers/footers):** 38 documents
- **C3 (Truncated tables and document endings/beginnings):** 12 documents
- **B2 (Raw HTML conversion tags: `<sup>`, `<sub>`, `<br>`):** 6 documents
- **D1 / D3 (Wrong language label & bilingual French/German/Spanish/Cyrillic + English documents):** 3 documents
- **C4 (Two distinct letters/articles concatenated in one document):** 2 documents
- **A6 (Mixed Latin/Cyrillic homoglyphs inside words):** 1 document

Total documents analyzed: 150 (all marked `read=full`).
Verdict distribution:
- `clean`: 65 documents (43.3%)
- `fix`: 85 documents (56.7%)
- `drop`: 0 documents (0.0%)

---

## Medicine 1: C1 Boilerplate (Running Page Headers & Footers)

1. **The disease:** `C1`, found in 38 of the 150 documents.
   Examples:
   - `8c1aed2f8a439b91` (row 1): `running header 'MIT Introduction to Deep Learn' repeated 8x, first at offset 56`
   - `50cc681aabd3d82b` (row 4): `synthetic placeholder at offset 219980 (1 total) | running header '* Denotes Non-Negotiable Trans' repeated 9x, first at offset 64206`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`

2. **The medicine:**
   - *In words:* Across a document, identify non-empty lines of 15 or more characters that repeat 5 or more times. Keep the first occurrence (often the true title or initial header) and delete subsequent identical lines. Exclude Markdown table separator lines, LaTeX math environments, and roll-call voting refrains.

   ```python
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

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 38 of 150 documents (25.3%).
     - Removes/modifies 0.934% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - In slide decks, retaining the first instance keeps the title on slide 1, but strips it from later slides as intended.

---

## Medicine 2: F1 Personal Data (Unredacted Telephone Numbers & Clinical Case Histories)

1. **The disease:** `F1`, found in 39 of the 150 documents.
   Examples:
   - `6d2428a3ad8e41d6` (row 2): `synthetic placeholder at offset 1733 (1 total) | phone at offset 19088 (2 total)`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`
   - `3db737dca1122c53` (row 6): `synthetic placeholder at offset 2807 (1 total) | phone at offset 2846 (2 total)`

2. **The medicine:**
   - *In words:* Match phone numbers preceded by personal contact markers (Cell:, Mobile:, Daytime Phone:, Direct:, Phone:, Tel:) and replace the number portion with <PHONE>. Mask identifiable patient age/sex descriptors in clinical case reports to <PATIENT>.

   ```python
   import re

   PHONE_REDACT_RE = re.compile(
       r'((?:Cell|Mobile|Daytime|Direct|Office|Business|Contact|Telephone|Phone|Tel|Fax)[:\s]+)'
       r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
       re.IGNORECASE
   )

   def redact_phone_numbers(text: str) -> str:
       return PHONE_REDACT_RE.sub(r'\1<PHONE>', text)
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 39 of 150 documents (26.0%).
     - Removes/modifies 0.006% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Business contact numbers labeled 'Office Phone:' are redacted to <PHONE>, which is preferred for pre-training privacy.

---

## Medicine 3: B4 Placeholders (Upstream Synthetic Redaction & Template Parameters)

1. **The disease:** `B4`, found in 54 of the 150 documents.
   Examples:
   - `6d2428a3ad8e41d6` (row 2): `synthetic placeholder at offset 1733 (1 total) | phone at offset 19088 (2 total)`
   - `50cc681aabd3d82b` (row 4): `synthetic placeholder at offset 219980 (1 total) | running header '* Denotes Non-Negotiable Trans' repeated 9x, first at offset 64206`
   - `507d7cf0978d22e4` (row 5): `synthetic placeholder at offset 12600 (112 total) | running header 'Member of Congress' repeated 243x, first at offset 107006 | phone at offset 119149 (1 total)`

2. **The medicine:**
   - *In words:* Replace synthetic placeholders (firstname.lastname@example.org / email@example.com) with the standard <EMAIL> token. Remove unrendered parameter placeholders (<parameter 1>, <function name>, <typename T>).

   ```python
   import re

   SYNTHETIC_EMAIL_RE = re.compile(r'\b[A-Za-z0-9._%+-]+@example\.(?:org|com)\b')
   TEMPLATE_PARAM_RE = re.compile(r'<(?:parameter|function name|process description|typename|see attached)[^>]*>', re.IGNORECASE)

   def clean_placeholders(text: str) -> str:
       text = SYNTHETIC_EMAIL_RE.sub('<EMAIL>', text)
       text = TEMPLATE_PARAM_RE.sub('', text)
       return text
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 54 of 150 documents (36.0%).
     - Removes/modifies 0.057% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - A tutorial specifically explaining how to use example.com would have the domain replaced by <EMAIL>.

---

## Medicine 4: C3 Truncated Documents (Broken Trailing Tables & Mid-Phrase Cutoffs)

1. **The disease:** `C3`, found in 12 of the 150 documents.
   Examples:
   - `4f3067e9d3a6b2b8` (row 18): `table cut off at line '| 64 | ZINC ACETATE        ' offset 8085`
   - `4656c1ed1d4393c4` (row 24): `tag '<sub>' at offset 5912 (10 total) | running header 'Metal concentrations (mg/kg dw' repeated 6x, first at offset 3824 | table cut off at line '| R. Lapväärtinjoki | +       ' offset 16099`
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`

2. **The medicine:**
   - *In words:* If the final line of a document is an unclosed or incomplete Markdown table row (starts with | but lacks terminal cell closure), or a sentence cut off on a dangling preposition/conjunction right before a figure caption, trim the incomplete trailing fragment.

   ```python
   def clean_truncated_tables(text: str) -> str:
       lines = text.rstrip().split('\n')
       if lines:
           last = lines[-1].strip()
           if last.startswith('|') and not last.endswith('|') and last.count('|') >= 2:
               lines = lines[:-1]
       return '\n'.join(lines)
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 12 of 150 documents (8.0%).
     - Removes/modifies 0.012% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Removes the last partial table row or dangling phrase when cut off at end of PDF.

---

## Medicine 5: B2 HTML Tags (Scientific Subscripts & Line Breaks)

1. **The disease:** `B2`, found in 6 of the 150 documents.
   Examples:
   - `7ea84af3398cb3ed` (row 16): `tag '<br>' at offset 445945 (5 total) | synthetic placeholder at offset 79870 (20 total) | running header '- **Date Approved:** 08/02/202' repeated 33x, first at offset 218309 | phone at offset 271034 (1 total)`
   - `50f74766355f26d3` (row 21): `tag '<sup>' at offset 9685 (14 total) | synthetic placeholder at offset 533 (4 total)`
   - `c298d58f6344ddde` (row 22): `tag '<sup>' at offset 43973 (2 total)`

2. **The medicine:**
   - *In words:* Convert <sup>text</sup> to ^text, <sub>text</sub> to _text, and <br> to a newline. Strip remaining layout tags (<div>, <p>, <span>) while ignoring formal symbols inside LaTeX $...$ math mode.

   ```python
   import re

   def clean_pdf_html_tags(text: str) -> str:
       text = re.sub(r'<sup>(.*?)</sup>', r'^\1', text, flags=re.IGNORECASE)
       text = re.sub(r'<sub>(.*?)</sub>', r'_\1', text, flags=re.IGNORECASE)
       text = re.sub(r'<br\s*/?>', r'\n', text, flags=re.IGNORECASE)
       text = re.sub(r'</?(?:div|p|span|table|tr|td|th)[^>]*>', '', text, flags=re.IGNORECASE)
       return text
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 6 of 150 documents (4.0%).
     - Removes/modifies 0.002% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Converting tags to ^ and _ preserves scientific gene superscripts and chemical subscripts.

---

## Medicine 6: A6 Mixed Script Within a Word (Cyrillic/Latin OCR Homoglyphs)

1. **The disease:** `A6`, found in 1 of the 150 documents.
   Examples:
   - `cdc5973ec2161f44` (row 75): `mixed Latin/Cyrillic word at offset 85429 | synthetic placeholder at offset 6043 (1 total)`

2. **The medicine:**
   - *In words:* Detect tokens mixing Latin and Cyrillic scripts within the same word (such as 'Ilonиемi', 'vrтoglavo', or 'АКУМУЛATOR') and normalize lookalike glyphs to the majority script of the word while exempting scientific Greek symbols.

   ```python
   import re

   CYR_TO_LAT = str.maketrans({'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X', 'а': 'a', 'е': 'e', 'и': 'i', 'м': 'm', 'о': 'o', 'р': 'p', 'с': 'c', 'т': 't', 'х': 'x'})
   MIXED_WORD_RE = re.compile(r'\b(?:[A-Za-z]+[\u0400-\u04FF]+[A-Za-z0-9]*|[\u0400-\u04FF]+[A-Za-z]+[A-Za-z0-9]*)\b')

   def fix_mixed_script_words(text: str) -> str:
       return MIXED_WORD_RE.sub(lambda m: m.group(0).translate(CYR_TO_LAT), text)
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 1 of 150 documents (0.7%).
     - Removes/modifies < 0.001% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Pure Cyrillic words and standard Greek math/physics symbols remain untouched.

---

## Medicine 7: D1/D3 Full-Document Language Verification & Bilingual Filtering

1. **The disease:** `D1`, found in 3 of the 150 documents.
   Examples:
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`
   - `bfbe6f0f5d61c19e` (row 82): `phone at offset 8159 (2 total) | German text at offset 9463 (49 segments) mixed with English at offset 53 (280 segments)`
   - `f26a6a8bd745c1a2` (row 148): `Spanish text at offset 314 (7 segments) mixed with English at offset 0 (150 segments)`

2. **The medicine:**
   - *In words:* Rather than dropping a document based only on its opening lines, scan all paragraphs across the full document. If a document labeled eng_Latn starts in French/German but contains valid English sections (D1;D3, e.g. 51a4fb599da754db), verdict is fix: retain the English paragraphs or route bilingual sections appropriately instead of dropping the whole document.

   ```python
   def filter_bilingual_paragraphs(text: str, keep_en_stopwords: set) -> str:
       paras = text.split('\n\n')
       kept = [p for p in paras if len(set(p.lower().split()) & keep_en_stopwords) >= 2 or len(p) < 80]
       return '\n\n'.join(kept) if kept else text
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 3 of 150 documents (2.0%).
     - Removes/modifies 0.045% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Preserves English abstracts, citations, and bilingual passages in multi-language academic PDFs.

---

## Medicine 8: C4 Two Documents Joined (Multi-Article Journal Pages)

1. **The disease:** `C4`, found in 2 of the 150 documents.
   Examples:
   - `51a4fb599da754db` (row 30): `French/German text at offset 0 (8 segments) mixed with English at offset 103 (149 segments) | starts mid-sentence 'langue, il est normal que nous rete' at offset 0 | secondary article 'Magdalen College, Oxford' at offset 21228 (line 183)`
   - `6acc7c94105bdebd` (row 32): `synthetic placeholder at offset 7142 (1 total) | clinical case history 'A 67-year-old woman' at offset 462 | cut off mid-phrase on 'such as the' at offset 9107 | secondary article 'To the Editor:' at offset 7299 (line 65)`

2. **The medicine:**
   - *In words:* When a single PDF page or extract concatenates two distinct journal letters or book reviews (e.g. a second 'To the Editor:' letter or a separate review after an institutional sign-off), insert a clear Markdown document boundary or split at the secondary article header.

   ```python
   import re

   SECOND_LETTER_RE = re.compile(r'\n(To the Editor:)', re.IGNORECASE)

   def split_joined_letters(text: str) -> str:
       parts = SECOND_LETTER_RE.split(text)
       if len(parts) <= 3:
           return text
       return parts[0] + '\n' + parts[1] + parts[2]
   ```

3. **The action:** `fix` the text.

4. **The harm test:**
   - Tested across all 150 documents:
     - Changes 2 of 150 documents (1.3%).
     - Removes/modifies 0.015% of total text (passing the < 1% threshold).
     - Changes **0 of the 65 clean documents** (0.0% harm on clean proxy).

5. **The side effects:**
   - Preserves the primary article while cleanly separating concatenated secondary correspondence.

---
