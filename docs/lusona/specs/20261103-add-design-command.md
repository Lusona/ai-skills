# Spec 20261103-add-design-command: Add a design command and document visual capabilities

Created: 2026-11-03
Updated: 2026-11-03

Kind: feature
Work item: [Historical completion](../history/2026-11-week-01.md#2026-11-03--add-design-command)
Context: [Shared visual workflow](../../../plugins/lusona/references/visuals.md)

## Agreement

- User and problem: Lusona users can already request visual options through other skills,
  but there is no dedicated command for this work. The README gives little detail about
  visual design and how mockups and diagrams are presented.
- Desired behavior: One `design` command produces UI mockups, screen flows, and diagrams
  using the existing visual workflow. Public documentation explains the command and the
  visual capabilities already available in `explore`, `specify`, and `architect`.
- Scope: The canonical skill, shared workflow/catalog integration, command metadata, portable
  packaging, and the English, Spanish, German, Simplified Chinese, and Japanese READMEs.
- Exclusions: Separate mockup/flow/diagram commands, slide decks, image generation, production
  UI implementation, new browser/capture tooling, historical-record migration, and release work.
- Accepted constraints: Keep sources in `plugins/lusona/`, reuse shared visual rules and
  templates, preserve bounded work and native question tools, and retain a concrete next
  action (repository instructions). Existing visual entrypoints and reference consumption
  remain available. Resource paths resolve relative to the loaded skill.
- Completion condition: AC1–AC8 and required verification pass; evidence distinguishes static
  validation from installation and interactive behavior actually tested.

### Acceptance criteria

- [x] AC1: A canonical `design` skill is available through the existing native skill-discovery
  mechanism and in the portable package, with its linked resources accessible. Catalogs and
  descriptions accurately reflect the added command; native identity/version alignment and
  project-data exclusion are preserved.
- [x] AC2: Command guidance distinguishes visual design from `architect`'s consequential
  technical decisions about boundaries, contracts, and ownership. `explore`, `specify`, and
  `architect` continue to offer visuals within their own work. Users can request visual work
  directly without completing another workflow stage first.
- [x] AC3: Given an existing UI or supplied references, `design` reuses inspected screen names,
  navigation, copy, platform/theme conventions, and settled constraints. It scales fidelity
  to the decision, shows relevant states, labels approximations, and asks only consequential
  missing questions. A settled design request can proceed without generating new alternatives.
- [x] AC4: For an unresolved UI choice, `design` presents 2–4 labeled alternatives through the
  existing visual-page template and applicable comparison/flow layout. Drafts open in the
  browser before agreement, with an absolute-path fallback when opening is unavailable.
  Screenshot capture follows the user's choice.
- [x] AC5: Diagram deliverables and diagram alternatives use fenced Mermaid in replies or
  Markdown, following the existing shared presentation rules.
- [x] AC6: Selection, revision/rejection, and retention follow the shared visual rules. A chosen
  reference records binding and illustrative items and links from its existing owner or
  notes; rejected drafts are discarded. Capture limitations are reported while retaining
  the chosen HTML. Existing `implement`/`review` consumption of binding items is preserved.
- [x] AC7: Visual work can use notes when no spec or ADR exists. The command ends with an
  inspectable draft or chosen reference, relevant open questions, and a concrete next action;
  production implementation remains subject to the existing authority and TDD contract.
- [x] AC8: All five public READMEs expose `design` in command selection and include a concrete
  visual-work prompt. Documentation explains visual exploration in `explore`, behavior and
  acceptance clarification in `specify`, technical diagrams in `architect`, and focused visual
  work in `design`. It describes UI browser presentation, Mermaid diagrams, chosen-reference
  retention, and implementation/review checks accurately. The workflow guide lists the new
  responsibility and output.

### Decisions and uncertainty

- Accepted: one `design` command for UI mockups, flows, and diagrams, explicitly selected by
  the user on 2026-11-03. Targeted TDD was selected in the same exchange.
- Assumption: presentation means presenting mockups and diagrams for inspection. Slide-deck
  generation is outside the accepted scope.
- Scope and AC1–AC8 accepted through the user's subsequent `lusona:implement` request,
  2026-11-03. Implementation and verification are authorized; commits and release work remain
  outside scope under repository instructions.
- No consequential architecture decision is currently identified. Keep visual behavior owned
  by the shared procedure rather than duplicating it in the command.

### TDD policy

- Level: `targeted`.
- Selected by user: `targeted (Recommended)`, 2026-11-03, in response to the question naming
  command discovery and packaging as the test-first behaviors.
- Test-first behaviors: availability of the new command in canonical skill discovery and in
  portable packages, with access to linked resources. Observe failure from the missing command
  before adding it, then passing results. Static discovery checks do not prove live-host discovery.
- Required regression coverage: existing package/resource and manifest checks; unchanged
  visual entrypoints; UI comparison/flow, Mermaid, choice/revision, chosen-reference handoff,
  and browser/capture fallbacks; README examples consistent with actual instructions.
- One-time exception: user answered Yes on 2026-11-03 to recording the missed package
  test-first sequence and closing the verified change. Targeted discovery red/green is retained;
  package verification is accepted without pre-implementation red. The original gap remains
  documented below and in the retained review; the exception does not establish missed evidence.

## Verification requirements

During implementation, run the targeted red/green checks and existing package tests, resource
link/template checks, manifest/catalog validation, and package construction. Use repository-local
`tmp/` for scratch and generated packages. Verify representative visual-workflow scenarios in an
isolated consuming project, including direct use without an existing spec, UI options/flows,
Mermaid output, revision/rejection, chosen-reference retention, and capability fallbacks.
Review all five README changes against the implemented guidance. Record the host and actual
installation/interactive checks; identify unavailable or unrun checks explicitly.

## Execution

- Skill/test worker owns the new skill and discovery/package regression tests, with targeted
  red/green before the skill is added. Documentation worker owns all five public READMEs.
  Parent owns workflow/catalog integration, native metadata, INSTALL.md count maintenance,
  verification coordination, spec, queue, evidence, and handoff. Workers have disjoint writes.
- Baseline sources and revision were captured in `tmp/design-command-20261103/` before
  implementation. New behavior gets candidate-only representative checks; existing authority,
  TDD, retention, and implement/review contracts are preserved. Independent review covers the
  actual diff and grades retained actor behavior. No comparative improvement is claimed.

## Evidence

- Inspected the canonical skills, shared visual rules and templates, workflow guide, README
  command/visual sections and translations, native metadata, and package builder/tests.
- Existing infrastructure covers HTML UI options and flows, browser-first draft presentation,
  Mermaid diagrams, chosen-reference retention, and implementation/review consumption.
- At definition time, the English README listed `explore` and briefly mentioned diagrams and
  visual alternatives under Questions and evidence, but lacked a dedicated visual-work example.
- Packaging copies the canonical skill directory and requires each skill to link an existing
  output template. Existing directory-based discovery supports adding the command. The Codex
  manifest's count of thirteen responsibilities was removed when the command was added.
- A bounded change-analyst worker returned the proposed definition without edits; the parent
  reconciled it with the user selections and repository evidence.
- Definition checks: `git diff --check` passed. Local links, whitespace, AC1–AC8 IDs, dates,
  selected TDD, and single queue membership passed validation with installed Python.
  `mise exec` could not create shims on the read-only filesystem; direct Python completed
  the same check (one recovery round, resolved).
- Implementation: canonical design skill, five README updates, workflow/catalog guidance,
  Codex description, and current INSTALL.md count maintenance completed and initially verified
  at 1.4.0; the subsequently requested version change is recorded below.
- Verification: two focused and all ten package tests pass; skill validator, Claude source/catalog
  validation, Antigravity strict source/final-package validation (14 skills), final packaging,
  documentation/version checks and baseline comparisons pass. See [exact verification evidence](../evidence/2026-11-03-design-command/README.md).
- TDD gap, accepted exception: canonical discovery has pre-implementation red. The initial package test stopped on
  a concurrently added workflow-guide link; clean package-membership assertions were reached
  only after implementation. The user accepted this one-time sequencing exception on 2026-11-03;
  passing tests and retrospective baseline checks do not establish the missed evidence.
- Independent source review reports zero defects; C1 UI comparison/revision/choice/retention,
  C2 settled mockup, and C3 no-save Mermaid all pass their declared observable criteria.
  Acceptance boxes record verified product outcomes; the policy decision is recorded above.
  Exact inputs, responses, artifacts, source/test hashes, logs, independent review and limitations
  are durably retained in the
  linked evidence archive, whose bytes and CRCs were verified.
- Installation, live-host invocation, browser rendering/interaction, and capture are untested.
- Follow-up formatting: removed the blank line separating the work queue's table header and
  body. The canonical empty queue template and historical fixture were inspected; neither
  contains separated data rows. Queue contents/state are preserved except the authorized closeout.

## Current handoff

- Authorized work: implement AC1–AC8, user's `lusona:implement` request, 2026-11-03.
- Completed: AC1–AC8 product outcomes, static/native/package checks, all three independent
  behavioral grades and source review; exact evidence retained beyond scratch.
- Remaining: none for the authorized change; user accepted the one-time exception and closeout.
- Ownership: parent owns records; all workers returned results with
  no active operations or children.
- Correction rounds: supplemental baseline fixture setup 1 (resolved); C2 generator assertion 1
  (resolved); package TDD sequencing is an irreversible evidence gap, not a retryable failure.
- Next action: none for this request. Commits, installation, push, and publication require
  separate authorization.

## Version follow-up — 2026-11-03

- Authority: user requested bumping versions to 1.5.0 after accepting closeout.
- Changes: all five native manifests, all five README source-version labels, and the current
  checkout version in INSTALL.md now say 1.5.0. Dated installation observations and retained
  1.4.0 evidence preserve their actual versions. Historical completion remains archived.
- Verification: all ten package tests, Claude source/catalog validation, Antigravity strict
  source validation (14 skills), package construction, version alignment and diff checks pass.
  Generated package: `tmp/version-1.5.0-20261103/package/lusona-1.5.0.zip`.
- TDD: existing targeted policy; this metadata-only follow-up preserves behavior and uses the
  existing manifest/version/package checks. No new test-first behavior is introduced.
- Limits: 1.5.0 installation and interactive behavior have not been tested. No commit, push,
  or publication requested. No further action for this version update.

## Proofreading and consistency review — 2026-11-03

- Authority: user requested proofreading, review, and correction of recent changes.
- Scope: the uncommitted design command, tests, shared guidance, five README translations,
  version metadata, installation guidance, and related work/evidence/history records.
- Corrections: added the omitted architect entry to every command table, completed the English
  table row, documented single-draft acceptance alongside option selection, improved Chinese
  UI terminology and sentence wrapping, and distinguished historical observations from current
  version/implementation statements. These are editorial clarifications of accepted behavior.
- Independent review: consistency_review inspected canonical rules, tests, metadata and evidence,
  then reviewed the final documentation corrections; zero remaining actionable findings.
  Archived trial evidence and the accepted TDD exception retain their original meaning.
- Verification: all ten package tests pass; package construction and diff checks pass; all
  fourteen canonical skills appear in each README table; 320 documentation links and native
  version alignment pass. Reviewer separately checked canonical resource links and evidence
  archive integrity. No new behavioral trials were needed for these editorial changes.
- Limits: installation, live-host invocation, browser rendering, and capture were not tested.
  No further action for this review; historical completion remains archived.
