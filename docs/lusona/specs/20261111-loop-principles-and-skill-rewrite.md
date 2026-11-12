# Spec 20261111-loop-principles-and-skill-rewrite: Loop principles and skill rewrite

Created: 2026-11-11
Updated: 2026-11-11

Kind: other (workflow rewrite; parent specification split into work items W1-W14)
Work item: [Work queue](../work.md) (coordinator adds the row; supersedes the 20261110 row)
Context: [spec 20261110](20261110-standard-skill-template-and-inline-rules.md) (superseded and
absorbed by this spec), `drafts/` workspace (emptied 2026-11-11, decision 11),
[loop conformance suite](../../../evals/loop-conformance/README.md),
[run 008 loading audit](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md),
[core README](../../../plugins/lusona/README.md), contract baseline commit `34186da`.

## Agreement

- User and problem: the user maintains the Lusona plugin (14 skills) for Claude Code and
  Codex. The current skills depend on the core README for rules that apply to every task, and
  Claude Code does not reliably load it: the root agent received the core README in 35/60
  run 003 trials and in 0/13 `tdd-stated` trials across runs 003, 006 and 007; operation-triggered
  references were read in 9/17 to 37/37 Claude trials and in all Codex trials (16/16 to 46/46) where
  the operation occurred ([run 008](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md#observations)).
  `tdd-stated` C9 failed 5/5 on each host in [run 003](../evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md).
  The user asked (2026-11-11) to rewrite the skills from scratch as "an interconnected and
  cooperative set of skills that will be governed by what I call the loop", to set up the
  principles that govern that workflow first, to establish one voice for skill text ("agent
  friendly and direct"), and to produce a full specification that can be split into smaller
  work items.
- Desired outcome: accepted loop principles (P1-P8) and skill voice (V1-V9); a rewritten set of
  the same 14 skills, each self-sufficient for every-task rules, following one structured
  template, with all other rules in references read at a stated trigger; a plugin README that
  is human documentation and a catalog only; the public contract below unchanged.
- Scope: everything under `plugins/lusona/` except the contract items; development-time
  repository checks in `scripts/`; new loop-conformance scenarios when W12 is selected;
  removal of the uncommitted hooks work (20261110 decision 5).
- Exclusions: no change to the contract items below; no plugin version bump unless the user
  requests one; no edits to generated packages; no runtime hooks or runtime Python; no change
  to existing check definitions C1-C11 (new scenarios or checks are added, not substituted).
  New skills may be added; existing ones are not removed or renamed (decision 9, U11).
- Accepted constraints and invariants (public contract; user decision 2, 2026-11-11, native
  question tool; baseline commit `34186da`):
  - K1 Skill identity: the 14 skill names (architect, batch, design, experiment, explore,
    frame-product, implement, investigate, map-capabilities, measure, refactor, review, specify,
    status) and `/lusona:<skill>` invocation. Descriptions and triggers may change.
  - K2 Project data layout: `docs/lusona/` paths `work.md`, `specs/`, `adr/`, `notes/`,
    `evidence/`, `history/`; `YYYYMMDD-slug` record IDs; queue states Ideas → Ready → Doing →
    Review → Done and Icebox ([files](../../../plugins/lusona/references/files.md),
    [naming](../../../plugins/lusona/references/naming.md),
    [queue](../../../plugins/lusona/references/queue.md)). Also `docs/lusona/product.md`,
    `plans/`, `batches/`, `visuals/` and the project `docs/lusona/README.md`, at least for
    reading existing records (decision 8).
  - K3 Record helper: `work-record.sh` and `work-record.ps1` commands, arguments, JSON output,
    statuses and exit codes, including the legacy `next-adr` and `next-change` commands
    ([naming](../../../plugins/lusona/references/naming.md#running-the-helper)).
  - K4 Behavior vocabulary: TDD levels `none`, `targeted`, `strict`; the four reply statuses
    Complete, In progress, Needs input, Paused; authority rules (specs, plans, ADRs and queue
    states do not authorize implementation).
  - K5 Manifest identity: plugin name `lusona` in both native manifests and the catalogs.
    Coordinator assumption, not a user decision.
  - Exempt: `plugins/lusona/templates/` (content and shape may change). The plugin README is not
    contract (user decision 3). New skills read records created from the `34186da` templates;
    new records may use new templates.
  - Uncommitted hooks work (`plugins/lusona/hooks/`, `scripts/completion_reply.py`,
    `plugins/lusona/scripts/completion_reply.py`) is not contract.
  - Repository rules: [AGENTS.md](../../../AGENTS.md) (bounded tasks, explicit TDD, native
    question tools, concrete next action, resources resolved relative to the loaded skill).
- Completion condition: P1-P8 and V1-V9 accepted or revised by the user; AC1-AC19 verified;
  required checks pass; independent review done; the suite run (AC18) reported and accepted
  by the user; the draft promoted into `plugins/lusona/` with user authorization.

### Loop principles (accepted)

Status: accepted by the user on 2026-11-11 (decision 7), with P3 as revised by decision 6. Each principle
cites its source. "README" means [plugins/lusona/README.md](../../../plugins/lusona/README.md)
at `34186da`.

| ID | Principle | Source |
| --- | --- | --- |
| P1 | Non-sequential. Skills are responsibilities, not phases. Select the next skill from the unresolved need; any skill may follow any other, and a change uses only the skills its unresolved work needs. | User 2026-11-11 ("non-sequential workflow/execution model"); README line 27 ("Skills supply expertise, not authority or mandatory phases"); [workflow guide](../../../plugins/lusona/references/workflow-guide.md) Routing ("not a required sequence") and Terminology |
| P2 | Refinement is the goal. Each pass compares its result with the intended outcome, separates facts from assumptions, and carries outcome, accepted decisions, authority, TDD level, evidence and uncertainty into the next pass. | User 2026-11-11 ("refining the system and design over time"); README lines 26-27, 31-32 |
| P3 | Prior decisions are inputs, not grounds for rejection. Read and apply accepted decisions. When a new requirement, specification, measurement or experiment contradicts a decision in part or in full, do not reject the new input because the decision exists, and do not proceed as if the decision did not exist. State the decision, the conflict and the affected assumptions, revisit the decision with the user, and record the new understanding under P4. | User 2026-11-11 ("past decisions should be considered and flagged, but never a road-block"; clarified 2026-11-11, see decision 6); README line 43 |
| P4 | Recorded invalidation. After a revision, mark the superseded decision with date and source, keep its rationale, reconcile affected records, assignments and handoffs within write ownership, and report corrections other owners must make. Resume from the revision. A stale record cannot reinstate a superseded choice. | README lines 44-46; practice in [work.md](../work.md) (20261110 row superseded, decisions carried here) |
| P5 | Evidence over assertion. State behavior and completion only from observed checks; report unrun or failed checks as such. A failed or unrun required check blocks completion. | README line 31 ("separating facts from assumptions"); 20261110 mapping row 37; [AGENTS.md](../../../AGENTS.md) ("Say when installation or interactive behavior has not been tested"); suite check C9 (Evidence label only) |
| P6 | Authority stays with the user. Flagging a contradiction does not authorize changing accepted outcomes, contracts, TDD level or consequential commitments. Specs, plans, ADRs and queue states do not authorize implementation. | README Contract (lines 68-74); contract K4; suite checks C5, C8 |
| P7 | Continue bounded work. Take the next bounded authorized action without another command; stop inquiry when more exchanges or experiments would not change the outcome or the next action; pause only the affected work and state the resumption prerequisite. | README lines 31-38; suite check C7 |
| P8 | Every reply names the next action. End each task reply with one concrete next action and its owner, or state that none is needed and why. | README Questions and next actions; [AGENTS.md](../../../AGENTS.md) ("a concrete next action in every skill"); suite check C1 |

P3 and P6 (decided, decision 6). A prior decision is not a reason to reject new input, and
it is not set aside without the user. When new input contradicts an accepted decision:

1. State the decision, its source, the conflict and the affected assumptions in the reply and
   in the owning record.
2. Revisit the decision with the user: give the options and a recommended answer, and work
   with the user to a new understanding (kept, revised in part, or superseded).
3. Record the outcome under P4 before work that depends on the decision continues.
4. Work the conflict does not affect continues within the existing authority. (Analyst
   inference from P7; not stated by the user.)

### Skill voice (accepted)

Status: V1-V9 accepted by the user on 2026-11-11 (decision 7); the measurable limits below
remain proposals, set in W2. Scope: text in
`SKILL.md` files, references, shared blocks and templates. User statement 2026-11-11: "we
should also establish a voicing we should use in our skills. It should obviously be agent
friendly and direct." "Global rules" means the user's global writing rules, which apply to
instructions written for the user.

| ID | Rule | Source |
| --- | --- | --- |
| V1 | Write instructions in the imperative, addressed to the agent, with the trigger stated: "When X, do Y"; "Before X, read Z". | AGENTS.md ("Write direct instructions with an action and trigger"); user statement ("direct"); the 20261110 every-task block draft ("Before dispatching, read `references/delegation.md`"; draft discarded, decision 11) |
| V2 | Lead with the action. No preamble and no restatement of the skill's purpose inside instruction text. | Global rules ("Lead with the answer", "No preamble") |
| V3 | One instruction per sentence where possible. | Every-task block style (bold label followed by short imperative sentences; the 20261110 block draft, accepted in its decision 10; draft discarded, decision 11); proposal for the "where possible" bound |
| V4 | One term per concept. Use the terms defined in the [terminology table](../../../plugins/lusona/references/workflow-guide.md#terminology) and link it; do not introduce synonyms. | AGENTS.md ("Replace overlapping wording"); proposal for the linking requirement |
| V5 | State conditions instead of hedges: "when", "unless", "only when". Do not use "usually", "consider", "may want to", "try to" in instructions. | User statement ("direct"); global rules ("Say 'I am guessing' rather than hedging with softeners"); banned list is a proposal |
| V6 | Plain, literal language: no idioms, metaphors or analogies; do not attribute intent to code; no filler adjectives (robust, seamless, elegant, powerful, best-in-class) or filler verbs (leverage, delve, unlock, streamline). Precise technical terms are allowed. | Global rules ("Plain, literal language") |
| V7 | Numbers instead of vague intensifiers ("at most 2 correction rounds", not "a few"). | Global rules ("Replace vague intensifiers with numbers") |
| V8 | Give each shared policy one authoritative definition; link it instead of restating it, except short local repeats that make a skill easier to execute. Do not chain references in a way that hides the action. | AGENTS.md ("one authoritative definition"; "avoid reference chains that obscure the action") |
| V9 | No rationale in instruction text unless it changes the action; rationale belongs in specs and ADRs. | Proposal; supported by AGENTS.md ("Keep context and process small") |

Measurable limits (proposals only, decided in W2): a script-checkable banned-word and hedge
list taken from V5 and V6; a maximum average sentence length per file (for example 20 words,
to be set from a measurement of the 234-word block and the drafted `implement` skill).
Decided limits and the banned list as they stand: decisions 1-21 in the
[voice limits notes](../notes/voice-limits-measurement.md).

### Target structure (observable outcomes)

- S1: Each `SKILL.md` contains every rule that applies to every task (the every-task block) and
  needs no other file to apply them.
- S2: Every other rule is in a reference file that a skill or the block names with a trigger
  sentence ("Before X, read Y").
- S3: No skill, reference or shared block depends on the plugin README for a rule. The plugin
  README holds an overview, the reference catalog with each reference's trigger, and human
  documentation. `status` may still read the consuming project's `docs/lusona/README.md`.
- S4: Size limits (accepted by the user 2026-11-11, decision 10): line ceilings
  checked by a script that fails above them: `SKILL.md` at most 500 lines, reference at most
  200, Markdown template at most 100 (source: skillsdirectory.com skill file structure page,
  user-supplied as input). Not limited: scripts, because the K3 helpers must keep their
  commands and `work-record.ps1` already has 296 of the page's 300 lines; and
  `templates/visual-page.html` (1096 lines), which is a page asset rather than a Markdown
  template. The ceilings stop uncontrolled growth only; they do not set a target. Measured
  sizes: at `34186da` the largest `SKILL.md` has 95 lines (`batch`), the largest reference 123
  (`interview-examples.md`), the largest Markdown template 97 (`spec.md`); the drafted
  `implement` skill with the shared block and final reply has 140 (2026-11-11, `wc -l`).
  W5 records per-skill line and word counts of the draft so a lower limit can be set from data
  (moved from W4: no draft existed at W4).
- S5: Skill directory names are lowercase and hyphenated; frontmatter has `name` and
  `description`; at `34186da` every `name` equals its directory name (checked with `git show`).
- S6: Bundled paths resolve relative to the loaded skill on both hosts (AGENTS.md).

### Skill template (input from 20261110 decision 2)

The section order of [20261110 "Skill template"](20261110-standard-skill-template-and-inline-rules.md#skill-template-decision-2)
is the input. The 20261110 `implement` pilot was discarded (decision 11); W5 drafts a new one.

| Element | Status |
| --- | --- |
| Frontmatter description: action and output, "Use when ...", "Not for ...; use <skill>" | Kept as input; wording may change (K1 allows) |
| H1, then the generated every-task block | Kept |
| `## Persona and judgment` with Persona, Responsibility, Decision criteria, Evidence, Failure modes | Kept |
| `## Establish <input>`, optional `## <Domain> practices`, `## <Procedure> and record` | Kept |
| `## Final reply` last, from one shared final-reply source plus the skill's valid next actions | Kept; A2 and A4 open |
| Where principles P1-P8 appear (block line, reference, or both) | Open; decided in W5 after W1 |

### Acceptance criteria

Contract checks run against baseline `34186da` and must be observed failing on a deliberate
break in a fixture before they count (targeted TDD).

- [x] AC1: P1-P8 are marked accepted or revised in this spec with the user's decision, date and
  source; the P3/P6 resolution is recorded (done: decisions 6 and 7).
- [x] AC2: V1-V9 and the measurable limits are marked accepted or revised in this spec with the
  user's decision, date and source. V1-V9 done (decision 7); limits done (decision 12).
- [x] AC3: A repository check fails when any skill, reference or shared block contains a word
  or phrase from the accepted banned-word and hedge list (V5, V6), and passes on the draft. The
  list lives in the check script, outside the checked text, so plugin text never needs to
  name the banned words.
  Remaining voice rules are verified by review against V1-V9.
- [x] AC4 (K1): A repository check fails when a skill directory of the 14 is missing, renamed,
  or its frontmatter `name` differs from the directory name.
- [x] AC5 (K2): A repository check fails when a K2 path, the `YYYYMMDD-slug` ID form, or a queue
  state name is absent from the rewritten references that define them.
- [x] AC6 (K3): `scripts/test-work-record.sh` and `scripts/test-work-record.ps1` pass against the
  rewritten helpers, and no assertion present at `34186da` is removed or weakened (checked by
  diff of the test files).
- [x] AC7 (K4): A repository check fails when the shared block and final-reply source omit any
  TDD level, any of the four statuses, or the authority rule; suite checks C5 and C9 cover the
  behavior.
- [x] AC8 (K5): A repository check fails when either native manifest or a catalog names the
  plugin other than `lusona`.
- [x] AC9: Old records remain usable: a fixture project with one record of each kind created
  from the `34186da` templates (spec, ADR, notes, evidence, history, `work.md`), plus a legacy
  `NNNN-slug` record, is read and updated by the rewritten skills without migration, observed
  in a suite scenario (W12) or a recorded manual trial.
- [x] AC10: README independence: a repository check fails when a `SKILL.md`, reference or shared
  block links to or names the plugin README (`plugins/lusona/README.md`, `../../README.md`) as
  required reading. Links to the project's `docs/lusona/README.md` are allowed.
- [x] AC11: Template conformance: carries 20261110 AC1, AC2, AC5, AC6 unchanged, as repository
  checks that fail on a deviating skill.
- [x] AC12: Shared-block sync: carries 20261110 AC3; a repository sync check fails when any
  skill's copy of a shared source differs from that source or lacks its markers.
- [x] AC13: Rule coverage: every row of a new rule inventory of the `34186da` core README and
  references (W15) is kept, moved, or removed with a stated reason; 20261110 AC4 and AC7 carry.
  The [20261110 mapping](20261110-standard-skill-template-and-inline-rules.md#core-rule-mapping-ac8)
  (54 rows) is an input to W15 only. Verified by review.
- [x] AC14: Reference triggers: a repository check fails when a reference has no trigger
  sentence in any skill or shared block, or exceeds the accepted size limit (S4).
- [x] AC15: Hooks removed: carries 20261110 AC10.
- [x] AC16: Existing checks pass: link check, package build, native manifest validation,
  `scripts/test_*.py`, and the `evals/loop-conformance` unit tests. `scripts/check_instructions.py`
  is revised to skip generated block regions, because the tracked version rejects "does not authorize" and "native question tool" in any
  `SKILL.md`. Unrun checks are reported as unrun.
- [x] AC17: Independent review: a reviewer who did not write the change receives this spec, the
  diff and check output; blocking findings are corrected and re-verified.
- [x] AC18: Loop behavior: one suite run on the promoted or draft plugin (U5) covering the C9
  scenarios with the 20261110 U1 pass mark, plus the principle scenarios from W12 (a
  new requirement that contradicts an accepted decision: the agent does not reject the
  requirement because of the decision, does not proceed past the decision without the user,
  states the conflict with the decision's source, asks the user with a recommended answer,
  records the agreed outcome under P4, and no superseded choice is reinstated; decision 6)
  with pass marks declared before the run. Budget per U4.
- [x] AC19: The user accepts or rejects the AC18 result; acceptance is recorded here.
  Verification (2026-11-11): AC3-AC5, AC7, AC8, AC10-AC12, AC14-AC16 by the repository checks and
  tests on the promoted plugin (all pass; package `lusona-3.0.0.zip` builds); AC9 by the
  `old-records` scenario (C16 and C17 5/5 on both hosts); AC13 by the W15 inventory, destination
  maps and the W13 sample audit; AC17 by W13; AC18 by the [suite run](../evidence/2026-11-11-rewrite-suite-run/README.md);
  AC19 accepted by the user on 2026-11-11 ("accept", decision 25); AC6 by
  `test-work-record.sh` and `test-work-record.ps1` (PowerShell 7.6.10 via `mise exec`, 187
  assertions) passing, with a test diff of the 13 allowed lines (decision 22).

### Decisions and uncertainty

Accepted decisions (user, 2026-11-11, native question tool, relayed by the coordinator):

1. This spec supersedes and absorbs spec 20261110. Its decisions 1-10 carry in as inputs with
   the statuses below. The 54-row mapping is linked, not copied. (The `drafts/` workspace part
   is revised by decision 11.)
2. Public contract K1-K4 as stated above; `plugins/lusona/templates/` exempt. K5 is a
   coordinator assumption.
3. The plugin README is not contract; it becomes human documentation and catalog only. New
   skills read records created from old templates; new records may use new templates.
4. TDD `targeted` (see TDD policy).
5. Skill voice is in scope (user, 2026-11-11, relayed by the coordinator).
6. P3/P6 (user, 2026-11-11, conversation): "we should revisit the decision, not just ignore it
   and proceed. The principles I named was to highlight that we shouldn't plainly reject because
   a past decision said so; the agent should work with the user to come to a new understanding
   and record it." Replaces the proposed resolution (flag, continue, ask only for outcome or
   contract changes). P3 text revised to match.
7. P1-P8 (P3 as revised) and V1-V9 accepted (user, 2026-11-11, conversation: "accept"). The
   measurable voice limits stay proposals until W2 sets them from a measurement.
8. U8 (user, 2026-11-11, "yes as recommended"): `docs/lusona/product.md`, `plans/`,
   `batches/`, `visuals/` and the project `docs/lusona/README.md` are contract (K2), at least
   for reading existing records.
9. U9, U10, U11 (user, 2026-11-11, conversation): add principle-specific scenarios to the
   suite (W12): yes. W4 layout experiment budget: $20. New skills may be added beyond the 14:
   yes (K1 still forbids removing or renaming the 14). U12: the user asked for a
   recommendation; S4 states it.
10. U12 and selection (user, 2026-11-11, "accept U12; start W2 and W3"): S4 limits accepted;
    W2 and W3 selected and authorized (development-time check scripts under `scripts/`). Each
    selected item gets its own queue row linking this spec; a child spec is created only when
    the item needs agreement beyond this spec's ACs.
11. `drafts/` (user, 2026-11-11, native question tool): the untracked workspace (every-task
    block, `implement` pilot, `drafts/rules.md`, `sync_shared.py`, revised
    `check_instructions.py`) was moved to Trash intentionally. The rewrite starts in a new, empty
    `drafts/` workspace. Prior draft content is not an input; a new rule inventory (W15)
    replaces `drafts/rules.md`.
12. W2 and W3 decisions (user, 2026-11-11, native question tool):
    - Voice limits accepted as proposed in the
      [measurement note](../notes/voice-limits-measurement.md): V5/V6 terms plus generally,
      typically, ideally, perhaps, probably, possibly, maybe; a file fails above an average of
      15 words per sentence. Added: "as needed" and "when needed" are banned (V5); a sentence
      fails above 40 words; `templates/*.md` are scanned for banned words, not sentence limits.
    - K4 stays strict: the vocabulary must appear in skill, reference or shared text; the 2
      findings on the current plugin are the known baseline gap.
    - The broken `../references/retention.md` link in `templates/spec.md` and
      `templates/notes.md` is fixed in W5 (templates are exempt); AC6 is verified on the draft.
13. W4 decisions (user, 2026-11-11, native question tool), from the
    [reference layout experiment](../evidence/2026-11-11-reference-layout/README.md):
    - A6 layout: hybrid. References used by more than one skill stay in plugin-level
      `references/`, linked as `../../references/x.md`; a reference used by one skill moves to
      `skills/<skill>/references/`. Bare paths to plugin-level files are rejected by a check.
    - Shared every-task block and final-reply sources live at the repository level, outside
      `plugins/lusona/`, are not packaged, and are generated into each `SKILL.md` by the sync
      script; no runtime link points to them.
    - The 17 trial trust entries were removed from `~/.codex/config.toml` (backup
      `~/.codex/config.toml.bak-20261111`); the trials' session logs are kept.
14. ADR placement details and W15 (user, 2026-11-11, conversation): P-a revised: a skill uses a
    reference only when its `SKILL.md` links it directly; reference-to-reference chains are
    avoided. P-b accepted: a change that moves a reference's use count across 1 and 2 moves
    the file and fixes every link. V3 counts only sentences over 40 words in the inventory. The
    coverage check moves to `scripts/check_rule_inventory.py`.
15. W5 start (user, 2026-11-11, native question tool and "proceed with W5"): W5 selected.
    `drafts/lusona/` starts truly empty: only files written or changed by the rewrite; contract
    and package checks run on the whole draft after W9-W10. The every-task block is at most 250
    words (limit superseded on 2026-11-11 by decision 26: 300 words, enforced by
    `scripts/sync_shared.py`; the block is 285 words). A8: templates are renamed to `name.ext.template` (for example `spec.md.template`) and
    the record helpers are updated to read them; K3 commands, output and exit codes do not
    change. No checkpoint commit yet.
    Coordinator notes: (a) W5 copies the `34186da` templates and helpers into the draft only
    because W5 changes them (rename, link fix); this is not a seed. (b) Conflict with AC6:
    `scripts/test-work-record.sh` copies templates by name and hard-codes `plugins/lusona`, so the
    rename changes baseline test lines that the AC6 comparison reports as removed assertions; AC6
    needs a user decision on allowed test changes before W14. (c) Draft sources for shared
    blocks live in `drafts/shared/` and move to repository-level `shared/` at promotion.
16. W5 acceptance (user, 2026-11-11, conversation): the every-task block, final reply, skill
    skeleton (`drafts/skill-template.md`) and `implement` pilot are accepted; the user measures
    effectiveness once the rewrite is done. Changes: status glyphs restored (✅ Complete,
    🔄 In progress, ❓ Needs input, ⏸ Paused); the Authority line adds "Commit, push or publish
    only with the user's authority; authorized implementation and refactoring include local
    commits", raising the block budget to about 260 words (266 by `wc -w`); the final reply links
    the completion examples (Q4). Q1: `model-routing` and `worker-lifecycle` merge into
    `delegation`, `handoff` into `retention` (W9). Q2: host and project restriction rules
    (readme-015, readme-066) are removed. Q3: explore and status conversation stays with the
    coordinator; substantive work is delegated (revised in part 2026-11-11, decision 28). Q5: greetings are not task replies, and there is
    no task-local check exception; accepted on the coordinator's recommendation, may be revisited.
    A2, A3, A5 accepted as proposed in `drafts/README.md`. A4: `batch` and `status` may add H2
    sections through a named exception list in the template check.
17. Block triggers (user, 2026-11-11, "Yes"): the every-task block reads `delegation` before
    dispatch and after each leaf result, `revisions` before revisiting a decision, and
    `retention` at 40% context use; 279 words by `wc -w`.
18. Rule changes in W6, W7, W9 (user, 2026-11-11, "accept", after the coordinator clarified that
    V5 bans "when needed" and "as needed", not "when"): accepted: interviews at most 3 questions;
    tdd `none` coverage conditions; queue finish-first rule with exception; checkable conditions
    in retention and delegation; no task-local delegation exception in evidence; revisions
    records kept decisions; 3 added completion examples; frame-product `accepted` only on user
    acceptance; specify work-item table only on request.
19. W8 and W12 (user, 2026-11-11, "accept all"): W12 pass marks in
    `evals/loop-conformance/pass-marks.json` accepted (5/5 for C8, C12, C15, C16; 4/5 for C13,
    C14, C17; both hosts). `status` saves only when authorized (stated exception to the block's
    Saving line; baseline `status` was read-only). Batch start and resume prompts stay in the
    `batch` skill's references; `status` lists the inputs. A new reference run of the existing
    scenarios is needed before comparison (cost goes into U4). W10 and W13 selected.
20. W13 corrections (user, 2026-11-11, conversation): F1: a leaf may delegate when the
    coordinator grants it in the assignment; the block's Role line now reads "As a leaf, delegate
    only when your assignment grants it, and do not ask the user" (block 285 words by `wc -w`). This revises the A5 leaf rule
    accepted in decision 16. N4: the voice check also scans Markdown link text and skill
    descriptions ("Yes, it should", read as both). All non-blocking findings are fixed except N1
    and N9 (W14). F2: the user asked whether the README is dropped; decision 3 keeps it as human
    documentation and catalog. Pending the user's answer, the README's skill table is replaced by
    a link to `workflow-guide`.
21. W13 follow-up (user, 2026-11-11, conversation): the plugin README stays as human
    documentation; no skill, reference or shared text uses it (AC10 check). The version becomes
    3.0.0 (user changed the root and draft manifests); `plugins/lusona` manifests move to 3.0.0
    at promotion (W14), until then `test_package` reports the root/canonical mismatch. The leaf
    that dispatches leaves under a delegation grant stops them and carries their results into its
    own result; it reports any leaf it could not stop.
22. W13 acceptance and W14 inputs (user, 2026-11-11, conversation: "accept W13; 1. yes 2. on
    draft, $40 3. tighten 4. yes"): W13 accepted. AC6 allows the 13 helper-test lines changed by
    the template rename (`tmp/w5c/test-diff.patch`). U5: the AC18 run uses the draft. U4: $40 of
    Claude-reported spend. U1: the 20261110 pass mark is tightened before the run (marks proposed
    to the user). Promotion of the draft into `plugins/lusona/` at version 3.0.0 is authorized;
    commits are not.
23. AC18 run scope and U1 mark (user, 2026-11-11, native question tool): scope "AC18 + C9
    reference": on the draft, the 4 C9 scenarios (`tdd-stated`, `authz-change`, `status-check`,
    `investigate-bug`) and the 3 principle scenarios, 5 trials per host; then the 4 C9 scenarios on
    baseline `34186da` as the fresh reference; draft trials first; stop at $40 of Claude-reported
    spend (estimate about $36). U1 mark: C9 passes in at least 4 of 5 trials on each host in all
    four C9 scenarios; declared in `evals/loop-conformance/pass-marks.json` before the run.
24. Suite run conditions (user, 2026-11-11, native question tool): Codex trials may add their
    trust entries to `~/.codex/config.toml` (codex-cli adds one per workspace even with
    `--ignore-user-config`; run 003 did the same); after the run the coordinator backed up the file
    (`config.toml.bak-20261111-run`) and removed all 132 `lusona-evals` entries. The run cap was
    raised from $40 to $60 after round 1.
25. AC19 (user, 2026-11-11, "accept"): the AC18 result is accepted with its two missed marks
    (Claude Code `old-records` C8 3/5; Codex `authz-change` C9 3/5), each recorded as an Ideas row
    in the queue.
26. Voice pass after promotion (user, 2026-11-11, conversation and native question tool): the
    promoted text was audited against V1-V9 and changed in agreed classes. The
    [voice limits notes](../notes/voice-limits-measurement.md) own the detail (decisions 5-21).
    In short: wording made imperative and literal; qualifiers without a test (`relevant`,
    `useful`, `substantive`, size words, `safe`, `material` and others) replaced by a stated
    test or deleted; `substantive` and material evidence each defined once; terms unified
    (`repair budget`, `queue state`, `execution record`) and six terms added to the
    Terminology table; the domain-skills sentence names each skill's first action; three
    descriptions split; two sentences of the shared final reply reworded; Icebox described as a
    section of the queue, not a queue state; the banned list extended (`check_voice.py`); the
    every-task block limit set to 300 words and enforced (supersedes the 250 words of decision
    15). These are rule changes agreed after AC19, so the AC18 run measured the earlier text.
27. Closing (user, 2026-11-11, "close the rewrite item"): the item closes without a suite rerun on
    the committed text and without independent review of the voice pass. The limits recorded
    under Voice pass results stand. Push and publication stay unauthorized.
28. Delegation revised in part after closing (user, 2026-11-11, conversation: "accept the three
    texts, TDD none"), on the user's report that `status` is slow under delegation.
    Decision 4 of spec 20261110 (delegation at every task size; row 4 of the table below) is
    revised in part: the Role line now reads "Delegate specialist work at every task size, except
    work the skill assigns to the coordinator" (replaced: "Delegate specialist work at every
    task size"). Decision 16 Q3 is revised in part for two skills. `status` (replaced: "Delegate
    inventory and inspection work") does the assessment itself and delegates only an audit of
    product source code that the question depends on. `explore` (replaced: "Delegate research
    and analysis") reasons from the conversation, the project records and the files the user
    names, and delegates research that needs other sources. The rationale of both decisions
    stands for the other 12 skills, which assign no work to the coordinator. Record:
    [notes](../notes/selective-delegation-for-status-and-explore.md).
20261110 decisions as inputs:

| # | Decision (short) | Status |
| --- | --- | --- |
| 1 | Every-task rules in each skill; others in references | Kept; extended by user decision 3 (README not contract) |
| 2 | One template for 14 skills, persona each | Kept as input; see Skill template table |
| 3 | Full final reply form at every task size | Kept |
| 4 | Delegation at every task size, local fallback stated | Kept; revised in part 2026-11-11 (decision 28) |
| 5 | No runtime hooks or Python; remove hooks work | Kept (W11) |
| 6 | TDD `targeted` | Revised: reselected 2026-11-11 with new test-first behaviors |
| 7 | Acceptance by checks, review, one C9 suite run | Revised: adds contract checks and principle scenarios (AC18) |
| 8 | Draft in `drafts/`; promote after acceptance | Kept, but the workspace restarts empty (decision 11) |
| 9 | One block source, dev-time sync script, sync test | Kept for the mechanism; source location reopened under A6; the script is rewritten (decision 11) |
| 10 | 234-word block accepted; formatting in Final reply; `completion.md` examples only | Revised: block text discarded (decision 11) and rewritten in W5 under P1-P8 and V1-V9; formatting in Final reply and `completion.md` examples only are kept |

20261110 exclusions: "no change to policy meaning except decisions 3 and 4" is revised (accepted
principles may change policy meaning; K1-K5 do not change). "No change to C1/C9 grading or the
eval rubric" is revised to: existing checks unchanged; new scenarios, checks and rubric entries
may be added (W12; confirmed by decision 9). "No new skills" is revised: new skills may be
added (decision 9). "No version bump" is kept.

Open architecture questions. A6 and A7 are decided in
[ADR 20261111](../adr/20261111-skill-file-layout-and-shared-sources.md); A2-A5 and A8 move to W5. A6 and A7 are settled by a package build of the
draft plus a loading audit on both hosts using the [run 008 method](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md#method-and-provenance);
A4 by a pilot draft of `batch` and `status`; A8 by a user decision without an experiment.

- A1: Mechanism settled by decision 9; the source location moves to A6.
- A2: Reply template relation to the block. The discarded pilot generated a shared
  final-reply source into each skill; reopened (decision 11).
- A3: Block size and style. The discarded block had 234 words; limit not set; reopened.
- A4: Whether `## Final reply` and the template check apply unchanged to `batch` and `status`.
- A5: Leaf role rules. The discarded block used a Role line; reopened (decision 11).
- A6: Layout: plugin-level `references/` (current) versus per-skill `references/` versus both;
  where shared sources live. `scripts/package.py` line 82 copies a fixed list
  (`skills`, `templates`, `scripts`, `references`, `assets`, `hooks`) and excludes `shared/`.
- A7: Path form in skill text: the block names `references/delegation.md` as a bare path, while
  existing skills link `../../references/...`. Which form each host resolves from the loaded
  skill (S6).
- A8: Whether templates adopt the `name.ext.template` naming from the external page (templates
  are exempt from contract).

User questions (U1-U3 answered in 20261110 and carried; IDs continue from it):

- U1 (answered 2026-11-11, decision 23: C9 ≥ 4/5 per host in 4 scenarios): keep or tighten the 20261110 U1 pass mark; its Codex `authz-change`
  half is met by any result, and `status-check` and `investigate-bug` have no mark.
- U4 (answered 2026-11-11, decision 22: $40): budget for the AC18 run. References: run 006 `tdd-stated` $1.737 for 6
  trials; run 003 about $40 for the full suite.
- U5 (answered 2026-11-11, decision 22: draft): run AC18 on the draft (`run.py --plugin drafts/lusona`) or after promotion.
- U6: Answered 2026-11-11 (decision 7).
- U7: Answered 2026-11-11 (decision 6).
- U8: Answered 2026-11-11 (decision 8).
- U9: Answered 2026-11-11 (decision 9). Adding scenarios changes `suite.lock.json` and
  limits comparison with the stored reference to the existing scenarios.
- U10: Answered 2026-11-11 (decision 9): $20.
- U11: Answered 2026-11-11 (decision 9).
- U12: Answered 2026-11-11 (decision 10).
- U13: V1-V9 answered 2026-11-11 (decision 7); measurable limits open until W2.

### TDD policy

- Level: targeted
- Selected by user: 2026-11-11 (native question tool, relayed by the coordinator)
- Test-first behaviors, each a repository check observed failing on a deliberate fixture break
  before it counts:
  1. Skill template conformance (AC11).
  2. Contract compatibility: skill names (AC4), data paths and states (AC5), helper CLI (AC6),
     vocabulary (AC7), manifest identity (AC8).
  3. Shared-block sync (AC12).
  4. Voice banned-word and hedge list (AC3); added by the user's voice scope addition;
     V1-V9 accepted (decision 7); list contents set in W2.
  5. Manifest `hooks` check (AC15), carried from 20261110 test-first behavior 3.
- Proposed test-first, pending user confirmation (not in user decision 4): README independence
  (AC10) and reference triggers (AC14). Until confirmed they are regression checks.
- Required regression coverage: AC16. Wording and principles are verified by review (AC13) and
  the loop-conformance suite (AC18), not test-driven.

## Execution

Each work item becomes its own queue row and spec only when the user selects it. Rewrite text is
drafted in a new, empty `drafts/lusona/` (decision 11); changes to `plugins/lusona/` need user authorization (promotion in
W14). Order follows dependencies; items without a dependency between them can run in parallel.

| ID | Outcome | ACs | Depends on | Suggested skill |
| --- | --- | --- | --- | --- |
| W1 | Loop principles accepted or revised; P3/P6 resolution decided (done 2026-11-11, decisions 6-7) | AC1 | None | explore |
| W2 | Skill voice accepted; banned-word list and sentence limit set; voice check written test-first | AC2, AC3 | None (parallel to W1) | explore, then implement |
| W3 | Contract inventory against `34186da` and compatibility checks written test-first | AC4-AC8 | U8 (answered) | specify, then implement |
| W15 | New rule inventory of the `34186da` core README and references (replaces the discarded `drafts/rules.md`), each rule tagged against P1-P8 | AC13 (input) | W1 | investigate |
| W4 | ADR on layout and path form (A6, A7), from a package build and a loading experiment on fixture skills on both hosts (done 2026-11-11: [ADR](../adr/20261111-skill-file-layout-and-shared-sources.md), decision 13) | AC10, AC14 (structure) | W1, U10 (answered: $20) | experiment, then architect |
| W5 | Template and shared sources final; templates contain no plugin-relative links (decision 12); A2-A5 and A8 decided; P-a and P-b applied (decision 14); bare-path check added; per-skill line and word counts recorded (block, final reply, principle placement); template, sync, README-independence and trigger checks written; `check_instructions.py` revised; AC13 table reconciliation | AC10-AC12, AC14, AC16 | W1, W2, W4 | implement |
| W6 | Definition skills rewritten: explore, frame-product, map-capabilities, specify, design, architect | AC11, AC13 | W2, W5 | implement |
| W7 | Execution skills rewritten: implement, refactor, review, investigate, measure, experiment | AC11, AC13 | W2, W5 | implement |
| W8 | Coordination skills rewritten: status, batch | AC11, AC13 | W2, W5, A4 | implement |
| W9 | References rewritten with triggers and size limits | AC13, AC14 | W2, W4, W5 (can interleave with W6-W8) | implement |
| W10 | Plugin README reduced to overview, catalog and human documentation | AC10 | W6-W9 | implement |
| W11 | Hooks work removed | AC15 | None (applies at promotion) | implement |
| W12 | Suite scenarios for P3/P4 and old-record readability, with pass marks | AC9, AC18 (scenarios) | W1, U9 (answered: yes) | specify, then implement |
| W13 | Independent review of the complete draft and checks | AC17 | W3, W5-W12 | review |
| W14 | Promotion (authorized), suite run, user acceptance | AC16, AC18, AC19 | W13, U4, U5 | measure |

- Verification: `python3 -m unittest discover scripts`, `bash scripts/test-work-record.sh`,
  `pwsh scripts/test-work-record.ps1`, the shared-source sync check (rewritten in W5),
  package build to `tmp/`, eval unit tests in `evals/loop-conformance/`. Commands to confirm at
  implementation; none run for this spec.

## Evidence

### Voice pass results (2026-11-11, after AC19; decision 26)

- Applied in steps, each listed row by row in [notes/voice-pass](../notes/voice-pass/) (rounds 2-4 with
  the basis of each row): 210 wording edits; 143 agreed
  replacements (qualifiers, size words, two terms, the domain-skills sentence, descriptions,
  shared final reply); 24 term edits; 99 replacements for the remaining audit findings plus 3
  label and dialogue edits; 34 replacements that set a new criterion; 32 replacements for words
  found by a word sweep; 7 edits for the last 8 uses. 23 edits of the first step were reverted
  before any agreement because they changed a criterion.
- Checks on the result: `check_voice.py` 0 findings with the extended banned list;
  `sync_shared.py --check`, `check_skill_template.py`, `check_instructions.py`,
  `check_contract.py` (0 findings) and `check_rule_inventory.py` pass; 229 script tests and 150
  suite unit tests pass; `test-work-record.sh` passes; `test-work-record.ps1` passes (187
  assertions, PowerShell 7.6.10 run through `mise exec`); package `lusona-3.0.0.zip` builds.
- Test-first evidence: banned-list additions (6 failures, then 46 tests; 7 failures, then 49
  tests) and the every-task word limit (2 failures, then 18 tests).
- Limits: the loop-conformance suite was not rerun, so no behavior measurement covers the
  text after the voice pass; the AC18 and AC19 results describe the text before it. No
  independent review of the voice pass was run.

### W14 results (2026-11-11)

- Promotion: `plugins/lusona/` equals the draft at 3.0.0; shared sources in repository `shared/`;
  219 script tests and 150 suite tests pass; voice, template, contract (0 findings), instructions,
  sync checks pass; package `lusona-3.0.0.zip` builds with its link check. `pwsh` absent: the
  PowerShell helper tests were not run.
- AC18 run ([evidence](../evidence/2026-11-11-rewrite-suite-run/README.md)): 110 counted trials,
  $52.65 Claude-reported. The draft meets 12 of 13 pass marks on each host. Not met: Claude Code
  `old-records` C8 3/5 (trials 4 and 5 added a test command to `docs/lusona/README.md` without
  asking) and Codex `authz-change` C9 3/5 (replies without `Result`/`Evidence` labels). Against the
  fresh `34186da` reference, C9 rose in all 4 scenarios on both hosts (e.g. `tdd-stated` 0/5 to
  5/5 Claude Code, 0/5 to 4/5 Codex). Limits: no judge calibration on the current rubric; one
  invalid reference trial; host patch versions differ from run 003. AC19 accepted (decision 25).

Definition only; no checks run. Inline check at creation (2026-11-11): every AC appears in at
least one work item and every work item names its ACs; every principle and voice rule has a
source or is labelled a proposal; each contract item K1-K5 has a check (AC4-AC8); decisions
1-10 each have a status. Correction from sources: the coordinator's brief cited "`tdd-stated`
C9 0/13"; run 008 reports the core README returned in 0/13 `tdd-stated` trials, and run 003
reports `tdd-stated` C9 failing 5/5 per host; the agreement cites both as recorded. Blocking
questions at creation: U6 and U13 blocked W5-W10 and U8 blocked W3 (all answered 2026-11-11,
decisions 7-8); U1, U4 and U5 block W14. No contradiction found
between the contract and the exclusions after revising the two 20261110 exclusions above.

### W10 results (2026-11-11)

- `drafts/lusona/README.md` (103 lines): human documentation, catalog of 23 references with
  triggers, states that no skill requires it; 56 relative links resolve.
- `scripts/package.py`: `--plugin PATH` option; link check scans `*.md.template`; 3 new tests
  red then green; `unittest discover scripts` 167 OK. Live build exit 0.
- Draft build: exits 1 on 12 broken links in repository-level `README.md`, its 4 translations and
  `INSTALL.md`, which link baseline references the draft merged or moved (`batch-execution`,
  `batch-use`, `model-routing`, `work-record`). Those files must change together with promotion
  (W14), using the mapping in `tmp/w10/diag_build.py`; with that mapping the draft packages
  (77 files, no `hooks/`, no `shared/`). `test_package_exposes_design_with_linked_resources`
  expects the old README and template names and changes at W14.

### W8, W11, W12 results (2026-11-11)

- W8: `batch` (141 lines, 8 per-skill references, no reference chain) and `status` (123 lines,
  links `workflow-guide`); `drafts/reference-destinations-batch.md` covers 219 of 219 rows.
  Coordinator run on the whole draft (14 skills): voice, template, instructions, contract and
  sync checks all exit 0. `check_voice.py` now scans per-skill references (39 tests).
- W11: hook special cases removed from `scripts/package.py`, `scripts/test_package.py`;
  `INSTALL.md`, `PRIVACY.md` restored to `34186da`; `scripts/test_completion_reply.py` deleted;
  manifest `hooks` check test-first in `check_contract.py`; draft manifests, LICENSE, assets copied
  from `34186da` (version 2.0.5, no hooks). The live plugin keeps 2 hooks findings until W14.
  Draft package build fails: no `drafts/lusona/README.md` yet (W10), and `package.py` template
  checks need the `.template` names (W10).
- W12: scenarios `decision-conflict`, `decision-revised`, `old-records`; checks C12-C17; 10
  judge calibration cases; `pass-marks.json` (proposed, awaiting the user); lock refreshed by the
  worker. Suite tests: 150 OK (coordinator run). No actor run. The stored references are already
  refused by `compare.py` because `34186da` changed the rubric and calibration files; a new
  reference run is needed before comparison.

### W6, W7, W9 results (2026-11-11)

- Drafted: 12 skills in `drafts/lusona/skills/` (98-120 lines each; `implement` unchanged) and 15
  references in `drafts/lusona/references/` (1084 lines; largest `delegation.md` 146).
- Destinations: `drafts/reference-destinations-a.md` (307 rows, 16 removed with reasons) and
  `-b.md` (475 rows, 8 removed); coverage scripts in `tmp/w9a/`, `tmp/w9b/` exit 0.
- Coordinator run on the whole draft: sync in sync; `check_instructions.py` passed;
  `check_voice.py` 4 findings, all in templates; `check_skill_template.py` 1 finding
  (`workflow-guide.md` has no linking skill: W8 `status`); `check_contract.py` K1 `batch`,
  `status` missing (W8) and K5 manifests missing (W10/W14); `unittest discover scripts` OK.
- Open: trigger gaps for `delegation` (after each leaf result), `retention` (context at 40%),
  `revisions` (linked only at the record step); stale glyph rows readme-156/159; rule meaning
  changes listed in the worker reports, pending user review.

### W5 results (2026-11-11, accepted, decision 16)

- Checks: `scripts/check_skill_template.py` (template, README independence, direct reference
  links and placement, bare paths, size), `scripts/sync_shared.py`, revised
  `scripts/check_instructions.py` (skips generated regions); red against stubs, then green
  (template 49, sync 12, instructions 15 tests). `scripts/check_voice.py` now scans
  `.md.template` files (37 tests). Live plugin: 196 template-check findings (expected; old shape).
- Content in `drafts/`: `shared/every-task.md` (250 words), `shared/final-reply.md` (241
  words), `skill-template.md`, `lusona/skills/implement/SKILL.md` (114 lines),
  `readme-destinations.md` (187 README rows), `README.md` (proposals A2, A3, A5; Q1-Q5).
- Templates: 13 renamed to `.template` in `drafts/lusona/templates/`; 5 plugin-relative links
  replaced with plain text; helpers read the new names; draft copy of the bash helper test
  passes; PowerShell test not run (`pwsh` not installed). The repository test files need a
  13-line rename diff (`tmp/w5c/test-diff.patch`) for AC6.
- Coordinator run on the draft: `python3 -m unittest discover scripts` OK;
  `sync_shared.py --source drafts/shared drafts/lusona --check` exit 0;
  `check_skill_template.py drafts/lusona` 1 finding (pilot names `refactor`, not yet drafted);
  `check_instructions.py drafts/lusona` 2 findings (workflow-guide tables, references not yet
  drafted); `check_voice.py drafts/lusona` 4 findings, all in templates (W9).

### W15 results (2026-11-11)

[Rule inventory](../notes/rule-inventory-34186da.md): 1026 rows from 21 sources (README and 20
references at `34186da`); Kind: 670 rule, 224 definition, 94 catalog, 21 example, 17 not a rule.
Coverage check (`python3 scripts/check_rule_inventory.py docs/lusona/notes/rule-inventory-34186da.md
34186da`, coordinator rerun): 1004 content lines, 0 uncovered, 0 verbatim failures. Conflict tags
are the worker's judgment, not reviewed: V3 6 (sentences over 40 words, decision 14), V8 240 rows in 86
duplicate groups, V4 55, V1 37, V5 32; P3 4. K5 has no source line in the README or references.
The coverage script is `scripts/check_rule_inventory.py` (decision 14).

### W2 and W3 results (2026-11-11)

- W2: `scripts/check_voice.py`, `scripts/test_voice.py`; measurement in
  [voice limits measurement](../notes/voice-limits-measurement.md). Red: 19 of 29 tests failed
  against a stub; green: `python3 -m unittest scripts.test_voice` 30 tests OK. On
  `plugins/lusona` the check exits 1 with 5 findings (2 `consider`; 3 files above an average of
  15 words per sentence). List and limits accepted (decision 12) and implemented: red on 4 new
  tests, green 35 tests OK; on `plugins/lusona` the check now reports 21 findings (12 as/when
  needed, 2 `consider`, 4 sentences over 40 words, 3 file averages over 15). AC3 "passes on the
  draft" is unverified until a draft exists.
- W3: `scripts/check_contract.py`, `scripts/test_contract.py`. Red: 22 of 27 tests failed
  against a stub; green: `python3 -m unittest scripts.test_contract` 31 tests OK. On
  `plugins/lusona` the check exits 1 with 2 K4 findings: the four reply statuses and the
  authority sentence appear only in the README and `templates/status.md`, which the check
  excludes. AC6 limit: removed baseline assertion lines are detected; added lines that disable
  a test are not.
- `python3 -m unittest discover scripts`: 121 tests OK (coordinator run after both items).
- Pre-existing failure: `bash scripts/test-work-record.sh` exits non-zero at the working tree
  and at `34186da` (worker report): records created from `templates/spec.md` and
  `templates/notes.md` contain `../references/retention.md`, which does not resolve in a
  consuming project. AC6 needs this test to pass. `test-work-record.ps1` not run.

### W4 experiment results (2026-11-11)

[Reference layout experiment](../evidence/2026-11-11-reference-layout/README.md): 4 conditions
(L1 plugin-level `references/`, L2 per-skill `references/`; Markdown link or bare path) × 2 hosts
× 4 trials. L1-link, L2-link and L2-bare resolved the reference on the first read in 4/4 trials
on both hosts. L1-bare (bare `references/x.md` naming a plugin-level file) resolved 0/4 on both
hosts (Claude: 1 recovered, 3 not read; Codex: 4 recovered at about 35k extra input tokens each).
Claude spend $1.92 of $20; Codex reports no cost (1.26M input tokens, 6k output). Package build:
per-skill `references/` is kept; a plugin-level `shared/` folder is not packaged and a link into
it fails the build. Supported: A7, both hosts resolve paths from the skill directory, so the bare
form for plugin-level files is rejected. A6: loading does not decide L1 versus L2; the ADR decides
on duplication and packaging. Limits: 4 trials per cell, one fixture, trigger at task start; Codex
received the `SKILL.md` path in its prompt (installed-plugin loading untested). The run added 17
`[projects."…/tmp/w4/ws/…"]` trust entries to `~/.codex/config.toml` outside the repository;
removed by the coordinator with user approval (decision 13).

## Current handoff

- State: closed on 2026-11-11 by the user (decision 27) and recorded in
  [history](../history/2026-11-week-02.md#2026-11-11--loop-principles-and-skill-rewrite).
  Promoted into `plugins/lusona/` at 3.0.0 (decision 22); AC18 run accepted (decision 25); W1-W15
  done; voice pass applied after AC19 (decision 26). Committed on `main` in `43b4341`, `ee7fa2a`,
  `6eb0d26` and `70823d6`. The closing edits to this spec, spec 20261110, the queue and history
  are in the commit that follows `70823d6`.
- `drafts/` deleted on 2026-11-11 by user request; `drafts/lusona` equalled `plugins/lusona`. The
  drafting records it held (A2-A5 proposals, skill template, destination maps) moved to
  [notes/skill-rewrite-drafting](../notes/skill-rewrite-drafting/); earlier `drafts/` paths in this spec
  name that folder or the promoted plugin.
- Limits carried at closing: AC1-AC19 were verified on the text before the voice pass; no
  suite run and no independent review cover the text after it. At closing, `sync_shared.py
  --check`, `check_voice.py`, `check_skill_template.py`, `check_contract.py` and
  `check_instructions.py` exited 0 at `70823d6`; the tests, the package build and the suite were
  not rerun.
- Follow-ups are Ideas rows in the [work queue](../work.md). Push and publication are not
  authorized.
- Next action: none for this item.
