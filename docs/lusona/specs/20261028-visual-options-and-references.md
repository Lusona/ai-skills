# Spec 20261028-visual-options-and-references: Visual options and retained visual references

Created: 2026-10-28
Updated: 2026-10-28

Kind: feature

## Agreement

- User and problem: A Lusona user choosing among generated visual mockups sees the final result
  rarely match the chosen mockup, because the chosen visual is not kept as a reference that
  implementation and review use. The user also wants visual aids in discussion.
- Desired behavior: (1) Before committing to a concept, architecture, or UI, the skill offers
  2-4 visual options and the user picks one. (2) Spec, architecture, and other discussion
  include explanatory diagrams when they clarify the decision. (3) The
  chosen visual is retained as a reference with a binding list; implement treats binding items
  as acceptance input and review checks them.
- Scope: `explore`, `specify`, `architect` (produce options and diagrams); `implement`, `review`
  (consume the retained reference). Shared guidance or a template may be added in
  `plugins/lusona/`; new resource paths are proposed, not acceptance criteria.
- Exclusions: click-to-select local server (deferred to a separate later change);
  `frame-product`, `map-capabilities`, `investigate` changes; image-diffing tooling; commits,
  publication. Version bump to 1.3.0 added at the user's request, 2026-10-28.
- Accepted constraints and invariants (all source: user, 2026-10-28):
  1. Static files are the stored reference: Mermaid in Markdown for diagrams. For mockups, PNG
     images of the chosen option's screens and states plus the HTML source that produced them
     (revised by the user, 2026-10-28; earlier: standalone HTML only).
  2. Commit only the chosen reference and its binding list, proposed at
     `docs/lusona/visuals/<slug>/` in the consuming project; rejected options are discarded.
  3. Include a diagram when it clarifies the decision (revised by user, 2026-10-28 audit follow-up).
  4. In conversation, simple diagrams appear inline as Unicode/ASCII text; larger diagrams are
     written as an HTML page rendering Mermaid and opened in the browser.
  5. Option selection is by letter through the native question tool or terminal; no click capture.
  6. Binding aspects default to layout regions, element order, which controls exist, and
     information hierarchy; illustrative aspects default to colors, copy, and spacing, unless
     the user marks them binding.
  7. If no screenshot tool is available, review checks binding items against code/markup,
     reports the visual comparison as unrun, and identifies what remains unverified.
  8. Works across Claude Code, Codex, Cursor, and Xcode; no host-specific rendering required.
  9. Existing behavior for user-supplied visual references (`specify`) is preserved.
  10. The retained reference records each rejected option in one line with the reason; no
      rejected files are kept.
  11. Retaining a user-supplied reference with a binding list is opt-in.
  12. A bundled HTML template owns only the page shell: header, status, question, notes panel,
      theme, and viewer, plus an optional browser frame. Mobile panels have no simulated hardware. Option content is free and styled for the
      target platform; the grayscale wireframe kit is a fallback (revised by the user, 2026-10-28,
      after reviewing an example iOS mockup; earlier: kit-only mockup bodies).
  13. Options are one file per option plus an index page, or, when options differ in one part,
      one flow page with an in-place option switch (revised by the user, 2026-10-28).
  14. Diagram pages use the same shell with a Mermaid body variant (user, 2026-10-28).
  15. Mockups reuse the project's existing UI: screen names, navigation, tab bars, and copy
      from the codebase; placeholders only for content that does not exist yet (user, 2026-10-28).
  16. An option may be a flow of 2-5 ordered screens; step numbering only for real sequences
      (user, 2026-10-28).
  17. Mockups show states relevant to the choice, including failure when it affects the decision
      (user, 2026-10-28).
  18. Each page states its fidelity and lists open questions and must-not-happen rules
      (user, 2026-10-28).
  19. Content rules: scale fidelity to the question, explain the question on each page, and use
      real content when it matters (user, 2026-10-28).
  20. Theme follows the OS setting; a Theme button overrides it per browser (user, 2026-10-28).
  21. Open draft HTML in the browser for direct inspection; if unavailable, report its absolute
      path. Do not capture drafts or substitute PNGs. Capture only after the user agrees to
      the design (user clarification, 2026-10-28).
- Completion condition: AC1-AC9 and AC11-AC19 verified (AC10 superseded) per the TDD section, independent review, and repository
  checks pass. Human acceptance of the changed skill wording is required.

### Acceptance criteria

- [x] AC1: When a concept, architecture, or UI choice needs visual comparison, the skill presents
  2-4 labeled options, each viewable (inline text, or HTML file), and asks the user to choose by
  letter through the native question tool or terminal. No fewer than 2 or more than 4 options.
- [x] AC2: When the user picks a mockup option, the chosen visual is saved as a reference (static
  files per constraint 1; wording revised 2026-10-28 from "standalone HTML for mockups", which
  AC11 now details) together with a list of
  binding and illustrative aspects and a one-line reason per rejected option, and the owning record (spec, ADR, or notes when no spec
  exists yet) links it. Without a user marking, the defaults in
  constraint 6 apply. Rejected option files are not saved or committed.
- [x] AC3: If the user rejects all options or asks for revision, no reference is saved; the skill
  offers revised options. A reference is saved only after a choice.
- [ ] AC4 (audit revision): Include a diagram when it clarifies the decision; otherwise omit it.
- [x] AC5: A simple diagram is shown inline as Unicode/ASCII text in the reply. A larger diagram is
  written as an HTML page rendering Mermaid and opened in the browser; if the browser cannot be
  opened, the skill reports the file path instead.
- [x] AC6: `implement`, given a spec that links a retained reference, treats each binding item as
  acceptance input and reports the status of each in its result. Illustrative items are not
  treated as acceptance.
- [ ] AC7 (audit revision): `review` checks each binding item against the result and reports each as met, unmet, or
  unchecked. With no screenshot tool, it checks against code/markup, reports the visual comparison
  as unrun, and identifies what remains unverified.
- [x] AC8: A spec with no visual reference leaves `implement` and `review` behavior unchanged.
  A user-supplied reference is captured as before in `specify`; it is saved with a binding list
  under AC2 rules only when the user asks to retain it.

- [x] AC9 (revised 2026-10-28): Every generated option, index, flow, and diagram page uses the
  bundled shell: a header with the record ID (or topic), option letter when it is an option,
  status (draft option, option index, chosen reference, or diagram), and the question; a notes
  panel with binding and illustrative items, fidelity, and open questions; light and dark themes
  that follow the OS with a Theme button override. The shell fills the viewport. Pages are
  self-contained except the pinned Mermaid script.
- [x] AC10 (superseded by AC13, 2026-10-28): Mockup bodies use only the template's wireframe kit
  classes and its color tokens, so options differ in structure rather than styling.
- [x] AC11 (revised 2026-10-28): For 2-4 options, each option is its own file and `index.html`
  shows them side by side, with a one-at-a-time view and expand to full size. After a choice,
  each shown screen and state of the chosen option is saved as a PNG, with the option's HTML source
  (status changed to chosen reference) beside it. The index and rejected options are not retained.
- [x] AC12: A diagram page uses the same shell with the Mermaid body variant; the Mermaid source
  stays readable when the script cannot load.
- [ ] AC13 (frame-removal revision): Option content resembles the target platform and the project's existing UI (for
  example iOS conventions, Material styling, or the
  project's web theme). The wireframe kit is used only when no platform look is known. Real
  screen names, navigation, and copy from the codebase are reused; placeholders are labeled.
  Mobile content uses plain, content-sized panels without phone bezels, hardware cutouts,
  or simulated system bars.
- [x] AC14: An option may be a flow of 2-5 ordered screens shown together; steps are numbered only
  when they are a sequence.
- [ ] AC15 (audit revision): Show states relevant to the choice as state switches or separate
  frames, including failure when it affects the decision.
- [x] AC16: When options differ in one part of a flow, one page shows the flow with an option
  switch that updates the mockup in place, a one-line tradeoff per option, and the recommended
  option marked. The user still chooses by letter.
- [x] AC17: Each page states what is approximate (for example, production uses system components)
  and lists open questions and must-not-happen rules in the notes panel.
- [x] AC18: Each page explains the question it asks; fidelity matches the question (wireframe for
  structure, closer styling for look and feel); real content is used when it affects the judgment.
- [x] AC19: Binding items may refer to specific screens and states of the retained images.
  `implement` and `review` read the PNGs and the HTML source; review compares a screenshot of the
  result with the PNGs when a screenshot tool is available, and otherwise reports the comparison
  as unrun under AC7.

- [ ] AC20 (user clarification): Before design agreement, open draft HTML in the browser, or
  report its absolute path if opening is unavailable. No draft screenshots are captured or
  substituted for browser inspection. Capture the chosen design only after agreement.

### Decisions and uncertainty

- Accepted decisions and source: constraints 1-20 above (user, 2026-10-28); scope and AC1-AC8
  accepted by the user on 2026-10-28; TDD level below. Revised AC9, AC11, and new AC13-AC19
  accepted with implementation authority by the user, 2026-10-28; shell direction A (Blueprint)
  chosen by the user, 2026-10-28.
- Assumptions and unresolved questions:
  - Technical: where option-generation guidance lives (in each of explore/specify/architect, or
    one shared reference they link to); an implementation design choice, not an acceptance criterion.
  - Technical assumption, unverified: Mermaid HTML pages load the Mermaid script from the network.
    Offline hosts may not render them. No resolution is chosen here.
  - Technical: `docs/lusona/visuals/<slug>/` and any new shared reference or template path are
    proposals; naming rules for `<slug>` are not yet checked against the naming reference.
  - Technical: how `implement` and `review` find the reference (spec link assumed sufficient).
  - Technical: PNG capture uses any available screenshot tool; when none is available the HTML source is
    retained alone and the missing images are reported. Not yet verified on Codex, Cursor, or Xcode.

### TDD policy

- Level: targeted
- Selected by user: in the specify session, 2026-10-28
- Test-first behaviors: (a) when the user picks a generated mockup option, the chosen visual is
  saved as a reference with a binding/illustrative list and linked from the spec (AC2); (b)
  `implement`, given a spec linking a reference, treats binding items as acceptance and reports
  them (AC6). For each, observe the baseline (unchanged canonical source) fail before editing,
  then obtain matched candidate evidence, per [CONTRIBUTING.md](../../../CONTRIBUTING.md#behavioral-evidence).
- AC9-AC12 (accepted with implementation authority by the user, 2026-10-28): targeted. Test-first:
  (c) generated options are templated files plus `index.html` (AC9, AC11), baseline = 1.3.0
  working-tree source before template edits. Candidate-only: AC10, AC11 retention, AC12.
- AC9, AC11 (revised) and AC13-AC19: targeted (user, 2026-10-28). Test-first
  (d) an iOS project fixture gets platform-styled options with its real screen names (AC13), and
  (e) a choice retains PNGs per screen and state plus HTML source (AC11), baseline = working tree
  before these edits. Others candidate-only.
- Required regression coverage (candidate-only checks with a coverage rationale): option count
  2-4 (AC1), rejection saves nothing (AC3), diagram inclusion and textual-only skip (AC4), inline
  versus HTML presentation (AC5), review checklist and unrun-comparison reporting (AC7), no-reference
  and user-supplied-reference behavior unchanged (AC8). Matched baseline is required if any of these
  is claimed as an improvement or touches a consequential shared boundary (authority, TDD,
  completion). Before trials, declare cases, conditions, run budget, and stopping condition.

## Execution

- Approach: one shared reference `plugins/lusona/references/visuals.md` (proposed) owns option
  generation, diagram presentation, retention, and consumption rules; explore, specify, architect,
  implement, and review link it with a one-line trigger; the core References table lists it;
  `references/files.md` lists `docs/lusona/visuals/<record-id>/`. Public README sentence and its
  four translations are updated if behavior is described there.
- Verification: frozen trial design, fixtures, tasks, and evaluator criteria under
  `tmp/visual-references-20261028/` (hashes in `frozen.sha256`): baseline C1/C2, then candidate
  C1-C6, independent grading; then `git diff --check`, `claude plugin validate plugins/lusona`,
  `claude plugin validate .claude-plugin/marketplace.json`, `python3 scripts/package.py --output
  tmp/visual-references-20261028/package`. Durable evidence goes to
  `docs/lusona/evidence/2026-10-28-visual-references/`.
- Mermaid script source (technical): pin a jsDelivr URL with an exact version; keep the Mermaid
  source in a `<pre class="mermaid">` block so the text stays readable when the script cannot load.

## Evidence

- Checks and outcomes: [trial record](../evidence/2026-10-28-visual-references/README.md).
  TF-a (AC2) baseline fail, candidate pass. TF-b (AC6) baseline pass (characterization, no red),
  candidate pass. Regression C3-C6 candidate pass. Independent grader: Opus agent separate from
  the implementer and trial runner.
- Review: same independent agent reviewed the source diff: 0 blocking, R1 medium (specify diagram
  trigger), R2-R4 low (README placement and wording, draft location). All four fixed after grading;
  fixes not re-run in trials.
- Repository checks after fixes: `git diff --check` clean; `claude plugin validate plugins/lusona`
  passed (existing install-line advisory); `claude plugin validate .claude-plugin/marketplace.json`
  passed; `python3 scripts/package.py --output tmp/visual-references-20261028/package-final` passed.
- AC9-AC12: [run 002](../evidence/2026-10-28-visual-references/runs/002/README.md). TF-c baseline
  fail, candidate pass. Run 1 failed AC10 and AC11 from source defects F1-F2; one correction round
  fixed F1-F5; run 2 passes AC10 and AC11; AC12 passes (run 1). N1 fixed after run 2 without re-run.
  Repository checks after N1: `git diff --check`, both `claude plugin validate`, and
  `scripts/package.py` pass.
- Revised AC9, AC11 and AC13-AC19: [run 003](../evidence/2026-10-28-visual-references/runs/003/README.md).
  TF-d and TF-e baseline fail, candidate pass; AC9, AC14-AC19 pass (E4 with a wording deviation).
  Grader findings F1-F8 fixed in one correction round; repository checks pass after the fixes.
- Remaining verification and limitations: AC6 lacks red evidence; AC4 in specify/architect has no
  trial; one observation per case on Claude Code with Sonnet actors; browser rendering, offline
  Mermaid, native installation, and Codex/Cursor/Xcode untested.
- Changes: Version 1.3.0 in three native manifests and five READMEs; validation and
  packaging rerun and passed (`lusona-1.3.0.zip`). 12 modified files (5 skills, core README, files.md, 5 public READMEs) and
  2 new files (`references/visuals.md`, `templates/visual-reference.md`).

## Current handoff

- Authorized work: implementation of AC1-AC19 (AC10 superseded), version bump to 1.3.0, and a
  local commit (user, 2026-10-28).
- Completed and remaining work: complete. AC1-AC19 implemented and verified as recorded above;
  accepted by the user ("accept", 2026-10-28).
- Try it: open `tmp/visual-platform-20261028/samples/site/index.html` (three iPhone flows),
  `b.html` (state switch with a failure state), and `switch.html` (in-place option switch).
- Correction rounds: run-003 review findings, 1 total, material progress.
- Human acceptance and delivery: accepted 2026-10-28; committed at the user's request; not pushed
  or published.
- Next action: none for this request; pushing or publishing requires a separate request.

## Audit follow-up (2026-10-28)

- Authority: user requested applying the audit recommendations and correcting this spec.
  This supersedes constraints 3, 7, and 17 and revises AC4, AC7, and AC15. Capture uses any
  available screenshot tool; the missing-capture fallback is unchanged. Skill entrypoints
  link the shared rules without repeating retention instructions.
- Presentation clarification: constraint 21 and AC20 make browser inspection precede design
  agreement and screenshot capture. This applies to generated design pages; implementation
  review still compares the result against the agreed reference.
- TDD: retain the selected targeted policy; no named test-first behavior is changed.
- Earlier completion and trial results above describe the original version, not these revisions.
  Revised criteria remain unchecked pending behavioral validation; installation and interactive
  behavior have not been retested. Static checks cover links, packaging, and source consistency.
- Delivery: user authorized folding this follow-up into the last two commits without a version
  bump. Static checks and packaging pass; behavioral validation remains pending. The user will
  handle the force-push. Next action: validate revised diagram, state-selection, capture, and review behavior.

- Frame correction (user, 2026-10-28): remove simulated phone hardware and fixed phone aspect
  ratios from the HTML template, retaining platform-styled app content in plain panels.
  Constraint 12 and AC13 supersede the earlier frame requirement. Static validation only;
  browser layout remains untested. Existing generated pages are not changed by template edits.
