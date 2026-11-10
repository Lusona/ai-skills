# Notes: completion-reply-conformance

Context: the [completion-reply change](../specs/20261109-completion-reply-conformance.md), prompted by
[reference run 003](../evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md).

## 2026-11-09 — Rule or grading change for completion replies

### Question and authority

User authorized investigation and a decision on rule text, checks, or neither. No production
implementation, new paid actor/judge run, commit, or publication was authorized during the
investigation. TDD was then unset; the subsequent specification records the user's targeted
selection and current authority.

### Evidence

[Offline audit run 004](../evidence/2026-11-09-loop-conformance-pilot/runs/004/README.md)
owns the methods, provenance, all 40 trial classifications, exact affected trials, examples,
loading limitations, replay verification, and independent review findings.

The failures include real label and next-action omissions, five form-only next-action failures,
and seven semantic-judge false passes. No observed C9 failure is a parser false negative.
Neither an explicit host formatting override nor a second-turn-only loss explains the sample.
The cause of actor omissions remains unconfirmed; recorded loading gaps on Claude do not
establish missing model context, and Codex received the core rule in every audited trial.

### Decision

Recommend **both**, narrowly: clarify completion-reply coverage and correct C1's semantic
rubric/calibration, retaining C9 requirements/parser and C1's prescribed-label computation.
The user invoked Specify on this recommendation and selected targeted TDD on 2026-11-09.
The [change spec](../specs/20261109-completion-reply-conformance.md) now owns the intended
behavior, scope, acceptance criteria, TDD policy, verification allowance, and current handoff.
The wording benefit remains untested; the semantic-judge inconsistency is demonstrated.

Checks alone would leave actual omissions unchanged. Rule text alone would leave a demonstrated
judge inconsistency. Neither would leave both unresolved. Low scores establish nonconformance;
they do not establish that a wording change will improve behavior.

Corrected the source report's “six” form-only failures visibly to five, without changing the
stored grades/reference. Updating rubric/calibration later changes suite hashes; comparisons
must use matched grading definitions, not silently compare a new suite with this reference.

### Verification and limits

- Diagnostic engineer audited all 40 C9 finals and C1 judgments. A separate read-only reviewer
  independently checked the original replies, counts, hashes, grading, and override claims;
  no blocking finding remained. Coordinator replay verified all 40 grades/hashes and 50 original
  turn replies. Existing checker unit tests: 51 passed.
- No new actor/judge trials, installation, or interactive behavior tests ran. Improvement from
  the candidate rule text is unmeasured. The 40 additional judged-only C1 cells were not audited.
- During investigation, rule/check source files and reference counts remained unchanged.
  Only findings, evidence, the visible observation correction, and the owning queue row
  were updated. The subsequent implementation is recorded in the linked change spec.

## 2026-11-09 — Does the clarification improve actor replies?

The user authorized the previously proposed matched actor evaluation with “proceed”. The
[source/grading implementation](../specs/20261109-completion-reply-conformance.md) remains
complete; this is a separate bounded evaluation, not a reopened implementation.

[Run 006 design](../evidence/2026-11-09-loop-conformance-pilot/runs/006/design.md) owns the
predeclared hypothesis, workload, ordering, guardrails, budget, and decision thresholds.
Both versions use the corrected grading rubric; only the plugin core communication paragraph
differs. The finite allocation is 24 actor trials, up to 24 judge calls, $20 Claude-reported
spend and 60 minutes. No retries, production changes, or automatic extension.

## 2026-11-10 — Where the reply rule lives, and a fixed skill structure

### Question and authority

User invoked `lusona:explore`: the next-action part of final replies appears in about a third
of replies on both hosts, and Claude follows instructions and templates exactly when it applies
them. Proposal under discussion: rewrite the instructions to be shorter and more direct, and give
every skill a fixed structure modeled on architect. Discussion only. No source edits, actor runs,
budget, or TDD selection were authorized. This section uses existing records only.

### Evidence

C9 passes by scenario, pooling run 003 (5 per cell) with both arms of run 006 (3 + 3).
The plugin snapshots differ between runs; C9 is computed and unchanged.

| Host | `authz-change` | `tdd-stated` |
| --- | --- | --- |
| Claude Code | 10/11 | 0/11 |
| Codex | 2/11 | 0/11 |

- The run 006 clarified arm scored 2/6 C9 on each host, which matches the user's one-third figure.
  The aggregate hides a split: Claude passes the security change and never the small fix.
- Claude visible core reads: `authz-change` 11/11, `tdd-stated` 0/11 (run 004 audit, run 006).
  Where reading varies within a scenario (run 003 `status-check`, `investigate-bug`): read 5,
  passed 2; not read 5, passed 0. Reading is collinear with scenario, the sample is small, and
  the comparison is post hoc. This is a hypothesis, not a confirmed cause.
- Rule in context but not applied: Codex visibly received the communication paragraph in every
  audited trial and passed `tdd-stated` 0/11. Claude `status-check` 2, 4 and 5 read the core and
  failed. In run 007, the `authz-change` actor read the core and bypassed delegation, citing the
  size of the fix.
- Skill bodies: 13 skills end with `## Next action`; explore ends with `## Outcome and next action`.
  Only implement names Result, Evidence and Next action, in an uncommitted working-tree line from
  run 007. The other final sections describe reply content in prose without the labels; for
  example, architect: "Return the decision, supporting evidence, what it resolves, and what remains
  uncertain." Only architect and review use the `Persona and judgment` section with
  Responsibility, Decision criteria, Evidence and Failure modes.
- Run 006 rewrote one core paragraph and nothing else: **Refine**. Codex C9 0/6 → 2/6, Claude
  C9 3/6 → 2/6. Streamlining the whole instruction set, removing "substantive" and the
  exceptions, and an inline skill block on Codex are untested.
- Run 007 is the only run where a skill body named the fields; hooks were also on, so the effects
  cannot be separated. Claude `tdd-stated`, no core read recorded: turn 1 had Result and Evidence
  labels but no status or table (one hook-requested rewrite passed); turn 2 passed on first draft.
  Structure: baseline 1/3, candidate 2/3 first draft and 3/3 after the rewrite. One trial per arm.

### Hypotheses

- H1 delivery: the reply contract is in the linked core, not in the SKILL.md text that the host
  injects. No core read was recorded in any Claude small-fix trial; an unrecorded read does not
  prove the text was absent.
- H2 small-task exemption: with the rule in context, both hosts omit the form on small tasks.
  The word "substantive" and the rule's exceptions permit that reading.
- H1 and H2 can both hold. Neither is confirmed.

### Options

| Option | Evidence | Tradeoff |
| --- | --- | --- |
| Reword the core only | Run 006: Refine; `tdd-stated` 0/6 on both hosts | Does not reach Claude when it skips the core (H1) |
| Literal reply block as the last section of every SKILL.md | Untested in isolation; Claude passed 7/10 when the core text was visibly read (run 003); run 007 confounded with hooks; no Codex evidence | 14 copies of about 8 lines; a test must keep them equal to the core |
| Remove "substantive" and the exceptions that permit skipping | None | Targets H2 on both hosts; must keep the worker-result and user-override exceptions |
| Stop hook validation | Run 007: one requested rewrite succeeded | Claude Code only; OpenAI's public directory excludes plugins with hooks; needs Python 3 |
| Smaller required form on small tasks | None | Changes the accepted contract and C9 |
| Fixed skill structure | None for compliance | Maintainability and a fixed slot for the reply block; does not address H1 or H2 by itself |

### Proposed direction (not accepted)

Replace each skill's `## Next action` with `## Final reply`: a literal fill-in block plus that
skill's valid next actions. The core keeps the authoritative definition; a repository test checks
that each skill's block uses the core's labels and status words. In the core and the block, remove
"substantive" and the exceptions that permit skipping, keeping worker results and user/host
overrides. The block's effect on Codex is a guess: Codex already had the rule in context. Adopt
the architect/review structure for all skills as a separate, maintainability-only change:

1. Frontmatter: `description` = action and output, "Use when …", "Not for …; use <skill>".
2. `# <Title>` and the fixed core-loading line.
3. `## Persona and judgment`: Persona, then Responsibility, Decision criteria, Evidence, Failure modes.
4. `## Establish <input>`: what to read, when to ask, where to route.
5. `## <Domain> practices`: optional checks; apply the relevant ones.
6. `## <Procedure> and record`: steps, records, authority limits.
7. `## Final reply`: the literal block and this skill's next-action choices.

### Open questions

- Must the remedy work on Codex without hooks? If yes, hooks are excluded and only instruction
  text remains; neither inline skill text nor unconditional wording has been run on Codex.
- Is the full form (Result with status, Evidence, next-action table) required on a two-line fix,
  or is a smaller form acceptable there?

### Decisions (user, 2026-11-10)

- Accepted: the remedy must work without hooks, through instruction text only, on Claude Code and
  Codex. Reason: no known way to run the hooks without Python on Windows and macOS.
- Accepted: every final reply uses the full form (Result with status, Evidence, next-action table
  or the no-action label), including small tasks. Reason: a consistent form lowers the chance of
  omitting it on a larger task. Consequence: remove "substantive" and the size-based reading of
  the exceptions; C9 requirements stay unchanged.
- Open: what happens to the uncommitted hooks and Python validator from the direct-instruction
  work (`plugins/lusona/hooks/`, `scripts/completion_reply.py`, mechanical validation in
  `references/completion.md`). Options: remove them, keep them as an optional Claude-only check,
  or leave them uncommitted until the probe result.

### Proposed probe (declined by the user on 2026-11-10; retained for reference)

- Question: does a literal `## Final reply` template in the injected skill text, with unconditional
  wording, make both hosts produce the full form on a small fix?
- Scenario `tdd-stated`; score both turns' final replies with the computed C9 and Next action
  label checks. No judge calls.
- Arm A: plugin at HEAD `9f2260f`, no hooks. Arm B: A plus the template as implement's final
  section and unconditional wording in the core reply paragraph. Testing both changes together
  matches the accepted direction; it cannot separate their effects.
- Five trials per host per arm (20 trials, 40 actor calls), alternating arm order, fresh isolated
  workspace per trial, reuse the run 006 driver and isolation settings.
- Cost basis, run 006 `tdd-stated`: Claude 6 trials, $1.737 reported, 203 s; Codex 6 trials,
  919 s, dollar cost unavailable. Proposed caps: $6 Claude-reported, 60 minutes, no retries.
- Proposed rule, to freeze before any call: adopt if arm B passes C9 on at least 8 of 10 replies
  on each host and exceeds arm A by at least 5 replies on each host; reject if B exceeds A by at
  most 1 reply on both hosts; otherwise refine.

### Loading frequency (user question, 2026-11-10)

[Run 008](../evidence/2026-11-09-loop-conformance-pilot/runs/008/README.md) owns the counts and
method. Claude's root agent received the core README in 35/60 run 003 trials, and the outcome
is set by scenario (0/5 or 5/5 in 10 of 12 cells; `tdd-stated` 0/13 across runs). Codex received
it in 72/72 under a harness prompt that names the skill path. References were read in most
trials once their operation occurred; those counts omit operations never performed. Claude
dispatched workers in 17 of 43 trials that read the core and 0 of 33 that did not (association).

Implication: the core holds rules every task needs (reply form, delegation, authority), and on
Claude it is skipped in whole scenarios, decided at the start of the task. In the proposed probe,
version B's core rewording cannot act on Claude `tdd-stated`; the Claude half tests the skill
template only. A reply template
in each skill covers the reply form only; delegation and the other core-only rules stay absent
in those trials. Proposed alternatives to weigh: inline the rules every task needs into each skill;
make the skill's first instruction an unconditional read of the core; or shrink the core so the
required part can be inlined. None is tested.

### Core loading: changes so far and options (2026-11-10)

The user declined the probe and asked for options instead.

Changes since run 003: no committed plugin change since `42b8145`. Uncommitted: core wording
(reply rule, authority checkpoint, delegation phrasing), two implement lines that link core
sections, a refactor TDD link, `references/completion.md`, hooks and the Python validator. Every
skill still opens with the same line: "Apply the core; read linked procedures only when their
operation applies." Observed after the wording changes: Claude `tdd-stated` core reads 0/6 in
run 006 version B and 0/1 in the run 007 candidate. Nothing changed suggests better loading.

Sizes: core 1,937 words; skills 280–899 words. Core sections that apply on every task: authority
(Contract), delegation (Personas and subagents), completion gate and reply form (Review and
communication), next actions (Questions and next actions), about 800 words today. The rest is
meta (Loading rules, Assigned leaves), a catalog (References), or operation-triggered (TDD,
commits, saving, context budget).

| Option | Delivery | Cost | Risk |
| --- | --- | --- | --- |
| 1. Imperative first line: read the core in full before any other action | Still the model's choice | One line per skill; ~2,600 tokens per task | Small tasks may still skip it; no evidence either way |
| 2. Inline the whole core in each skill, generated | Guaranteed with the skill | Skills grow 2–7×; no fewer rules | Rarely needed rules compete with always-needed ones |
| 3. Split: short always-on block in each skill, generated from one source; other rules move to operation-triggered references | Guaranteed for always-on rules; references load on their operation (run 008: most read once the operation occurred) | Decide the always-on list; generator and sync test (development-time Python only) | Rules misclassified as operation-triggered stay skippable |
| 4. Installer adds the core to project CLAUDE.md/AGENTS.md | Every session | Loads in non-Lusona work; plugin path differs per install and OS; edits user files | Scope and portability |
| 5. Core as its own skill | Model must invoke it | Small | Same choice point as the link |

Proposed (not accepted): option 3, with the fixed skill structure giving the block a slot after the
title and the reply template the last section. The README becomes a catalog and human
documentation rather than the agent's required rulebook.

Open: does the "consistent even on small tasks" principle also apply to delegation? Run 007's
actor skipped delegation because the fix was small; the answer decides the block's delegation rule.

Accepted (user, 2026-11-10): stop relying on the README for rules that apply to every task. Each
skill carries a short block of those rules; everything else moves into reference files read when
the agent performs the matching action. Also accepted: standardize all skills on one template,
give every skill a persona, and use references where appropriate. Next: specify the change.

Accepted answers (user, 2026-11-10, native question): delegation applies to every task size;
TDD `targeted` for the change; fold the uncommitted direct-instruction work into the new change
and remove its hooks and Python validator; acceptance by repository checks, independent review
and one loop-conformance run on the C9 scenarios after implementation, budget approved then.
The spec `specs/20261110-standard-skill-template-and-inline-rules.md` will own scope and handoff.

### Records gap

`specs/20261109-direct-instruction-checkpoints.md` is linked from the work queue Review row,
this file, and run 007, but is absent from the working tree, git history, and the three stashes
(including untracked files).
`tmp/direct-instruction-checkpoints/` holds only scratch artifacts. Not recreated.

## Current handoff

- [Run 006 result](../evidence/2026-11-09-loop-conformance-pilot/runs/006/README.md): **Refine**.
  Codex C1/C9 rose from 0/6 to 3/6 and 2/6; Claude C1 stayed 3/6 and C9 fell from 3/6 to
  2/6. All four `tdd-stated` cells remain 0/3 for both checks. The cross-host adoption criteria
  and clarified Claude delegation guardrail were not met. No audited C9 parser false negative
  or C1 judge disagreement justifies relaxing the checks.
- Collection and analysis are complete: 24 valid trials, 36 actor turns, 24 harness judges,
  $11.176008015 Claude-reported spend, 48.68 minutes. The linked evidence owns detailed results,
  the nonbinding budget/timeout deviation, loading visibility and small-sample limitations.
  [History](../history/2026-11-week-02.md#2026-11-09--completion-reply-actor-evaluation)
  owns closure; source implementation remains separately closed.
- Recovery: retained run 006 artifacts and its ignored local `raw.zip` preserve captures,
  conditions, scripts, grades and hashes. Scratch remains under
  `tmp/completion-actor-evaluation/`. No active operations remain; do not restart the ledger.
- The user subsequently authorized all four mechanisms and accepted the principle of one
  authoritative policy definition with useful short local instructions. The
  [new implementation spec](../specs/20261109-direct-instruction-checkpoints.md) owns that scope,
  decisions and current handoff. [Run 007](../evidence/2026-11-09-loop-conformance-pilot/runs/007/README.md)
  verifies structural repair but retains failed delegation in both candidate tasks. The source
  changes are implemented; behavioral acceptance remains open in the [work queue](../work.md).
- Historical diagnosis: one diagnostic round, total 1 and consecutive without progress 0.
  This new intervention evaluation is not another correction round.
- 2026-11-10 exploration (sections above): user accepted text-only (no hooks), the full form on
  every reply, option 3 (every-task block in each skill plus operation references), delegation at
  every task size, and removal of the hooks and Python validator; the probe was declined. The
  missing implementation spec linked above is not recreated; its queue row is superseded by the
  [standard skill template spec](../specs/20261110-standard-skill-template-and-inline-rules.md),
  which owns scope, the AC13 pass mark (U1-U3 answered 2026-11-10) and the current handoff.
