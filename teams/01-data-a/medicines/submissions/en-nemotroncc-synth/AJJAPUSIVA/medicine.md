# English synthetic Parquet — diagnosis medicine (DRAFT)

## Scope and method
Source: `en-nemotroncc-synth.parquet`, 500 rows. Human decisions currently cover rows 1–150 only. Rows 151–500 have not been reviewed. Labels and original source IDs remain separately traceable. The cleaned output is an optional working derivative, not a replacement for the original data or the required submission labels.

## Confirmed interventions
- Drop document rows 22 (F3), 113 (C5 / search-result collage), and 124 (C5/C1 / snippets lacking coherent article).
- Join 101+102, 114+115, 116+117, 119+120, 121+122+123, 142+143 in source order.
- Remove an affiliate disclosure from 111; an automated-citation disclaimer from 112; the email subscription call-to-action from 120.
- Split row 125 at the confirmed new question beginning `i have a 2003 chev s-10 pickup`, retaining the Infiniti G37 and Chevrolet S-10 material as two separate entries.
- Remove the clearly anomalous character sequence `e~ \\` in row 148; normalize the known broken LaTeX sigma commands in 95.

## Unresolved precision / do not fabricate
- Rows 75, 76: manually reviewed local join applied; C3 remains provisional because both source rows end in complete sentences.
- Rows 109, 110: manually reviewed body join and separate Q&A applied locally. Missing list after row 110's `such as:` remains unresolved; C3 is provisional for row 109.
- The rest of the 500-row dataset is not asserted to be clean. Inspect the review-status column before downstream use.

## Row 16: manual C4 medicine
- Document: `a14eaa5e58baf3c3`. A manual review selected a four-way split at candidate topic boundaries. These are not verified original article boundaries.
- Evidence: topic changes before `Australia's English`, `England and Wales,`, and `Welsh, a Celtic language,`.
- Rule: apply only to this document ID and exact reviewed source text. Split into Irish education, Australian languages, English legal jurisdiction, and Celtic languages. Preserve all characters, including boundary whitespace; derive segment IDs from the source ID.
- Zero-based character offsets (end exclusive): `0:188`, `188:338`, `338:409`, `409:1091`.
- Code (after checking the source ID and exact source text):

```python
bounds = [0, 188, 338, 409, 1091]
segments = [text[a:b] for a, b in zip(bounds, bounds[1:])]
assert "".join(segments) == text
```

- Applied locally: one source document becomes four segments; no characters are deleted, added, or rewritten. The original source and previous reviewed package remain intact.
- Validation: all four segments are nonempty, contiguous, and reconstruct the 1,091-character original exactly; the local Parquet round-trip matches the segments.
- Harm test: not run; no gold set was supplied. Reconstruction verifies preservation only, not semantic correctness or the required gold-set harm threshold.
- Side effects: splitting can remove cross-topic context. The final Celtic-language block still needs content review. Do not apply this document-specific rule to other rows.

## Row 34: manual C4 medicine
- Document: `5958fb6996158153`. A manual review selected five paragraph-level topic blocks: 3D printing, disruptive technologies, military contracts/mobile devices, AI, and Digi.me. Original article boundaries remain unverified.
- Evidence: paragraphs start with `Disruptive technologies span`, `Microsoft's employees raised`, `AI is increasingly integrated`, and `Digi.me, founded`.
- Rule: apply only to this document ID and exact reviewed source text. Split at the four stated paragraph starts. Preserve all characters and whitespace; derive segment IDs from the source ID.
- Zero-based character offsets (end exclusive): `0:386`, `386:689`, `689:897`, `897:1270`, `1270:1399`.
- Code (after checking source ID and exact source text):

```python
bounds = [0, 386, 689, 897, 1270, 1399]
segments = [text[a:b] for a, b in zip(bounds, bounds[1:])]
assert "".join(segments) == text
```

- Applied locally: one source document becomes five segments, with no rewriting or deletion. The original source and previous reviewed package remain intact.
- Validation: segments are nonempty and contiguous; joining them reconstructs all 1,399 original characters exactly. The local Parquet round-trip matches the segments.
- Harm test: not run; no gold set was supplied. Text preservation does not validate semantic correctness or establish compliance with the gold-set harm threshold.
- Side effects: the original may be a compiled technology summary; splitting can remove context. Some blocks still mix subtopics (notably military contracts and mobile devices). No finer split is assumed, and this rule must not be applied to other rows.

## Rows 75-76: manual list reconstruction (C3 provisional)
- Documents: `60f1a32f80f6a3cf` and `ab4f03c12b813b47`. Row 75 promises 15 films but ends at numbered entry 11. Row 76 overlaps on Moonstruck and supplies four further films.
- Rule: for these two exact source texts only, append row 76 after row 75 with two newlines. Retain row 76's Moonstruck paragraph as additional detail under item 11. Prefix its four remaining film paragraphs with `12. ` through `15. `, in source order. Do not rewrite or discard either Moonstruck description.
- Code (after checking source IDs and exact source text):

```python
markers = ['"Obvious Child"', '"Sabrina"', "\"She's Gotta Have It\"", '"To All The Boys I\'ve Loved Before"']
starts = [text76.index(marker) for marker in markers]
ends = starts[1:] + [len(text76)]
joined = text75 + "\n\n" + text76[:starts[0]]
joined += "".join(f"{n}. " + text76[a:b]
                  for n, a, b in zip(range(12, 16), starts, ends))
```

- Applied locally: two documents become one 15-entry list. Both source IDs remain traceable. All source characters remain in order; only 18 characters (a two-newline separator and four numbering prefixes) are added.
- Validation: entries are numbered 1-15; both original source texts can be recovered exactly using the source-piece map; the local Parquet round-trip matches the joined record.
- Harm test: not run; no gold set was supplied. These checks do not establish the required gold-set harm threshold.
- Side effects: source continuation is inferred from list contents, not verified against the original article. Moonstruck still has two descriptions, deliberately retained to avoid losing distinct details. Existing factual inconsistencies in the text are not repaired. C3 remains provisional under the repository's mid-sentence/code-block definition. Do not generalize this join to other rows.

## Row 81: B4 placeholder medicine
- Document: `d2fb665c40af5edb`. The billing explanation contains `-DATE-` at zero-based character offset 326.
- Manually reviewed action: replace `Total Due After -DATE-:` with `Total Due After the Due Date:`. This is a generic explanation of a billing term; no calendar date is inferred or inserted.
- Rule: apply only to this source document and exact heading, with exactly one matching occurrence. Classify as B4 (template junk in prose).

```python
old = "Total Due After -DATE-:"
new = "Total Due After the Due Date:"
assert text.count(old) == 1
cleaned = text.replace(old, new, 1)
assert cleaned.replace(new, old, 1) == text
```

- Applied locally: one placeholder is replaced; all other source text is unchanged. Original data is retained separately.
- Validation: exactly one target heading; reversing the replacement reconstructs the source exactly; local Parquet round-trip matches the result.
- Harm test: not run; no gold set was supplied. This document-specific check does not establish the required gold-set harm threshold.
- Side effects: do not apply this substitution to an actual bill requiring a specific date, or to unrelated uses of `-DATE-`.

## Rows 109-110: join article bodies and preserve Q&A separately
- Documents: `d896f8ca6a2beae1` and `fdd2b470571c5e4d`. Row 109 ends its body with a leading-platforms heading; row 110 starts with discussion of leading platforms. Source Parquet metadata confirms both share the same article URL, WARC record ID `84ec882b-7e1b-42c1-bce9-812e0e3345e3`, and source partition. This supports common provenance; it does not recover missing content or verify full original ordering. Both have `kind2=diverse_qa_pairs`, so Q&A is source synthetic content, not assumed boilerplate.
- Manually reviewed rule: for these two exact source texts only, split each at its first `\n\nQuestion:`. Keep that delimiter with its Q&A. Join the two bodies in source order with two newlines, and retain each Q&A block separately with its source ID. Preserve both source IDs on the joined body. Do not rewrite answers or invent a missing list.

```python
bodies, qa_blocks = [], []
for text in (text109, text110):
    boundary = text.index("\n\nQuestion:")
    body, qa = text[:boundary], text[boundary:]
    assert body + qa == text
    bodies.append(body)
    qa_blocks.append(qa)
joined_body = "\n\n".join(bodies)
```

- Applied locally: two mixed article/Q&A records become one article body and two separate Q&A records. All original source characters remain recoverable; only a two-newline join separator is inserted.
- Validation: each body plus its Q&A reconstructs its exact source text. Local Parquet round-trip matches all three output records; both source IDs are preserved on the joined body.
- Unresolved: the article still ends `with all leading business systems such as:`. Flag the missing list; do not claim the joined article is complete. Row 109 has no mid-sentence cutoff, so its C3 diagnosis remains provisional. Q&A factual accuracy has not been checked.
- Harm test: not run; no gold set was supplied. Reconstruction checks do not establish semantic correctness or the required gold-set harm threshold.
- Side effects: the inferred continuation could be wrong; moving Q&A changes context. Keep both Q&A blocks and provenance, and do not generalize this rule to other records.

## Reproducibility
The document-specific code above records the new transformations for rows 16, 34, 75-76, 81, and 109-110. Use the source document IDs and stated offsets or exact markers to reproduce them on the original sample pack. Local review manifests and Parquet derivatives are not part of this submission. The earlier `first150_cleaning_manifest.json` and build script do not include these new transformations. Gold-set harm tests remain pending.
