# Spec 20261115-concrete-instruction-language: Concrete instruction language

Created: 2026-11-15
Updated: 2026-11-15

Kind: other — wording-only change
Work item: [Completion history](../history/2026-11-week-03.md#concrete-instruction-language)
Context: User accepted the voice recommendation on 2026-11-15 and requested a specification, with script validation.

## Agreement

- Problem: compressed, abstract wording makes some Lusona instructions harder to interpret even when they pass sentence-length checks.
- Outcome: retain calm precision, replace abstract passages with concrete actions and conditions, and add explanations or examples that resolve uncertainty about execution. Preserve the force and meaning of obligations without reprimands or emphatic repetition.
- Scope: review the instruction prose in `shared/`, `plugins/lusona/skills/`, `plugins/lusona/references/` and `plugins/lusona/templates/`; change only passages with an identified interpretation problem. Record reviewed files, changed passages and reasons. Do not impose an edit quota or rewrite already concrete instructions.
- Exclusions: workflow behavior, authority, TDD requirements, record schemas, command interfaces, terminology meanings, checker behavior except the conditional shared-block limit increase below, historical records, marketing prose, installation and publication.
- Constraints: follow [the audit](../../skill-audit.md), including V1–V9, VP1–VP7, shared-source ownership and the existing sentence limits. The every-task block limit may increase from 300 to 400 words when the concrete-language rewrite requires it; 400 is a ceiling, not a target. Edit generated regions only by regenerating from `shared/`.
- Completion: changed text passes the existing script checks and the applicable audit items; an independent reviewer verifies meaning preservation and the concrete-language criteria. Report unrun checks rather than claiming acceptance. No installation or agent-behavior improvement claim follows from text checks.

### Acceptance criteria

- [x] AC1: Each changed passage preserves its trigger, action, scope, authority, exceptions and limits. Record the original and replacement with their source locations. Any proposed semantic change is separated from this wording-only change and returned for a user decision.
- [x] AC2: Each replacement identifies the action and its object, and states the condition that selects it. The actor may be the agent addressed by an imperative. Review names the interpretation problem removed; expanding word count alone does not satisfy this criterion. Preserve established technical terms, explaining their use instead of substituting new synonyms.
- [x] AC3: Each added explanation or example resolves a named execution ambiguity. It agrees with the governing rule and adds no new obligation. General background and rationale that does not affect execution remain outside instruction text, under V9. Do not add an example to every instruction by default.
- [x] AC4: Changed prose states obligations directly, without accusations, reprimands, rhetorical questions or repeated emphatic capitalization. Formatting may identify required actions; it must not replace a concrete condition or instruction.
- [x] AC5: Run `scripts/check_voice.py` against the complete proposed plugin before acceptance, with unchanged defaults. Require exit 0: no banned terms, file average at most 15 words per sentence, and no sentence over 40 words. Respect the checker’s template exclusions. Run the shared-region check. Keep the 300-word every-task limit unless the rewrite needs more space; then raise it to 400, update its tests and audit documentation, and verify acceptance at 400 words and rejection at 401. Do not compress concrete wording solely to retain 300 words. Record exact commands and outcomes for baseline and final text.
- [x] AC6: Apply the audit’s checks for each changed file type, including packaging/link validation, contract checks and independent review where required. Review AC1–AC4 manually: passing the scripts does not establish concrete language, calm tone or semantic equivalence. Resolve findings under the audit’s acceptance rules.

### Decisions and uncertainty

- Accepted direction: the user approved calm precision, concrete language, more explanations and examples, and restrained emphasis. Source: conversation on 2026-11-15.
- Scope assumption: this is an editorial pass over canonical instruction prose, not a redesign of the workflow or automated language checker.
- Existing V9 permits explanations only when they affect execution. This spec applies that boundary rather than silently repealing it. Broader teaching commentary would require a separate decision.
- Revised in part, user conversation on 2026-11-15: the earlier requirement to preserve the 300-word every-task limit is replaced by permission to raise it to 400 when needed. The earlier limit came from voice decision 10 in [voice limits](../notes/voice-limits-measurement.md); it bounded shared context. The user accepts the increase to preserve concrete language. All other checker limits remain unchanged. Reconcile that record and the audit when implementing the limit change.
- No work-item split was requested.

### TDD policy

- Level: targeted.
- Selected by user: conversation on 2026-11-15, “targeted”.
- Recommendation updated at implementation entry: `targeted`, testing acceptance at 400 words and rejection at 401 before changing the limit. The earlier `none` recommendation covered the prose-only pass. The user selected `targeted` on 2026-11-15. Existing script checks, audit and editorial review still apply.
- Test-first behaviors: acceptance at 400 words; rejection at 401 in check and sync modes, with no writes on rejection. Other checker changes remain outside scope.

## Evidence

Baseline: `d43c44ccea845b62bd326c1ce3413f238dda2848`; working tree was clean before specification.

Checks executed on 2026-11-15:

| Check | Observed result |
| --- | --- |
| `mise exec -- python3 scripts/check_voice.py plugins/lusona` | Exit 0, no findings |
| `mise exec -- python3 scripts/check_instructions.py plugins/lusona` | Exit 0, instruction checks passed |
| `mise exec -- python3 scripts/sync_shared.py --source shared plugins/lusona --check` | Exit 0, shared regions in sync |
| Existing voice checker on a scratch copy of the shared block with the user-approved example | Exit 0; proposed sentences count as 6 and 11 words; complete block has 302 words, exceeding the separate 300-word limit |
| Existing voice checker on the revised scratch example below | Exit 0; complete block has 299 words |

Original: “Pause only affected work; state what resumes it.”

User-approved example: “Continue work that is not blocked. For blocked work, name the input or decision needed to continue.”

Earlier 300-word-compatible alternative (not required after the user accepted an increase): “Continue unblocked work. For blocked work, name the input or decision needed to continue.”

The preferred wording remains the user-approved example; its 302-word total is within the permitted future 400-word ceiling. The current checker still enforces 300.

The preview changed only a scratch copy at `tmp/concrete-language-preview/shared/every-task.md`; canonical instructions are unchanged. Preview command: `mise exec -- python3 scripts/check_voice.py tmp/concrete-language-preview`. Block counts used Python whitespace splitting, matching the documented word-count convention. The original sentence has 8 words; its brevity does not prove clarity.

A read-only editorial leaf inspected the checker and existing voice decisions. Its criteria and findings were reconciled into AC1–AC6. Routing: `gpt-6.1-sol`, a bounded analysis of existing rules. No independent review of future rewritten instructions has occurred.

Invocation mistake: `check_instructions.py --help` treated `--help` as a plugin path and exited 1 with missing-table findings. The explicit plugin-path invocation above passed; these were not findings against the plugin.

Limitations: the checker uses heuristic sentence boundaries and cannot assess abstraction, explanations, examples or semantic preservation. Full packaging, contract, unit and agent-conformance checks were not run for this specification-only change. No final rewrite exists to validate yet.

## Implementation evidence

- Targeted TDD: updated the boundary tests before the constant. The 18-test suite exited 1 with 3 expected failures: accepting 400 words, reporting the 401/400 check boundary, and rejecting 401 without writes. After raising the limit, all 18 passed (exit 0).
- Full script suite: 231 tests passed. Loop-conformance suite code: 150 tests passed; no agent trial ran.
- Bash helper checks passed. PowerShell 7.6.10 helper checks passed, 203 assertions. Native Windows/Windows PowerShell 5.1 were not exercised; helper code is unchanged.
- Voice, template, instruction, contract, historical rule inventory and shared-sync checks passed. Native plugin and marketplace validation passed. Package built successfully in `tmp/concrete-language-package`; final reviewed package built in `tmp/concrete-language-package-reviewed`.
- Reviewed all 15 skill entrypoints, 15 central references, 8 nested batch references, 13 Markdown templates, the HTML template instructional comment and both shared sources. Left concrete passages unchanged. No new scenario examples were needed; the invariants definition and latest-run explanation clarify existing actions.
- Delegated editorial passes owned disjoint skill and reference/template files. Parent owned shared text, scripts, integration and records. Independent reviewer `/root/independent_audit`, model `gpt-6.1-sol`, did not author the edits.
- Independent review identified two semantic regressions: an unconditional TDD question and loss of the transient-entry qualifier. Both corrected: only an unset level triggers the question; only obsolete transient batch entries may be replaced. Correction round 1 for each finding, 0 consecutive rounds without progress. A third finding restored the defined term “content identity” instead of narrowing it to file content. Corrected in one round. Independent reviewer confirmed all three corrections; no open findings.
- No commits, publication, installation or interactive behavior tests. These are wording changes, not evidence of improved agent behavior. All executable checks required for this change were run; unchanged native Windows helper behavior is not claimed.

### Executed verification commands

Each command exited 0 after the changes. Counts and limits are recorded above. The targeted test command first exited 1 as recorded in the red evidence.

- `mise exec -- python3 -m unittest discover -s scripts -p test_sync_shared.py`
- `mise exec -- python3 -m unittest discover scripts`
- `mise exec -- python3 -m unittest discover -s evals/loop-conformance`
- `mise exec -- bash scripts/test-work-record.sh`
- `mise exec powershell@7.6.10 -- pwsh -NoProfile -File scripts/test-work-record.ps1`
- `mise exec -- python3 scripts/check_voice.py plugins/lusona`
- `mise exec -- python3 scripts/check_skill_template.py`
- `mise exec -- python3 scripts/check_instructions.py plugins/lusona`
- `mise exec -- python3 scripts/check_contract.py`
- `mise exec -- python3 scripts/check_rule_inventory.py`
- `mise exec -- python3 scripts/sync_shared.py --source shared plugins/lusona --check`
- `mise exec -- claude plugin validate plugins/lusona`
- `mise exec -- claude plugin validate .claude-plugin/marketplace.json`
- `mise exec -- python3 scripts/package.py --output tmp/concrete-language-package-reviewed`
- `git diff --check`

### Passage ledger

The following before/after blocks record changed source lines against baseline `d43c44c`. Generated copies are omitted. File headings identify the source; quoted lines identify each changed passage. Changes replace compressed nouns or implicit actions with named actions and conditions; existing technical vocabulary is retained. The template spacing correction repairs a sentence boundary. The final shared source has 329 words under the 400-word ceiling.

#### shared/every-task.md

Before:

> **Decisions.** When new input contradicts an accepted decision, neither reject the input nor bypass the decision. Before revisiting, read [revisions](../../references/revisions.md). State the decision, source and conflict; revisit it with the user; record the outcome.
> **TDD.** Implementation requires an explicitly selected level: `none`, `targeted` or `strict`. Until selected, only define and plan; ask, recommending a level. Read [TDD](../../references/tdd.md) before selecting or applying it.
> **Progress.** Take the next bounded authorized action unprompted. Stop inquiry that cannot change the next action. Pause only affected work; state what resumes it.
> **Evidence.** Claim behavior only from observed checks; report unrun and failed checks. Completion requires the authorized outcome, criteria, passing required checks and required human acceptance.

After:

> **Decisions.** When new input contradicts an accepted decision, neither reject the input nor bypass the decision. Before revisiting, read [revisions](../../references/revisions.md). Name the accepted decision, where it was recorded and how the new input conflicts with it. Revisit the decision with the user and record the outcome.
> **TDD.** Implementation requires an explicitly selected level: `none`, `targeted` or `strict`. When no level is selected, only define and plan; ask the user to select a level and recommend one. Read [TDD](../../references/tdd.md) before selecting or applying it.
> **Progress.** Take the next bounded authorized action unprompted. Stop inquiry that cannot change the next action. Continue work that is not blocked. For blocked work, name the input or decision needed to continue.
> **Evidence.** Describe behavior only when observed checks support the claim. Name checks that failed or were not run. Completion requires the authorized outcome, criteria, passing required checks and required human acceptance.

#### plugins/lusona/references/delegation.md

Before:

> - Occupied capacity is not unavailability. Wait for working leaves; reuse or release finished ones.
> - Installation, an anchor link, or another leaf's read does not prove that the leaf has the text.
> 3. A status label alone is not evidence. When a required check is missing, or the result contradicts the assignment or its evidence, apply step 4.

After:

> - When all agent slots are occupied, wait for working leaves. Reuse or release finished leaves; occupied slots do not make delegation unavailable.
> - Do not assume a leaf has the text because the plugin is installed or an anchor link exists. Another leaf reading it does not establish that this leaf has the text.
> 3. Check the reported results; do not accept a status label as evidence. When a required check is missing, or the result contradicts the assignment or its evidence, apply step 4.

#### plugins/lusona/references/evidence.md

Before:

> - A dated single file is itself an exact run.
> - Keep a topic's current conclusion and latest comparable result distinct from its chronologically latest run.

After:

> - For a result saved in one dated file, link that file as the exact run.
> - Identify the current conclusion and latest comparable result separately from the most recent run. The most recent run need not support that conclusion or comparison.

#### plugins/lusona/references/retention.md

Before:

> - These saves are working-tree edits, not commit boundaries. Commit them with the increment they belong to.
> - When a fact gains a change record or ADR owner, replace the notes copy with a link.

After:

> - Save these records in the working tree. Commit them with the increment they belong to; saving a record does not require a separate commit.
> - When a change record or ADR becomes the owner of a fact, replace that fact in notes with a link.

#### plugins/lusona/references/tdd.md

Before:

> - Required regression coverage is separate from test-first sequencing.

After:

> - Keep the required regression coverage regardless of whether tests must be written first.

#### plugins/lusona/references/visuals.md

Before:

> - Binding items are acceptance input. Illustrative items are not.

After:

> - Use binding items to judge acceptance. Do not require the result to match illustrative items.

#### plugins/lusona/references/naming.md

Before:

> - Branch on status and exit code, not on the `message` text.

After:

> - Choose the next action from the returned status and exit code. Do not use the `message` text to choose it.

#### plugins/lusona/skills/implement/SKILL.md

Before:

> - Before dependent or concurrent work, establish consumed and produced interfaces, ownership, and mutable verification resources.
> - Fix a plan omission inline when known evidence resolves it; add no approval step. Revise the approach as evidence changes, within authority.

After:

> - Before dependent or concurrent work, establish ownership, name the interfaces the work uses and provides, and identify verification resources that can change.
> - When known evidence resolves a missing part of the plan, update that part without adding an approval step. Revise the approach as evidence changes, within authority.

#### plugins/lusona/skills/refactor/SKILL.md

Before:

> - Before selecting or applying TDD for the restructuring, writing a characterization test or changing an assertion, read [TDD](../../references/tdd.md). Restructuring starts green and stays green.

After:

> - Before selecting or applying TDD for the restructuring, writing a characterization test or changing an assertion, read [TDD](../../references/tdd.md). Start restructuring with passing checks and keep those checks passing.

#### plugins/lusona/skills/review/SKILL.md

Before:

> 9. Use one reviewer unless defect subtlety or consequences require more. As coordinator with more than one reviewer, reconcile, deduplicate and consolidate the returned findings. Mechanical checks do not replace semantic review.

After:

> 9. Use one reviewer unless defect subtlety or consequences require more. As coordinator with more than one reviewer, resolve conflicting findings, remove duplicates and combine the findings into one report. Mechanical checks do not replace semantic review.

#### plugins/lusona/skills/investigate/SKILL.md

Before:

> - When attempts stop producing new evidence, stop. Report what was ruled out and name the missing input or a different experiment.

After:

> - When attempts stop producing new evidence, stop those attempts. Report what was ruled out and name the missing input or a different experiment.

#### plugins/lusona/skills/specify/SKILL.md

Before:

> - Map every acceptance criterion to at least one item. Name the criteria of every item.

After:

> - For every acceptance criterion, name at least one work item that satisfies it. List the criteria each item satisfies.

#### plugins/lusona/skills/architect/SKILL.md

Before:

> - Where more than one component can update the same state, specify the invariants.

After:

> - Where more than one component can update the same state, specify the invariants: the conditions those updates must preserve.

#### plugins/lusona/skills/batch/SKILL.md

Before:

> - Evidence: owning records, leaf results inspected against their assignment, observed check output, content identities and host lifecycle evidence. A completion notification, saved assignment state, branch name or disjoint file list is not evidence of completion, cessation or independence.
> - Persist dispatch intent before starting an assignment, and evidence links before releasing its ownership.
> - Keep dependents that need the missing result ineligible. Continue independent selected work.

After:

> - Evidence: owning records, leaf results inspected against their assignment, observed check output, content identities and host lifecycle evidence. Do not infer that work finished, writers stopped or assignments are independent from a completion notification, saved assignment state, branch name or disjoint file list.
> - Record the assignment you intend to dispatch before starting it. Save its evidence links before releasing ownership.
> - Do not dispatch work that needs the missing result. Continue independent selected work.

#### plugins/lusona/skills/status/SKILL.md

Before:

> 9. Give a count only with an evidence-backed unit and scope. Do not add capabilities, tasks and checks into one total. Do not invent percentages, dates or estimates.

After:

> 9. When giving a count, name what you counted, the scope and the evidence supporting the count. Do not add capabilities, tasks and checks into one total. Do not invent percentages, dates or estimates.

#### plugins/lusona/skills/batch/references/authority.md

Before:

> - Advance independent settled work without waiting for the whole batch. Disjoint files do not prove independence.

After:

> - Advance independent settled work without waiting for the whole batch. Do not assume two items are independent because they edit different files.

#### plugins/lusona/skills/batch/references/integration.md

Before:

> - An intent is not evidence of transfer. Missing result metadata is not permission to apply again.

After:

> - Do not treat a recorded transfer intent as proof that the transfer happened. When result metadata is missing, do not assume you may apply the transfer again.

#### plugins/lusona/skills/batch/references/workspaces.md

Before:

> - A branch name or a plain status listing does not establish content identity.

After:

> - Do not use a branch name or a plain status listing as proof of content identity.

#### plugins/lusona/templates/batch.md.template

Before:

> Replace obsolete transient entries while retaining recovery identities and durable round charges.

After:

> Replace transient entries that no longer describe current coordination. Keep the identifiers needed to resume work and the recorded charges against the repair budget.

#### plugins/lusona/templates/spec.md.template

Before:

> handoff.Preserve existing execution records in place; do not copy their

After:

> handoff. Preserve existing execution records in place; do not copy their

## Independent audit result

Reviewer `/root/independent_audit` (`gpt-6.1-sol`) returned pass, with no open findings. R1 (conditional TDD selection), R2 (transient entries), and R3 (content identity terminology) were corrected and independently rechecked.

Pass: P0, P3–P7; T10–T13; L1–L3, L5–L12; V1–V9; VL1–VL5; VP1–VP7; B1–B6; K1–K7; G1–G3, G5; E1–E8; D1–D7; AC1–AC6.

Not applicable: P1–P2, P8, T1–T9, T14 (no changed routing, establishment procedure, skill structure, reply actions or exceptions); L4, L13 (no resource moves/additions); B7–B9 (explicit shared-text change, no new block or reply additions); G4, E9 (no renamed template field or new skill).

## Current handoff

- Authorized implementation is complete and independently reviewed. No commit, push or publication performed.
- Targeted TDD and required checks passed. Installation, interactive behavior, agent trials and native Windows behavior were not tested or claimed.
- No remaining work for this request. Completion is recorded in [history](../history/2026-11-week-03.md#concrete-instruction-language).
