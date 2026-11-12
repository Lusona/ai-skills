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

## Current handoff

- Authorized work: English accepted, four translations synchronized and circular SVG revision
  implemented under user authorization; TDD `none` from the recorded selection.
- State: README translations, plugin README reduction and SVG proportion/typography refinement
  complete and verified. All changes remain in the working tree.
- Ownership: writer released SVG; coordinator owns integration and this record. Reviewer
  completed its assignment; no active file operations remain.
- Next action: none for this refinement. No commit, push or publication is authorized.
