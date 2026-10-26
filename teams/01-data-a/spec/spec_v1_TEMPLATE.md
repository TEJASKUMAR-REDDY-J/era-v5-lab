# G1 Data A — Shared Cleaning Specification v1

> **Status:** DRAFT — template; not an approved cleaning specification  
> **Spec owner:** Vijay Patil (G1 lead)  
> **Contributors:** [GitHub handles / PRs]  
> **Coverage:** English, Code, Math, Science (G1); Indic rules supplied and reviewed with G2  
> **Target freeze:** 31 October 2026, 23:59 IST  
> **Git location:** `teams/01-data-a/spec/spec_v1.md`  
> **Repository revision tested:** `[commit SHA]`  
> **Spec version / last updated:** `v1.0.0-draft` / `[YYYY-MM-DD HH:MM IST]`

**Purpose.** Define one reproducible set of cleaning rules proposed from diagnosis submissions, with explicit applicability, implementations, order, exceptions, and gold-set harm-test evidence. Only rules meeting the release criteria in §2 are eligible for the frozen spec.

**Source of truth.** Disease meanings, medicine content and 1% harm threshold follow [`diagnosis/DISEASES.md`](../../../diagnosis/DISEASES.md). G1's original week-1 task requires gold CSVs, a shared harm-test tool, and this frozen spec.

## 1. Scope and inputs

| Category | Owner | Included sources / packs | Status |
|---|---|---|---|
| English | G1 | `[exact pack IDs]` | TODO |
| Code | G1 | `[exact programming-language pack IDs]` | TODO |
| Math | G1 | `[exact pack IDs]` | TODO |
| Science | G1 | `[exact pack IDs, including FinePDFs if applicable]` | TODO |
| Indic | G2 (integrated by G1) | `[G2 spec/PR and exact applicability]` | PENDING |
| Code-adjacent (issues/PRs/commits/notebooks) | `[confirm G1 vs G2 with Rohan]` | `[IDs]` | BLOCKED |

**Input inventory** (fill from actual merged or reviewed PRs):

| Pack ID | Source / language | Gold CSV path | Gold count | Medicine source PRs / links | Owner | Readiness |
|---|---|---|---:|---|---|---|
| `[pack_id]` | `[source; language]` | `teams/01-data-a/gold/[pack_id]_gold.csv` | TBD | `[PR URL(s)]` | `[@handle]` | PENDING |

### Gold-set contract

- Each gold CSV stores **only** `doc_id,reader_1,reader_2` (GitHub handles).
- Gold entries require two **distinct** reviewers who each labelled the same `(pack_id, doc_id)` as `read=full, verdict=clean`. Handle duplicate and conflicting submissions deterministically and document the policy in the gold-generator README.
- The reference target in `DISEASES.md` is approximately **200 documents per language/code language**. G1's original assignment also requests **one CSV per Data A pack**. Keep both requirements visible and obtain instructor confirmation of how to judge coverage.
- If the gold set is missing, empty, invalid, or too small to support an agreed test, record **NOT_EVALUATED**.
- Store the exact pack digest, gold digest and reviewed-label revision with each test; regenerated gold sets invalidate previous results until rerun.

## 2. Non-negotiable acceptance criteria

A rule can be marked **APPROVED** only if all are satisfied:

1. **Diagnosed need:** A disease code from `DISEASES.md`, number of occurrences and supporting `doc_id` examples appear in the contributing medicine(s). The medicine requirement is for diseases seen **more than five times** per submitted slice; mergers of equivalent medicines are documented.
2. **Defined behavior:** A precise detector and executable implementation (regex or Python function), action (`fix` or `drop`), applicability/scope, failure behavior and side effects are specified. `flag`/manual review may be recorded as a separate proposal but is **not** a substitute for testing mutating cleaning rules.
3. **Positive evidence:** At least one diseased example is demonstrably treated as intended without introducing new damage. Record what happened and relevant tests.
4. **Gold harm test:** Each applicable test reports `gold_count`, `changed_count`, `dropped_count`, and number of **unique** gold `doc_id`s changed or dropped. Exact text differences count as changes.
5. **Threshold:** `harm_pct = 100 × affected_unique / gold_count`. **PASS if and only if `gold_count > 0` and `harm_pct <= 1.0`**; otherwise FAIL, or NOT_EVALUATED when a valid comparison cannot be performed. A document changed and dropped counts **once** in the numerator. Independently list changed and dropped counts.
6. **Applicability coverage:** Test against gold sets for every pack to which this rule will be applied. A rule failing one applicable pack is not globally approved. A non-applicable pack is **N/A**, not PASS.
7. **Safety:** Do not publish E3/F1 secrets or personal data in this spec, logs, test fixtures or PRs. Supply only type, masked/synthetic examples and offsets; omit hex bytes for E3/F1. Preserve valid Indic ZWJ/ZWNJ and use NFC where Unicode normalization is appropriate; do not silently apply NFKC.
8. **Integration:** Confirm rule ordering, interaction/conflict resolution and a combined-pipeline regression test. Test failures remain visible; do not quietly exclude difficult cases.
9. **Evidence:** Link result artifact(s), rule implementation revision, gold version, owner and reviewer. A proposed threshold exception or unresolved instructor question must be **BLOCKED/DEFERRED**, not APPROVED.

### Test outcome values

| Status | Meaning | Allowed in frozen approved rule list? |
|---|---|---|
| `APPROVED` | All applicable gold tests pass, evidence complete, integration checked | Yes |
| `CANDIDATE` | Implemented; evidence incomplete or under review | No |
| `FAILED` | At least one applicable gold test exceeds 1%, or a correctness check fails | No |
| `BLOCKED` | Required input/decision unavailable (e.g. G2 rule/G9 fingerprint) | No |
| `DEFERRED` | Intentionally excluded from v1 with documented rationale | No |

## 3. Rule registry (single source of truth)

Do **not** paste all medicines verbatim. Deduplicate equivalent rules, retain contributor links, and give each distinct approved or candidate behavior a stable rule ID such as `DA-A1-001`. Disease code is separate from rule ID. Add one line per rule, and maintain its full record in §4.

| Rule ID | Disease code | Short name | Action | Applies to | Owner | Priority/order | Harm outcome | Status | Full record |
|---|---|---|---|---|---|---:|---|---|---|
| `DA-[CODE]-001` | `[A1/B3/...]` | `[short name]` | `fix/drop` | `[pack IDs or exact scope predicate]` | `[@handle]` | TBD | NOT_EVALUATED | CANDIDATE | [Rule card](#rule-card-da-code-001) |

**Registry checks:** Every record uses a unique ID; every scope matches an explicit set of pack IDs or a deterministic predicate; every APPROVED rule has a matching successful harm-test record; do not mark unimplemented ideas as executable rules.

## 4. Per-rule record — copy for EACH proposed rule

### Rule card: `DA-[CODE]-001`

> **Status:** CANDIDATE — **this block is a blank template**

| Field | Value |
|---|---|
| Rule ID / title | `DA-[CODE]-001` — `[human-readable title]` |
| Disease code / definition | `[code]` — `[exact disease from DISEASES.md]` |
| Origin | `G1 / G2`; `[pack_id]`; `[github handle]`; `[medicine file link]`; `[PR link]` |
| Occurrence frequency | `[N of 500; or N of actually inspected docs]` |
| Supporting documents | `[doc_id_1]`, `[doc_id_2]`, `[doc_id_3]` (no sensitive payloads) |
| Problem / intended correction | `[one or two precise sentences]` |
| Preconditions / trigger | `[exact detector, guards, metadata checks]` |
| Scope | `[allowlist of pack IDs, source categories, language labels; exclusions]` |
| Action | `fix` / `drop` |
| Implementation | `[repository path]` and `[callable name or versioned regex]` |
| Execution stage / order | `[stage, numeric order; dependencies]` |
| Idempotence expectation | `[expected apply(apply(doc)) == apply(doc)? explain exceptions]` |
| Side effects / false positives | `[specific legitimate text this might damage]` |
| Rollback / failure mode | `[leave unchanged / fail closed / report error; do not guess]` |
| Implementer / reviewer | `[@handle]` / `[@handle]` |
| Decision | `CANDIDATE / APPROVED / FAILED / BLOCKED / DEFERRED` |

#### 4.x.a Medicine behavior (words and executable reference)

**Proposed rule:** `[Describe the exact steps including exceptions; specify whether matching means fixing text or dropping the whole document.]`

```python
# ILLUSTRATIVE CONTRACT ONLY; replace with real, reviewed code and a path.
# Any metadata-dependent rule must declare which metadata fields it uses.
def apply_rule(text: str, metadata: dict) -> tuple[str | None, bool]:
    """Return (new_text, dropped). A dropped document returns (None, True)."""
    raise NotImplementedError("Replace with the rule implementation")
```

**Examples:** Use *synthetic* literals when illustrating E3/F1 or other sensitive cases.

| Test | Document ID or synthetic fixture | Input condition (safe description) | Expected result | Observed result |
|---|---|---|---|---|
| Positive 1 | `[doc_id or fixture]` | `[described defect]` | `[fix/drop]` | PENDING |
| Positive 2 | `[doc_id or fixture]` | `[described defect]` | `[fix/drop]` | PENDING |
| Negative/guard | `[fixture]` | `[valid text at risk]` | No change | PENDING |

#### 4.x.b Gold-set harm-test record

- **CLI:** `python teams/01-data-a/tools/harm_test.py [exact tested invocation]`
- **Test implementation commit SHA:** `[SHA]`
- **Rule implementation commit SHA:** `[SHA]`
- **Result artifact(s):** `[safe JSON/CSV path(s) or PR links]`
- **Timestamp (IST):** `[timestamp]`

| Pack ID | Gold CSV / SHA-256 | Gold N | Changed | Dropped | Affected unique | Harm % | PASS/FAIL/N/A | Notes |
|---|---|---:|---:|---:|---:|---:|---|---|
| `[applicable_pack]` | `[gold path; digest]` | TBD | TBD | TBD | TBD | TBD | NOT_EVALUATED | `[reason]` |

**Aggregate summary (informational only):** `[total N and unique affected; don't use an aggregate to hide a per-pack failure]`.

**Decision rule:** All applicable pack rows must PASS with `harm_pct <= 1.0`. Record and investigate exactly which gold IDs were affected. For private data, output IDs and redacted classifications only, not text.

#### 4.x.c Integration and reviewer sign-off

- Depends on: `[other rule IDs / none]`
- Conflicts with: `[other rule IDs / none]`
- Pipeline order / reason: `[e.g. decoding before boilerplate removal]`
- Combined-pipeline result: `[path; affected IDs; percentage; PASS/FAIL/NOT_EVALUATED]`
- Reviewer notes: `[accepted exceptions and evidence]`
- **Owner review:** `[@handle / date]`
- **Independent review:** `[@handle / date]`
- **Final decision:** `[APPROVED/FAILED/BLOCKED/DEFERRED]`; `[reason]`

<!-- Duplicate the complete Rule card section for every candidate; then update §3. -->

## 5. Canonical execution plan and clashes

**Principle:** Do not assume individually safe rules are jointly safe. Run only rules whose scope applies, in one documented order. This table is a proposed ordering worksheet, **not an approved universal pipeline**.

| Stage | Rule IDs in sequence | Why this order? | Known interaction | Combined test status |
|---|---|---|---|---|
| 00: Guard / scope | `[IDs or helper]` | Establish source, language, document type | Prevent prose rules touching code/Indic | PENDING |
| 10: Character safety | `[IDs]` | `[rationale]` | Preserve format, Unicode script integrity | PENDING |
| 20: Markup / boilerplate | `[IDs]` | `[rationale]` | Avoid damaging code, math or scientific notation | PENDING |
| 30: Source-specific cleaning | `[IDs]` | `[rationale]` | Avoid rule clashes between pack families | PENDING |
| 40: Data safety / contamination | `[IDs]` | `[rationale]` | Sensitive-data handling and G9 input | PENDING |
| 90: Post-clean checks | `[IDs]` | Validate structure after mutation | Check nonempty output and script integrity | PENDING |

**Conflict ledger**

| Rule A | Rule B | Conflicting input case / fixture | Chosen order or exclusion | Verification | Owner |
|---|---|---|---|---|---|
| `[ID]` | `[ID]` | `[safe example]` | `[decision]` | `[test path / result]` | `[@handle]` |

**Combined-pipeline harm test:** run the exact ordered, scope-filtered candidate pipeline against applicable gold sets. Publish affected-document IDs and counts; a combined failure blocks the conflicting pipeline until resolved even if component rules separately pass. Keep positive diseased fixtures to show the pipeline still removes intended problems.

## 6. G2 Indic integration and G9 dependencies

### G2 handoff

| Item | Source PR / SHA | Named G2 owner | G1 integrator | Scope | Test results | Status |
|---|---|---|---|---|---|---|
| Indic rule set | `[link]` | `[@handle]` | `[@handle]` | `[Indic pack IDs]` | `[links]` | BLOCKED |

**Minimum checks:** Honor NFC (do not silently substitute NFKC), retain meaningful ZWJ/ZWNJ, preserve matra/virama sequences, and prevent language-agnostic English/code cleaners from destroying good Indic text. Ensure G2's approved rules have the same fields and 1% evidence standard before integrating into the G1 frozen spec.

### G9 fingerprint handoff (disease F2)

- Expected delivery: **31 October 2026**.
- Owner / link / version: `[G9 contact + PR/hash]`.
- F2 implementation stage: `[candidate / blocked / validated]`.
- If the necessary fingerprints or runnable validation are missing at freeze, record the F2 rule as **BLOCKED**, explicitly note the incomplete dependency, and do **not** claim it passed.

## 7. Coverage, decisions, and exclusions

### Coverage summary

| Source family / language | Packs assigned | Gold files generated | Gold IDs counted | Rules proposed | Rules approved | Rules failed / blocked | Reviewer |
|---|---:|---:|---:|---:|---:|---:|---|
| English | TBD | TBD | TBD | TBD | TBD | TBD | `[@handle]` |
| Code | TBD | TBD | TBD | TBD | TBD | TBD | `[@handle]` |
| Math | TBD | TBD | TBD | TBD | TBD | TBD | `[@handle]` |
| Science | TBD | TBD | TBD | TBD | TBD | TBD | `[@handle]` |
| Indic (from G2) | TBD | TBD | TBD | TBD | TBD | TBD | `[@handle]` |

### Deferred / rejected / unresolved proposals

| Rule ID / disease | Why not approved? | Evidence | Next action / owner |
|---|---|---|---|
| `[rule ID]` | `[harm >1%, missing gold, false positive, no implementation, pending G2/G9]` | `[link]` | `[next step]` |

### Instructor decisions still needed

| Question | Decision owner | Requested on | Answer / PR link | Impact if unresolved |
|---|---|---|---|---|
| Gold target per pack vs per language | Rohan | `[date]` | PENDING | Coverage acceptance |
| Data A vs Data B code-adjacent ownership | Rohan | `[date]` | PENDING | Scope / tests |
| Rule interaction / single-pass acceptance | Rohan | `[date]` | PENDING | Freeze confidence |
| Gold disagreement (2 clean vs third fix/drop) | Rohan | `[date]` | PENDING | Gold construction |
| F2 input received at freeze | G9 / Rohan | `[date]` | PENDING | Benchmark-leak rule |

## 8. Freeze record — complete only on 31 October

> Until completed, this file remains a **draft**.

- [ ] Assigned Data A packs and ownership finalized.
- [ ] Gold CSVs created with correct headers and **IDs only**; coverage shortfalls disclosed.
- [ ] Contributing medicines inventoried; duplicate/conflicting proposals resolved or tracked.
- [ ] Every APPROVED rule has a versioned executable implementation and positive examples.
- [ ] Every APPROVED rule has per-applicable-pack harm-test results **at or below 1%**.
- [ ] Changed and dropped gold IDs can be audited without revealing sensitive text.
- [ ] Combined pipeline/order reviewed, tested and cross-pack conflicts resolved.
- [ ] G2 Indic contribution merged and tested, or an explicit unfulfilled dependency is recorded.
- [ ] G9/F2 status disclosed accurately.
- [ ] Final rule registry, all result links, owners, commit SHAs and open issues are current.
- [ ] Independent reviewer approves the version to freeze.

| Freeze field | Value |
|---|---|
| Frozen version | `[v1.0.0]` |
| Freeze timestamp (IST) | `[2026-10-31 HH:MM]` |
| Frozen git commit | `[SHA]` |
| G1 lead / sign-off | `Vijay Patil — [approval/PR]` |
| Independent reviewer | `[@handle — approval/PR]` |
| Number of APPROVED rules | `[N]` |
| Outstanding dependencies | `[none / numbered exceptions]` |
| Final spec status | `DRAFT / FROZEN_WITH_EXCEPTIONS / FROZEN` |

**Change control after freeze.** Any rule edit requires a new revision (e.g. `v1.0.1`), new rule and pipeline harm tests on pinned gold files, explanation of the changed behavior, and documented reviewer approval. Preserve this frozen revision for audit and for Weeks 2–4 handoffs.

## 9. Week 2–4 handoff

| Week | Downstream consumer / work | Required artifact from this spec | Owner / link |
|---|---|---|---|
| Week 2 | Tokenizer sample / dedup design; rotations auditing cleaned documents | Frozen ordered rule list, source scopes, tests, exceptions | `[owner/link]` |
| Week 3 | Scaled cleaning audit; rotations checking tokenized shards | Per-rule manifests, counts, pinned code revision and regression fixtures | `[owner/link]` |
| Week 4 | Dry-run 2 shard checks / launch readiness | Validated cleaner revision, exceptions, audit trail, no silent spec drift | `[owner/link]` |

---

**Template authorship note.** This file is a proposed structure for G1's shared spec, based on the week-1 assignment, team discussion, and the repository's `DISEASES.md`. Placeholder counts, commands, rules and decisions are **not empirical results**. Obtain instructor approval where the original brief is ambiguous, and remove template-only text before freezing.
