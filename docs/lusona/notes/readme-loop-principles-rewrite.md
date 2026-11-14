# Notes: readme-loop-principles-rewrite

Context: direct documentation change without a spec. The user asked on 2026-11-11 to rewrite
the root README to match the loop principles of
[spec 20261111](../specs/20261111-loop-principles-and-skill-rewrite.md#loop-principles-accepted),
English first, translations after the user approves the English text.

## 2026-11-11 — Rewrite the root README around the loop principles

### Question and scope

- Agreement: rewrite `README.md` at the repository root so that it describes the workflow by
  loop principles P1-P8 and agrees with the 3.0.0 plugin sources.
- Scope (user, 2026-11-11, native question tool, "Whole file"): every section of `README.md`,
  including Installation and Development.
- Not in scope until the user approves the English text: `README.es.md`, `README.de.md`,
  `README.ja.md`, `README.zh-CN.md`. Not in scope: `plugins/lusona/README.md`, the loop image,
  `INSTALL.md`, plugin sources, a version bump.
- TDD level: `none` (user, 2026-11-11, native question tool).
- Acceptance: the user approves the English text.
- Assumption (coordinator): the README is text for human readers, so it follows the user's
  global writing rules (answer first, plain literal language, numbers in place of vague
  intensifiers). Voice rules V1-V9 are scoped to skill text by the spec.

### Evidence

- Method: one leaf (technical writer, write ownership of `README.md` only) rewrote the file from
  the accepted principles, `plugins/lusona/references/`, `shared/`, the skill descriptions and
  `INSTALL.md`, and returned a table that maps each statement about agent behavior to a source
  line. The coordinator read the whole draft and compared these statements with their sources:
  the five revision steps and the record outcomes (`revisions.md`), the correction limits of 2
  consecutive and 4 total rounds (`corrections.md`), the batch assignment ceiling and repair
  budget (`skills/batch/SKILL.md:55,59`), the 2-4 visual options (`visuals.md:7`), and the
  Antigravity check (`INSTALL.md:115-116`). The other rows of the leaf's table were not
  rechecked line by line.
- Result (2026-11-11, working tree on `c9bd02a`):
  - `python3 -I tmp/readme-rewrite/check_links.py .`: 69 relative links and anchors resolve; the
    12 Index entries equal the 12 `##` headings in order.
  - `python3 scripts/package.py --output tmp/readme-rewrite-pkg`: exit 0, `lusona-3.0.0.zip`
    built with its link check.
  - `git diff --check -- README.md`: clean. `README.md` is the only tracked file changed.
  - Line count 368 before and after. URLs, fenced install and development commands, the
    language row, the version text and the warning box are unchanged.
- After the leaf's draft the coordinator made four edits: one sentence that states what the
  loop is (from the image text), "red evidence" replaced by "evidence of the intended failure",
  the four spec conditions turned into a list (the sentence had 44 words), and the resume
  example prompt of the previous README restored. Rerun after these edits: link check (no
  errors), package build (exit 0), `git diff --check` (clean). `python3 scripts/test_package.py`:
  14 tests pass. The banned-term and sentence-length functions of `scripts/check_voice.py`,
  called on `README.md`: 0 banned terms (the previous README had 10), no sentence over 40 words.
  File length is now 378 lines.
- Coordinator error: the assignment told the leaf that the file had 286 lines and should not
  grow. The file had 368 lines and the user set no length limit. The items listed below as
  dropped for length were dropped under that constraint.
- Limitations: Markdown, the reply example table and the image were not rendered. The Mermaid
  diagram was removed, not replaced. `scripts/check_voice.py` targets plugin text and was not
  run on the README; a grep for the filler words of V6 found none.

### Conclusion and decisions

- New outline: opening; Loop principles (P1-P8 table); Start and choose a skill; Authority and
  TDD level; Decisions and revisions; Evidence and completion; Records and resumption; Replies
  and next actions; Installation; Reference; Contributing; License; Development.
- Corrected against the 3.0.0 sources: a contradicted decision is revisited with the user, not
  "within existing authority"; the coordinator delegates specialist work at every task size
  (the old text let exploration and status dialogue stay local); the reply example uses the
  `**Result:**` form; the blockquote below the table is a continuation directive for another
  session, not a prompt to send; "TDD policy" became "TDD level"; "command" and "action group"
  became "skill"; the plugin README is labelled a catalog.
- Removed because no 3.0.0 source supports them: "A user-requested pause requires you to resume
  the work"; the sentence on dependencies and shared state determining ordering; the sentence on
  source-size reductions and token savings; "completing a diagnosis does not mean the defect is
  fixed".
- Dropped for length; each stays in its linked reference (the resume example prompt was
  dropped too and then restored): the interview paragraph, the planning-depth paragraph,
  "routine design choices stay within implementation or refactoring", the visual capture fallbacks, and the rule that records link
  exact evidence runs.
- Found outside the authorized scope, not changed: "TDD policy" in `skills/specify/SKILL.md:3`,
  `INSTALL.md` and `CONTRIBUTING.md`; "command" in the image text and its alt text; "thirteen
  skills" in the `INSTALL.md` record of the 1.4.0 Antigravity check.

## 2026-11-11 — Recreate the loop image

### Question and scope

- Scope change (user, 2026-11-11, conversation): "good... let's recreate the SVG to match better
  illustrate the principles and the loop. Use brighter colors and contrast". The loop image
  `plugins/lusona/assets/workflow-loop.svg` is now in scope; the earlier entry listed it as out
  of scope. TDD level `none` carries over (same change; user, 2026-11-11, native question tool).
- "good" is the user's reply to the request to approve the English README text. Coordinator
  reading: the English text is accepted. The translations wait until the image is chosen,
  because the alt text, the caption and the loop sentence in `README.md` depend on it.
- Problem with the current image (rendered and inspected): six skills are drawn in a ring with
  arrows, which reads as an order and conflicts with P1; the principles do not appear; the
  labels say "command". Contrast of its fills against the `#f8fafc` background: detail text
  `#4b6373` 6.02:1, group labels `#587282` 4.84:1 (4.41:1 on the `#eaf0f5` panel), arrows `#59819a` 3.99:1, ring `#e1eaf0` 1.16:1.
- Content fixed by the coordinator for every option: the loop is choose, act, check, repeat;
  the 14 skills are an unordered set with no arrows between them; each of P1-P8 appears with
  its short name from the workflow guide at the place it applies (P1 choose, P2 return path,
  P3 and P4 the revisit-with-the-user branch, P5 check, P6 the user's authority over act, P7
  the loop itself, P8 the reply).
- Constraints: self-contained SVG (no external fonts, images, scripts or `foreignObject`),
  opaque background, no `prefers-color-scheme`, text contrast at least 4.5:1 and arrows and
  strokes at least 3:1, legible at 1100 px and 800 px width, `xmllint --noout` passes.
- Options (visuals reference, 2-4 options when the choice depends on layout or appearance): two
  drafts in the ignored `tmp/loop-svg/`, A and B; the user chooses by letter.

### Evidence

- Two leaves each drew one option into the ignored `tmp/loop-svg/` (drafts, not retained):
  - A (`a.svg`, 1100x820): white background; ring with Choose (blue), Act (orange), Check
    (green); each principle is a magenta badge on its element; `You` on the left with the
    revisit branch drawn as a round trip from Choose and back; skills band along the bottom.
    No link from `You` to Act; P6 sits inside the `You` box.
  - B (`b.svg`, 1100x800): dark navy background; horizontal track Choose, Act, Check with the
    return path underneath; numbered colored markers keyed to a list of the eight principles;
    skills inside the track under Act; `You` above Act with a link to it. Adds the heading
    "Loop principles" above the list.
- Coordinator checks on both (2026-11-11): `xmllint --noout` passes; no `foreignObject`, image,
  script, link or `prefers-color-scheme`; all 14 skill names present; "command" absent; each
  renders without overlap or clipping in `rsvg-convert` and in headless Chromium at 1100 px.
  Contrast scripts rerun: A minimum 5.02:1 for text and 4.88:1 for strokes; B minimum 6.77:1
  for text and 5.65:1 for strokes and markers. The 800 px renders were inspected by the leaves,
  not by the coordinator. Neither was viewed on GitHub or with macOS or Windows fonts.

## 2026-11-11 — English draft verification for the current request

- Current request: rewrite the English README around the principles that drove the skill
  rewrite; wait for English approval before translations. Reused the existing working-tree
  draft and the recorded TDD level `none`.
- Changes in this pass: clarified that there is no required skill sequence; stated the goal
  of refining the system and design; restored P2's distinction between facts and assumptions.
  These follow accepted P1/P2 in the linked spec. Earlier acceptance above concerns the
  earlier text; this revision is presented for approval under the current request.
- Review: read-only technical documentation leaf `/root/readme_review`, `gpt-6.1-sol`, medium
  reasoning (standard tier for semantic comparison across the accepted principles and source
  rules), returned zero substantive findings. It checked the whole README and diff against
  P1-P8, shared blocks and relevant sources, including the three final prose changes.
  No correction rounds. Host reports the leaf completed; no active leaf work remains.
- Final checks: `python3 -I tmp/readme-rewrite/check_links.py .` passed (69 relative links
  and anchors; 12 index entries match 12 sections); `git diff --check -- README.md` passed;
  `python3 scripts/package.py --output tmp/readme-english-review-final-20261111` built
  `lusona-3.0.0.zip` with manifest and link validation. Translation diffs are empty.
- Limits: rendering, installation and interactive behavior were not tested in this pass.
  Earlier package unit-test evidence remains above; those unchanged tests were not rerun.

## 2026-11-11 — Approved English and translation synchronization

- Authority: the user answered "yes, I approve" to the explicit question approving the
  current English README and updating the four translations. English acceptance is now
  recorded; translation work is authorized. TDD `none` carries over from this change.
- Scope: synchronize `README.es.md`, `README.de.md`, `README.ja.md` and `README.zh-CN.md`
  with approved `README.md`. Preserve commands, links, identifiers and numeric constraints;
  translate prose, headings and local anchors. The earlier image choice remains separate.
- Execution: one multilingual technical writer, `/root/translate_readmes`, owns the four
  translation files. Routing: `gpt-6.1-sol`, high reasoning, standard tier with language and
  semantic judgment across four complete documents. Coordinator owns records and verification.
  Follow translation with independent semantic review, link/anchor/index checks, command parity,
  diff inspection and package validation. No runtime behavior changes or test-first coverage.

### Translation verification

- All four translations are synchronized. Independent read-only reviewer
  `/root/translation_review` (`gpt-6.1-sol`, high reasoning, standard tier for multilingual
  semantic comparison) reviewed every translation and its diff against approved English:
  zero concrete findings. Review covered P1-P8, all 14 skills, authority, TDD, numeric limits,
  acceptance, revisions, records, examples, installation and development. The reviewer also
  checked the writer's final German clarification of `--check`; no findings.
- Coordinator checks on final text: `python3 -I tmp/readme-rewrite/check_translations.py`
  passes for each language (72 links, 12 index entries, heading hierarchy, local anchors,
  fenced commands, P1-P8 and exact reply labels). The writer's exact inline-code comparison
  also passes for all four. English SHA-256 remains
  `f4e7215895c8c8fd37e7e8ec762ba153988a807d30efe29b1669e68c85dfc4ab`.
- `git diff --check` passes. `python3 scripts/package.py --output
  tmp/readme-translations-20261111-verified` builds `lusona-3.0.0.zip`, including final text,
  with manifest and link validation. `python3 scripts/test_package.py` passes all 14 tests;
  it ran before two Spanish whitespace cleanups and the final German clarification. Final
  parity, diff and package checks ran after those edits.
- Limits: no human native-speaker review, rendered layout, installation or interactive
  behavior testing. No correction rounds or unresolved translation findings. Writer released
  ownership; writer and reviewer assignments completed without active operations.

## 2026-11-11 — Circular SVG revision

- Authority: the user requested an SVG recreation with brighter colors and contrast and
  explicitly prefers the current circular layout and split. TDD `none` carries over.
- Layout agreement: retain the left circular diagram and right skill grouping. The circle
  will show choosing, acting, checking and repeating/refining; skill selection follows the
  unresolved need. Show all P1-P8 through concise labels and relationships, and retain all
  14 skills in the grouping. User authority and revisiting decisions with the user are explicit.
- Earlier image options A/B remain unselected. The current request supplies a layout direction
  for this implementation; neither old draft is applied and no A/B choice blocks this revision.
- Scope: `plugins/lusona/assets/workflow-loop.svg`, matching alt text and captions in the five
  root READMEs and plugin README, plus this record. Preserve the approved README body.
- Implementation owner: `/root/svg_revision`, SVG information designer, `gpt-6.1-sol`, high
  reasoning (standard tier, established layout and semantic requirements). The leaf owns only
  the SVG and scratch previews; coordinator owns documentation integration and records.
- Checks: XML validity, self-contained SVG, semantic coverage of principles and skills, text
  contrast >=4.5:1 and meaningful arrows >=3:1, rendered inspection at 1100 and 800 pixels,
  independent visual/content review, relative links, package validation and diff inspection.
  Color and spacing choices are implementation decisions within the requested direction.

### SVG result and evidence

- Implemented at `plugins/lusona/assets/workflow-loop.svg`, 1100×830: circular
  Choose → Act → Check → Refine loop on the left, user authority at the center, conditional
  decision-revision branch below, all 14 skills grouped on the right and P8 in a footer.
  Blue, orange, teal and purple distinguish actions and groups. All P1-P8 are visible.
- Binding layout/content constraints met: circular left/right split; no required sequence
  between skill names; all principles and skills represented; brighter contrasting colors.
  XML has accessible title/description and no external resources or active content.
- One visual correction round resolved center-label overflow and coordination-card padding.
  Total 1, consecutive without progress 0. Final `rsvg-convert` renders at 1100 and 800 pixels
  were inspected by writer, coordinator and independent reviewer without overlap or clipping.
- Contrast audit `python3 tmp/loop-svg-revision/audit_svg.py`: minimum text 5.652:1,
  meaningful strokes 4.269:1, loop arrows 4.570:1. Exact pairs in scratch
  `tmp/loop-svg-revision/contrast.json`. Reviewer independently calculated text and arrow minima.
- Independent reviewer `/root/svg_review`, `gpt-6.1-sol`, high reasoning (standard tier for
  semantic, visual and accessibility review), reported zero actionable findings after reviewing
  actual SVG, both renders, P1-P8 and all six README caption/alt-text deltas.
- Chromium preview initially exited 133: sandbox denied a local socket operation. One retry
  with approved sandbox escalation exited 0. Coordinator inspected
  `tmp/loop-svg-revision/chromium-1100.png`: no visible clipping or overlap. This environment
  correction had total 1 round, consecutive without progress 0.
- Final checks pass: `xmllint --noout plugins/lusona/assets/workflow-loop.svg`, SVG audit,
  `python3 -I tmp/loop-svg-revision/check_readmes.py` (72 links and 12 index entries per
  translation), English link/index check (69 relative links, 12 entries), `git diff --check`,
  `python3 scripts/package.py --output tmp/loop-svg-revision-package`, and all 14 tests in
  `python3 scripts/test_package.py`. Compared all six READMEs to the pre-SVG package snapshot:
  only image alt text and associated captions changed in this pass.
- Limits: no live GitHub rendering, screen-reader test or alternative-platform font test.
  No installation test; no plugin behavior changes. No commit, push or publication.

## 2026-11-11 — Reduce the plugin README to unique information

- Authority: user requested removing content from `plugins/lusona/README.md` that repeats
  the root README. TDD `none` carries over from this documentation change.
- Scope: plugin README only, plus this record. Retain its unique resource catalogue and
  package-local links; remove duplicated overview, loop image/principles and invocation
  guidance. Point readers to the repository README for those topics. Preserve installed-plugin
  portability and discoverability of references, templates and record helper entrypoints.
- Owner: technical documentation editor `/root/reduce_plugin_readme`, `gpt-6.1-sol`, medium
  reasoning (standard tier for editorial judgment within a fixed documentation boundary).
  Coordinator owns integration, verification and this record. No new behavior or tests.
- Verification: compare with root README and pre-edit plugin document; check catalogue
  completeness, incoming anchors, local links, package build and whitespace. Independent
  review is not required for this single-writer documentation reduction.

### Plugin README result and evidence

- Reduced from 88 lines / 958 whitespace-delimited words to 59 lines / 382 words. Retained
  the human-catalog/loading distinction, 23 references with purpose labels, 13 templates and
  two helper entrypoints. The product introduction, diagram, principles and invocation guidance
  are replaced by one repository README link. No workflow policy changed.
- Coordinator inspected the final document and diff against root README. File inventory
  comparison confirms all 38 unique bundled resources are listed; 39 local links resolve
  because naming is linked twice. No active documentation links to the removed `#the-loop`
  or `#skills` anchors were found. Historical records have older missing anchors unrelated
  to this removal; those records were not edited.
- Verification: `git diff --check` clean; skill-template check passes; voice check reports
  no findings; `python3 scripts/package.py --output tmp/plugin-readme-reduction-package`
  builds the 3.0.0 archive; all 14 tests in `python3 scripts/test_package.py` pass.
- Limits: rendered Markdown, external URL reachability, installation and interactive behavior
  were not tested. No correction rounds. Writer released ownership with no active operations.

## 2026-11-11 — Refine SVG proportions and consistency

- Authority: user requested a narrower right side, more symmetrical left boxes, consistent
  font weight and a visible authority arrow. TDD `none` carries over. These are refinements
  of the current SVG; preserve its content, palette and circular split.
- Scope: SVG only plus this record. Reassigned `/root/svg_revision` (same model/routing)
  ownership of SVG and `tmp/loop-svg-refinement/`; coordinator owns records and final checks.
- Criteria: reduce right-column width from 392 pixels; equal dimensions and mirrored
  placement for the four action boxes; consistent typography by role; center authority box
  has clear whitespace and a visible connector to Act. Preserve P1-P8 and all 14 skills.
- Verification: inspect renders at 1100 and 800 pixels, check box geometry and connector
  clearance, XML/content/contrast audit, focused independent visual review and package build.
  The earlier review reported no clipping, but the user identified visual imbalance and the
  compressed connector; the present criteria explicitly address those shortcomings.

### Proportion refinement result and evidence

- Right cards narrowed from 392 to 327 pixels (16.6%). All four action boxes are 200×112,
  radius 16, with mirrored centers around (365,363). Each uses the same centered text roles
  at vertical offsets 31,53,78,99. Authority is centered with equal 50-pixel side gaps.
- Authority connector now has a 31-pixel shaft and 8-pixel arrowhead, with clear space before
  the Act border; it was previously a 9-pixel shaft inside a 14-pixel box gap.
- Font weights use common role classes: headings, principle labels and skill names 700;
  explanatory text 400. Removed per-text size/weight overrides. Compact skill-purpose labels
  fit the narrower column; all 14 skills and P1-P8 remain.
- One content-fit adjustment shortened the P5 label after first-render inspection. Full P5
  semantics remain in the description and Check copy. Final 1100/800 renders were inspected
  by writer, coordinator and `/root/svg_review`; independent review returned zero findings
  and verified all four user requests against actual geometry and rendered images.
- Coordinator checks pass: XML validation, `geometry_audit.py` and `audit_svg.py` in
  `tmp/loop-svg-refinement/`, `git diff --check`, and package build to
  `tmp/loop-svg-refinement-package`. Contrast unchanged: text minimum 5.652:1; meaningful
  strokes 4.269:1. Browser screenshot outside the sandbox succeeded and was inspected at1100px.
- Scratch evidence: `tmp/loop-svg-refinement/before.svg`, `final-1100.png`, `final-800.png`,
  `chromium-1100.png`, `geometry.json` and `contrast.json`. Final XML and package checks cover
  the revised asset. Package unit tests were not rerun for this geometry-only change.
- Limits: no live GitHub or screen-reader test. Leaf Chromium attempts hit profile/sandbox
  setup failures; coordinator's previously approved escalation supplied the browser check.
  No code changes, commits, push or publication. SVG ownership released; review complete.

## 2026-11-13 — Human engineer readability proposal

- Authority: user requested rereading `README.md` and proposing an update. This authorizes
  assessment and a saved proposal, not a README rewrite. No TDD selection is needed for
  this discussion; the earlier implementation selection does not expand current authority.
- Baseline: `dac7ebb`, clean working tree at entry. README has 397 lines and 3,333
  whitespace-delimited words; Installation starts at line 299.
- Prior decision: the principles-first English outline was accepted on 2026-11-11 above.
  Recommendation: revise its presentation to put first use before procedural detail.
  The prior decision remains accepted until the user accepts a revision. No principle,
  workflow rule, skill responsibility, command or supported-host claim is being changed.

### Findings and recommended changes

| Current passage | Reading problem | Proposed update |
| --- | --- | --- |
| Opening and Loop principles, lines 5-56 | Introduces eight policy concepts before showing a first use | Explain purpose in two short paragraphs, then provide installation and one first request |
| Start and choose a skill, lines 58-122 | Combines setup, resumption, catalog, invocation syntax and five examples | Separate getting started from skill selection; keep one complete request near the start |
| Installation, line 299 | Instructions for starting appear after most operating policy | Move concise host installation instructions before invocation, keeping warning and testing caveats visible |
| Authority and TDD, lines 124-169 | Mixes user decisions, testing requirements, batch limits and delegation | Keep authority and the three TDD levels prominent; link detailed coordination rules |
| Decisions through Replies, lines 171-297 | Requires readers to process record mechanics and edge cases during onboarding | Summarize expected behavior and link the existing authoritative references |

Recommended order:

1. What Lusona does: purpose, hosts, version and source/release distinction.
2. Get started: native installation, new session, host invocation syntax, optional setup,
   and a first status request. State that users can choose another skill directly.
3. Choose a skill: retain all 15 skills, group them by reader intent, and add a short output
   column. Say explicitly that the groups are not stages or a required sequence.
4. Work on a change: one complete request showing outcome, scope, acceptance criteria,
   TDD level and delivery boundary. Retain the invitation-expiry example.
5. What to expect: authority, TDD table, observed verification, decision revisions, saved
   records and result/evidence/next-action replies. Use short explanations and links.
6. Workflow principles: retain the diagram and a compact explanation; link the P1-P8 table.
7. Further reading, contributing and license. Link contributor commands from CONTRIBUTING.

Existing destinations for detail:

- Full P1-P8 definitions and routing: `plugins/lusona/references/workflow-guide.md`.
- Revision procedure: `plugins/lusona/references/revisions.md`.
- Correction budgets: `plugins/lusona/references/corrections.md`.
- Delegation and model routing: `plugins/lusona/references/delegation.md`.
- Record fields, save conditions and handoffs: `plugins/lusona/references/retention.md`.
- Reply-format rules and examples: `plugins/lusona/references/completion.md`.
- Installation detail and verification limits: `INSTALL.md`; contributor commands:
  `CONTRIBUTING.md`. Preserve current limitations beside any retained host instructions.

Proposed opening:

> Lusona provides 15 skills for product and engineering work with coding agents. Use them
> to explore an idea, define a change, investigate a failure, implement a feature, or review
> a diff. Choose the skill that matches the work; there is no required sequence.
>
> Each skill tells the agent how to carry out its part of the work, verify the result, and
> record what another session needs. You control the authorized scope. Task replies report
> the result, evidence, and next action.

Alternative: keep all policy detail and only reorder the sections. This preserves a
single-page reference, but retains most of the reading burden. The recommended option
uses concise explanations with links; it adds navigation when a reader needs the full rule.

### Proposal evidence and limits

- Coordinator and technical-editor leaf `/root/readme_proposal` read the whole README.
  Leaf routing: `gpt-6.1-sol`, medium reasoning, standard tier for editorial judgment within
  an existing document. Leaf returned findings, an outline and sample wording, without edits.
- Coordinator checked the cited section positions, current word count, existing references,
  contributor translation requirement and prior acceptance. Integrated the leaf's ordering
  findings; additionally recommends reducing duplicated procedural detail.
- No independent implementation review is required for this proposal-only task. No plugin
  sources, shared blocks, templates, commands, manifests or README files changed, so the
  addition audit in `docs/skill-audit.md` is not applicable to this saved discussion.
- No readability user test, rendered Markdown review, installation or interactive test ran.
  Readability benefits are editorial judgments, not measured results. No correction rounds.
- Future rewrite checks: preserve rule meaning and installation caveats; check links and
  incoming anchors; synchronize four translations; inspect rendered Markdown and final diff.
- Leaf completed and released file ownership; no active operations. Host has no shutdown
  control, so process termination is not claimed.

## Previous handoff (2026-11-11)

- Authorized work: English accepted, four translations synchronized and circular SVG revision
  implemented under user authorization; TDD `none` from the recorded selection.
- State: README translations, plugin README reduction and SVG proportion/typography refinement
  complete and verified. All changes remain in the working tree.
- Ownership: writer released SVG; coordinator owns integration and this record. Reviewer
  completed its assignment; no active file operations remain.
- Next action: none for this refinement. No commit, push or publication is authorized.

## 2026-11-13 — Apply readability revision

- User accepted the proposal and authorized applying it: "apply this, and let me read it
  before committing". Revise the accepted principles-first presentation in part: use the
  proposed reader-first order and concise summaries, preserving workflow meaning. The earlier
  outline and its rationale remain above as history.
- Scope: five root READMEs and this owning record. TDD `none` carries over from the user's
  2026-11-11 selection for this documentation change. Verify links, commands, skill coverage,
  translated meaning, rendered layout and packaging. No test-first behavior changes.
- Independent review will cover the coordinated English and translation edits. No skill,
  reference, template, shared text or record helper command is changing; the plugin addition
  audit does not apply. No new spec is needed for a presentation-only documentation change.
- Commit, push and publication are prohibited pending the user's review and later instruction.

### English rewrite and checks

- English writer `/root/readme_edit`, `gpt-6.1-sol`, medium reasoning, standard tier,
  changed only README.md. Coordinator inspected the full draft. It has 2,103 words versus
  3,333 before (36.9% fewer); all 15 skills remain, with intent groups and output descriptions.
  Installation precedes invocation and the first request. Legacy heading anchors are retained.
- Baseline: English link/index check passed (71 relative links, 12 index entries), diff
  whitespace check passed, and baseline package built as 3.1.0. Scratch is in
  `tmp/readme-human/`; `before.md` preserves the English baseline.
- English checks: 61 links resolve; all previous anchors, 15 skill links and language
  navigation remain; installation commands match HEAD; `git diff --check` passes. Package
  validation built 3.1.0 successfully after the English rewrite.
- Independent reviewer `/root/readme_review`, `gpt-6.1-sol`, medium reasoning, wrote none
  of the change. It compared the diff and summary claims with canonical references and
  reported no findings; independently verified links, skill coverage, commands and whitespace.
- Local rendering: Bun.markdown HTML plus headless Chromium at 1100 pixels. Coordinator
  inspected sampled opening, skill-table, expectations and closing sections: no clipping.
  This is a local approximation of Markdown layout, not live GitHub rendering. Initial
  Chromium sandbox run failed on a socket operation; one approved escalation succeeded
  (environment correction: total 1, consecutive without progress 0).
- Translation assignments: `/root/translate_europe` owns Spanish/German;
  `/root/translate_asia` owns Simplified Chinese/Japanese. Both use `gpt-6.1-sol`, medium
  reasoning, standard tier for translation within a fixed English source. Coordinator owns
  the record and integration; independent review follows translation.
- Installation and interactive host behavior were not tested. No plugin behavior changed.

### Final translation and integration evidence

- Both translation writers completed their assigned files and released ownership. Independent
  reviewer `/root/readme_review` read all four translations against the final English text
  and reported no findings. It checked authorization, TDD, commit semantics, independent
  review, optional setup, studies, installation caveats, scope boundaries and skill outputs.
- `python3 tmp/readme-human/check.py` passes all five READMEs: 61 links each, all legacy
  heading anchors preserved, all 15 skills present, identical language navigation and Bash
  commands, matching heading hierarchy and nonlocal link targets. Each local link resolves.
- `python3 scripts/package.py --output tmp/readme-human/translated-package` built the
  3.1.0 archive successfully. `git diff --check` passes. Only the five root READMEs and
  this existing notes file are modified. No commit, push or publication occurred.
- All writer and reviewer assignments are complete, with no active file operations.
  The host exposes no shutdown control; process termination is not claimed for
  `/root/readme_edit`, `/root/translate_europe`, `/root/translate_asia` or `/root/readme_review`.
- Human reading and acceptance remain pending as requested. Translation rendering, live
  GitHub rendering, installation and interactive host behavior were not tested. No content
  correction rounds; the single environment correction is recorded above.

## 2026-11-13 — Remove HTML anchors and introduce status

- User reports that raw HTML anchors render visibly and requests a one-line `/status`
  introduction plus GitHub notice annotations. This revises the earlier choice to preserve
  legacy bookmarks with explicit anchors: remove those tags and use current heading anchors.
  Historical bookmark compatibility is no longer a criterion; current document links must work.
- Add one opening TIP with `/status` and a link to host-specific invocation syntax; remove
  the repeated multi-paragraph status introduction. Use NOTE for the source/release distinction
  and IMPORTANT for explicit TDD selection; keep the existing installation WARNING.
- Scope remains five READMEs and this record, TDD `none`; no commit authorized. Specialist
  writer `/root/readme_callouts`, `gpt-6.1-sol`, medium reasoning, owns the five READMEs.
  Coordinator owns checks and records. Before-images are in `tmp/readme-callouts/`.
- Result: all five READMEs now have no raw anchor tags, one translated opening TIP line,
  source NOTE, TDD IMPORTANT and installation WARNING. The status authority sentence moved
  into the existing authority paragraph. One reconciliation round preserved that explicit
  meaning; total 1, consecutive unresolved 0.
- Final checks: all five pass the updated link/heading/notice/skill/command checker (62 links
  each), and `git diff --check` passes. Package validation built 3.1.0 at
  `tmp/readme-callouts/package`. Legacy-anchor assertions were removed to match the user's
  requested correction; current heading-link checks remain.
- Independent reviewer `/root/readme_review` checked the exact correction delta in all five
  files and reported no findings, including final status authority wording. Writer and
  reviewer released ownership, with no active operations. Host shutdown remains unavailable.
  Live rendering and installation were not tested for this correction. No commit occurred.

## 2026-11-13 — Make first use the README's focus

- User reports that readers feel they must learn the workflow before using it and requests
  a more direct README with secondary documents for deep dives. This revises the prior
  decision to retain the full skill catalog and workflow summaries in the README.
- Authorized scope: shorten all five root READMEs; create `docs/usage.md` for invocation,
  skill selection and examples, and `docs/workflow.md` for operating details and principles.
  Keep the one-line status TIP and GitHub notices, no raw HTML anchors. Detailed guides are
  initially English, explicitly labeled from translated READMEs. Existing INSTALL.md is
  the installation destination and remains unchanged by this work.
- Baseline: working-tree READMEs and INSTALL.md saved under `tmp/readme-simple/` before
  editing. INSTALL.md has pre-existing edits, as does Antigravity wording in README.md;
  preserve these rather than restoring HEAD. Baseline five-README link checks and
  `git diff --check` pass.
- TDD `none` continues from the user's 2026-11-11 documentation selection. No behavioral
  rules change; this is human-facing documentation, outside the bundled-plugin addition
  audit. Verify destinations, translated meaning, current links, rendering and packaging;
  independent review covers coordinated writing. No commit, push or publication authorized.
- Writer `/root/simple_entry_docs`, `gpt-6.1-sol`, medium reasoning, owns English README
  and the two guides. Coordinator owns record/integration; translations follow stable English.
- Packaging dependency: the portable catalog includes the root README through an explicit
  allowlist, so its two new linked guides must be included there. `/root/package_guides`,
  `gpt-6.1-sol`, medium reasoning, owns only `scripts/package.py` and its test file to add
  those two paths. Preserve exclusion of `docs/lusona/` and all other project data. Baseline
  `python3 scripts/test_package.py` passes 16 tests. Existing TDD `none` remains applicable;
  verify exact public-guide selection, project-data exclusion and archive contents.
- English result: 299 whitespace-delimited words, down from the 2,034-word working-tree
  baseline (85.3% fewer). README retains first action, installation link, one plain-language
  example, user control and optional deeper reading. Guide destinations: host syntax,
  setup, 15 skills and examples in usage; authority/TDD, evidence, records, decisions,
  replies and diagram/principles in workflow. Installation remains in INSTALL.md.
- Writer finished and released ownership. Coordinator read all three documents and inspected
  a 1100-pixel local Chromium rendering of the short README: no clipping. GitHub callouts
  appear as ordinary labeled blockquotes in this local renderer; live GitHub was not tested.
- Package maintainer finished and released ownership. All 16 package tests pass after its
  change, including exact public-doc selection, source/archive bytes and project-data
  exclusion. No correction rounds. `/root/translate_short_readmes`, `gpt-6.1-sol`, medium
  reasoning, owns only four translated READMEs; guides remain English and are labeled as such.
- Final verification: `python3 tmp/readme-simple/check.py` passes all five READMEs (17 links
  each), usage (27 links) and workflow (28 links), including current headings, translated
  link/notice/code parity, 15-skill coverage, no raw anchors, and unchanged INSTALL.md.
  `python3 scripts/package.py --output tmp/readme-simple/final-package` builds 3.1.0 with
  working resource links; `git diff --check` passes. The two new guides are untracked files
  ready for later inclusion in a user-authorized commit.
- Independent reviewer `/root/simple_docs_review`, `gpt-6.1-sol`, medium reasoning, wrote
  none of the change. Reviewed English, both guides, packaging code/tests, then all four
  translations: no findings. It verified preservation of workflow meaning, first-use focus,
  exact guide packaging and explicit English labels in translated links.
- Existing INSTALL.md edits are byte-identical to the entry snapshot. No plugin rule,
  manifest, version, or installed skill changed. No commits, push or publication occurred.
- All four assignments (English writer, package maintainer, translator and reviewer) are
  complete with no active file operations. Host shutdown controls remain unavailable;
  termination is not claimed. Installation, interactive behavior, live GitHub rendering
  and translated rendering were not tested. No content correction rounds were needed.

## 2026-11-13 — Make the first task self-contained

- User rejected relocation/shortening as insufficient: first use still requires following
  links to learn what to do. Revise the presentation criterion from word reduction to a
  complete first-use path on the README: install, invoke status, make one request, understand
  the expected response and continue. Detailed guides remain optional.
- Scope: five READMEs plus this record. Preserve existing INSTALL, guides and packaging
  changes. Keep exact supported host syntax inline, no raw HTML anchors, short GitHub
  callouts, user authority and verification accuracy. No fixed word ceiling; avoid catalogs
  and procedural explanations. TDD `none` continues; no commit/push/publication authorized.
- Baseline saved in `tmp/readme-first-use/`; five-README/guide checks and whitespace pass.
  Verification will include walking the reader's first task without following a guide,
  command/link/translation parity, independent review and local rendering.
- Writer `/root/first_task_readme`, `gpt-6.1-sol`, medium reasoning, owns the five READMEs.
  English now provides inline installation and host-specific status syntax, one invitation
  expiry request, expected assessment, a plain-language behavior decision, a bounded
  implementation reply and final-check expectations. Guides remain optional reference.
- Independent reviewer `/root/first_use_review`, same model and reasoning, wrote no text.
  English review found no defects: first task can be followed without documentation links,
  commands match INSTALL and invocation matches usage, status assessment stays read-only
  until the implementation follow-up. Shortcut TIP and translations await final review.
- Final result: five READMEs now walk through a first task on the same page, with a shortcut
  for existing installations. Writer applied one coordinator correction to that TIP before
  translation; total 1, consecutive unresolved 0. English is 586 whitespace-delimited words;
  added runnable commands and continuation examples intentionally replace the shorter
  page's required navigation. No claim that shorter alone means easier onboarding.
- Final independent review includes the TIP and all translations: no findings. It confirmed
  exact command parity, host distinctions, example meaning, read-only assessment, bounded
  authorization, testing question, final-result expectations and localized shortcut anchors.
- `python3 tmp/readme-first-use/check.py` passes: 16 links per README, 27 usage and 28
  workflow links, all current anchors, translation/notice/command parity, 15 retained skills,
  unchanged INSTALL.md and all three inline command blocks matching INSTALL.md.
  Packaging to `tmp/readme-first-use/package` succeeds; `git diff --check` passes.
- Local English HTML/Chromium rendering inspected at 1100 pixels: invocation table and
  walkthrough display without clipping. Renderer shows GitHub notices as labeled blockquotes.
  Installation, interactive behavior, live GitHub, translated rendering and a real-user
  onboarding trial were not tested. Earlier package unit checks remain applicable; packaging
  code did not change in this increment. Guides, INSTALL and package scripts were preserved.
- Writer and reviewer assignments complete, ownership released, no active operations.
  Host shutdown remains unavailable; no termination claim. Nothing committed or published.

## 2026-11-13 — Add light everyday usage

- User requested a light usage section. Added a compact Everyday use section before optional
  reading in all five READMEs: four plain-language requests for exploring, investigating,
  reviewing and resuming, plus one sentence about constraints. No new commands or links.
- Writer `/root/light_usage`, `gpt-6.1-sol`, medium reasoning, owned only the READMEs.
  TDD `none` carries over. Baselines are in `tmp/readme-light-usage/`; coordinator read each
  translated insertion and confirmed the other content is unchanged. No independent review
  trigger applies to this single-writer, presentation-only addition; earlier reviews remain
  valid for untouched text.
- Verification: each file has only the 13-line insertion; existing content remains byte-for-byte
  recoverable by removing it. Current link/heading/notice/command parity check and
  `git diff --check` pass. No added links or packaging code changes justify rerunning package
  tests. Rendered layout, installation and interactive behavior were not tested this increment.
- Writer complete, ownership released, no active operations; shutdown control unavailable.
  No correction rounds or commits. Guides, INSTALL, scripts and plugin sources unchanged.

## 2026-11-13 — Expand usage into grouped commands

- User requested commands and groups because the light examples provided insufficient data.
  Replace only Everyday use in all five READMEs with five intent groups and all 15 commands,
  each with a short purpose. This revises the earlier choice to keep the command catalog only
  in the optional guide; the first-task walkthrough remains intact.
- Groups: start/resume; explore/plan; define a change; build/check; investigate/compare.
  Short `/name` forms explicitly identify Antigravity App/CLI syntax, with Claude Code and
  Codex CLI prefixes and a reference to the existing invocation method for other hosts.
  Groups are not mandatory stages. Optional setup, authorization and review boundaries stay.
- Writer `/root/usage_commands`, `gpt-6.1-sol`, medium reasoning, owned the five sections.
  Coordinator checked purposes against current skill descriptions and requested one wording
  correction: design creates visuals, rather than merely inspecting them. All translations
  corrected; total 1, consecutive unresolved 0. TDD `none` carries over; no plugin rules change.
- Checks pass: exactly 15 canonical command names and five groups per README, matching order,
  translated heading/notice/command parity, current links and `git diff --check`. Comparison
  with `tmp/readme-command-groups/` confirms all text outside these sections is unchanged.
  No links, package paths or scripts changed; previous package evidence remains applicable.
- Single-writer presentation change has no independent-review trigger. Coordinator reviewed
  final content. Rendering, installation and interactive invocation were not tested in this
  increment. Writer completed and released ownership; no active operations, shutdown control
  unavailable. No commit, push or publication.

## 2026-11-13 — Double-check README links

- User requested link verification, specifically the opening TIP's
  `#2-get-a-recommendation`. Read-only audit: README.md line 9 matches the heading at line 51.
  GitHub's documented section-link rules remove the period, lowercase letters and replace
  spaces with hyphens; the fragment is correct. Source:
  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
- Independent verifier `/root/readme_link_audit`, `gpt-6.1-sol`, medium reasoning, checked
  all five READMEs and both guides: 125 local link/image occurrences, including 20 fragments,
  resolve; no duplicate heading slugs. Translated TIP fragments match their localized headings.
  The existing checker also passes. No document source changes were needed.
- Two unique external URLs (10 occurrences) checked by public GET with curl: blog returns
  HTTP 200; GitHub issue chooser redirects to login and returns HTTP 200. Initial web-tool
  fetches returned cache misses; curl supplied the missing evidence (one bounded fallback).
- Preview limitation found: earlier scratch HTML in `tmp/readme-first-use/` has no heading
  IDs, keeps file links relative to its scratch directory, and predates the grouped usage
  section. It is evidence for the earlier layout only, not for working link navigation.
  This does not establish which renderer the user is using. No claim of live GitHub click
  testing or user-viewer testing. Do not reuse that preview to validate links.
- Verifier complete, no edits or active operations. Host shutdown unavailable. No commits.

## 2026-11-13 — Final translation synchronization

- User requested updating translations after the link check. `/root/final_translation_sync`,
  `gpt-6.1-sol`, medium reasoning, compared all four complete translations with final English.
  They already contain the incremental changes; no further edits were needed. Full semantic
  comparison found no omissions or drift in examples, commands, groups, scope or caveats.
- Checks pass: links/anchors, headings, inline-command spellings and occurrence counts,
  all 15 commands in five groups, English-guide labels, scoped whitespace and byte comparison
  with `tmp/readme-translation-final/`. No source file changed in this pass. No installation
  or interactive test ran. Leaf complete, no active work, no commits; shutdown unavailable.

## Current handoff

- First-use walkthrough plus grouped command reference applied and verified in all five READMEs.
  Coordinator owns integrated working tree and this record; no active operations remain.
- Next action: user reads the README and supplies feedback or later commit
  instructions. No commit, push or publication authorized. TDD remains `none`.
