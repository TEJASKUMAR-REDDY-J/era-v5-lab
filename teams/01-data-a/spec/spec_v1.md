# G1 Data A — Spec v1: parent medicine (DRAFT; not frozen)

> **Status:** English + code candidate consolidation only. Not approved until every
> rule and the combined sequence pass rerun on refreshed gold sets; math and science
> remain unincorporated, and G2 Indic rules are pending their team delivery.

## Scope and source provenance

- English source: `en-medicines/medicine_en.md` (SHA-256 `00bd447008ac29b3c18d3010ef221daf8216696fefdcd611a57ad0c8d02374e2`).
- Code source: `code-medicines/medicine_code.md` (SHA-256 `96021cde9a6570471be4f02c119059a952fc0d85b5558b4229dcd6a02d95bc02`).
- Source rule implementations have been copied without modification.
- Rules execute in the order listed; drops stop later rules on a document.
- Only clean documents with independent reader votes belong in the harm-test gold set.
- Gold counts and results printed in old medicine sheets are historical, not current approvals.

## Conflict resolution decisions

- Include all 25 code rules from the canonical code sheet, honoring their `LANGS` scope.
- Include 19 English KEEP rules; exclude the 5 rules marked DROP.
- Cross-domain English/code rules are separated through mutually exclusive `LANGS` values.
- The code-python pack has no approved canonical code rule scope in this source sheet; it is NOT certified.
- Multiple rules for one disease are retained only when proposed as complementary by the source sheet;
  the combined-rule test must still pass for each affected pack.
- **Safety precedence:** `DA-E3-001` drop runs before `DA-E3-003` mask, which differs
  from the source code-sheet section order; rerun all applicable gold and positive fixtures.
- **Code overlap:** `DA-B3-008` marker repair precedes `DA-B4-005` PII-placeholder repair;
  all E4 licence-fix rules follow E4 licence drop, preserving source-order among fixes.
- **English C1:** select `DA-C1-006`, exclude `DA-C1-002` and `DA-C1-005` which failed gold;
  **English C5:** select `DA-C5-002`, exclude failed `DA-C5-001`.
- **English F1:** prefer `DA-F1-003` to redundant `DA-F1-002`.
- **English C2/C3/B4:** retain complementary KEEP rules in source order; check combined interactions.

| Excluded English rule | Reason |
|---|---|
| `DA-C3-001` | Its labelled positives are covered by complementary kept C3 rules |
| `DA-C5-001` | Failed the English gold harm threshold |
| `DA-C1-005` | Failed gold harm on multiple English packs |
| `DA-C1-002` | Failed en-dclm gold harm threshold |
| `DA-F1-002` | Redundant with better-coverage DA-F1-003 |

## Harm-test evidence — REQUIRED BEFORE FREEZE

Every accepted rule must show changed, dropped, denominator, 1% verdict and pack/gold/code
hashes from the refreshed gold sets. Both individual and `ALL IN ORDER` must PASS.
Reports are intentionally pending here; historical 0% results are not reused.

## Pending sources

- **Math:** final canonical executable medicines and current gold harm evidence pending.
- **Science:** final canonical executable medicines and current gold harm evidence pending.
- **Code Python:** code canonical sheet excludes this pack; scope/medicine decision pending.
- **G2 Indic:** team has not provided approved rules; integrate and test upon receipt.
- **G9 F2 fingerprints:** pending October 31 policy and benchmark hashes.

## Approved candidate rule blocks (not yet harm-certified)

## 1. `DA-A4-001` · A4 lost bytes (U+FFFD) · drop · all 5 · source: code
1. **Disease:** A4 lost bytes (U+FFFD) · drop · all 5.
2. **Medicine:** the text holds U+FFFD (unless it mentions 0xfffd).
```python
RULE_ID = "DA-A4-001"
CODE = "A4"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-python"  # pack whose medicine this came from
import html, re

def medicine_a4(text: str) -> str | None:
    return None if ("\ufffd" in text and "0xfffd" not in text.lower()) else text


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(medicine_a4(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 2. `DA-E1-005` · E1 generated code · drop · all 5 · source: code
1. **Disease:** E1 generated code · drop · all 5.
2. **Medicine:** generator banner in a header comment ("Code generated", "auto-generated"...), or a Kiota/goformation fingerprint.
```python
RULE_ID = "DA-E1-005"
CODE = "E1"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
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
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 3. `DA-E1-004` · E1 generated code · drop · all 5 · source: code
1. **Disease:** E1 generated code · drop · all 5.
2. **Medicine:** generator banner in the first 15 lines, or 20+ `#[doc = "..."]` lines.
```python
RULE_ID = "DA-E1-004"
CODE = "E1"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-rust"  # pack whose medicine this came from
import html, re

MARKER_LINE = re.compile(r"^(?:<(?:reponame|filename|gh_stars)>[^\n]*)\n?")

GENERATED = re.compile(
    r"(?i)(auto-?generated|automatically generated|code generated|generated by|@generated"
    r"|do not (?:directly )?edit|this file is generated)"
)

def _strip_marker(text: str) -> str:
    return MARKER_LINE.sub("", text, count=1)

def e1_generated(text: str):
    """E1: drop when a generated banner is in the first 15 lines, or 20+ #[doc = "..."] lines."""
    body = _strip_marker(text).split("\n")
    head = "\n".join(body[:15])
    if GENERATED.search(head) or sum('#[doc = "' in l for l in body) >= 20:
        return "drop", ""
    return "keep", text


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(e1_generated(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 4. `DA-E1-001` · E1 generated code · drop · all 5 · source: code
1. **Disease:** E1 generated code · drop · all 5.
2. **Medicine:** generator marker before or just after the package clause, or a Kiota/goformation fingerprint.
```python
RULE_ID = "DA-E1-001"
CODE = "E1"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
import html, re

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


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(drop_generated(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 5. `DA-E1-002` · E1 generated code · drop · all 5 · source: code
1. **Disease:** E1 generated code · drop · all 5.
2. **Medicine:** "auto-generated", "do not edit", `sourceMappingURL` or a minified file (<=2 lines, >10k chars). Detector: returns True/False.
```python
RULE_ID = "DA-E1-002"
CODE = "E1"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-js-ts"  # pack whose medicine this came from
import html, re

GENERATED = re.compile(
    r"(?i)(auto[- ]?generated|autogenerated|do not edit|"
    r"var searchData\s*=|code generated by|sourceMappingURL=)"
)

def is_generated_artifact(text, filename=""):
    minified = text.count("\n") <= 2 and len(text) > 10000
    return bool(GENERATED.search(text)) or minified


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(is_generated_artifact(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 6. `DA-E1-006` · E1 generated code · drop · all 5 · source: code
1. **Disease:** E1 generated code · drop · all 5.
2. **Medicine:** decompiler or generator marker (Jad/Procyon, "AUTO-GENERATED FILE", "This class was generated by", swagger...). Detector: returns True/False.
```python
RULE_ID = "DA-E1-006"
CODE = "E1"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-java"  # pack whose medicine this came from
import html, re

GEN = re.compile(r'Decompiled by (Jad|Procyon)|Code generated by [^\n]{0,60}Generator|AUTO-GENERATED FILE'
                 r'|generated by a tool and any changes will be overwritten|Automatically generated - do not modify'
                 r'|This class was (automatically )?generated by|auto generated by the swagger'
                 r'|This is a generated file\. Not intended for manual editing')

def drop_e1(text): return bool(GEN.search(text))


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(drop_e1(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 7. `DA-E2-001` · E2 binary blob · drop · all 5 · source: code
1. **Disease:** E2 binary blob · drop · all 5.
2. **Medicine:** byte-array literals cover >=10% of the file, or base64 runs >=40%.
```python
RULE_ID = "DA-E2-001"
CODE = "E2"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
import html, re

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


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(drop_blob(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 8. `DA-E3-001` · E3 hard-coded secret · drop · rust, js-ts, java, cpp · source: code
1. **Disease:** E3 hard-coded secret · drop · rust, js-ts, java, cpp.
2. **Medicine:** a quoted value of 8+ chars assigned to api_key/token/password/secret. Detector: returns True/False.
```python
RULE_ID = "DA-E3-001"
CODE = "E3"
ACTION = "drop"
LANGS = {'javascript', 'typescript', 'rust', 'cpp', 'java'}
ORIGIN = "code-js-ts"  # pack whose medicine this came from
import html, re

SECRET_ASSIGNMENT = re.compile(
    r"(?i)\b(api[_-]?key|token|password|passwd|secret|auth[_-]?token)\b"
    r"\s*[:=]\s*([\"'])(?:(?!\2).){8,}\2"
)

def contains_secret_assignment(text):
    return bool(SECRET_ASSIGNMENT.search(text))


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(contains_secret_assignment(doc["text"]), doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 9. `DA-E3-003` · E3 hard-coded secret · fix · all 5 · source: code
1. **Disease:** E3 hard-coded secret · fix · all 5.
2. **Medicine:** known key formats and base32 seeds assigned to secret/seed/otp names -> `EXAMPLE_SECRET`.
```python
RULE_ID = "DA-E3-003"
CODE = "E3"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
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
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 10. `DA-E4-005` · E4 licence header · drop · all 5 · source: code
1. **Disease:** E4 licence header · drop · all 5.
2. **Medicine:** restrictive licence phrase in the first 60 lines ("free for personal use", "commercial use requires"...).
```python
RULE_ID = "DA-E4-005"
CODE = "E4"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
import re
RESTRICTIVE = re.compile(r"(?i)free for personal use|commercial use requires|non-?commercial use only|"
                         r"commons clause|not for commercial use|for evaluation purposes only")

def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    head = "\n".join(doc["text"].split("\n")[:60])
    return ("drop" if RESTRICTIVE.search(head) else "keep", doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 11. `DA-H3-001` · H3 vendored copy · drop · all 5 · source: code
1. **Disease:** H3 vendored copy · drop · all 5.
2. **Medicine:** `vendor/` folder in the file path.
```python
RULE_ID = "DA-H3-001"
CODE = "H3"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
import re

def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return ("drop" if re.search(r"(?:^|/)vendor/", doc["url"]) else "keep", doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 12. `DA-C3-002` · C3 broken code · drop · go · source: code
1. **Disease:** C3 broken code · drop · go.
2. **Medicine:** Go lexical check fails (unclosed string, rune or block comment; unbalanced brackets).
```python
RULE_ID = "DA-C3-002"
CODE = "C3"
ACTION = "drop"
LANGS = {'go'}
ORIGIN = "code-go"  # pack whose medicine this came from

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
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 13. `DA-F2-001` · F2 contest solution · drop · go, rust, js-ts · source: code
1. **Disease:** F2 contest solution · drop · go, rust, js-ts.
2. **Medicine:** path names LeetCode, Codeforces or AtCoder.
```python
RULE_ID = "DA-F2-001"
CODE = "F2"
ACTION = "drop"
LANGS = {'javascript', 'go', 'rust', 'typescript'}
ORIGIN = "code-go"  # pack whose medicine this came from
import re
CONTEST = re.compile(r"leetcode|codeforces|atcoder", re.I)

def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return ("drop" if CONTEST.search(doc["url"]) else "keep", doc["text"])
```
3. **Action:** drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 14. `DA-A1-001` · A1 invisible characters · fix · all 5 · source: code
1. **Disease:** A1 invisible characters · fix · all 5.
2. **Medicine:** delete U+FEFF (BOM).
```python
RULE_ID = "DA-A1-001"
CODE = "A1"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-cpp"  # pack whose medicine this came from
import html, re

def remove_bom_characters(text: str) -> str:
    return text.replace("\ufeff", "")


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(remove_bom_characters(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 15. `DA-A2-001` · A2 control characters · fix · all 5 · source: code
1. **Disease:** A2 control characters · fix · all 5.
2. **Medicine:** CRLF and lone CR -> LF.
```python
RULE_ID = "DA-A2-001"
CODE = "A2"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-cpp"  # pack whose medicine this came from
import html, re

def normalize_line_endings(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(normalize_line_endings(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 16. `DA-A6-001` · A6 look-alike letters · fix · all 5 · source: code
1. **Disease:** A6 look-alike letters · fix · all 5.
2. **Medicine:** Cyrillic look-alike letters inside Latin words -> Latin.
```python
RULE_ID = "DA-A6-001"
CODE = "A6"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
import re
HOMO = str.maketrans("аеорсухіјѕАВЕКМНОРСТХІЈЅ", "aeopcyxijsABEKMHOPCTXIJS")
MIXED = re.compile(r"\b(?=\w*[A-Za-z])(?=\w*[Ѐ-ӿ])\w+\b")

def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    t = MIXED.sub(lambda m: m.group().translate(HOMO), doc["text"])
    return ("fix" if t != doc["text"] else "keep", t)
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 17. `DA-B2-001` · B2 dataset metadata line · fix · all 5 · source: code
1. **Disease:** B2 dataset metadata line · fix · all 5.
2. **Medicine:** strip the `<reponame>`/`<filename>`/`<gh_stars>` line at the start.
```python
RULE_ID = "DA-B2-001"
CODE = "B2"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-js-ts"  # pack whose medicine this came from
import html, re

SOURCE_META = re.compile(
    r"\A(?:<(?:reponame|filename|gh_stars)>[^\r\n]*)+(?:\r?\n)?"
)

def remove_source_metadata(text):
    return SOURCE_META.sub("", text, count=1)


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(remove_source_metadata(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 18. `DA-B3-008` · B3 dataset markers · fix · all 5 · source: code
1. **Disease:** B3 dataset markers · fix · all 5.
2. **Medicine:** strip the marker lines at the start; `<EMAIL>` -> example address, `<NAME>` -> `[AUTHOR]`; remove chat tokens.
```python
RULE_ID = "DA-B3-008"
CODE = "B3"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-js-ts"  # pack whose medicine this came from
import html, re

import re

# \A anchors to the absolute start of the string.
# This prevents the regex from matching a <filename>-like line in the middle
# of a document body. Using ^ with re.MULTILINE would incorrectly match
# any line starting with the token, not only the document's first line.
_STARCODER_LINE = r'<(?:reponame|filename|gh_stars)>[^\n]*\n?'
STARCODER_PREFIX_RE = re.compile(r'\A(?:' + _STARCODER_LINE + r'){1,5}')

# Replace <EMAIL> anonymisation tokens.
# user@example.com uses the IANA-reserved example.com domain (RFC 2606)
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
    text = EMAIL_TOKEN_RE.sub('user@example.com', text)
    text = NAME_TOKEN_RE.sub('[AUTHOR]', text)
    text = OTHER_GHOST_RE.sub('', text)
    return text


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(fix_b3(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 19. `DA-B4-005` · B4 PII placeholders · fix · all 5 · source: code
1. **Disease:** B4 PII placeholders · fix · all 5.
2. **Medicine:** delete `<NAME>`/`<EMAIL>`/`<KEY>`/`<PASSWORD>` in comments and strings, `""` in code.
```python
RULE_ID = "DA-B4-005"
CODE = "B4"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-rust"  # pack whose medicine this came from
import html, re

PII_PLACEHOLDER = re.compile(r"<(?:NAME|EMAIL|KEY|PASSWORD)>")

COMMENT_LINE = re.compile(r"^\s*(//(?![!/])|/\*(?![!*])|\*|\*/|#)")

def b4_pii_placeholder(text: str):
    """B4: delete <NAME>/<EMAIL>/<KEY>/<PASSWORD> in comments and string literals, else use "".

    Mid-line test: an odd number of double quotes before the token means it is inside a string.
    """
    out = []
    for line in text.split("\n"):
        def sub(m):
            inside_string = line[: m.start()].count('"') % 2 == 1
            if inside_string or COMMENT_LINE.match(line) or line.lstrip().startswith("///"):
                return ""
            return '""'
        out.append(PII_PLACEHOLDER.sub(sub, line))
    new = "\n".join(out)
    return ("fix", new) if new != text else ("keep", text)


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(b4_pii_placeholder(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 20. `DA-C1-004` · C1 tool boilerplate · fix · all 5 · source: code
1. **Disease:** C1 tool boilerplate · fix · all 5.
2. **Medicine:** delete kubebuilder/operator-sdk scaffold notes ("EDIT THIS FILE!", "NOTE: json tags are required"...).
```python
RULE_ID = "DA-C1-004"
CODE = "C1"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-go"  # pack whose medicine this came from
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
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 21. `DA-C1-001` · C1 tool boilerplate · fix · all 5 · source: code
1. **Disease:** C1 tool boilerplate · fix · all 5.
2. **Medicine:** delete the NetBeans licence-template and IntelliJ "Created by" header comments.
```python
RULE_ID = "DA-C1-001"
CODE = "C1"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-java"  # pack whose medicine this came from
import html, re

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


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m5_strip_ide_boilerplate(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 22. `DA-E4-004` · E4 licence header · fix · all 5 · source: code
1. **Disease:** E4 licence header · fix · all 5.
2. **Medicine:** delete a leading comment block of 5+ lines that is >=40% licence text (doc comments kept).
```python
RULE_ID = "DA-E4-004"
CODE = "E4"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-rust"  # pack whose medicine this came from
import html, re

MARKER_LINE = re.compile(r"^(?:<(?:reponame|filename|gh_stars)>[^\n]*)\n?")

LICENCE = re.compile(
    r"(?i)(licensed under|permission is hereby granted|redistribution and use|public domain"
    r"|this source code form|all rights reserved|without warranties|general public license"
    r"|affero|mit license|apache license|free software|copyright|warranty|spdx|redistribute"
    r"|the software|the terms|permitted|liability|licen[cs]e|apache|distributed|rights|dedicated"
    r"|modified, or|you may not use)"
)

COMMENT_LINE = re.compile(r"^\s*(//(?![!/])|/\*(?![!*])|\*|\*/|#)")

def _strip_marker(text: str) -> str:
    return MARKER_LINE.sub("", text, count=1)

def _licence_density(block: str) -> bool:
    """3+ licence lines and at least 40% of the non-blank lines are licence text."""
    lines = [l for l in block.split("\n") if l.strip(" /*#\t")]
    hits = sum(bool(LICENCE.search(l)) for l in lines)
    return hits >= 3 and hits * 10 >= len(lines) * 4

def e4_licence_header(text: str):
    """E4: remove a leading comment block of 5+ lines that holds licence text.

    The block is either one /* ... */ comment or a run of // lines (single blank lines allowed
    inside). //! and /// doc comments are never part of it.
    """
    body = _strip_marker(text)
    prefix = text[: len(text) - len(body)]
    if body.lstrip().startswith("/*"):
        end = body.find("*/")
        block, rest = (body[: end + 2], body[end + 2 :]) if end != -1 else ("", body)
        n = block.count("\n") + 1
    else:
        lines = body.split("\n")
        n = 0
        i = 0
        while i < len(lines):
            if COMMENT_LINE.match(lines[i]):
                n = i + 1
                i += 1
            elif not lines[i].strip() and i + 1 < len(lines) and COMMENT_LINE.match(lines[i + 1]):
                i += 1
            else:
                break
        block, rest = "\n".join(lines[:n]), "\n".join(lines[n:])
    if n >= 5 and _licence_density(block):
        return "fix", prefix + rest.lstrip("\n")
    return "keep", text


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(e4_licence_header(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 23. `DA-E4-007` · E4 licence header · fix · all 5 · source: code
1. **Disease:** E4 licence header · fix · all 5.
2. **Medicine:** delete the first `/* */` block when it is 8+ lines and names Apache, MIT or GPL.
```python
RULE_ID = "DA-E4-007"
CODE = "E4"
ACTION = "fix"
LANGS = {'javascript', 'go', 'rust', 'typescript', 'cpp', 'java'}
ORIGIN = "code-java"  # pack whose medicine this came from
import html, re

TOK = re.compile(r'^(?:<(?:reponame|filename|gh_stars)>[^\n<]*)+\n?')

LIC = re.compile(r'Apache License|Licensed to the Apache|Permission is hereby granted|GNU (Lesser |Affero )?General Public License')

def fix_e4(text):
    b = TOK.sub('', text, count=1)
    lead = len(b) - len(b.lstrip('\ufeff \r\n\t'))
    m = re.match(r'/\*.*?\*/', b[lead:], re.S)
    if m and m.group(0).count('\n') >= 7 and LIC.search(m.group(0)):
        return text[:len(text) - len(b)] + b[lead + m.end():].lstrip('\r\n')
    return text


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(fix_e4(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 24. `DA-E4-002` · E4 licence header · fix · rust, js-ts, java, cpp · source: code
1. **Disease:** E4 licence header · fix · rust, js-ts, java, cpp.
2. **Medicine:** delete a leading licence comment block when `package`/`import` follows it.
```python
RULE_ID = "DA-E4-002"
CODE = "E4"
ACTION = "fix"
LANGS = {'javascript', 'typescript', 'rust', 'cpp', 'java'}
ORIGIN = "code-java"  # pack whose medicine this came from
import html, re

LIC_HEAD = re.compile(r"\A(\s*)/\*.*?\*/[ \t]*\n", re.S)

LIC_WORDS = re.compile(r"licen[cs]e|permission is hereby granted", re.I)

def m4_strip_licence_header(t: str) -> str:
    m = LIC_HEAD.match(t)
    if not m or not LIC_WORDS.search(m.group()):
        return t
    if not re.match(r"\s*(package|import)\b", t[m.end():]):
        return t
    return t[m.end():].lstrip("\n")


def _std(out, text):
    # source result in the shared form: str -> fix/keep, None or True -> drop, False -> keep
    if out is None or out is True: return ("drop", text)
    if out is False: return ("keep", text)
    if isinstance(out, str): return ("fix" if out != text else "keep", out)
    action, new = out
    if action == "drop": return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m4_strip_licence_header(doc["text"]), doc["text"])
```
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 25. `DA-E4-006` · E4 licence header · fix · go, js-ts, java · source: code
1. **Disease:** E4 licence header · fix · go, js-ts, java.
2. **Medicine:** delete a licence comment block of 4+ lines in the header, a boxed `/* */` header, or a licence block at the end.
```python
RULE_ID = "DA-E4-006"
CODE = "E4"
ACTION = "fix"
LANGS = {'javascript', 'go', 'java', 'typescript'}
ORIGIN = "code-go"  # pack whose medicine this came from
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
3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** See original source and new per-pack evidence; not yet independently certified.

## 26. `DA-A4-002` · A4 replacement characters · fix+drop · aneeshads · source: English

1. **Disease:** A4 replacement characters. Documents labelled with it (fix or drop, all label sheets): dclm 1, fineweb-edu 1, nemotroncc 1, synth 0. Examples where this rule acts on a labelled document: no labelled document in these packs.
2. **Medicine:** Delete one or two replacement characters U+FFFD. Drop the document when it has three or more: the bytes were lost before release, and a text with many holes is not worth repairing.

```python
RULE_ID = "DA-A4-002"
CODE = "A4"
ACTION = "fix+drop"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
def medicine_a4(text):
    n = text.count("\ufffd")
    if n == 0:
        return ("keep", text)
    if n >= 3:
        return ("drop", text)
    return ("fix", text.replace("\ufffd", ""))


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_a4(doc["text"])
```

3. **Action:** fix+drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** The character that a U+FFFD stood for is gone, so a word can lose a letter. A long, good document with three holes is dropped whole.

**Decision (guideline 2):** KEEP, passes; no labelled case in these packs, and no other rule for this code passes.

## 27. `DA-B4-009` · B4 template and code junk · fix+drop · deepjyotisaha · source: English

1. **Disease:** B4 template and code junk. Documents labelled with it (fix or drop, all label sheets): dclm 25, fineweb-edu 8, nemotroncc 9, synth 36. Examples where this rule acts on a labelled document: `3e44df6a7ddb0098` (en-fineweb-edu): 41 characters removed, the first at offset 0.
2. **Medicine:** Two parts. - template junk (fix): remove what a web page left unfilled: "{{ title }}", "{% if … %}", "${name}", a code expression in backticks such as "`page.data.shortTitle || page.data.title`", "NaN" or "undefined" right after ":", "=" or "$", and a line that is only "undefined", "NaN" or "null"; - mostly code (drop): a line is a code line when it has at least two code tokens ("::", "->", "==", "&&", "{", "}", a line ending in ";", a line starting with "import", "def", "return", "public", "$ ", "Sub", …) and at least one for every six words; a table row "|cell||cell|" is never a code line. A document whose code lines hold more than half of its characters is dropped; - code snippets inside an article are kept on purpose (decided 27 Oct): tutorials and manual pages with a few lines of code are good training text, and cutting them risks removing real content.

```python
RULE_ID = "DA-B4-009"
CODE = "B4"
ACTION = "fix+drop"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # deepjyotisaha's medicine.md, medicine 4
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

# ----- B4 template and code junk ------------------------------------------------------------------------------
# Part 1, fix: template expressions left in the text by a web page that was not filled in.
B4_TEMPLATE = re.compile(
    r"\{\{[^{}\n]{0,80}\}\}"                          # {{ title }}
    r"|\{%[^\n]{0,80}?%\}"                            # {% if x %}
    r"|\$\{[^{}\n]{0,80}\}"                           # ${name}
    r"|`[\w.]+(?:\s*(?:\|\||&&)\s*[\w.]+)+`"          # `page.data.shortTitle || page.data.title`
    r"|(?<=[:=$])\s*(?:undefined|NaN)\b"              # Price: NaN, name=undefined
    r"|^[ \t]*(?:undefined|NaN|null)[ \t]*$", re.M)   # a line that is only "undefined"

# Part 2, drop: a document that is mostly code. A line is a code line when it carries at least B4_MIN_TOKENS code
# tokens and at least one for every B4_WORDS_PER_TOKEN words. The document is dropped when code lines hold more than
# B4_SHARE of its characters. Code in this pack is often flattened onto one line, so tokens are counted, not lines.
B4_CODE_TOKENS = re.compile(
    r"::|->|=>|==|!=|<=|>=|&&|\|\||\+\+|\+=|-=|\);|\)\s*\{|[{};]\s*$|\}"
    r"|^\s*(?:#include|import\s|from\s+\S+\s+import|def\s|class\s|public\s|private\s|static\s|void\s|return\b"
    r"|require\s|var\s|let\s|const\s|function\b|Sub\s|End Sub|Dim\s|\$\s|>>>\s|>\s)"
    r"|\b(?:End Sub|ByVal|As Integer|System\.out|printf|println)\b", re.M)

B4_MIN_TOKENS, B4_WORDS_PER_TOKEN, B4_SHARE = 2, 6, 0.5

TABLE_ROW = re.compile(r"^\s*\|.*\|\|")  # "|cell||cell|": a flattened table, not code

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

def b4_spans(text):
    """B4: the document is dropped if it is mostly code; otherwise template expressions are removed."""
    code = sum(e - s for s, e in b4_code_lines(text))
    if text.strip() and code > B4_SHARE * len(text.strip()):
        return [(0, len(text), "B4-mostly-code")]
    return [(m.start(), m.end(), "B4-template") for m in B4_TEMPLATE.finditer(text)]


def _std(out, text):
    # source result (spans) in the shared form, as clean() reads it: a "B4-mostly-code" span -> drop, else the spans go
    if out and out[0][2] == "B4-mostly-code": return ("drop", text)
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(b4_spans(doc["text"]), doc["text"])
```

3. **Action:** fix+drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** the medicine finds 1 of the 16 labelled cases. On the whole pack it changes 1 document. The mostly-code part drops no document of this pack: the most code-like one (document 10) has code in only 3% of its text. The other B4 documents are articles with a code snippet (a Visual Basic or Java listing, a Ruby example, a command manual page, a Haskell mailing-list post), kept on purpose; the readers' labels remain the record of them. Code flattened into a prose line by the original crawl is hard to tell from prose with symbols, which is why the drop needs more than half of the document to be code.

**Decision (guideline 2):** KEEP, passes and fixes 1 labelled rows that DA-B4-006 do not.

## 28. `DA-C3-004` · C3 truncated document · fix+drop · maheshsv · source: English

1. **Disease:** C3 truncated document. Documents labelled with it (fix or drop, all label sheets): dclm 103, fineweb-edu 34, nemotroncc 44, synth 50. Examples where this rule acts on a labelled document: `1ff0d9db2ef30443` (en-nemotroncc-synth): 33 characters removed, the first at offset 0; `2fc62e1bd955eae6` (en-nemotroncc-synth): 126 characters removed, the first at offset 0; `3e6bb6fb3b9b57a6` (en-nemotroncc-synth): 100 characters removed, the first at offset 0.
2. **Medicine:** take the passage before the first `Question:` line. (a) If its last line is a prose line (20 characters or more, not a bullet, not a `Key: value` line, not an `Answer:` line) and does not end with sentence punctuation or a closing bracket, cut that line back to its last sentence end, or remove the line if it has none. (b) If its first line starts with a lower-case letter and is 40 characters or more, cut it up to its first sentence end. Keep the QA block. The constants are the ones his sheet gives in words under the code. The guard (only documents with a `Question:` line, the form his rule was written for) is added here: without it the rule touches 7 en-dclm, 2 en-fineweb-edu and 5 en-nemotroncc gold documents.

```python
RULE_ID = "DA-C3-004"
CODE = "C3"
ACTION = "fix+drop"
LANGS = {"en", "eng"}
ORIGIN = "en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "maheshsv"  # maheshsv's medicine.md, medicine 1
import re

# the constants his sheet gives in words under the code
MIN_PROSE_LINE = 20
MIN_LEAD_LINE = 40
MIN_KEEP_CHARS = 200
QA_START = re.compile('^\\s*Question:', re.M)
TERMINAL = re.compile('[.!?…]+[\\"\'”’)\\]]*$|[)\\]]$|[\\"”’]$')
LIST_MARK = re.compile('^(?:[-*•–—]|\\d+[.)]|[a-z][.)])\\s')
KEY_VALUE_LINE = re.compile('^[^:\\n]{1,60}:\\s')
ANSWER_LINE = re.compile('^(?:Answer|A)\\s*[:.]|\\bAnswer:\\s')
SENTENCE_END = re.compile('[.!?…][\\"\'”’)\\]]*\\s')
CODE_LIKE = re.compile('[$/\\\\=(){}<>|]|--|\\bnpm\\b|\\bpip\\b|\\bgit\\b')

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


def _std(out, text):
    # source result (new_text or None, changed) in the shared form: None -> drop, else fix/keep by the text
    new, changed = out
    if new is None: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    if not QA_START.search(doc["text"]):  # added: only texts with a Question: section
        return ("keep", doc["text"])
    return _std(trim_truncation_both_ends(doc["text"]), doc["text"])
```

3. **Action:** fix+drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** 23 of the 47 labelled documents are out of reach: cuts inside the passage and the shortest orphan lines (`The Festival`, 12 characters) need a rejoin of consecutive chunks from the same URL, not a trim. Convention: a chunk that ends on a bare heading whose body sits in the next chunk is labelled C3 (orphan heading); the blind second reader called those complete, so expect disagreement on exactly those rows. False positives, constructed and confirmed: a first line that starts with a lower-case brand name (`iPhone …`, `eBay …`) and runs 40 characters or more loses its first sentence; a complete last line of 20 characters or more without a full stop (a line of verse, a slogan, a heading such as `Frequently Asked Questions About Taxes`, a line ending in an emoji) is removed, which for a heading is the intended orphan-heading behaviour; a roman-numeral or abbreviated item (`ii. Keep the soil moist`, `Dr.`, `e.g.`) can be cut back to the abbreviation because `SENTENCE_END` treats it as a sentence end. False negatives: a fragment on a `Key: value` line (`Note: the company said that it would`), a capitalised start fragment, a fragment that happens to end with a full stop. Lines ending in a closing quote or bracket and en-dash bullets are now accepted as complete, and a code-like first line (`npm install …`) is never trimmed; an earlier version trimmed a complete parenthetical (`35ebd1eaea214130`). None of the false positives occurred in the proxy gold set.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (24).

## 29. `DA-C3-005` · C3 truncated document · fix+drop · aneeshads · source: English

1. **Disease:** C3 truncated document. Documents labelled with it (fix or drop, all label sheets): dclm 103, fineweb-edu 34, nemotroncc 44, synth 50. Examples where this rule acts on a labelled document: `52422fff81211f50` (en-dclm): 57 characters removed, the first at offset 341; `3092ad2616653075` (en-fineweb-edu): 19 characters removed, the first at offset 2858; `c5d61b53df104867` (en-nemotroncc): 37 characters removed, the first at offset 206.
2. **Medicine:** When the text ends in a teaser mark (`[...]`, `[…]`, `(more…)`, `Read more`, `[Read More >>>]`, `Continue reading`), remove the mark and the cut sentence before it, back to the last full sentence. A bare `...` is not a mark: clean documents end with one as style. If nothing is left, drop the document.

```python
RULE_ID = "DA-C3-005"
CODE = "C3"
ACTION = "fix+drop"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

C3_MARK = re.compile(r"(?:\[(?:\.\.\.|…)\]|\(more(?:\.\.\.|…)\)|\[?\s*read more\s*(?:>>>|>>|»|→|\.\.\.|…)?\s*\]?"
                     r"|continue reading\s*(?:»|→|\.\.\.|…)?)\s*$", re.I)
SENTENCE_END = re.compile(r"[.!?…][\"'”’)\]]*(?=\s)")


def medicine_c3(text):
    t = text.rstrip()
    head, _, last = t.rpartition("\n")
    m = C3_MARK.search(last)
    if not m:
        return ("keep", text)
    body = last[: m.start()].rstrip()
    ends = list(SENTENCE_END.finditer(body + " "))
    kept = body[: ends[-1].end()].rstrip() if ends else ""
    new = (head + ("\n" + kept if kept else "")).strip("\n") if head else kept
    return ("drop", text) if not new.strip() else ("fix", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_c3(doc["text"])
```

3. **Action:** fix+drop.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** An article whose last words really are `read more` is cut. A teaser whose last sentence is complete keeps it: only the mark goes.

**Decision (guideline 2):** KEEP, passes and fixes 4 labelled rows that DA-C3-004, DA-C3-003 do not.

## 30. `DA-A1-003` · A1 invisible characters · fix · shekar-maker · source: English

1. **Disease:** A1 invisible characters. Documents labelled with it (fix or drop, all label sheets): dclm 12, fineweb-edu 1, nemotroncc 2, synth 0. Examples where this rule acts on a labelled document: `10355b4f94c87a2c` (en-dclm): 1 characters removed, the first at offset 40; `bbe410dfbf6e94fe` (en-nemotroncc): 43 characters removed, the first at offset 111; `11c3cd0e50856c3e` (en-dclm): 2 characters removed, the first at offset 0.
2. **Medicine:** delete ZWSP, BOM, soft hyphen and the bidi embedding/isolate marks. Keep ZWJ/ZWNJ.

```python
RULE_ID = "DA-A1-003"
CODE = "A1"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm"  # pack whose medicine this came from
AUTHOR = "shekar-maker"  # shekar-maker's medicine.md, medicine 1
import re

A1_RE = re.compile("[​﻿­‪-‮⁦-⁩]")
def m_a1(text): return A1_RE.sub("", text), False


def _std(out, text):
    # source result (new_text, dropped) in the shared form: dropped -> drop, else fix/keep by the text
    new, dropped = out
    if dropped: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m_a1(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** a soft hyphen that a typesetter placed on purpose is deleted too, which joins the word correctly (`never­ending` → `neverending`), so no damage. Bidi marks in genuinely mixed-direction text (Arabic or Hebrew quotes inside English) would be lost; none in this pack. The medicine does not touch U+200C/U+200D.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (12).

## 31. `DA-A2-007` · A2 control characters · fix · aneeshads · source: English

1. **Disease:** A2 control characters. Documents labelled with it (fix or drop, all label sheets): dclm 3, fineweb-edu 0, nemotroncc 0, synth 0. Examples where this rule acts on a labelled document: `5d1fd12b101321f0` (en-dclm): 1 characters removed, the first at offset 12605; `7b1d879aa4e04769` (en-dclm): 14 characters removed, the first at offset 1653; `94f537dcf85f69f8` (en-dclm): 57 characters removed, the first at offset 2494.
2. **Medicine:** Remove the control characters U+0000 to U+001F (except tab and newline) and U+007F to U+009F. A carriage return is a control character too: CRLF and a lone CR become a newline.

```python
RULE_ID = "DA-A2-007"
CODE = "A2"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

A2_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")


def medicine_a2(text):
    new = A2_CONTROL.sub("", text.replace("\r\n", "\n").replace("\r", "\n"))
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_a2(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A form feed used as a page break is removed, so the two pages run together. Every document with Windows line endings counts as changed.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (3).

## 32. `DA-A3-002` · A3 mojibake · fix · shekar-maker · source: English

1. **Disease:** A3 mojibake. Documents labelled with it (fix or drop, all label sheets): dclm 7, fineweb-edu 4, nemotroncc 2, synth 0. Examples where this rule acts on a labelled document: `5d1fd12b101321f0` (en-dclm): 1 characters removed, the first at offset 12604; `53dadf5fc6ee123a` (en-fineweb-edu): 16 characters removed, the first at offset 380; `7b1d879aa4e04769` (en-dclm): 104 characters removed, the first at offset 518.
2. **Medicine:** detect the double-decoding signatures, repair with `ftfy.fix_text`, and drop the document only if the signature is still dense after repair (the bytes are gone, not just mis-decoded).

```python
RULE_ID = "DA-A3-002"
CODE = "A3"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm"  # pack whose medicine this came from
AUTHOR = "shekar-maker"  # shekar-maker's medicine.md, medicine 2
import ftfy
import re

A3_RE = re.compile(r"â€[\x80-\xbf‘-™]?|Ã[\x80-\xbf\u0080-ÿ]|Â[\xa0-\xbf]|[\x80-\x9f]")
def m_a3(text):
    if not A3_RE.search(text): return text, False
    new = ftfy.fix_text(text)
    return new, len(A3_RE.findall(new)) * 1000 / max(len(new), 1) > 1.0


def _std(out, text):
    # source result (new_text, dropped) in the shared form: dropped -> drop, else fix/keep by the text
    new, dropped = out
    if dropped: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m_a3(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** the signature regex misses mojibake that went through a non-UTF-8 round trip, for example Cyrillic `й` standing in for `é` (`Pokйmon` in `68575a61a90990d5`, `Diffйrents` in `467b5c0aa1d13de8`) and symbol-font gibberish (`3dc93ffbd87ba839`): 3 of the 7 labelled documents are not touched. `ftfy` can in rare cases "repair" legitimate text that happens to look like mojibake (`Ã` followed by a letter in Portuguese); the gold run will show whether that happens in English.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (5).

## 33. `DA-A5-001` · A5 wrong normal form · fix · aneeshads · source: English

1. **Disease:** A5 wrong normal form. Documents labelled with it (fix or drop, all label sheets): dclm 3, fineweb-edu 0, nemotroncc 0, synth 0. Examples where this rule acts on a labelled document: `10355b4f94c87a2c` (en-dclm): 2 characters removed, the first at offset 650; `68575a61a90990d5` (en-dclm): 12 characters removed, the first at offset 992; `c64a732a64b1ce8b` (en-dclm): 1 characters removed, the first at offset 5013.
2. **Medicine:** Normalise the text to NFC, the form the lab uses.

```python
RULE_ID = "DA-A5-001"
CODE = "A5"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import unicodedata


def medicine_a5(text):
    new = unicodedata.normalize("NFC", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_a5(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** The bytes of decomposed text change, not its look. A text about Unicode normalisation loses the difference between its examples.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (3).

## 34. `DA-B1-002` · B1 HTML entities · fix · aneeshads · source: English

1. **Disease:** B1 HTML entities. Documents labelled with it (fix or drop, all label sheets): dclm 1, fineweb-edu 0, nemotroncc 0, synth 0. Examples where this rule acts on a labelled document: `1992526bd6e98869` (en-dclm): 28 characters removed, the first at offset 1500.
2. **Medicine:** Decode the common HTML entities (`&amp;`, `&nbsp;`, `&quot;`, `&lt;`, `&gt;`, dashes, quotes, `&#NNN;`, `&#xHH;`). `&nbsp;` becomes a plain space.

```python
RULE_ID = "DA-B1-002"
CODE = "B1"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import html
import re

B1_ENTITY = re.compile(r"&(?:amp|nbsp|quot|apos|lt|gt|mdash|ndash|hellip|rsquo|lsquo|rdquo|ldquo|copy|reg|trade"
                       r"|#\d{2,6}|#x[0-9a-fA-F]{2,5});")


def medicine_b1(text):
    new = B1_ENTITY.sub(lambda m: html.unescape(m.group()).replace("\xa0", " "), text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_b1(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A text that shows entities on purpose (an HTML tutorial) is changed. An entity that is not on the list stays.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (1).

## 35. `DA-B2-002` · B2 HTML tags · fix · aneeshads · source: English

1. **Disease:** B2 HTML tags. Documents labelled with it (fix or drop, all label sheets): dclm 3, fineweb-edu 1, nemotroncc 1, synth 0. Examples where this rule acts on a labelled document: `6d1051dc3ca46585` (en-dclm): 92 characters removed, the first at offset 2391; `a845e6c52e035cbb` (en-fineweb-edu): 20 characters removed, the first at offset 256.
2. **Medicine:** Remove common HTML tags (`<div>`, `<p>`, `<br/>`, `<span ...>`, `<li>`, `<strong>`, ...) when the text has at least two of them and is not about HTML (no code fence, `class=`, `<!DOCTYPE`, or the words html, tag, element). A single tag is often a mention, not markup.

```python
RULE_ID = "DA-B2-002"
CODE = "B2"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

B2_TAG = re.compile(r"</?(?:div|span|p|br|li|ul|ol|img|table|tr|td|th|tbody|thead|strong|em|font|iframe|script|style|center|hr)"
                    r"(?:\s[^<>]{0,200})?\s*/?>", re.I)
B2_ABOUT_HTML = re.compile(r"```|\bclass\s*=|<!DOCTYPE|\bhtml\b|\btag\b|\belement\b", re.I)


def medicine_b2(text):
    if B2_ABOUT_HTML.search(text) or len(B2_TAG.findall(text)) < 2:
        return ("keep", text)
    new = re.sub(r"[ \t]{2,}", " ", B2_TAG.sub(" ", text))
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_b2(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A text that quotes tags as examples without those words loses them. `<br>` and `<p>` become a space, not a line break, so lines can run together.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (2).

## 36. `DA-B3-009` · B3 ghost chat markers · fix · aneeshads · source: English

1. **Disease:** B3 ghost chat markers. Documents labelled with it (fix or drop, all label sheets): dclm 0, fineweb-edu 0, nemotroncc 0, synth 0. Examples where this rule acts on a labelled document: no labelled document in these packs.
2. **Medicine:** Remove chat-template tokens: `<|im_start|>`, `<|endoftext|>`, `<|eot_id|>` and the like, `[INST]`, `<<SYS>>`, `<think>`, and a line that starts with `### Assistant:`, `### User:`, `### Human:` or `### System:`. DISEASES.md calls B3 the most dangerous disease.

```python
RULE_ID = "DA-B3-009"
CODE = "B3"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

B3_MARKER = re.compile(r"<\|(?:im_start|im_end|endoftext|system|user|assistant|eot_id|begin_of_text|end_of_text"
                       r"|start_header_id|end_header_id|fim_prefix|fim_middle|fim_suffix)\|>|\[/?INST\]|<</?SYS>>|</?think>"
                       r"|^\s*###\s*(?:Assistant|Human|User|System)\s*:", re.I | re.M)


def medicine_b3(text):
    new = B3_MARKER.sub("", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_b3(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** An article about prompting a language model loses its examples. A real forum page with `### User:` headings loses those headings.

**Decision (guideline 2):** KEEP, passes; no labelled case in these packs, and no other rule for this code passes.

## 37. `DA-B4-006` · B4 template and code junk · fix · shekar-maker · source: English

1. **Disease:** B4 template and code junk. Documents labelled with it (fix or drop, all label sheets): dclm 25, fineweb-edu 8, nemotroncc 9, synth 36. Examples where this rule acts on a labelled document: `6da64e1f3aa0f61c` (en-dclm): 379 characters removed, the first at offset 6275; `6011e88c8cc9c77d` (en-nemotroncc-synth): 13 characters removed, the first at offset 1353; `e3fba14beec00b2b` (en-dclm): 28 characters removed, the first at offset 0.
2. **Medicine:** delete the residue tokens, not the document.

```python
RULE_ID = "DA-B4-006"
CODE = "B4"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm"  # pack whose medicine this came from
AUTHOR = "shekar-maker"  # shekar-maker's medicine.md, medicine 3
import re

B4_RES = [re.compile(r"\b[\w-]+\.(?:jpe?g|png|gif|webp)(?:\s*-\s*[\d.]+\s*K)?\b", re.I),
          re.compile(r"\bfbq\([^)]*\);?|\bgtag\([^)]*\);?|\bga\('send'[^)]*\);?"),
          re.compile(r"\{\{\s*[\w.]+\s*\}\}|\$\{[^}]{1,40}\}"),
          re.compile(r"^(?:undefined|NaN|null)\s*$", re.M)]
def m_b4(text):
    new = text
    for rx in B4_RES: new = rx.sub("", new)
    return re.sub(r"[ \t]{2,}", " ", new) if new != text else text, False


def _std(out, text):
    # source result (new_text, dropped) in the shared form: dropped -> drop, else fix/keep by the text
    new, dropped = out
    if dropped: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m_b4(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** recall is low (2 of 23 labelled documents): most B4 in this pack is placeholder text glued into words (`holder maleChase`, `Lance-Earl-Ladn-C-trucsLance`) or an unrendered theme string, which no regex can separate from prose. A tutorial that legitimately names `image.png` loses that filename.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (3).

## 38. `DA-C1-006` · C1 boilerplate · fix · aneeshads · source: English

1. **Disease:** C1 boilerplate. Documents labelled with it (fix or drop, all label sheets): dclm 389, fineweb-edu 306, nemotroncc 43, synth 76. Examples where this rule acts on a labelled document: `010283c475f53e9d` (en-dclm): 34 characters removed, the first at offset 804; `06bacb0867128c27` (en-fineweb-edu): 49 characters removed, the first at offset 921; `494be9a546e5e0f2` (en-nemotroncc): 16 characters removed, the first at offset 0.
2. **Medicine:** Remove a line of 8 words or fewer that starts with a site phrase: shekar-maker's list (share, follow us, related posts, read more, posted by, tags:, log in, subscribe, copyright, privacy policy, ...) and more found in the labels (print recipe, account login, most popular, you may also like, cookie banners, previous/next article, return to, back to, photo credit, ...). Only the lines go: the rest of the text, blank lines included, stays as it was. If nothing is left, drop the document. Unlike `DA-C1-002`, which also collapses every run of blank lines, it changes no document in which it removes no line.

```python
RULE_ID = "DA-C1-006"
CODE = "C1"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

C1_SITE = re.compile(r"^(?:share (?:on|this|via)|tweet|follow (?:us|me|@)|like us|related (?:posts?|articles?|links?|games?)"
    r"|read more|click (?:here|to)|leave a (?:comment|reply)|post(?:ed)? (?:a )?comment|no comments?|\d+ comments?"
    r"|posted (?:by|on|in)|filed under|tags?:|categor(?:y|ies):?|labels?:|skip to|you are here|home\s*[>»|]"
    r"|log ?in|sign (?:in|up)|register|subscribe|newsletter|all rights reserved|copyright|©|privacy policy"
    r"|terms of (?:use|service)|powered by|back to top|print this|email this|previous post|next post|older post"
    r"|newer post|view (?:all|profile)|contact us|advertisement|sponsored|links to this post|<< home)", re.I)
C1_MORE = re.compile(r"^(?:print recipe|account login|most popular|you may also like|related (?:documents|stories|items|videos)"
    r"|previous article|next article|share this (?:article|story|page|post)|pin it|whatsapp|facebook|twitter|linkedin|pinterest"
    r"|accept(?: all)? cookies|this (?:web)?site uses cookies|cookie (?:policy|settings)|jump to|report abuse|permalink"
    r"|reply$|add (?:a )?comment|(?:\d+ )?responses?$|leave a response|recent posts|popular posts|archives?$|search for:"
    r"|search$|menu$|navigation$|main menu|toggle navigation|scroll to top|go to top|loading\.\.\.)"
    r"|^(?:return to|back to)\b|^anonymous said\b|^(?:photo|image|picture) (?:credit|courtesy|by)\b|^for more information\b"
    r"|^this (?:page|entry|post) (?:was|is)\b|^see more\b|^more (?:info|details|stories|news)\b", re.I)


def medicine_c1(text):
    lines = text.split("\n")
    keep = [ln for ln in lines
            if not (ln.strip() and len(ln.split()) <= 8 and (C1_SITE.search(ln.strip()) or C1_MORE.search(ln.strip())))]
    if len(keep) == len(lines):
        return ("keep", text)
    new = "\n".join(keep).strip("\n")
    return ("drop", text) if not new.strip() else ("fix", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_c1(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A real short line that starts with one of the phrases (a heading `Contact us`, `Register now for the course`) is removed. A site line of more than 8 words, or site text inside a longer line, is missed.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (193).

## 39. `DA-C2-002` · C2 repeated lines · fix · shekar-maker · source: English

1. **Disease:** C2 repeated lines. Documents labelled with it (fix or drop, all label sheets): dclm 38, fineweb-edu 6, nemotroncc 22, synth 1. Examples where this rule acts on a labelled document: `1e13b455581e96ca` (en-dclm): 87 characters removed, the first at offset 4105; `0e3e6fdfe3d7d698` (en-nemotroncc): 100 characters removed, the first at offset 8989; `d7ece2193f620b9b` (en-nemotroncc-synth): 46 characters removed, the first at offset 285.
2. **Medicine:** a line of 20+ characters that appears 3 or more times is kept once; if the repeated lines are more than 30% of the non-empty lines the document is dropped.

```python
RULE_ID = "DA-C2-002"
CODE = "C2"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm"  # pack whose medicine this came from
AUTHOR = "shekar-maker"  # shekar-maker's medicine.md, medicine 5
from collections import Counter

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


def _std(out, text):
    # source result (new_text, dropped) in the shared form: dropped -> drop, else fix/keep by the text
    new, dropped = out
    if dropped: return ("drop", text)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(m_c2(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** a refrain in a poem or song, a repeated stage direction in a play, or a repeated table header is collapsed to one copy. Short repeated lines (under 20 characters, e.g. `Post a Comment`) are left to Medicine 4.

**Decision (guideline 2):** KEEP, passes and fixes 7 labelled rows that DA-C2-003 do not.

## 40. `DA-C2-003` · C2 repeated lines · fix · aneeshads · source: English

1. **Disease:** C2 repeated lines. Documents labelled with it (fix or drop, all label sheets): dclm 38, fineweb-edu 6, nemotroncc 22, synth 1. Examples where this rule acts on a labelled document: `28bd69b4ed987643` (en-dclm): 92 characters removed, the first at offset 5172; `0e3e6fdfe3d7d698` (en-nemotroncc): 153 characters removed, the first at offset 8989; `7638c21903d9cd96` (en-dclm): 54 characters removed, the first at offset 2020.
2. **Medicine:** Remove the later copies of a paragraph (40 characters or more, compared with spaces collapsed) that already appeared in the document. The first copy stays where it was.

```python
RULE_ID = "DA-C2-003"
CODE = "C2"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re


def medicine_c2(text):
    parts = re.split(r"(\n\s*\n)", text)
    seen, out = set(), []
    for i, part in enumerate(parts):
        flat = " ".join(part.split())
        if i % 2 == 0 and len(flat) >= 40:
            if flat in seen:
                if out:
                    out.pop()  # the blank line before the copy
                continue
            seen.add(flat)
        out.append(part)
    new = "".join(out)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_c2(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A refrain in a poem or a song, or a quotation repeated on purpose, loses its later copies.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (14).

## 41. `DA-C2-004` · C2 repeated lines · fix · aneeshads · source: English

1. **Disease:** C2 repeated lines. Documents labelled with it (fix or drop, all label sheets): dclm 38, fineweb-edu 6, nemotroncc 22, synth 1. Examples where this rule acts on a labelled document: `1e13b455581e96ca` (en-dclm): 29 characters removed, the first at offset 4105; `b888d78a21618c96` (en-fineweb-edu): 38 characters removed, the first at offset 5207; `8fa9168e8da3a2d4` (en-dclm): 64 characters removed, the first at offset 440.
2. **Medicine:** Keep one of the same line (15 characters or more) written two or more times in a row.

```python
RULE_ID = "DA-C2-004"
CODE = "C2"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
def medicine_c2(text):
    out = []
    for ln in text.split("\n"):
        if out and len(ln.strip()) >= 15 and ln.strip() == out[-1].strip():
            continue
        out.append(ln)
    new = "\n".join(out)
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return medicine_c2(doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A line doubled on purpose, for emphasis or in verse, loses its copy.

**Decision (guideline 2):** KEEP, passes and fixes 1 labelled rows that DA-C2-003, DA-C2-002 do not.

## 42. `DA-C3-003` · C3 truncated document · fix · deepjyotisaha · source: English

1. **Disease:** C3 truncated document. Documents labelled with it (fix or drop, all label sheets): dclm 103, fineweb-edu 34, nemotroncc 44, synth 50. Examples where this rule acts on a labelled document: `4b96b283ee061cdb` (en-dclm): 32 characters removed, the first at offset 4838; `2067313a5e000336` (en-fineweb-edu): 161 characters removed, the first at offset 2427; `1c6092da9a709c2e` (en-nemotroncc): 100 characters removed, the first at offset 304.
2. **Medicine:** Remove the last line of a document when it is an unfinished sentence: the last non-empty line has at least six words and ends on a word no complete sentence ends on (for example "the", "of", "to", "visit", "they") or on ":" or ",", and the C1 medicine does not already remove it. The document then ends at its last complete line. Run after the C1 medicine. Two broader rules were tested and rejected (25 Oct): "the last line ends with any lower-case letter" also removed titles and author notes at the end of good documents, and "the text starts with a lower-case letter" also removed dictionary entries that start in lower case. Those cases stay with the readers. Without the pack's line counts (harm_test.py passes only the document), the scorer cannot tell which lines repeat across the pack: the author reports a different result on 7 of 500 documents then.

```python
RULE_ID = "DA-C3-003"
CODE = "C3"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # deepjyotisaha's medicine.md, medicine 2
import math

import re

# ----- C1 phrase rules -----
SHORT = 120

START_LINES = 3

C1_RULES = {
    'C1-teaser-line': (re.compile('(?i)^\\W{0,6}(?:read more|continue reading|explore further|click here|learn more about|to learn more about|find out more|for further information|view all\\b|view larger map|show summary details|share this|choose a citation style|call now)'), 'anywhere'),
    'C1-teaser-inline': (re.compile('(?i)(?:\\[\\.\\.\\.\\]\\s*read more\\.?|\\s+continue reading\\s*→?|\\s*\\bread more\\s*»?|(?<=[.!?])\\s*learn more about [^.!?]{0,60})\\s*$'), 'inline'),
    'C1-byline-alone': (re.compile("^[Bb]y\\s+[A-Z][\\w.'-]+(?:\\s+[A-Z][\\w.'-]+){0,3}$"), 'anywhere'),
    'C1-byline': (re.compile("(?i)^(?:by\\s+[A-Z][\\w.'-]+(?:\\s+[A-Z][\\w.'-]+){0,3}\\b.*|from:\\s.*|posted:?\\s.*|updated\\s.*|published\\s.*|contributed by\\s.*|written by\\s.*|latest revision\\s.*|(?:(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\\s+)?(?:(?:January|February|March|April|May|June|July|August|September|October|November|December)\\s+\\d{1,2},?\\s+\\d{4}|\\d{1,2}\\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\\s+\\d{4})\\.?)$"), 'start'),
    'C1-credit': (re.compile("(?i)^\\W{0,3}(?:©|copyright\\b|\\(c\\)\\s*\\d{4}|source:|article source:|website:|courtesy:|photo:|image:|editor'?s note:|editor:|correction|published\\s+\\d{1,2}\\s)"), 'anywhere'),
    'C1-navigation': (re.compile('^(?=.{0,160}$)(?:[^|:»\\n]+\\s(?:\\||:|»)\\s){3,}[^|:»\\n]+$|^.*»\\s*\\|\\|.*»\\s*\\|?$'), 'anywhere'),
    'C1-promotion': (re.compile("(?i)^\\W{0,3}(?:paperback:|hardcover:|publisher:|language:\\s*\\w+$|isbn-1[03]:|product dimensions:|indian edition also available|we've sent an email with your order|help support .{0,40} and get|don't forget to check out|click on the .{0,30} to follow me|subscribe to (?:our|the) newsletter)"), 'anywhere'),
}

# ----- C1 line scorer: feature patterns -----
LINK_WORDS = re.compile('(?i)\\b(?:read more|click|view (?:all|full|larger|more|current|details|profile|cart)|share|follow|subscribe|sign up|log ?in|register|download|visit|learn more|find out|contact|call now|order|buy|shop|newsletter|comment|rate|advertis|explore further|continue reading|related|see also|tags?)\\b')

URL = re.compile('(?i)https?://|www\\.|\\.(?:com|org|net|edu|gov|co\\.uk)\\b')

COPY = re.compile('(?i)©|\\bcopyright\\b|all rights reserved')

DATE = re.compile('(?i)\\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\\.?\\s+\\d{1,2},?\\s+\\d{4}\\b|\\b\\d{1,2}\\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\\s+\\d{4}\\b|\\b(?:19|20)\\d{2}\\b')

SEPARATORS = re.compile('\\s\\|\\s|\\|\\||»|\\s:\\s|\\s/\\s')

BYLINE = re.compile("^(?:[Bb]y\\s+[A-Z][\\w.'-]+(?:\\s+[A-Z][\\w.'-]+)*(?:,|$)|(?i:from|posted|updated|published|written by|contributed by|photo|image|source|courtesy)\\s*:|(?i:posted|updated|published)\\s+(?:on\\s+)?\\d)")

KEY_VALUE = re.compile('^[-•*]?\\s*[A-Z][\\w -]{1,25}:\\s+\\S')

FULL_DATE = re.compile('(?i)\\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\\.?\\s+\\d{1,2},?\\s+\\d{4}\\b|\\b\\d{1,2}\\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\\s+\\d{4}\\b|\\b\\d{1,2}/\\d{1,2}/\\d{2,4}\\b')

MENU_SEP = re.compile('[A-Za-z]\\s(?:\\||»|:)\\s[A-Za-z]|»')

GATE_WORDS = re.compile('(?i)^back to\\b|\\bphoto credit|^contributors?:|^last (?:reviewed|updated)\\b|^article id:|community guidelines|customer reviews')

GATE_REPEAT = 3

END_PUNCT = '!").?’”'

# ----- C1 line scorer: trained weights (c1tune.py, 25 Oct) -----
THRESHOLD = 0.97

B = -1.5507480049898266

WEIGHTS = [
    (-0.30147706176797767, 0.34978991596638653, 0.4769034824871978),  # short_60
    (0.06330518850698173, 0.5189075630252101, 0.4996423771656242),  # short_120
    (-1.0656012937788908, 4.7404142964275575, 1.1558346577519014),  # log_length
    (-0.3355137904314126, 0.6646533613445378, 0.4721115032936311),  # ends_sentence
    (0.6530189039369719, 0.1951155462184874, 0.39628962973426646),  # first_3
    (0.7681479054606566, 0.22163865546218486, 0.4153492057267116),  # last_3
    (0.20484508311329477, 0.5134065615572345, 0.326095004751047),  # rel_position
    (0.6020056915946318, 0.08403361344537816, 0.34111980628726096),  # link_words
    (0.34674133673120544, 0.01365546218487395, 0.11605598118797099),  # url
    (0.21358949882641426, 0.010766806722689076, 0.103203114304226),  # copyright
    (0.39027972267177646, 0.09243697478991597, 0.2896418151111693),  # date
    (1.1117791213605204, 0.03571428571428571, 0.3472365619951357),  # separators
    (0.8316447868841712, 0.22243452191582483, 0.2374418810653674),  # capitalised
    (-0.26558805523900925, 0.22006302521008403, 0.4142888979613596),  # bullet
    (0.6554049595691624, 0.011029411764705883, 0.10444024152457473),  # byline_start
    (0.2809341884722034, 0.004732622556344163, 0.07264101150947193),  # repeated_docs
    (0.5335299651420944, 0.014400859555666128, 0.04813878573134519),  # digits
    (-0.1330440782326233, 0.07589285714285714, 0.26482660724934853),  # few_words
    (-0.5184152439383056, 0.3434873949579832, 0.47487240961410254),  # next_is_paragraph
    (0.004603588072813513, 0.3542542016806723, 0.4782866956427239),  # prev_is_paragraph
]

MAX_LINE = 200

MAX_SHARE = 0.2

MIN_DROP_CHARS = 300

EXPAND_FACTOR = 0.5

# ----- C3 -----
DANGLING = ['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'could', 'for', 'from', 'had', 'has', 'have', 'he', 'her', 'his', 'i', 'if', 'in', 'including', 'into', 'is', 'it', 'its', 'more', 'most', 'not', 'of', 'on', 'or', 'our', 'see', 'she', 'such', 'than', 'that', 'the', 'their', 'these', 'they', 'this', 'those', 'to', 'very', 'visit', 'was', 'we', 'were', 'when', 'which', 'while', 'who', 'whose', 'will', 'with', 'would', 'you', 'your']

def _merge(spans):
    """Overlapping spans joined into one, keeping the rule of the first."""
    out = []
    for s, e, rule in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(e, out[-1][1]), out[-1][2])
        else:
            out.append((s, e, rule))
    return out

def _raw_lines(text):
    """(offset, line) for every line, empty ones included."""
    pos = 0
    for line in text.split("\n"):
        yield pos, line
        pos += len(line) + 1

def _lines(text):
    """(offset of the stripped line, stripped line) for every non-empty line."""
    out = []
    for pos, raw in _raw_lines(text):
        s = raw.strip()
        if s:
            out.append((pos + raw.index(s), s))
    return out

def _norm(line):
    return " ".join(line.lower().split())

def c1_phrase_spans(text):
    """(start, end, rule) of every span the phrase rules remove."""
    spans, k = [], 0
    for off, line in _raw_lines(text):
        stripped = line.strip()
        if not stripped:
            continue
        k += 1
        for rule, (rx, where) in C1_RULES.items():
            if where == "inline":
                m = rx.search(line)
                if m and len(stripped) > SHORT:
                    spans.append((off + m.start(), off + m.end(), rule))
                    break
                continue
            if where == "start" and k > START_LINES:
                continue
            limit = {"C1-navigation": 160, "C1-promotion": 220}.get(rule, SHORT)
            if len(stripped) > limit or not rx.search(stripped):
                continue
            spans.append((off, off + len(line), rule))
            break
    return spans

def line_features(text, repetition=None):
    """The 20 features of every non-empty line, in the order of FEATURES.
    repetition: optional {normalised line: number of documents containing it}; without it every line counts once."""
    repetition = repetition or {}
    lines = _lines(text)
    n = len(lines)
    feats = []
    for k, (off, s) in enumerate(lines):
        words = s.split()
        caps = sum(1 for w in words if w[:1].isupper()) / max(1, len(words))
        nxt = len(lines[k + 1][1]) if k + 1 < n else 0
        prv = len(lines[k - 1][1]) if k > 0 else 0
        feats.append([
            float(len(s) <= 60), float(len(s) <= 120), math.log(1 + len(s)), float(s[-1] in END_PUNCT),
            float(k < 3), float(k >= n - 3), k / max(1, n - 1),
            float(len(LINK_WORDS.findall(s))), float(bool(URL.search(s))), float(bool(COPY.search(s))),
            float(bool(DATE.search(s))), float(len(SEPARATORS.findall(s))), caps,
            float(s[:1] in "-•*|►>"), float(bool(BYLINE.match(s))),
            math.log(max(1, repetition.get(_norm(s), 1))), sum(ch.isdigit() for ch in s) / len(s),
            float(len(words) <= 3), float(nxt > 200), float(prv > 200),
        ])
    return lines, feats

def line_score(x):
    """The probability that a line is boilerplate: logistic regression on standardised features."""
    z = B + sum(w * (v - m) / s for v, (w, m, s) in zip(x, WEIGHTS))
    return 1 / (1 + math.exp(-z))

def gate_signal(line):
    """An explicit boilerplate signal: link words, web address, ©, a full date, a byline or menu separators.
    A table row "|cell||cell|" without link words is content."""
    if line.startswith("|") and "||" in line and "»" not in line and not LINK_WORDS.search(line):
        return False
    return bool(LINK_WORDS.search(line) or URL.search(line) or COPY.search(line) or FULL_DATE.search(line)
                or BYLINE.match(line) or MENU_SEP.search(line))

def _signal(line, repetition):
    """gate_signal, plus the gate additions of 27 Oct: GATE_WORDS, and a line found in GATE_REPEAT or more
    documents of the pack (needs the pack's repetition counts; without them this part never fires)."""
    return (gate_signal(line) or bool(GATE_WORDS.search(line))
            or repetition.get(_norm(line), 1) >= GATE_REPEAT)

def c1_spans(text, repetition=None):
    """The C1 medicine. Returns (spans to remove, flagged_for_drop)."""
    rep = repetition or {}
    phrase = c1_phrase_spans(text)
    phrase_hits = {s for s, _, _ in phrase}
    lines, X = line_features(text, repetition)
    scores = [line_score(x) for x in X]
    inline = {k for k, (o, s) in enumerate(lines)
              if any(o <= a < o + len(s) for a, _, r in phrase if r == "C1-teaser-inline")}
    remove = {k for k, (off, s) in enumerate(lines) if off in phrase_hits}
    remove |= {k for k, sc in enumerate(scores)
               if sc >= THRESHOLD and len(lines[k][1]) <= MAX_LINE and _signal(lines[k][1], rep) and k not in inline}
    changed = True
    while changed:                          # block expansion
        changed = False
        for k in sorted(remove):
            for j in (k - 1, k + 1):
                if 0 <= j < len(lines) and j not in remove and j not in inline and len(lines[j][1]) <= 120 \
                        and lines[j][1][-1] not in END_PUNCT and scores[j] >= EXPAND_FACTOR * THRESHOLD \
                        and (_signal(lines[j][1], rep) or KEY_VALUE.match(lines[j][1])):
                    remove.add(j)
                    changed = True
    spans = [(lines[k][0], lines[k][0] + len(lines[k][1]), "C1-phrase" if lines[k][0] in phrase_hits else
              "C1-scorer") for k in sorted(remove)]
    spans += [sp for sp in phrase if sp[2] == "C1-teaser-inline"]
    removed = len({p for s, e, _ in spans for p in range(s, e)})
    if text and removed > MAX_SHARE * len(text) and removed > MIN_DROP_CHARS:
        return [], True                      # too much would go: drop the document instead
    return spans, False

def c3_spans(text, repetition=None):
    """The C3 medicine: remove the last line when it is an unfinished sentence and C1 does not remove it."""
    lines = [(o, l) for o, l in _raw_lines(text) if l.strip()]
    if not lines:
        return []
    off, last = lines[-1]
    c1, flagged = c1_spans(text, repetition)
    if flagged:
        c1 = [(0, len(text), "C1-drop-flag")]
    if any(s < off + len(last) and e > off for s, e, _ in c1):
        return []
    s = last.rstrip()
    words = s.split()
    if len(words) >= 6 and (s[-1] in ":," or words[-1].lower() in DANGLING):
        return [(off, off + len(last), "C3-unfinished-end")]
    return []


def _std(out, text):
    # source result (spans to remove) in the shared form, as clean() removes them
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(c3_spans(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** the medicine finds 2 of the 14 labelled cases. It misses cut-offs that do not end on a dangling word or a colon (for example a teaser ending in "..."), and documents that start in the middle of a sentence. Some labelled cut-offs are removed by the C1 medicine first, because their last line is also a link ("…For more information about the collection, visit"). On the whole pack it changes 4 documents; checked on 25 Oct, one of them is a title ending in "On" ("The Saga Lives On"), which is a wrong removal.

**Decision (guideline 2):** KEEP, passes and fixes 14 labelled rows that DA-C3-004 do not.

## 43. `DA-C5-002` · C5 keyword lists and SEO spam · fix · aneeshads · source: English

1. **Disease:** C5 keyword lists and SEO spam. Documents labelled with it (fix or drop, all label sheets): dclm 61, fineweb-edu 16, nemotroncc 27, synth 7. Examples where this rule acts on a labelled document: `4604f40da35906cc` (en-fineweb-edu): 69 characters removed, the first at offset 40.
2. **Medicine:** Remove a line that is a tag list: it starts with `Tags:`, `Tag:`, `Keywords:`, `Tagged with:`, `Topics:` or `Filed under:`. Lists of commas or pipes without such a word are left alone: in clean documents they are stat lines, ingredient lists and genre lists.

```python
RULE_ID = "DA-C5-002"
CODE = "C5"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-dclm, en-fineweb-edu, en-nemotroncc, en-nemotroncc-synth"  # pack whose medicine this came from
AUTHOR = "aneeshads"  # new in this sheet
import re

C5_PREFIX = re.compile(r"^(?:tags?|keywords?|tagged(?: with| in)?|topics?|filed under)\s*:", re.I)


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
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** A real heading such as `Topics:` before a list in an article is removed. Keyword spam without the prefix is missed.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (1).

## 44. `DA-F1-003` · F1 personal data · fix · deepjyotisaha · source: English

1. **Disease:** F1 personal data. Documents labelled with it (fix or drop, all label sheets): dclm 13, fineweb-edu 8, nemotroncc 7, synth 2. Examples where this rule acts on a labelled document: `1992526bd6e98869` (en-dclm): 169 characters removed, the first at offset 216; `051b7e2ff46aa18c` (en-fineweb-edu): 20 characters removed, the first at offset 3580; `17f4af14c04c9fde` (en-nemotroncc): 14 characters removed, the first at offset 824.
2. **Medicine:** Remove every email address, phone number and ID number, together with a label in front of it ("Tel:", "Fax:", "Phone:"). Nothing is put in its place: a placeholder such as "[phone]" would teach the model to write our own made-up token (decided 27 Oct). The patterns are the scanner's F1 patterns: - emails, except FineWeb's own example.com replacements; - phone numbers: international ("+44 …"), US ("(307) 234-6765", "855-305-3903"), UK and Indian numbers that start with 0, and any number after a Tel, Fax, Phone or Mobile label; - ID numbers: US social security numbers, PAN numbers, and card and Aadhaar numbers only when their check digit is valid (the Luhn test for cards, the Verhoeff test for Aadhaar), so a run of years or a product code is not taken for one; - not personal data: a match inside a journal reference, an ISBN, a DOI or a run of years is left alone; - a line with no letter or digit left after the removal ("Tel: … / Fax: …") is removed whole.

```python
RULE_ID = "DA-F1-003"
CODE = "F1"
ACTION = "fix"
LANGS = {"en", "eng"}
ORIGIN = "en-fineweb-edu"  # pack whose medicine this came from
AUTHOR = "deepjyotisaha"  # deepjyotisaha's medicine.md, medicine 3
import re

# ----- F1 personal data -----------------------------------------------------------------------------------
# The scanner's F1 patterns (dictionaries.py, 24 Oct). (kind, pattern, check): check is the check-digit test an ID
# number must pass. A labelled number ("Tel: 0123 456 789") is removed together with its label.
F1_PATTERNS = [
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"), None),
    ("labelled-number", re.compile(r"(?i)\b(?:tel|telephone|phone|fax|mobile|mob|cell)\b\.?\s*(?:no\.?\s*)?:?\s*"
                                   r"[+(]?\d[\d ().-]{5,}\d"), None),
    ("phone", re.compile(r"\+\d[\d\s().-]{7,18}\d"), None),
    ("phone", re.compile(r"\(\d{3}\)\s?\d{3}[-.\s]\d{4}\b"), None),
    ("phone", re.compile(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b"), None),
    ("phone", re.compile(r"\b0\d{2,4}[\s-]?\d{3,4}[\s-]?\d{3,4}\b"), None),
    ("us-ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), None),
    ("card", re.compile(r"\b(?:\d[ -]?){12,18}\d\b"), "luhn"),
    ("aadhaar", re.compile(r"\b\d{4}\s\d{4}\s\d{4}\b"), "verhoeff"),
    ("pan", re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b"), None),
]

F1_EMAIL_SKIP = ("example.com", "example.org", "example.net")  # FineWeb's own replacements, not personal data

# A match that overlaps one of these is not personal data: journal reference, ISBN, DOI, run of years
F1_NOT = [
    re.compile(r"\d+\s*\(\d+\)\s*:\s*\d+\s*[-–]\s*\d+"),
    re.compile(r"(?i)\bISBN(?:-1[03])?:?\s*[\dXx-]{10,17}|\b97[89]-\d{1,5}-\d{1,7}-\d{1,7}-[\dXx]\b"),
    re.compile(r"\b10\.\d{4,9}/\S+"),
    re.compile(r"\b(?:1[89]|20)\d{2}(?:\s+(?:1[89]|20)\d{2}){2,}\b"),
]

_VERHOEFF_D = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
               [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
               [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
               [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

_VERHOEFF_P = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
               [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
               [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

def _luhn(digits):
    """The check-digit test of payment card numbers."""
    total = 0
    for k, ch in enumerate(reversed(digits)):
        d = int(ch)
        if k % 2:
            d = d * 2 - 9 if d > 4 else d * 2
        total += d
    return total % 10 == 0

def _verhoeff(digits):
    """The check-digit test of Aadhaar numbers (the first digit is never 0 or 1)."""
    if digits[:1] in ("0", "1"):
        return False
    c = 0
    for k, ch in enumerate(reversed(digits)):
        c = _VERHOEFF_D[c][_VERHOEFF_P[k % 8][int(ch)]]
    return c == 0

def _merge(spans):
    """Overlapping spans joined into one, keeping the rule of the first."""
    out = []
    for s, e, rule in sorted(spans):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(e, out[-1][1]), out[-1][2])
        else:
            out.append((s, e, rule))
    return out

def f1_spans(text):
    """F1: every email, phone number or ID number, removed with its label. A line left with no letter or digit
    after the removal ("Tel: … / Fax: …") is removed whole."""
    not_personal = [m.span() for rx in F1_NOT for m in rx.finditer(text)]
    spans = []
    for kind, rx, check in F1_PATTERNS:
        for m in rx.finditer(text):
            s, e = m.span()
            if kind == "email":
                if m.group(0).lower().endswith(F1_EMAIL_SKIP):
                    continue
            elif any(s < b and a < e for a, b in not_personal):
                continue
            digits = re.sub(r"\D", "", m.group(0))
            if check == "luhn" and not _luhn(digits) or check == "verhoeff" and not _verhoeff(digits):
                continue
            spans.append((s, e, "F1-" + kind))
    spans = _merge(spans)
    out = []
    for s, e, rule in spans:
        ls = text.rfind("\n", 0, s) + 1
        le = text.find("\n", e)
        le = len(text) if le < 0 else le
        rest = text[ls:s] + text[e:le]
        for s2, e2, _ in spans:  # other values on the same line go too
            if ls <= s2 and e2 <= le and (s2, e2) != (s, e):
                rest = rest.replace(text[s2:e2], "")
        out.append((ls, le, rule) if not re.search(r"[^\W_]", rest) else (s, e, rule))
    return _merge(out)


def _std(out, text):
    # source result (spans to remove) in the shared form, as clean() removes them
    new = text
    for s, e, _ in reversed(_merge(out)):
        new = new[:s] + new[e:]
    return ("fix" if new != text else "keep", new)


def medicine(doc):
    if doc.get("lang_label") not in LANGS:
        return ("keep", doc["text"])
    return _std(f1_spans(doc["text"]), doc["text"])
```

3. **Action:** fix.
4. **Harm test:** PENDING rerun on updated gold; record changed, dropped, percent, pack and gold hashes.
5. **Side effects:** the medicine finds 13 of the 13 labelled cases. On the whole pack it changes 8 documents, all of them labelled F1. It misses personal data with no fixed shape: names, home addresses, and numbers written in words or grouped in an unusual way. Every phone number counts, also an organisation's (decided 24 Oct). After the removal a sentence such as "call … for details" can read oddly.

**Decision (guideline 2):** KEEP, passes and fixes the most labelled rows (25).

## Harm test (whole sheet, in run order)

| pack | gold | rules FAIL alone | all rules: changed / dropped / harm | the KEEP rules: changed / dropped / harm |
|---|---|---|---|---|
| dclm | 62 | DA-C1-005, DA-C1-002 | 24 / 1 / 40.32% FAIL | 0 / 0 / 0.00% PASS |
| fineweb-edu | 160 | DA-C5-001 | 1 / 4 / 3.12% FAIL | 0 / 0 / 0.00% PASS |
| nemotroncc | 34 | DA-C1-005 | 2 / 0 / 5.88% FAIL | 0 / 0 / 0.00% PASS |
| synth | 96 | none | 0 / 0 / 0.00% PASS | 0 / 0 / 0.00% PASS |
