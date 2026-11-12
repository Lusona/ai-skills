# Notes: voice limits measurement (W2)

Owner: [20261111 loop principles and skill rewrite](../specs/20261111-loop-principles-and-skill-rewrite.md), W2,
AC2 and AC3. Measured 2026-11-11. The user decided the limits on 2026-11-11 (see
Decisions).

## Question

Which banned-word and hedge list (V5, V6) and which maximum average sentence length per
file can a script check, and how many current files fail each candidate value?

## Method

- Text measured: `plugins/lusona/skills/*/SKILL.md` (14 files) and
  `plugins/lusona/references/*.md` (21 files in the working tree, 20 at baseline);
  templates (12 files) reported separately. `plugins/lusona/shared/` does not exist.
- Revisions: working tree on 2026-11-11 (uncommitted changes; adds
  `references/completion.md`) and baseline `34186da` read with `git show`. Baseline has
  46 files, working tree 47.
- Check exit status: 0 clean, 1 with findings, 2 when no file is scanned.
- Instrument: the functions in `scripts/check_voice.py` (`sentence_lengths`, `terms_in`),
  called from a scratch script `tmp/voice/measure.py` (not kept in the repository). The
  measurement and the check use one implementation.
- The spec names two further inputs: the 234-word block and the drafted `implement` skill.
  Neither exists in the repository (`drafts/` is absent; decision 11 discarded the block),
  so neither was measured.

### Sentence rules

- Excluded: YAML frontmatter, fenced code blocks, headings (`#`), table rows (`|`).
- A blank line, a heading, a table row, and the start of a list item end a sentence.
- Inside prose, a sentence ends at a whitespace-separated token that ends in `.`, `!` or
  `?`, optionally followed by closing `"`, `'`, `)`, `]`, `*` or `_`. The tokens `e.g.`,
  `i.e.`, `etc.`, `vs.` and `cf.` do not end a sentence.
- A word is a token that contains a letter or digit. Inline code counts as 1 word. Link
  text counts; link targets do not. HTML comment text counts (this affects template
  numbers only; skills and references have no HTML comments in prose).
- Semicolons and colons do not end a sentence. All 14 sentences over 30 words in skills
  and references were read: each is a real sentence, most joined by semicolons.
- Templates consist of `Label: <placeholder>` lines without terminal punctuation, so
  consecutive lines merge into one "sentence" (83 words in `templates/batch.md`, 37 in
  `templates/adr.md`). Template sentence statistics are not meaningful under these rules.

### Term match rules

- Whole word, case-insensitive. A letter or digit on either side prevents a match
  (`reconsider`, `unusually` do not match); a hyphen or underscore does not
  (`over-leveraged` and `_usually_` match).
- Words of a phrase match across any whitespace, including a line wrap. The finding
  reports the line where the phrase starts.
- Excluded regions: frontmatter, fenced code, inline code, Markdown links (text and
  target, including links wrapped over lines).
- Scanned: prose, headings, table cells (skills/batch has instructions in table cells),
  block quotes, HTML comments (an agent reads them).
- Double-quoted text is not excluded. AC3 keeps the list in the script so that plugin text
  never needs to quote a banned word.

## Results

### Summary, skills and references

| Measure | Working tree | Baseline `34186da` |
| --- | ---: | ---: |
| Files | 35 | 34 |
| Sentences | 1185 | 1147 |
| Words per sentence, mean | 13.47 | 13.49 |
| Words per sentence, median | 12 | 13 |
| Words per sentence, 90th percentile | 22 | 21 |
| Words per sentence, 95th percentile | 25 | 25 |
| Words per sentence, maximum | 75 | 75 |
| File average, minimum / median / maximum | 10.8 / 13.5 / 17.6 | 10.8 / 13.4 / 17.6 |

Templates (working tree and baseline identical): 12 files, 301 sentences, mean 9.98,
median 9, 90th percentile 17, maximum 83; file averages 5.6 to 15.1.

### Files failing each average limit (skills and references, working tree)

| Maximum average words | Files failing | Fraction |
| ---: | ---: | ---: |
| 14 | 13 | 13/35 (37%) |
| 15 | 3 | 3/35 (9%) |
| 16 | 1 | 1/35 (3%) |
| 17 | 1 | 1/35 (3%) |
| 18 | 0 | 0/35 |
| 20 (spec example) | 0 | 0/35 |

At 15 the failing files are `references/corrections.md` (17.6), `references/evidence.md`
(15.6) and `references/retention.md` (15.5). Baseline gives the same counts out of 34.

### Long single sentences (skills and references, working tree)

| Words per sentence over | Sentences | Files |
| ---: | ---: | ---: |
| 30 | 14 | 10 |
| 35 | 5 | 4 |
| 40 | 4 | 3 |
| 50 | 1 | 1 |

The file average does not catch the longest sentence: `references/retention.md:14` has 75
words in a file whose average is 15.5.

### Candidate terms (skills and references, working tree, excluded regions removed)

| Term | Source | Count | Locations or classification |
| --- | --- | ---: | --- |
| usually | V5 | 0 | |
| consider | V5 | 2 | `skills/architect/SKILL.md:46`, `references/model-routing.md:7`; both instructions |
| may want to | V5 | 0 | |
| try to | V5 | 0 | |
| robust, seamless, elegant, powerful, best-in-class | V6 | 0 | |
| leverage, delve, unlock, streamline | V6 | 0 | |
| generally, typically, ideally, perhaps, probably, possibly, maybe | analyst proposal | 0 | |
| might | analyst candidate | 1 | `references/interview-examples.md:30`, quoted example dialogue |
| should | analyst candidate | 18 | 15 in example dialogue lines (`**User:**`, `**Assistant:**`) in `interview-examples.md`; 3 instructions (`skills/explore/SKILL.md:32`, `skills/map-capabilities/SKILL.md:19`, `references/work-record.md:14`) |
| may (alone) | analyst candidate | 21 | all permission ("Workers may ...") |
| can | analyst candidate | 35 | not classified one by one |
| when needed | analyst candidate | 6 | vague condition; 6 instructions |
| as needed | analyst candidate | 2 | vague condition; `skills/status/SKILL.md:25`, `references/evidence.md:30` |
| often, several, various, very, a few, if possible, where possible, as appropriate | analyst candidate | 0 | |
| considered | inflection of V5 | 0 (1 in `templates/adr.md` heading "Alternatives considered") | participle, not a hedge |

Baseline counts are identical. Templates contain no term from the original proposed list; they contain 4 `when needed` / `as needed`.

## Decisions

User, 2026-11-11, relayed by the coordinator during W2:

1. Banned list accepted as proposed, including the 7 analyst additions. Implemented in
   `TERMS` in `scripts/check_voice.py`:
   - V5: `usually`; `consider`, `considers`, `considering` (not `considered`);
     `may want to`; `try to`, `tries to`, `trying to`.
   - V5, added by the user decision: `as needed`, `when needed` (vague conditions),
     matched across line wraps.
   - V6: `robust`, `seamless`, `elegant`, `powerful` and their `-ly` adverbs;
     `best-in-class`; `leverage`, `delve`, `unlock`, `streamline` and their `-s`, `-d`/`-ed`,
     `-ing` forms.
   - Analyst additions: `generally`, `typically`, `ideally`, `perhaps`, `probably`,
     `possibly`, `maybe`.
   - Not banned: `may` alone (21 of 21 are permission), `can` (35; not classified one by
     one), `should` (15 of 18 in example dialogue), `might` (1, in example dialogue).
2. File-average limit accepted: a file fails when its average is above 15 words per
   sentence (`DEFAULT_MAX_AVG_WORDS = 15`, `--max-avg-words N`). `references/model-routing.md`
   at 15.0 passes. 3 of 35 files (9%) fail.
3. Per-sentence maximum adopted: a sentence fails when it has more than 40 words
   (`DEFAULT_MAX_SENTENCE_WORDS = 40`, `--max-sentence-words N`). 4 sentences in 3 of 35
   files fail.
4. Templates (`templates/*.md`) are scanned for banned terms only, not for sentence
   limits.

User, 2026-11-11, voice pass after promotion (request in conversation; items 6-9 through the
native question tool). The exact replacements are listed per class in
[round 2](voice-pass/round-2-agreed-replacements.md); the wording edits that preceded them are in
[round 1](voice-pass/round-1-wording-edits.md):

5. (Superseded in part by decision 14.) Banned list extended with 5 vague conditions: `when relevant`, `when useful`, `if needed`,
   `if relevant`, `omit when unnecessary`, matched across line wraps. Test written first
   (6 failures observed, then 46 tests pass). 0 findings on `plugins/lusona` after the pass.
   Not added: `when applicable` and `if applicable` (4 uses remain in templates), and the bare
   words `relevant` and `useful` (1 template column header and 1 template field label remain;
   `useful` also occurs in the `interviews.md` example dialogue, which stays as written).
6. Qualifiers without a test replaced by a stated relation or deleted: 76 replacements
   (`relevant` 50, `substantive` 13, `useful` 13). `substantive` is defined once, in
   `references/retention.md` under "When to save".
7. Size words (`small`, `short`, `brief`, `concise`, `compact`, `minimal`, `large`, `several`)
   deleted or replaced by a limit the text already stated (`one-sentence`, `one or two
   sentences`): 31 replacements, 4 of which restate a rule (review headings, reviewer count,
   capability set, inventory grouping).
8. (The "not selected" part is superseded by decision 11.) Terms: `repair allowance` becomes `repair budget`, including the batch template's field
   label and table headers; `lifecycle state` of a queue item becomes `queue state`. Not
   selected: one term for files under `docs/lusona/plans/`, and terminology rows for
   `accepted`/`settled` decision and `skill prompt`/`continuation directive`.
9. The domain-skills sentence names each skill's first action in 9 skills, and "applicable"
   becomes "that cover the task's technology or domain" in 12 skills.

User, 2026-11-11, round 3 of the voice pass ("address the still open items"; decisions through
the native question tool). Listing per class, with the basis of each row:
[round 3](voice-pass/round-3-remaining-findings.md):

10. The every-task block keeps its text (285 words) and gets an enforced limit of 300 words:
    `WORD_LIMITS` in `scripts/sync_shared.py`, counted as `wc -w` counts. Test written first
    (2 failures observed, then 18 tests pass). This replaces the 250 words stated in spec
    decision 15, which no script enforced.
11. Terms: a file under `docs/lusona/plans/` is an "execution record" (replaces "separate plan",
    "companion plan", "split records" in 22 lines). The Terminology table in
    `references/workflow-guide.md` gains rows for execution record, accepted decision, settled
    decision, skill prompt and continuation directive. "settled" and "accepted" stay two terms:
    a settled decision also covers a routine decision recorded within delegated authority. The
    accepted-decision row reads "recorded as accepted, by the user or under existing
    authorization", because `architect` step 5 allows Status `accepted` under existing
    authorization; this is wider than the wording shown in the question ("the user accepted").
12. Remaining audit findings (144 still matched the text): 99 replacements applied in three
    classes: 26 reworded with the same rule, 64 that replace an untested word with a test
    another line already states (6 of them repeat edits reverted in round 1, now with their
    source line), and 9 deletions of sentences that repeat a rule stated completely elsewhere.
    8 findings are kept as written, with the reason in the listing.
13. Held for the user's review, not applied: 34 replacements that would set a criterion no line
    of the plugin states (class N in the listing). Also open, with no draft (class O in the
    listing): about 30 uses of words without a test that the audit rows did not cover, found by
    a word sweep (`safe`/`unsafe`, `disposable`, `ordinary`, `material` outside its two
    definitions, `expensive`, `oversized`, `when allowed`, `insufficient`, `broader`, `fresh`,
    `normal`, and `ready` as a condition).
14. Banned list: `when applicable`, `if applicable`, `relevant`, `irrelevant`, `useful`
    (with `usefully`). `when relevant`, `when useful` and `if relevant` from decision 5 are now
    covered by the bare words and were removed as separate terms. Test written first
    (7 failures observed, then 49 tests pass). To reach 0 findings, the batch template column
    header "Relevant items" became "Items", the product template label "Useful horizon, if
    established" became "Horizon, if established", and one word was removed from an example
    dialogue line in `references/interviews.md`.
15. `references/queue.md` describes Icebox as a section of the queue, not a queue state; a
    parked row keeps its queue state. The name Icebox stays in the reference.

User, 2026-11-11, in conversation ("apply all 34 class N rows and draft class O"):

16. The 34 class N replacements held under decision 13 are applied as drafted. Each sets a
    criterion that no line of the plugin stated before; the listing gives the basis per row.
    One follow-on difference: `skills/frame-product/SKILL.md` now says "vision" where it said
    "ambition", while `references/interviews.md` still says "ambition".

User, 2026-11-11, in conversation ("close class O"):

17. (Superseded by decision 18.) Class O is closed with the text unchanged. A word sweep after decision 16 found 48 lines
    with a word that has no stated test (`safe`/`unsafe`, `disposable`, `ordinary`, `material`
    outside its two definitions, `expensive`, `oversized`, `when allowed`, `insufficient`,
    `broader`, `fresh`, `normal`, `ready` as a condition, and one `command`). 32 replacements
    were drafted and none is applied; the current wording is accepted. This supersedes the
    "also open" part of decision 13. The draft is in [round 4](voice-pass/round-4-open-words.md).

User, 2026-11-11, in conversation ("apply class O"):

18. The 32 class O replacements drafted under decision 17 are applied: 16 replace the word with
    a test another line already states, 7 remove the word with the rule unchanged, 1 deletes a
    repeated sentence in `references/naming.md`, and 8 set a criterion that no line stated or
    choose one of two supported readings. 16 lines are kept as written: 14 uses of `material`
    under its two definitions, the definition line of material progress, and `expensive` in
    `skills/status/SKILL.md`, for which the files support three readings. `oversized` in
    `references/delegation.md` also stays; no line states a size test.

User, 2026-11-11 (native question tool), the last 8 uses listed as still without a test:

19. `skills/status/SKILL.md`: "expensive or mutating checks" becomes a check "that mutates
    state, or one that needs a resource budget or authority the request did not grant" (test
    from `references/evidence.md`, Study entry). Not chosen: mutating checks only; a check
    whose recorded result is still valid.
20. `references/delegation.md`: "oversized" is deleted; for blocked work the rule is "split a
    separable outcome".
21. Six uses replaced with wording another line already states, or with the word removed:
    "unnecessary complexity" (`implement`), "unneeded abstractions" twice (`refactor`),
    "necessary dependencies" twice (`map-capabilities`), "enough to repeat the check" (notes
    template).

Also applied on the user's request, without a question: 2 sentences of the shared final reply
reworded, 3 skill descriptions split at the first sentence, and 2 description phrases made
literal (`frame-product`, `investigate`). The loop-conformance suite was not rerun after these
changes; the run recorded for AC18 measured the earlier text.

Proposal alternatives the user did not choose: average 16 (1 of 35 files fail), 18 or 20
(0 of 35); per-sentence 30 words (14 sentences in 10 files).

## Check result on `plugins/lusona` (working tree, accepted limits)

`python3 scripts/check_voice.py` exits 1 with 21 findings:

| Rule | Count | Locations |
| --- | ---: | --- |
| `when needed` | 9 | skills batch:63, implement:34, implement:47; references commits:32, naming:14, retention:73; templates brainstorm:37, notes:43, spec:63 |
| `as needed` | 3 | `skills/status/SKILL.md:25`, `references/evidence.md:30`, `templates/product.md:64` |
| `consider` | 2 | `skills/architect/SKILL.md:46`, `references/model-routing.md:7` |
| sentence over 40 words | 4 | `references/corrections.md:18` (45), `references/evidence.md:39` (47), `references/retention.md:14` (75), `references/retention.md:42` (41) |
| file average over 15 | 3 | `references/corrections.md` (17.6), `references/evidence.md` (15.6), `references/retention.md` (15.5) |

These are expected before the skill rewrite and are not a W2 failure.

## Limits

- Sentence splitting is a heuristic; abbreviations outside the 5 listed, decimal numbers
  followed by a space, and sentences ending in a code span or link without punctuation
  can shift counts by 1 sentence. A `...` token ends a sentence ("(V1, V2, ...)" in
  `references/visuals.md`); `etc.` at a true sentence end merges two sentences.
- Template sentence length is not checked (decision 4); their field lines merge into
  long "sentences" under the splitting rules.
- The check cannot verify AC3's "passes on the draft" because no draft exists.
- Remaining voice rules (V1-V4, V6 idioms, V7-V9) are not script-checkable here and stay
  with review.
