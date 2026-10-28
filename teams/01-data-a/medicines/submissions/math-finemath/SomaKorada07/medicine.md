# Medicine sheet: math-finemath (SomaKorada07)

Pack: 500 documents, `HuggingFaceTB/finemath | finemath-4plus`, all labelled `en`, every document read in full.
Labels: 322 fix, 101 clean, 77 drop. Code for every medicine: `medicines.py` (stdlib + pandas; regexes shared with `scan_pack.py`).

**Harm test status.** The English gold set (Data A / Data B, due Thu 29 Oct) is not out yet, so the Gold column is
_pending_; run `python medicines.py <gold_en.parquet>` and fill it in. Until then each medicine is tested on a **proxy**:
the 101 pack documents that were read in full and labelled `clean`. "Caught" is how many of the documents labelled
with that disease the medicine actually changes (its recall on this pack).

| # | Disease | Labelled docs | Action | Caught | Pack: changed / dropped | Proxy clean (101): changed / dropped | Gold (en) |
|---|---|---|---|---|---|---|---|
| 1 | C1 boilerplate | 328 | fix | 109 | 109 / 0 | 0 / 0 | _pending_ |
| 2 | C2 repeated lines / passages | 187 | fix | 40 | 57 / 0 | 0 / 0 | _pending_ |
| 3 | C5 keyword / link lists | 50 | fix (drop via verdict when the page is mostly spam) | 5 | 5 / 0 | 0 / 0 | _pending_ |
| 4 | C3 truncated | 49 | drop previews, trim teaser cuts | 15 | 5 / 12 | 0 / 0 | _pending_ |
| 5 | A1 invisible characters | 15 | fix | 14 | 14 / 0 | 0 / 0 | _pending_ |
| 6 | B4 template junk | 18 | fix | 9 | 9 / 0 | 0 / 0 | _pending_ |
| 7 | B5 broken LaTeX / markdown | 28 | fix | 5 | 7 / 0 | 0 / 0 | _pending_ |
| 8 | A3 mojibake | 11 | fix | 10 | 10 / 0 | 0 / 0 | _pending_ |
| 9 | B2 HTML tags | 8 | fix | 3 | 3 / 0 | 0 / 0 | _pending_ |
| 10 | A6 symbol-font / look-alike glyphs | 9 | fix | 5 | 5 / 0 | 0 / 0 | _pending_ |
| 11 | D3 mixed-in foreign script | 10 | fix (drop if >30% foreign) | 5 | 7 / 1 | 0 / 0 | _pending_ |
| 12 | C4 two documents joined | 7 | drop (manual) | – | no automatic medicine | – | – |
| 13 | D4 machine-translated / spun text | 22 | drop (manual) | – | no automatic medicine | – | – |
| 14 | A5 compatibility forms | 6 | fix | 6 | 6 / 0 | 0 / 0 | _pending_ |
| 15 | F1 personal data | 7 | fix | 2 | 8 / 0 | 1 / 0 | _pending_ |

All medicines pass the 1% rule on the proxy set (worst: 1 of 101 = 0.99%). The proxy set is not the gold set: the real test is still to run.

---

## Medicine 1: C1 boilerplate
1. **Disease:** C1, 328 documents (most web pages keep some site chrome). `72f073c36305b095` "posted by gamer chick" @13; `de1b08a158de9ae9` "This preview shows page" @95; `92bef36fe0c0fc40` "Replies / Views" related-thread blocks @9487.
2. **Medicine:** delete a line that is a known chrome phrase (`C1`), or that contains a site-chrome phrase (`C1_SITE`, ~70 phrases seen in this pack: GMAT Club headers, "View Full Document", OEIS footer, "My Personal Notes arrow_drop_up", …) and is at most 120 characters; delete `Replies\n<n>\nViews\n<n>` blocks.
   ```python
   keep = [l for l in t.split('\n') if not (C1.fullmatch(l) or (C1_SITE.search(l) and len(l) <= 120))]
   ```
3. **Action:** fix.
4. **Harm test:** proxy 0 changed / 0 dropped. Gold: _pending_.
5. **Side effects:** recall is only 109 / 328: the phrase list is fitted to sites seen here, so new sites' menus and footers are missed. A forum title ending in `[#permalink]` is removed (the question usually repeats in the post). A real line that is only "Share", "Views" or "Tags:" would be removed. Found and fixed while testing: "The time now is" deleted the problem statement "If the time now is 9 o'clock" (now needs hh:mm).

## Medicine 2: C2 repeated lines and passages
1. **Disease:** C2, 187 documents. `92bef36fe0c0fc40` "• Introductory Physics Homework Help" @9487 (x10); `98e5be6db6c1c81e` "Mathematical Practice 3: Construct viable…" @2979 (x2); `e9bc93d8821adcec` the same reading passage before each question (x4–5).
2. **Medicine:** (a) a non-code line of 15+ characters that appears 5+ times keeps only its first copy; (b) a passage (blank-line block, 150+ characters, not a bullet list, not answer options, not code) that appears more than once keeps only its first copy (ruling 13).
3. **Action:** fix.
4. **Harm test:** proxy 1 changed / 0 dropped (0.85%). Gold: _pending_.
5. **Side effects:** the proxy change is natural restatement: an author repeats a sentence on purpose (`5ee756dbf1307a6f`) and the copy is lost. Repeated per-question passages (`e9bc93d8821adcec`) lose their later copies, so later questions lose their context. Recall 40 / 187: short repeated titles and quoted questions under 150 characters are kept.

## Medicine 3: C5 keyword / link lists
1. **Disease:** C5, 50 documents. `25901665fc855b35` "See more: What Did Greg Giraldo…" @3568; `b124803aff87e2d9` "Domain And Range Notes Teachers Pay Teachers…" @5708; `1eff00a48b3b10a0` SEO FAQ farm.
2. **Medicine:** delete lines starting `See more:` and lines made of 5+ comma-separated Title-Case phrases of 2–8 words.
   ```python
   SEO = re.compile(r"(?m)^(?:See more: .*|(?:[A-Z][\w’'&.-]*(?: [\w’'&.-]+){1,7}, ){5,}.*)$")
   ```
3. **Action:** fix; a page that is mostly SEO is dropped by its verdict (most of the 46 are `drop`).
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** recall is 5 / 50: most C5 here is whole spun/SEO pages, which only a drop decision handles. A real comma list of Title-Case names (bibliography, theorem names) would be deleted.

## Medicine 4: C3 truncated documents
1. **Disease:** C3, 49 documents. `de1b08a158de9ae9` Course Hero preview cut at "s[R2(Cgs" @3238; `9d26c83f14d2087f` "We hav" @772 (paywall); `4e1e6a7902a4435e` teaser ending "deeper unders..." @6566.
2. **Medicine:** drop a document that carries a preview/paywall banner (`This preview shows|Sign up to view the full|View Full Document|intentionally blurred sections`); if a document ends in a teaser cut (`word...` or `word…`), trim back to the last full sentence.
   ```python
   if PREVIEW_RX.search(t): return None
   if re.search(r'\w(?:\.\.\.|…)$', t.rstrip()): t = t[:last_full_stop + 1]
   ```
3. **Action:** drop (previews) / fix (teasers).
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** a good document that merely quotes "View Full Document" would be dropped. Recall 15 / 49: a document that stops mid-solution with no marker (`b6a1ee1fa12a6d5e` code cut at @4908) cannot be detected by a rule. A first version that trimmed every last line without end punctuation changed 6 of 117 clean documents (headings, signatures, answer lists) and was replaced.

## Medicine 5: A1 invisible characters
1. **Disease:** A1, 15 documents. `064d8dd19536d1d8` U+200E LRM @9 (x2); `8f09ea36d06abaef` U+00AD soft hyphen @3180 (x4); `263a5308b96d2e4a` U+200B @6754.
2. **Medicine:** delete U+200B, U+FEFF, U+00AD, U+200E, U+200F, U+2060, U+202A–U+202E, U+2066–U+2069. ZWJ/ZWNJ are never touched (ruling 12).
   ```python
   A1_RX = re.compile(r'[​﻿­‎‏⁠‪-‮⁦-⁩]')
   ```
3. **Action:** fix.
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** a ZWSP used as the only word separator joins two words. LRM/RLM matter in RTL text (safe in this English pack; do not run on RTL packs). U+2062 INVISIBLE TIMES in MathML text (1 document) is not removed.

## Medicine 6: B4 template junk
1. **Disease:** B4, 18 documents. `2d9c3add6852f806` "{{ 'ml-label-loading-course' | message }}" @0 (x14); `56027551326bb040` "{[ snackBarMessage ]}" @1482; `e967e3352605755f` "[TheoryMissing]" @102.
2. **Medicine:** delete `{[ name ]}`, `{{ name.attr | filter }}` (spaces inside, so LaTeX `{{x}}` is not hit), `{% … %}`, `[TheoryMissing]`, `document.write(…)`.
   ```python
   B4_RX = re.compile(r"\{\[\s*\w+\s*\]\}|\{\{\s+['\w][\w'.| :-]*\s+\}\}|\{%.*?%\}|\[TheoryMissing\]|document\.write\([^)]*\);?")
   ```
3. **Action:** fix.
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** a tutorial that teaches Angular/Jinja templates would lose its examples. Recall 9 / 18: AsciiMath leftovers such as `color(blue)(` are not covered.

## Medicine 7: B5 broken LaTeX / markdown
1. **Disease:** B5, 28 documents. `e73db44e20a89b36` "$$$where" @241 (x4); `951a4c150e019bd5` "[itex]" @23031; `3a2ccc88dfcd67c9` unclosed ``` fence @12634.
2. **Medicine:** exactly `$$$` → `$$`; forum BBCode `[itex] [/itex] [tex] [/tex] [math]` → `$`; an odd number of ``` fences gets a closing fence at the end.
3. **Action:** fix.
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** found while testing: `$$$$` is two adjacent display blocks and is valid (`3e136806c369dfbc`), so only exactly three dollars are changed. A literal `[math]` in prose becomes `$`. Recall 5 / 28: stray `$$` inside inline math (`3f15fccd9f76020b`) and LaTeX with stripped backslashes (`$mathbb`) cannot be repaired by rule.

## Medicine 8: A3 mojibake
1. **Disease:** A3, 11 documents. `c9e5d27233084b62` "â€™" @178 (x24; U+00E2 U+20AC U+2122); `ab295000bded241a` "ðŸ˜€" @118; `f79e6aeb5ebb6a5c` "тАЩ" @4628 (UTF-8 read as cp866).
2. **Medicine:** a short run starting with a UTF-8 lead byte seen as cp1252 (`Â Ã â ð Ð Ñ à á ä`) is re-encoded as cp1252 and decoded as UTF-8; kept only if that succeeds and is shorter. Same for cp866 `т[АБ].`.
3. **Action:** fix. All 10 repairs checked by hand (`Ben’s`, `statistics…`, `plano–convex`, `Here’s`, 😀).
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** the first version accepted any Latin-1 lead and turned `×`+NBSP into Hebrew `נ` in 2 clean documents; the lead set is now restricted. Real Latin-1 text could still be "repaired" when the run happens to decode as UTF-8 (rare).

## Medicine 9: B2 HTML tags
1. **Disease:** B2, 8 documents. `bf73e54bda1aabdb` "<br />" @367 (x18); `addb07a0a886743c` "<ul>" @6030; `951a4c150e019bd5` "</Math>" @22663.
2. **Medicine:** `<br>` → newline; remove simple formatting tags (`p div span a ul ol li sup sub strong em font b i center`); skip documents with a code fence or `<script>`.
3. **Action:** fix.
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** `x<sup>2</sup>` becomes `x2`. Recall 3 / 8: tags inside documents that also contain code, and broken fragments like `strong> Option`, are left.

## Medicine 10: A6 symbol-font private-use glyphs and look-alikes
1. **Disease:** A6, 9 documents. `9be631b8d8a8b294` U+F0C5 @6107 (should be ⊕); `c46f9ecdfac73e93` U+F0D8 @875 (x9); `f2746fa01fbc3cf4` "fɑstidious" @4992 (U+0251 U+0455 U+0461).
2. **Medicine:** map U+F000+code to the Symbol-font character for 46 codes (`(`, `)`, `=`, `⊕`, `∂`, Greek, brackets, …); leave other private-use characters.
3. **Action:** fix.
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** Wingdings uses the same code points: U+F0D8 as an arrow bullet becomes `¬`. Look-alike letters in spam (`fɑstidious`) and the Armenian apostrophe in `Math՚s` are not fixed (recall 5 / 9).

## Medicine 11: D3 mixed-in foreign script
1. **Disease:** D3, 10 documents. `b605c8aa5c37f266` Japanese title "ベクトル…" @23; `f2746fa01fbc3cf4` Ukrainian ad lines "Дивитися фільми…" @10238 (x4); `8210e5fa65c2f665` Marathi intro "पाईये" @144.
2. **Medicine:** delete a line when more than half of its letters are Cyrillic, Indic, CJK, kana, Hangul or Arabic; if such lines hold more than 30% of the document's letters, drop the document (that is D1).
3. **Action:** fix (drop when mostly foreign).
4. **Harm test:** proxy 0 / 0. Gold: _pending_.
5. **Side effects:** a legitimate quotation or title in another language is removed (DISEASES.md says D3 can be natural). Greek is excluded on purpose, since Greek letters are maths.

## Medicine 12: C4 two documents joined
1. **Disease:** C4, 7 documents. `dcaa196cc9b2af15` "A COVID-19 Prophecy" headline inside a units page @2843; `4d57615e33e7997e` "What mammal most abhors physical violence?" @573; `e68f196ec97b88a5` "What is Kanka?" @1865.
2. **Medicine:** none that is safe. A tested rule (cut a trailing block with no maths after a maths document) caught 0 of the labelled cases and changed 2 clean documents, so it is not proposed.
3. **Action:** drop by verdict. 4 of the 7 are also spam pages (C5) and are already `drop`; `e68f196ec97b88a5`, `c55fa2fcaeafd041` and `f6c1776061f622c6` (19 exam papers joined into one document) need the parts split or cut by hand or by a better splitter.
4. **Harm test:** not applicable (no automatic rule).
5. **Side effects:** none from automation; the cost is that C4 stays in documents nobody reviews.

## Medicine 13: D4 machine-translated or machine-spun text
1. **Disease:** D4, 22 documents. Most are SEO pages rewritten by a paraphrasing tool ("spun"): `4bbc06d580844d70` "optimistic integers that are only separating" @367 (for "positive integers that are only divisible"); `d3dc5a9f14a9a35a` "sine regulation" @658 (for "sine rule"); `a5d6914aacebfa97` "6 inches equals 3 thumbs up" @4121. A few are machine translations: `2b0dcb71433030d5` (German Wikipedia, LaTeX broken by the translator), `7fec63b917700801` "Because the byte unit inside the computer to represent the number are fixed-length" @478.
2. **Medicine:** no safe rule. Spun text is grammatical word by word; the signal is synonyms that make no sense in maths ("sine regulation", "optimistic integers"). A rule-based detector cannot see that without a language model. Proposed for later (not built, not tested): score each document with a small reference LM and a list of known spin substitutions ("sine regulation", "thumbs up" for inches, "optimistic" for positive), and send high scores to review.
3. **Action:** drop by verdict. 16 of the 22 are already `drop` (whole pages of spun SEO text); the 6 `fix` rows have one spun or translated paragraph inside an otherwise good page and need that paragraph cut by hand.
4. **Harm test:** not applicable (no automatic rule).
5. **Side effects:** none from automation. Ruling 11: ordinary spelling and grammar mistakes by people are not D4, so a future LM detector must be tuned not to flag forum posts by non-native writers.

## Medicine 14: A5 compatibility forms (PDF ligatures, fullwidth punctuation)
1. **Disease:** A5, 6 documents. `c16db13d63739369` "ﬀ" @313 (x91 ligatures: ﬀ ﬁ ﬂ ﬃ, U+FB00 U+FB01 U+FB02 U+FB03); `ce9b0d519779eba2` "ﬀ" @68 (x17); `addb07a0a886743c` fullwidth comma "，" @2666 (x2, U+FF0C) in English text translated from Chinese.
2. **Medicine:** replace the ligatures U+FB00–U+FB06 by their NFKC letters (ﬁ → fi, ﬀ → ff); replace fullwidth ASCII punctuation U+FF01–U+FF5E by the ASCII character, but only in documents where CJK characters are under 1% of the letters (real Chinese/Japanese text keeps its punctuation).
   ```python
   out = LIG_RX.sub(lambda m: unicodedata.normalize('NFKC', m.group()), t)
   if cjk_share(out) < 0.01: out = FULLWIDTH_RX.sub(lambda m: chr(ord(m.group()) - 0xFEE0), out)
   ```
3. **Action:** fix.
4. **Harm test:** see the table (proxy and gold columns). Gold: _pending_.
5. **Side effects:** a document that quotes a ligature as a character (a typography page) would lose it. Fullwidth digits in English text become ASCII digits, which is wanted here. Full NFKC is not applied: it would also change superscripts (x² → x2) and other maths symbols.

## Medicine 15: F1 personal data
1. **Disease:** F1, 7 documents (values never copied). `02c235b035b38798` email at offset 82 (x2); `ace41f52d349ca6b` email at offset 1447 (x2); `4477acbfa8e1a6da` phone number at offset 2074. Company numbers and business emails are not F1 (ruling 6).
2. **Medicine:** emails → `[email removed]`; NNN-NNN-NNNN phone numbers → `[phone removed]` when no digit is within 3 characters (skips number tables).
3. **Action:** fix.
4. **Harm test:** proxy 1 changed (0.85%). Gold: _pending_.
5. **Side effects:** business contacts are masked too (harmless for privacy; that is the proxy change). Recall 2 / 7: IP addresses (`0306000512344150`), obfuscated emails and messenger IDs are not matched.

---

### Found five times or fewer (no medicine required)
E1 code collapsed into one line by extraction, or generated code (5, `af9d1316d085d805` MATLAB program on one 3712-char line), E2 hash blobs and data arrays (5), B1 entities (4, `ab0dcfdea8b8f728` "&#40;1-2x&#41;"), D2 romanised Hindi (2, `c5b36a86af256f62` "Apne doubts clear karein"), A4 U+FFFD (3, `7c6df0c4a23c902b` "M�bius"), A2 control characters (3, `c16db13d63739369` U+0004), F2 competition problems from known contests (4: `296ba0775d5f6cca` IMO 2009 Q5, `b65447202cb074c9` AMC 8 2012, `8f09ea36d06abaef` IMO 1959 problem, `b22b5d72708d7f26` IMO 1964 problem), H2 (2), D1 (1, `ce878294b69f1b20` Chinese). No F3, E3, B3 or G-group cases.

### Not in the disease list
25 documents lost their formulas when the page was extracted (e.g. `161a7643db59ce25`, `8e9e5b4d6166454e`): the text says "the slope of the line tangent to the graph of at the point is". This is recorded in `note` only; it may deserve its own code.
