# Medicine sheet: cadj-stackexchange (smitasasindran)

Write one section for each disease that you found more than five times.


1. **Disease:** B3, ghost chat markers
- **Count:** 500 of 500 documents, 1,966 occurrences in total: 500 `<issue_start>` and 1,466 `<issue_comment>`.
- **Examples:**
     - `87116d4f6facd13b`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 302 and 495.
     - `c9e11c8baa07c6e0`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 944, 1367 and 4657.
     - `d78b5eeab23e7a55`: `<issue_start>` at offset 0, `<issue_comment>` at offsets 1120 and 302.

2. **Medicine:** 
Replace `<issue_start>` with `[issue_start]`   
Replace each `<issue_comment>` with `[issue_comment]`   

```python
import re

def cure_b3(text: str) -> str:
    text = text.replace("<issue_start>", "[issue_start]")
    text = text.replace("<issue_comment>", "[issue_comment]")
    return text
```

3. **Action:** fix the text. No document is dropped.

4. **Harm test:** PENDING. 

   | Gold set | Documents | Changed | Dropped | Result |
   |---|---|---|---|---|
   | _to fill_ | _to fill_ | _to fill_ | 0 | _pass if changed is 1% or less_ |

   The expected result is 0 changed for a gold set of source files, because they should contain none of these markers. If a gold set does contain `<issue_start>` or `<issue_comment>` text, those documents were not really clean, and that is worth reporting to the gold-set owners.

5. **Side effects:** 
Simple replace rule on exact match, should have no side effects


## Medicine 2

1. **Disease:** B4, redaction placeholders that look like HTML tags.
- **Count:** 162 occurrences in 53 documents: `<NAME>` 90 (24 docs), `<EMAIL>` 44 (13 docs), `<PASSWORD>` 27 (17 docs), `<KEY>` 1 (1 doc). About 130 of them are inside code snippets.
- **Examples:**
     - `a06ac825948fcdf1`: `@<NAME>,` at offset 1239.
     - `b79c9269b393f7ee`: `"email": "<EMAIL>",` at offset 119.
     - `32407cff5d9572ab`: `$password="<PASSWORD>";` at offset 410.

2. **Medicine:**
Replace the exact tags `<NAME>`, `<EMAIL>`, `<PASSWORD>` and `<KEY>` with `[NAME]`, `[EMAIL]`, `[PASSWORD]` and `[KEY]`.  
Leave the `username_N:` labels in place.  
Other tags (`<br>`, `<image>`, `<div>`) are left alone.

```python
import re

def cure_b4(text: str) -> str:
    return re.sub(r"<(NAME|EMAIL|PASSWORD|KEY)>", r"[\1]", text)
```

3. **Action:** fix the text. No document is dropped.

4. **Harm test:** PENDING. Run `cure_b2` on the gold set with the sample check below.

   | Gold set | Documents | Changed | Dropped | Result |
   |---|---|---|---|---|
   | _to fill_ | _to fill_ | _to fill_ | 0 | _pass if changed is 1% or less_ |

5. **Side effects:**
- In other code, `<NAME>` or `<KEY>` can be real syntax, for example a generic type `Map<KEY>` or a template. Replacing it would change the code. The gold-set test should show whether it happens in other languages.


