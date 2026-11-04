# Spec 20261103-realign-instructions-with-goals: Realign instructions with the work loop, light instructions, and delegation goals

Created: 2026-11-03
Updated: 2026-11-03

Kind: refactor
Work item: [Work queue](../work.md)
Context: [Audit baseline and rationale](#evidence); [Why we built Lusona Skills](https://blog.lusona.com/blog/when-the-workflow-became-another-job/)

## Agreement

- User and problem: The maintainers' goals are a shared work loop, light instructions, and
  delegation. An audit on 2026-11-03 found the loop stated consistently, but the instruction
  set compressed rather than reduced: contract rules are restated across the 14 skills, the
  always-loaded core carries optional material, catalog and routing guidance overlap across four places, and
  record requirements apply "even for small work". Delegation references agree with each
  other; AGENTS.md wording ("when useful") is weaker than the core's mandatory standard.
- Structural outcome: Each contract rule is stated once in the core. The sections every role
  must load contain only invariants. Records are proportional to the work. One skill catalog
  and one canonical skill-routing table exist in the workflow guide, with routing directed
  by the core and the table loaded when selection is unclear. AGENTS.md matches the core's
  delegation standard. Observable agent behavior at
  authority, TDD, completion, review-independence, and write-ownership boundaries is unchanged.
- Scope: `plugins/lusona/README.md`, the 14 `plugins/lusona/skills/*/SKILL.md` files,
  `plugins/lusona/references/*.md`, affected templates, the root `README.md` catalog table,
  `AGENTS.md`, and a duplication check in `scripts/`. Translated READMEs change only where
  the English catalog table changes.
- Exclusions: Changing the delegation standard (user decision 2026-11-03: keep mandatory);
  a word budget or budget test (user decision: baseline measurement only); removing any
  authority, TDD, completion, or independence rule; historical-record migration; release work;
  token or latency savings claims.
- Accepted constraints and invariants: Repository instructions (bounded tasks, explicit TDD,
  native question tools when permitted, concrete next action in every skill, small context
  and process). Correction limits, batch repair budgets, and queue lifecycle semantics keep
  their current meaning. Bundled links resolve relative to the loaded resource. All native
  manifests keep aligned identity and version.
- Completion condition: AC1–AC7 pass with required checks, independent review of the diff,
  and the baseline/after measurement recorded in evidence. Delivery is the working tree;
  commits need separate authorization.

### Acceptance criteria

- [x] AC1: Core invariants only. The sections listed in Loading rules as required for all
  roles contain authority, ask/continue/pause boundaries, TDD gate, completion and
  review-independence requirements, write ownership, the loading rule itself, and the
  Result/Evidence/Next action presentation rules. Optional study entry (measurement/experiment
  authority and budget) and context-budget mechanics are reachable from the References table
  and loaded by operation, not by every role.
  Every rule moved remains discoverable from its owning reference, and a one-sentence
  trigger stays in the core for each moved procedure: before starting a measurement or
  experiment, read the evidence rules; before correcting a failed check or review finding,
  read correction limits (already present); before a handoff, read the handoff procedure.
  The context-budget threshold itself (prepare around 40% and hand off before 50% when
  measured, otherwise checkpoint at task boundaries) stays in the core, because an agent
  must know the threshold before it can decide to hand off; only the handoff-content
  mechanics move.
  The core directs agents to select the next responsibility from the unresolved need,
  preserve existing authorization, and consult the canonical routing table when skill
  selection is unclear. The table itself is not mandatory reading for every role or for
  workers whose assignment is already settled.
- [x] AC2: Each contract rule stated once. No skill restates a rule the core already states.
  A script check fails when any `SKILL.md` contains a restated core clause, starting with
  the phrases "without a separate save request", "does not authorize", and "permitted native
  question tool" outside a link to the owning section; the check passes after the change.
  Each skill keeps its persona and judgment, distinctive rules, and Next action section.
- [x] AC3: Proportional records (amended 2026-11-03, see Decisions). Retention, queue,
  implement, refactor, specify, and the spec and notes templates no longer require a record
  "even for small work". A spec and queue row are required whenever the workflow calls for a
  spec (Specify defines every change in one), the user requests a spec or tracking, or a spec
  already exists; size and scope do not decide this. Direct implement or refactor work without
  a spec uses notes; investigations, measurements, and experiments use notes and evidence
  records. Delegated assignments and handoffs within one session keep their handoff in notes
  or the owning record. Ordinary dialogue and brief status need no record. Creating or
  updating a spec still requires its queue row. Material evidence
  records are required for comparative claims and named test-first behaviors; routine
  verification stays with its owner.
- [x] AC4: One skill catalog and one canonical skill-routing table. Both live only in
  `plugins/lusona/references/workflow-guide.md`: the catalog describes persona,
  responsibility, and output; the routing table maps observed need to skill or direct
  action and required inputs. Preserve the decision guidance currently in `status`,
  including acceptance/delivery and completed-scope cases that require no further skill.
  Routing is available from any entry point through the core's conditional loading rule
  in AC1. `status` uses the shared table; `batch` uses it and retains its additional
  dispatch prerequisites, dependencies, reconciliation, and ownership rules. Neither
  skill duplicates general routing guidance. The root README action-group table remains
  as user-facing orientation and links the guide. A script check requires the catalog
  and routing table in the guide and rejects either table duplicated elsewhere in the
  plugin, while allowing batch-specific dispatch conditions; its test-first sequence and
  fixtures are defined under TDD policy.
- [x] AC5: Delegation wording aligned. AGENTS.md states the core's standard: the coordinator
  delegates substantive specialist work and owns questions, reconciliation, integration,
  verification, and shared state; local execution is the fallback when delegation is
  prohibited or unavailable and never satisfies required independent review.
- [x] AC6: Baseline and after measurement. Words loaded for each role on a representative
  `implement` with one worker (coordinator: core required sections, skill, references read
  before dispatch and before commit; worker: assigned sections and skill) are recorded
  before and after the change in `docs/lusona/evidence/`, with the exact files counted and
  the method. No token, latency, or cost claim is made from the word counts.
- [x] AC7: Behavior preserved. Independent review of the final diff confirms that no
  authority, TDD, completion, independence, correction-limit, or write-ownership rule was
  removed or weakened, and that every removed sentence is either a duplicate of a retained
  sentence or an optional procedure now reachable from the References table. Package
  construction, resource link checks, native validation, and existing package and
  work-record tests pass.

### Decisions and uncertainty

- Accepted: scope AC1–AC4 topics, 2026-11-03, user selection of all four audit items.
- Accepted: keep mandatory delegation; align AGENTS.md to the core (AC5), 2026-11-03.
- Accepted: baseline measurement only, no budget test (AC6), 2026-11-03.
- Accepted: shared core routing guidance with one canonical table in the workflow guide,
  loaded when skill selection is unclear; status uses it and batch retains its additional
  dispatch prerequisites. User requested this spec update after discussing routing,
  2026-11-03. This accepts the routing revision, not all remaining criteria or implementation.
- Assumption: "restated" means the same requirement in different words, not only the
  listed phrases; the script check is a floor, and AC7 review covers the rest.
- Assumption: the batch dispatch table's per-responsibility input conditions are
  distinctive batch rules and stay; its skill descriptions do not.
- Accepted: the root README action-group table stays as user-facing orientation and links
  the guide, 2026-11-03, by accepting the criteria with that default.
- Accepted: AC1–AC7 as revised (AC1 triggers and context-budget threshold, AC3 session
  boundary and small-result rule, AC4 trimmed to its outcome), 2026-11-03. The user
  accepted scope, criteria, and targeted TDD; the item is Ready. Ready does not authorize
  implementation.
- Decision, 2026-11-03: the restated-clause check exempts skill frontmatter. The
  description is the host-facing selection cue, not loaded instruction text, so its
  authority clauses stay.
- Decision, 2026-11-03: the AC6 after measurement adds `references/handoff.md` to the
  coordinator's set, because the coordinator reads it before the handoff at the end of an
  implement. The worker set is unchanged.
- Decision, 2026-11-03 (parent): the brief/map rule from the 2026-10-31 F2 clarification is now
  a conditional in frame-product and map-capabilities ("when requested, update; otherwise
  discussion stays in notes") instead of "discussion alone does not authorize changes". The
  core's "ask before unauthorized changes to accepted outcomes" owns the prohibition. The
  independent review noted this as a rephrase around the checker pattern; the parent kept it
  because the conditional states the skill-specific behavior without repeating the core rule.
- Decision, 2026-11-03 (user): the Result/Evidence/Next action presentation rules stay in
  the always-loaded core. User feedback names knowing the next action as the most valued
  part of the workflow; removing ambiguity about where to go next is a central goal, so the
  format is an invariant, not an optional procedure.
- Decision, 2026-11-03 (user, after the contradiction review): a spec is recorded whenever the
  workflow calls for one or the user requests one; size and scope are not deciding factors,
  because a rigid rule is simpler than judging each case. The "resumed by a later session"
  trigger is removed, Specify always produces a spec, and investigations, measurements, and
  experiments use notes and evidence. AC3 amended accordingly.
- No consequential architecture decision identified; no ADR.

### TDD policy

- Level: `targeted`.
- Selected by user: 2026-11-03, in response to the question naming the candidate behaviors.
- Test-first behaviors: the restated-phrase check (AC2) and canonical catalog/routing
  checks (AC4). Observe AC2 and the missing canonical routing-table check failing against
  current sources before editing instructions, then passing after consolidation.
  Demonstrate duplicate rejection for both table types and acceptance of batch-specific
  dispatch conditions with fixtures. The existing single-catalog baseline should pass;
  it does not need an artificial failure against current sources.
- Required regression coverage: `python3 -m unittest discover -s scripts -p test_package.py`,
  `bash scripts/test-work-record.sh`, `python3 scripts/package.py --output tmp/<dir>`,
  `claude plugin validate plugins/lusona`, `git diff --check`, and local link resolution for
  changed Markdown.

## Verification requirements

Capture the baseline word counts and source hashes before edits (AC6). Run the targeted
checks and fixtures under the TDD policy above. Verify that the shared routing table
preserves the existing status decision cases and that core, status, and batch point to
its owner without making the table mandatory for settled assignments. After edits, run
the regression coverage above, record the after
measurement, and obtain an independent review of the full diff against AC7 with the actual
diff, this agreement, and the check evidence, without implementer conclusions. State checks
not run; agent behavior trials are not required for this behavior-preserving change unless
review finds a boundary rule changed in meaning.

## Execution

Implementation authorized 2026-11-03 (`lusona:implement`, "so I can use and review in
another project"). Ownership, disjoint writes:

- Editor A (core and references): `plugins/lusona/README.md`, `references/evidence.md`,
  `references/retention.md`, `references/queue.md`, `references/workflow-guide.md`, new
  `references/handoff.md`, `templates/spec.md`,
  `templates/notes.md`. Owns the AC3 rule text; keeps every existing level-2 heading in the
  core because skills link those anchors.
- Editor B (skills): architect, batch, design, experiment, explore, frame-product, implement.
- Editor C (skills): investigate, map-capabilities, measure, refactor, review, specify, status.
- Parent: `AGENTS.md`, root `README.md` guide link, `scripts/check_instructions.py`,
  `scripts/test_instructions.py`, verification, independent review dispatch, this record,
  queue, evidence.

Pinned core, unchanged by this change: Contract (authority, saving, queue ownership),
Questions and next actions, TDD, the completion and independence paragraphs of Review and
communication including its presentation rules, Assigned leaves, Personas and subagents,
the context-budget threshold. Only two things move out of the core: the study-entry
paragraph and the handoff-content mechanics, each replaced by a one-sentence trigger.

Editing rule for skills: drop a sentence only when the core or an already-linked reference
states the same requirement; otherwise keep it as written. Do not rephrase to avoid the
checker's patterns and do not join clauses with slashes.

- Increment 1 (done): queue to Doing; AC6 baseline in
  `../evidence/2026-11-03-realign-instructions/baseline.md`; checker and tests written;
  red observed and saved in `../evidence/2026-11-03-realign-instructions/red.md`:
  27 restated clauses in 13 skills, routing table missing from the guide and present in
  status; 6 fixture tests pass.
- Increment 2: parallel edits by A, B, C under the ownership above; parent edits
  AGENTS.md and the root README link.
- Increment 3: green checks, regression coverage, after measurement, independent review by
  a fresh agent given the diff, the agreement, and the evidence only; record and queue to
  Review for the user's acceptance in another project.

## Evidence

Implementation, 2026-11-03. Exact runs: [evidence](../evidence/2026-11-03-realign-instructions/README.md).

- Editors A (core, references, templates), B and C (seven skills each) worked on disjoint files;
  the parent edited AGENTS.md, the root README, the checker and tests, and one map-capabilities
  sentence for consistency with frame-product. All workers returned complete with no children.
- TDD, targeted: the restated-clause check and the routing-table check were observed failing
  against the baseline sources (27 restated clauses in 13 skills; routing table missing from the
  guide and present in status) and passing after edits. The frontmatter exemption and its
  fixture test were added after the red run; the red findings in body text are unaffected.
- Measurement, words loaded for a spec-linked implement with one worker: coordinator 6,277 to
  5,993 (the after set adds the new handoff reference); worker 3,607 to 3,195; core sections
  required for every role 1,309 to 1,157; the 14 skills 9,203 to 7,438. No token, latency,
  or cost claim.
- Checks passed after edits and again after review corrections: 9 instruction tests, checker,
  10 package tests, work-record tests, package build at `tmp/realign-20261103/package`, Claude
  plugin and marketplace validation, whitespace, 352 relative links and anchors.
- Independent review by a fresh read-only agent: AC1–AC7 met, no removed sentence without a
  retained owner. Corrected P2-1 (core Personas section pointed at a Work loop exception that had
  moved to evidence.md Study entry) and P2-2 (root README still said "even for small work").
  Removed implement's restated independent-review sentence for symmetry with refactor (P3-6).
  Remaining observations recorded in the evidence README.
- User review, 2026-11-03: removed three remaining general clauses (experiment scope-change
  approval, implement user-visible verification and documentation update, architect ADR
  requirement); the core Contract and Review and communication own them. The checker now
  matches phrases wrapped across lines, with two regression tests; against the baseline sources
  it finds 29 restatements, two more than the single-line run. All checks rerun and pass;
  measurements refreshed. These address R2
  and R3 below. R1 (specify created a spec unconditionally): record selection now follows
  retention first, the spec creation, queue reconciliation, and returned path are conditional
  on a spec being required, and the independent-review R1–R3 section below records the findings.
- Contradiction review, 2026-11-03, after the version bump to 2.0.0 (fresh read-only agent over
  the core, all references, 14 skills, templates, and the root README): 0 P1, 6 P2, 8 P3; all
  links and anchors resolved. All 14 corrected on the user's instruction: spec trigger
  (decision above); saved-handoff definition in the core, delegation, and queue; implement's
  closeout routed to the coordinator; correction counts in retention's list and the notes
  handoff; assignment results versus the user-facing format in the core; study-entry authority
  in the routing preamble; TDD question link; batch repair budget in assignment results; the
  root README's targeted-TDD example; review queue-write sentence; batch links to its shared
  rules; Leaf in the terminology table; presentation scope; root README reference list and
  records paragraph. Translations follow the root README changes with parity checks.
- Translations, 2026-11-03, on the user's request: the four translated READMEs carry the new
  workflow-guide sentence and the rewritten records paragraph. Parity check
  (`tmp/readme-localization/check.py`): section hierarchy, link targets, anchors, command blocks,
  inline code, and Mermaid topology match the English README for all four.
- Limits: static checks only; no agent behavior trials; installation and live-host invocation
  not tested. Translations are model-assisted editorial work, not native-speaker acceptance.

Audit baseline, 2026-11-03, uncommitted working tree at 1.5.0:

| Measure | Value |
| --- | --- |
| `plugins/lusona/README.md` | 1,675 words |
| Sections required for all roles | about 1,200 words |
| Coordinator reads before an implement dispatch and commit | about 6,300 words |
| All plugin instruction files | 22,600 words |
| Skills repeating the loading preamble | 14 of 14 |
| "without a separate save request" | 12 occurrences |
| "does not authorize" and variants | 26 occurrences |
| "permitted native question tool" and variants | 7 occurrences |
| Files carrying a skill catalog | 4: root README, workflow guide, status, batch |

Review correction, 2026-11-03: the four-file count above groups orientation, catalog,
routing, and dispatch guidance. Only the workflow guide contains the full skill catalog;
status and batch contain distinct decision tables. AC4 now distinguishes those roles.

Delegation references (delegation, model routing, worker lifecycle, batch execution) were
checked against each other; no contradiction found. The design-command change
(`20261103-add-design-command.md`) is the exhibit for record overhead on a small change.
Static source review only; no agent trials run.

### Spec review, 2026-11-03

Scope: the proposed agreement and AC1–AC7 against current canonical workflow sources,
with a delegated read-only specification review. No implementation or acceptance-criteria
changes were made. Recommendation: retain Ideas until the following definition gaps are
resolved and the user accepts the criteria.

- P2 — AC3 increases tracking requirements. Current retention rules and the notes template
  permit spec-free work to retain a handoff in notes. Requiring a spec and queue row whenever
  work spans "sessions or handoffs" changes that behavior; ordinary delegation could trigger
  it despite the goal of proportional records. Define the intended handoff boundary and
  explicitly preserve notes-only worker handoffs, or retain notes for resumable direct work.
  Also clarify when a small substantive result needs no record versus a short notes entry.
- P2 — AC4's literal check cannot produce the required current-source red. Only
  `plugins/lusona/references/workflow-guide.md` currently has the full Skill / Persona and
  responsibility / Output table. Status has an Evidence or gap / Recommended action table;
  batch has a Responsibility / Inputs and dispatch condition table. The root README is
  outside the proposed plugin-file count. Define the routing duplication the check must
  reject, or use a deliberate duplicate fixture to demonstrate rejection and revise the
  requirement to fail against current sources.
  Resolution, 2026-11-03: the accepted routing revision distinguishes the passing
  single-catalog baseline from the missing canonical routing table and requires duplicate
  rejection fixtures. AC4 and its TDD/verification wording were updated accordingly.
- Suggested clarification — AC1 should name the operation triggers for loading moved
  procedures. Discoverability from a reference table alone does not establish that agents
  will read study authority/budget rules before starting a study or context rules before
  a handoff. Preserve the relevant mandatory trigger while moving procedure details.

Verification: inspected the spec, core, relevant skills, retention/queue/evidence rules,
templates, and catalog headers. A read-only source scan confirmed one full catalog table.
Package tests, installation, agent behavior trials, and the proposed future checks were
not run; the approximate audit counts were not independently reproduced. The linked
rationale article could not be retrieved. Existing unrelated working-tree changes were
not reviewed. At review time, the next action was to amend AC3 and AC4 before acceptance.
The subsequent routing revision addresses the AC4 finding. Resolution, 2026-11-03: AC3 now
bounds the spec requirement to resumption by a later session and preserves in-session
handoffs in notes; AC1 now names the loading triggers and keeps the context-budget
threshold in the core. No review finding remains open. This review does not authorize
implementation.

### Follow-up implementation review, 2026-11-03

Scope: the uncommitted changes against `545b6e0`, including the new checker, tests,
handoff reference, and measurement artifacts. Two fresh reviewers
received the extracted agreement without implementation or prior review conclusions:
one covered core/references/templates and one covered all 14 skills. The parent reviewed
the checker and evidence and ran verification. Earlier reviewer attempts that encountered
prior conclusions were replaced for independent coverage.

Result: three P2 findings. The routing consolidation and moved procedures retain their
loading triggers; no removed authority, TDD, completion, independence, correction-limit,
or write-ownership safeguard was found without a retained applicable owner. AC2 and AC3
are not yet fully satisfied; this supersedes the earlier completion assessment for those
criteria.

- R1 — `plugins/lusona/skills/specify/SKILL.md:31`: spec creation remains unconditional,
  followed by queue reconciliation at line 50 and returning a spec path at line 56.
  A one-off clarification with no existing spec, tracking request, or later-session work
  therefore still creates a spec and queue row instead of taking AC3's notes/no-record
  path. Make record selection follow retention first, and make the downstream spec-only
  actions conditional on that selection. This is a source-supported conflict; no live
  agent trial was run.
- R2 — `plugins/lusona/skills/experiment/SKILL.md:43` repeats the core's requirement to
  ask before changing accepted scope/criteria. `skills/implement/SKILL.md:61` likewise
  repeats the core's user-visible verification and enduring-documentation requirements;
  `skills/architect/SKILL.md:68` repeats its ADR requirement. These remain multiple
  statements of core rules despite AC2's semantic single-owner criterion. Remove the
  general restatements while retaining specialist procedures and links to their owners.
- R3 — `scripts/check_instructions.py:50`: restated-clause matching processes one physical
  line at a time with literal spaces. A temporary fixture containing
  `Discussion does not authorize implementation.` produces a finding; inserting a newline
  between `not` and `authorize` produces none. Ordinary Markdown wrapping can therefore
  reintroduce a prohibited clause while checks pass. Match normalized body text across
  wrapped lines while preserving source locations and the intended link/frontmatter
  exemptions, and add a wrapped-phrase regression fixture.

Verification rerun: 9 instruction tests, instruction checker, 10 package tests, work-record
behavioral checks, package construction at `tmp/realign-review/package`, Claude plugin
and marketplace validation, `git diff --check`, and 352 relative links/anchors passed.
The after measurement reproduced exactly against current sources. Native validation used
the existing mise-installed Claude 2.1.317 executable directly after its wrapper failed
to create shims in the sandbox. No installation or live-host/agent behavior trials were run.
No implementation fixes were made. Review findings were saved in this owner; queue state
was not changed. Recommendation: address R1–R3 before acceptance; move to Doing when
authorized correction starts, then recheck the changed instructions and checker fixtures.

### Current-change consistency review, 2026-11-03

Scope: the six local commits `7e889a9..ea99970` (`origin/develop...HEAD`), with a clean
working tree at review entry. User requested review for contradictions and inconsistencies;
this review makes no implementation changes. Two independent read-only reviewers covered
the changed core/references and all 14 skills/templates; the parent checked documentation,
checker/tests, manifests, and measurement evidence.

Result: no confirmed contradictions in the workflow instructions; one P3 evidence-summary
inconsistency remains. In
[the measurement summary](../evidence/2026-11-03-realign-instructions/README.md#result),
the after value for the whole core README is 1,358 words, but its supporting
[after run](../evidence/2026-11-03-realign-instructions/after.md#coordinator) records 1,529.
The summary also reports 25,435 words in 49 Markdown files, whereas that run records
25,408 words in 48 files. These are incompatible values for the cited run, so readers
cannot reproduce the summary from its stated evidence. Historical runs need not match
later source revisions; the defect is the summary's disagreement with its own source.

Verification: all 21 Python instruction/package tests, the instruction checker, Bash
work-record behavioral checks, and diff whitespace checks passed. Installation,
interactive behavior, and agent behavior trials were not tested; native-host validation
and a full link/anchor audit were not rerun. Queue state remains unchanged.

Next action: reconcile the summary with a clearly identified supporting run, preserving
historical observations. This review does not authorize fixes. User acceptance from use
in another project remains outstanding.

### Measurement-summary correction, 2026-11-03

Authority: the user approved the proposed correction with "ok": retain the historical
runs, record a new run for `ea99970`, reconcile every summary row, and explain the
correction. The existing targeted TDD policy covers checker behavior; this correction
changes evidence documentation only and adds no test-first behavior. No commit, push,
or publication is authorized by this approval.

Resolution: the P3 finding above is closed. The
[corrected summary](../evidence/2026-11-03-realign-instructions/README.md#result) now cites
[the final ea99970 run](../evidence/2026-11-03-realign-instructions/final-ea99970.md).
Every summary row was recomputed, including baseline whole-file and routing counts.
The correction note preserves the previous claims and distinguishes them from the
new observations. Historical runs and the measurement instrument are unchanged.

Verification: the parent reproduced the saved instrument output and checked the skill
counts/hashes, evidence links, unchanged historical files, and absence of plugin/script
edits. An independent reviewer recomputed every summary row from both pinned revisions,
verified all 28 skill count/hash rows and instrument/role-file hashes, and found no defects.
Whitespace checks passed. Existing test results remain applicable to unchanged code;
installation and interactive behavior were not retested.

Correction round 1 resolved this finding; consecutive rounds without material progress: 0;
total: 1. The evidence editor and reviewer returned complete with no active operations
or children; the parent reconciled their results. The queue returns to Review pending
the previously required user acceptance. This correction remains uncommitted.

## Current handoff

- Authorized work: implement AC1–AC7 (`lusona:implement`, 2026-11-03); translations and
  commit authorized by the user on 2026-11-03. Push and publication are not authorized.
  The current evidence correction was approved separately with "ok"; no new commit
  authorization was given for it.
- Completed and remaining work: AC1–AC7 implemented, verified, independently reviewed, and
  corrected after three review rounds (P2-1, P2-2, R1–R3, contradiction review 1–14);
  translations aligned with parity checks; committed; version 2.0.0. Queue state Review.
  The later P3 measurement-summary correction is verified and independently reviewed,
  with its documentation changes uncommitted. Remaining: the user's acceptance after
  using the plugin in another project.
- Ownership: parent owns all records; no active workers or children.
- Correction rounds: measurement-summary finding resolved; consecutive without material
  progress 0, total 1.
- Try it: install from this checkout (INSTALL.md, local checkout) in another project, start a
  new session, run `/lusona:status` and one `/lusona:implement` with explicit TDD. Expected:
  the same authority, TDD, and completion behavior; skills no longer restate core rules; the
  agent uses notes for direct work unless tracking is requested.
- Next action: none for the evidence correction. User reports acceptance or defects from
  the other project; on acceptance, closeout to history.
