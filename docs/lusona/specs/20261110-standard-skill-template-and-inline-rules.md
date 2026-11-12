# Spec 20261110-standard-skill-template-and-inline-rules: Standard skill template and inline every-task rules

Created: 2026-11-10
Updated: 2026-11-10

Kind: refactor (instruction structure), with two policy clarifications (decisions 3 and 4)
Work item: [Work queue](../work.md) (row added by the coordinator; supersedes the row that links the missing `20261109-direct-instruction-checkpoints.md`)
Context: [completion-reply notes, 2026-11-10 sections](../notes/completion-reply-conformance.md),
[run 008 loading audit](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md),
[completion-reply spec](20261109-completion-reply-conformance.md),
[core README](../../../plugins/lusona/README.md)

## Agreement

- User and problem: Lusona users need rules that apply to every task (authority, delegation,
  TDD gate, saving, completion, questions, reply form) to reach the agent. On Claude Code the
  root agent received the core README in 35/60 run 003 trials, decided by scenario, so these
  rules were absent in whole scenarios (`tdd-stated` 0/13 across runs). Operation-triggered
  references were read in most trials once the operation occurred ([run 008](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md)).
- Desired structural outcome: each skill carries a short every-task rule block and a fixed
  section structure; all other core rules live in reference files read at the matching action;
  the core README becomes an overview and reference catalog. Observable behavior of the
  workflow is unchanged except decisions 3 and 4.
- Scope: all 14 `plugins/lusona/skills/*/SKILL.md`; `plugins/lusona/README.md`; reference files
  (existing, and new ones where the mapping below requires); removal of the uncommitted hooks
  work (`plugins/lusona/hooks/`, `plugins/lusona/scripts/completion_reply.py`, manifest `hooks`
  entries, the hook handling in `scripts/package.py` and `scripts/test_package.py`,
  `scripts/test_completion_reply.py`, the validation sections of `references/completion.md`, and
  the hook text in `INSTALL.md` and `PRIVACY.md`); development-time repository checks.
- Exclusions: no new skills; no change to C1/C9 grading or the eval rubric; no plugin version
  bump (only on explicit user request); no edits to generated packages; no change to policy
  meaning except decisions 3 and 4; no runtime hooks or runtime Python.
- Accepted constraints and invariants: decisions 1-7 below. Preserve bounded tasks, explicit
  TDD, native question tools when permitted, and a concrete next action in every skill
  ([AGENTS.md](../../../AGENTS.md)). Resolve bundled resources relative to the loaded skill.
- Completion condition: AC1-AC13 verified, required checks pass, independent review done, the
  suite run reported, and the user accepts that run's result.

### Skill template (decision 2)

Order for every skill:

1. Frontmatter: `description` = action and output, then "Use when ...", then "Not for ...; use <skill>".
2. H1 (skill name).
3. Every-task rule block.
4. `## Persona and judgment`: Persona, Responsibility, Decision criteria, Evidence, Failure modes.
5. `## Establish <input>`.
6. `## <Domain> practices` (optional checks; may be omitted only when the skill has none).
7. `## <Procedure> and record`.
8. `## Final reply` last: a literal reply template and that skill's valid next actions.

Literal reply template (content fixed by decisions 2 and 3; the exact markup is implementation):
**Result** with one of four statuses (Complete, In progress, Needs input, Paused); **Evidence**;
a table `Next action | Owner | Needs | Authority`, or `Next action: None for this request` with a
reason. [Architect](../../../plugins/lusona/skills/architect/SKILL.md) and
[review](../../../plugins/lusona/skills/review/SKILL.md) are the structural models.

### Core rule mapping (AC8)

Each current core README rule has exactly one destination. B = every-task block (short form),
R = reference file read when the trigger occurs, X = removed. Reference names marked new are
provisional until implementation; the destination type is fixed. Where one core sentence holds
two rules, each row is one rule. The implementer must confirm each X reason against the cited
file before deleting and move the rule to its stated fallback if the reason does not hold.

| # | Core section: rule | Dest | Destination and trigger |
| --- | --- | --- | --- |
| 1 | Loading rules: all roles read listed sections once per context; coordinators also read two more | X | Replaced by the block; the read-once model no longer exists |
| 2 | Loading rules: workflow role follows assigned responsibilities; host task or no-children rule does not create a leaf role | R | `delegation.md` Assigned leaves; trigger: assignment received or dispatched |
| 3 | Loading rules: identify source of supplied text; reuse unchanged text; installation does not prove availability | R | `delegation.md` Assignment contract; trigger: dispatching |
| 4 | Loading rules: host/project restrictions apply | B | Authority line |
| 5 | Loading rules: a change is a bounded outcome, a task is one step; task selection does not authorize the change | B | Authority line |
| 6 | Loading rules: consult routing table when skill selection is unclear | R | `workflow-guide.md`; trigger: unclear skill selection |
| 7 | Work loop: carry outcome, decisions, authority, TDD, evidence across handoffs; skills give expertise, not authority | B | Authority line |
| 8 | Work loop: answer direct questions first; reuse settled answers and valid checks | B | Questions line |
| 9 | Work loop: take the next bounded authorized action; stop inquiry when it cannot change the outcome; follow-ups steer | B | Questions line |
| 10 | Work loop: pause on request, missing input/capability/authority, or correction limit; state resumption prerequisite | B | Questions line (pause statement) |
| 11 | Work loop: before correcting or probing a failed check or finding, read corrections | R | `corrections.md`; trigger: observed failed check or review finding |
| 12 | Work loop: evidence undermines a decision: reopen, reconcile records, resume from the revision | R | New `revision.md` (or `handoff.md`; decided at implementation); trigger: evidence contradicts an accepted decision |
| 13 | Work loop: relate discovered gaps to goals; do not audit the product; findings do not expand authority | R | `retention.md`; trigger: a finding or gap is discovered |
| 14 | Work loop: read evidence rules before a measurement or experiment | R | `evidence.md`; trigger: before a measurement or experiment |
| 15 | Work loop: choose routine details without approval; ask only for consequential decisions | B | Questions line |
| 16 | Work loop: planning belongs to implementation; task lists only when needed | X | Restated in `implement/SKILL.md` lines on planning depth and in the spec template Execution section |
| 17 | Contract: read applicable domain skills first; report missing ones | B | Authority line |
| 18 | Contract: users control scope; check action against grant before changes to outcomes, contracts, TDD, dependencies, destructive actions | B | Authority line |
| 19 | Contract: specs, plans, ADRs, queue states, discussion, read-only review grant no implementation authority; planning-only stops | B | Authority line |
| 20 | Contract: implementation/refactoring includes local verified commits unless prohibited | B | Authority line (one clause) |
| 21 | Contract: push, publication, PRs, tickets, history rewrite need separate authority | B | Authority line (one clause) |
| 22 | Contract: read commits before commits/integration | R | `commits.md`; trigger: before a commit or integration |
| 23 | Contract: project-data paths belong to the consuming repository; never save in plugin resources | R | `files.md`; trigger: locating or saving a project record |
| 24 | Contract: only coordinators write shared queues, batch records, handoffs; leaf may update its record's handoff | R | `queue.md`; trigger: queue or shared-handoff update |
| 25 | Contract: save substantive outputs before handoff or completion, without waiting for a request; read-only and no-save prevail | B | Saving line (trigger and prevailing restrictions); record choice stays in `retention.md` |
| 26 | Contract: delegated read-only workers return findings for the coordinator to save | R | `delegation.md` Assigned leaves; trigger: assignment received |
| 27 | Contract: creating, updating, or using a spec requires queue tracking | R | `queue.md`; trigger: creating or changing a spec |
| 28 | Contract: consequential architecture decisions require ADRs | R | `retention.md`; trigger: saving a decision |
| 29 | Contract: saving neither selects TDD, requires Specify, nor authorizes implementation; requested documents remain deliverables | R | `retention.md`; trigger: saving |
| 30 | References: catalog table | R | Remains in the reduced README as the catalog (AC9) |
| 31 | References: batch execution governs selection, decisions, repair budgets, recovery | R | `batch-execution.md`; trigger: batch work |
| 32 | Questions: reach a concrete next step or state none is needed, with reason; no boilerplate on greetings | B | Final reply line; each skill's template |
| 33 | Questions: answer first, then ask or act; a proposed step does not authorize execution | B | Questions line |
| 34 | Questions: use native question UI (`AskUserQuestion`, `request_user_input`, `request_user_input_async`) when permitted, else plain text; do not switch modes | B | Questions line |
| 35 | Questions: recommend answers; state assumptions for optional preferences; silence is not consent | B | Questions line |
| 36 | TDD: implementation requires explicit selection; unset TDD permits definition only | B | TDD gate line; detail in `tdd.md` |
| 37 | Review: completion requires whole outcome, criteria, required checks, and human acceptance when required; failed or unrun required checks block it | B | Completion line |
| 38 | Review: conditions that require independent review; persona change is not independence; unmet review is reported | R | `delegation.md` Evaluate and reconcile; trigger: deciding whether review is required, or a review is unavailable |
| 39 | Communication: lead with blocking decisions, then results; report behavior, decisions, evidence, limits, next action | B | Final reply line; each skill's template |
| 40 | Communication: continuation directive at handoff or boundary | R | `handoff.md`; trigger: handoff or boundary |
| 41 | Communication: brief status answers, then continue; concrete actions and expected results for user-visible changes | R | `completion.md`; trigger: composing a reply for a status question or user-visible change |
| 42 | Communication: update product/architecture documentation for enduring changes | R | `closeout.md`; trigger: closing a change |
| 43 | Communication: pre-send check of every substantive final reply for Result, Evidence, next action | B | Final reply line; each skill's template |
| 44 | Communication: next-action table, directive in blockquote, proposed follow-up, plain `None for this request` form | B | Each skill's literal template |
| 45 | Communication: four statuses and their meanings; status describes the response, not queue state | B | Each skill's literal template |
| 46 | Communication: lists, tables, status summary columns, specialized tables, user/host formatting overrides | R | `completion.md`; trigger: composing a table-form reply or when a formatting override applies |
| 47 | Communication: assignment results use the Assignment results fields | R | `delegation.md` Assignment results; trigger: returning a leaf result |
| 48 | Assigned leaves: leaves follow Assigned leaves and Assignment results; no user interviews | R | `delegation.md` Assigned leaves; trigger: assignment received |
| 49 | Personas: coordinator delegates a skill's main specialist work; local fallback when delegation is prohibited or unavailable, stated in the reply; local work cannot satisfy independent review | B | Delegation line (all task sizes, decision 4) |
| 50 | Personas: occupied capacity is not unavailability; host capacity accounting; single batch pool | R | `worker-lifecycle.md`; trigger: dispatching or holding workers |
| 51 | Personas: read assignment contract and model routing before dispatch; worker lifecycle after results | R | `delegation.md`, `model-routing.md`, `worker-lifecycle.md`; trigger: before dispatch / after results |
| 52 | Context budget: handoff near 40%, target before 50%; checkpoint at task boundaries without telemetry | R | `handoff.md`; trigger: checkpoint or context-budget threshold |
| 53 | Uncommitted: validation procedure for the completion hook and `completion_reply.py` | X | Decision 5; removed with hooks and validator |
| 54 | Uncommitted: final-reply examples in `completion.md` | R | `completion.md` Examples; trigger: composing a final reply (hook sections deleted) |

### Acceptance criteria

- [ ] AC1: Each of the 14 skills has the template sections of this spec in the stated order, with
  `## Final reply` as the last section; "Establish" and "Procedure and record" headings may use
  skill-specific nouns, and `## <Domain> practices` may be absent only where recorded as having
  no optional checks. A repository check fails for a skill that deviates and passes for a skill
  in the target shape. (Architect and review today lack the block and `## Final reply`, so they
  also change.)
- [ ] AC2: Every skill's `## Persona and judgment` contains Persona, Responsibility, Decision
  criteria, Evidence, and Failure modes. A repository check fails when any field is missing.
- [ ] AC3: The every-task block text comes from one single source. A repository check fails when
  any skill's block differs from that source (mechanism per the ADR).
- [ ] AC4: The block states each of: authority (rows 4, 5, 7, 17-21), delegation at all task
  sizes with the stated local fallback (row 49), the TDD gate (row 36), the saving trigger
  (row 25), the completion definition (row 37), native question tools and next-step behavior
  (rows 8-10, 15, 33-35), and the final reply requirement (rows 32, 39, 43). Rows tagged B
  appear in the block or the skill's template; none is lost.
- [ ] AC5: Every skill's `## Final reply` contains the literal reply template of decisions 2 and
  3 (Result with the four statuses, Evidence, next-action table or `None for this request` with
  a reason, rows 44-45) and that skill's valid next actions. A repository check fails when a
  skill omits any template element.
- [ ] AC6: Every skill's description follows the stated form (action and output, "Use when ...",
  "Not for ...; use <skill>"), checked by repository check; descriptions name a different skill
  for each exclusion and that skill exists.
- [ ] AC7: Delegation and the full-form reply apply to every task size. No rule in the plugin
  (block, README, references, skills) conditions delegation or the reply form on task size,
  other than the stated fallback when workers are unavailable or prohibited.
- [ ] AC8: The mapping above is complete: every rule in the core README at the base commit
  `9f2260f` plus the uncommitted core edits is in exactly one row. After implementation each R
  destination exists with a stated trigger sentence in the block or skill that points to it, each
  X reason is confirmed true, and each B rule is present. A reviewer can check this by reading the
  table against the diff; the mapping is updated in this spec if implementation moves a rule.
- [ ] AC9: The core README contains only an overview, the reference catalog (with each
  reference's trigger), and human-facing documentation. It states no rule absent from the
  mapping and is not required reading by any skill.
- [ ] AC10: `plugins/lusona/hooks/` and `plugins/lusona/scripts/completion_reply.py` do not
  exist; neither manifest declares `hooks`; `package.py` and its tests contain no hook special
  case; `INSTALL.md` and `PRIVACY.md` contain no hook or validator text and do not claim Python is
  needed for plugin use; `references/completion.md` retains examples only. A repository check
  fails when a manifest declares `hooks`.
- [ ] AC11: Existing checks pass: link check, package build, native manifest validation,
  `scripts/test_*.py`, and the `evals/loop-conformance` unit tests. New template checks are part
  of this set. Unrun checks are reported as unrun.
- [ ] AC12: An independent reviewer (not the implementer) receives this spec, the actual diff and
  check output, and reports findings; blocking findings are corrected and re-verified.
- [ ] AC13: After AC1-AC12, one loop-conformance suite run on the C9 scenarios, including
  `tdd-stated`, is executed under a budget the user approves at that time. The result is reported
  with the evidence path and compared with the pass mark in U1. The user accepts or rejects it.

### Decisions and uncertainty

Accepted decisions (user, 2026-11-10, native question and discussion; recorded in the
[notes](../notes/completion-reply-conformance.md)):

1. Stop relying on the core README for rules that apply to every task. Each skill carries a
   short block of those rules; everything else moves to reference files read when the matching
   action is performed. Evidence: run 008.
2. Standardize all 14 skills on the template above, modeled on architect and review; every skill
   gets a persona; use references where appropriate.
3. Every final reply uses the full form, including small tasks.
4. Delegation applies to every task size: the coordinator delegates a skill's main specialist
   work; local work only when workers are unavailable or prohibited, stated in the reply.
5. No runtime hooks or Python. Instruction text only, for Claude Code and Codex. Fold the
   uncommitted direct-instruction work into this change: remove the hooks, validator and manifest
   entries; keep wording that survives the new structure; reconcile `completion.md`, INSTALL.md
   and PRIVACY.md. The spec for that work (`20261109-direct-instruction-checkpoints.md`) is
   missing from disk and history; this spec supersedes its queue row.
6. TDD `targeted`.
7. Acceptance: repository checks and independent review, then one suite run on the C9
   scenarios after implementation, budget approved at that time. Development-time Python
   (generator, tests) is acceptable; runtime Python is not.
8. Draft first (user, 2026-11-10: "Tentatively accept", with a request for "a draft directory to
   contain the rewrite" so the rewrite can be written by reviewing the rules directly and
   compared side by side). The rewrite is written in [`drafts/lusona/`](../../../drafts/README.md),
   a full copy of `plugins/lusona/`, with a verbatim rule inventory in `drafts/rules.md`.
   `plugins/lusona/` stays unchanged until the user accepts the draft; promotion then replaces
   its contents and deletes `drafts/`. This is a user-approved exception, for this change only, to
   the AGENTS.md instruction to edit `plugins/lusona/` directly. Acceptance of the scope and
   AC1-AC13 is tentative until the draft review.

9. A1 settled (user, 2026-11-10): the block has one source file; a development-time script
   writes it into each SKILL.md, and a test fails when a copy differs. No runtime include:
   Claude Code's `!` injection needs a shell per OS and Codex has no include mechanism. The user
   also asked to reduce the block substantially; the 841-word draft in `drafts/rules.md` is
   replaced by a shorter proposal in `drafts/block.md`.

10. Block and formatting (user, 2026-11-10): the 234-word block in `drafts/block.md` is accepted
    (conversation stays with the coordinator; no task-local check exception; greetings are not
    task replies). All reply-formatting rules go in each skill's `## Final reply` section;
    `references/completion.md` keeps examples only (AC10 unchanged). Rewrite edits stay in
    `drafts/` until the rewrite is complete.

Open architecture questions (for an ADR; not decided here):

- A1: Where the single source of the block lives (a reference file, a template, the README) and
  how skills receive it: generated into each SKILL.md, or hand copy plus a sync test (AC3).
- A2: How the reply template relates to the block: part of the block, a separate generated
  section, or each skill's own text. Skills differ only in their next-action list.
- A3: Block size limit and wording style, so the block stays short while covering AC4.
- A4: Whether the Final reply section and the template check apply to `batch` and `status`
  unchanged, given batch's parent-return and queue duties.
- A5: Where a leaf (assigned worker) obtains its role rules when the block tells a coordinator to
  delegate: the block must not make a leaf delegate or interview the user (rows 2, 26, 48).

User questions (U1-U3 answered by the user on 2026-11-10; U4 open until the run):

- U1, answered ("yes" to the recommended example): the AC13 run has a pass mark declared before
  the run. The run meets it when the computed C9 check passes in `tdd-stated` in at least 4 of 5
  trials on each host, and `authz-change` C9 passes are not below the run 003 reference on each
  host (Claude 5/5, Codex 0/5). Reference for `tdd-stated`: 0/5 on each host. The user then
  accepts or rejects the reported result. Known gaps, for the user to keep or close before the
  run: the Codex `authz-change` half is met by any result, and the other C9 scenarios
  (`status-check`, `investigate-bug`) have no mark.
- U2, answered: keep the Codex harness prompt. It names the skill path and asks for
  "applicable linked instructions"
  ([run 008](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md#observations)), so
  Codex always reads the skill; Claude receives the skill through a slash command. The AC13
  report states this limit on comparing hosts.
- U3, answered: the uncommitted eval and record edits (rubric, calibration, `suite.lock.json`,
  evals README, notes, specs, history, queue, evidence runs 004-008) are committed separately
  before implementation, so the AC13 run uses a committed rubric. The uncommitted plugin source
  edits (core README, references, skills, manifests, hooks, validator, packaging, AGENTS.md,
  INSTALL.md, PRIVACY.md) stay uncommitted and are folded into this change.
- U4, open: budget for the AC13 run (reference: run 006 `tdd-stated`, $1.737 Claude-reported for
  6 trials; run 003 about $40 for the full suite). Approved at run time per decision 7.
- U5, open: run AC13 on the draft before promotion (`evals/loop-conformance/run.py` accepts
  `--plugin`, so it can point at `drafts/lusona`) or after promotion as AC13 now states. Running
  on the draft leaves the live plugin unchanged if the result is rejected; promotion must then copy
  the measured files without change.

### TDD policy

- Level: targeted
- Selected by user: 2026-11-10 (native question)
- Test-first behaviors, each a repository check observed failing before the change:
  1. A test fails when a skill deviates from the template (AC1, AC2, AC5, AC6).
  2. A test fails when a skill's every-task block differs from its single source (AC3).
  3. A test fails when a manifest declares `hooks` (AC10).
- Required regression coverage: existing package, manifest, link, and eval-suite tests continue
  to pass (AC11). Wording is not test-driven; AC4, AC7, AC8, AC9 are verified by review.

## Execution

Approach is open until the ADR (A1-A5). Expected sequence (decision 8): rule inventory in
`drafts/rules.md`; user reviews it and the proposed every-task block; settle A1-A5 on a pilot of
the block plus one skill (`implement`) in `drafts/lusona/`, recorded as an ADR, before drafting
other skills; draft the remaining skills, references and README; user compares the draft side by
side and accepts it; with implementation authorized, write the three failing checks, promote the
draft, remove hooks work, run checks, independent review, suite run (before or after promotion
per U5).

- Verification: `python3 -m unittest discover scripts` (or the repository's check command),
  link check, package build to `tmp/`, manifest validation, eval unit tests in
  `evals/loop-conformance/`. Commands to confirm at implementation; none run for this spec.

## Evidence

Not started. Definition only. Inline check done at creation: the mapping rows and ACs agree on
rows cited; no contradiction found between decisions 3, 4 and the exclusions. Open at creation:
architecture questions A1-A5 and user question U3, none of which blocks the ADR. U3 was settled on
2026-11-10 by commit `34186da`.

## Current handoff

- Authorized work: definition (this spec) and drafting in `drafts/` (decision 8). Changes to
  `plugins/lusona/` are not authorized.
- Completed and remaining work: spec written; scope tentatively accepted; `drafts/lusona/`
  created as an identical copy of the working-tree plugin on 2026-11-10 (`diff -r` empty).
  `drafts/rules.md` written by a worker: 97 rows covering every content line of the core README
  and `references/completion.md`; quotes and coverage confirmed by a separate coordinator check.
  It lists 16 differences from the mapping above; four rules have no spec row. Its proposed
  every-task block keeps all B rules and is 841 words. Remaining: user review and decisions on
  the inventory's open questions (delegation exceptions in row 49, greeting exception in row 32,
  block size A3, `completion.md` content versus AC10), block and `implement` pilot with the ADR
  on A1-A5, remaining drafts, draft acceptance, implementation authorization, checks, review,
  suite run.
- Next action: user reviews `drafts/rules.md` and answers its open questions. Before the suite
  run the user keeps or tightens the U1 pass mark, sets U4 (run budget) and answers U5.
