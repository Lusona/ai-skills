# Spec 20261115-reconcile-task-lifecycle: Reconcile owned tasks before completion

Created: 2026-11-15
Updated: 2026-11-16

Kind: bug fix
Work item: [Active queue](../work.md)
Context: [Investigation and affected-session evidence](../notes/claude-task-lifecycle-regression.md)

## Agreement

- User and problem: Claude Code users see agents and background shells remain after a report is delivered. A completed notification can still report that the agent owns running background work. Current instructions do not explicitly reconcile background shells at handback; existing agent ownership wording is inconsistent.
- Desired behavior: before final handback or task completion, account for every known owned agent and background operation. Finish or stop operations that are no longer required, confirm the resulting state through available host evidence, and report any unresolved operation. Delivery of a report alone does not establish cleanup.
- Scope: canonical lifecycle and completion instructions, their shared entry triggers, assignment/recovery guidance where required, and evaluation coverage of the affected behavior. Include shells and background commands started by the coordinator or leaves, nested agents, and responsibility inherited or explicitly transferred to another coordinator.
- Exclusions: changing Claude Code, removing historical task entries from its UI, global process cleanup, terminating the user's current tasks, changing delegation frequency, redesigning the workflow, or diagnosing the specific child process in the reported run. Preserve unrelated working-tree changes from the completed language rewrite.
- Constraints: host controls and evidence determine what can be confirmed. Do not assume that ordinary agents exit automatically. Do not invent shutdown APIs or treat deleting transcripts as termination. Preserve material results before shutdown. Keep one authoritative lifecycle policy and concrete local triggers; follow [the audit](../../skill-audit.md) and existing shared-source ownership.
- Completion condition: AC1–AC8 pass, required repository checks pass, matched baseline/candidate behavioral evidence supports the completion and ownership changes, and independent review has no unresolved findings under the audit rules. Unavailable checks remain explicit; a script-only pass is insufficient.

### Acceptance criteria

- [ ] AC1: Before final handback, handoff or task completion, the responsible agent identifies known owned subagents and background commands/shells using task IDs or equivalent host handles. Responsibility includes inherited or transferred work, not only work personally launched. It accounts for descendants through their responsible leaf and escalates any descendants the leaf could not resolve.
- [ ] AC2: For owned work still required by the authorized assignment, continue or wait within its existing limits. For owned work no longer required, use the supported stop/close mechanism when permitted and verify the outcome. A completed command needs no redundant stop; a persistent idle teammate still needs explicit lifecycle handling. Preserve results before stopping work.
- [ ] AC3: A report delivery, final response, idle notification, shutdown request, or top-level completed status is not sufficient evidence that owned work has stopped. A notification that also reports running child work keeps lifecycle reconciliation open. The coordinator resolves or explicitly reports that work before claiming full completion.
- [ ] AC4: When controls, state visibility or shutdown confirmation are unavailable, report the operation's identity, last observed state, owner, missing capability and next action. Preserve recovery information and distinguish finished deliverables from unresolved cleanup. Do not claim termination, retry indefinitely, or block unrelated authorized work.
- [ ] AC5: Retain a running operation only when its continued purpose is within existing authorization and ownership is explicit. Record its identity, purpose, responsible owner and next observation/stop condition. This is an intentional handoff, not a cleanup success. Ownership transfer requires an accepting recipient or explicit user direction; ending a turn does not transfer ownership.
- [ ] AC6: Cleanup is limited to operations attributable to the task and within its authority. Do not stop unrelated user processes, shared services or another task's agents; do not delete transcripts, workspaces or team directories as a substitute. When ownership or stopping authority is unclear, report the uncertainty and request only the missing decision.
- [ ] AC7: Evaluation distinguishes confirmed exit, intentionally retained work, unresolved survivors and unavailable evidence. It fails false cleanup claims when a completion notification reports remaining child work. It does not infer a running process from an old UI entry or unmatched transcript call alone. Cover successful stop, failed/unconfirmed stop, inherited responsibility and unrelated-resource protection.
- [ ] AC8: Changed instructions pass the voice, shared-sync, template, contract, instruction, packaging/link and applicable audit checks. Behavioral trials exercise leaf handback and coordinator completion with owned background work; independent review checks authority, ownership and completion semantics. Record host/version, conditions, exact evidence and limitations.

### Decisions and uncertainty

- User requested specification after the matched-session finding, then selected `targeted` through the native question tool on 2026-11-15.
- Assumption: normal completion should leave no unaccounted owned work. Intentionally retained authorized operations and unavailable controls require explicit reporting; they do not justify a silent survivor.
- Proposed clarification of existing policy: replace ownership limited to “leaves you dispatched” with responsibility for assigned/inherited work, and replace categorical automatic-exit wording with host-observed lifecycle state. Add explicit background-operation reconciliation. This specification defines the change; it does not implement it.
- Unknown: the exact operation that remained active in the reported run and whether it later exited. Identifying it is not required to define the observed completion boundary, and this spec does not claim a confirmed OS process leak or that 3.0.0 caused it.
- User authorized implementation by invoking `lusona:implement` after this definition. No work-item split was requested.

### TDD policy

- Level: targeted.
- Selected by user: native question response, 2026-11-15, “targeted (recommended)”. This selection belongs to this change.
- Test-first behaviors: evaluation of completed-plus-running-child evidence, confirmed stop, unconfirmed/failed stop, intentional retention, inherited responsibility and unrelated-resource protection. Observe intended failing cases before changing evaluation code.
- Required regression coverage: existing evaluation and repository checks remain applicable. Instruction behavior uses matched baseline/candidate trials under CONTRIBUTING.md; unit tests alone do not establish compliance by an agent.

### Bug evidence

- Expected: report delivery and task shutdown are distinguished, and surviving owned operations are reconciled or reported.
- Observed: the C1 measurement leaf in the linked investigation successfully delivered a report through SubagentHandback. Its parent received a notification marked completed that explicitly said the agent still had background work running and might resume.
- Source: local Claude transcript from svc-lusona.ai, session 459b8507-f0c5-4600-91aa-63437ec82491; handback at 2026-11-16 06:32:30 UTC (2026-11-15 Pacific). Environment version and exact surviving operation were not captured.
- Reproduction status: observed transcript, not a reproduced live failure. No tasks were killed or user project files modified during investigation.
- Impact: the coordinator can mistake a delivered result for complete cleanup, leaving background work without a stated owner or next action.

## Verification approach

Before instruction edits, preserve a baseline including the current uncommitted language rewrite; HEAD alone is not that baseline. Use isolated task-owned fixtures and host-supported task controls. Do not use the user's real surviving operations as kill-test fixtures.

Proposed bounded behavioral coverage: three matched cases, one baseline and one candidate trial per case, on Claude Code with capabilities recorded before execution:

1. Leaf delivers while a background command remains; coordinator must observe and resolve/report the survivor.
2. Persistent or inherited agent needs shutdown; completion requires confirmation, and unavailable confirmation must be reported.
3. Authorized retained work and an unrelated sentinel resource; retain/transfer the first explicitly and leave the second untouched.

Proposed initial bound: six trials, at most 10 minutes per trial and 60 minutes total, stopping earlier on a reproducible blocker. Freeze exact scenarios, model, permissions, spend cap and outcome criteria before running; no paid run is authorized by this draft. If a host cannot expose a case, record the gap rather than inventing confirmation. Use deterministic fixtures to test evaluator classifications separately from live host trials.

## Evidence

- Read-only definition leaf `/root/lifecycle_definition` proposed lifecycle criteria and bounded validation. Its criteria were reconciled into AC1–AC8. The spec retains matched baseline/candidate cases for all three boundaries under the repository completion/ownership evidence rule.
- Reused the source comparison and affected-session observation in the linked notes; no new runtime reproduction was performed for specification.
- Domain guidance: skill-creator principles and repository skill audit apply. Preserve intent, avoid global cleanup authority, and make completion criteria observable.
- Implementation and static validation are recorded below. Required behavioral trials have not run.

## Implementation evidence

- Baseline preserves the earlier uncommitted language rewrite: [baseline archive](../evidence/2026-11-15-task-lifecycle/baseline.tar.gz), SHA-256 `7ee7e324329f1cc608f5cddbf1d4d2e7f9100208339b91798b4a8a3d7e6ab43b`. Captured before lifecycle instruction edits; HEAD alone is not this condition.
- Policy: `references/delegation.md` owns Task lifecycle; shared sources trigger it before handback/handoff/completion and require unresolved-operation reporting. Regenerated all skill regions. Updated batch references to the lifecycle name. Shared every-task block is 353 words under its 400-word ceiling.
- Evaluation: C18 integrated into checks, runner grade/report, scenario, rubric and observation-schema documentation. An independent observer must supply captured lifecycle evidence; absent observations are inconclusive. This is not an automated host-state probe.
- Targeted red/green: 10 initial C18 assertions failed before implementation. Two additional cases (strict boolean authorization and user-directed transfer) failed before correction; the transferred-ownership case failed before its correction. Final evaluation suite: 163 tests pass. One parent run during incomplete scenario integration failed its C18-coverage test; final suite resolves it.
- `mise exec -- python3 -m unittest discover scripts`: 231 passed.
- `mise exec -- python3 -m unittest discover -s evals/loop-conformance`: 163 passed.
- `mise exec -- bash scripts/test-work-record.sh`: passed.
- `mise exec powershell@7.6.10 -- pwsh -NoProfile -File scripts/test-work-record.ps1`: passed, 203 assertions.
- `mise exec -- python3 scripts/check_voice.py plugins/lusona`, `check_skill_template.py`, `check_contract.py`, `check_instructions.py plugins/lusona`, `check_rule_inventory.py`, and `sync_shared.py --source shared plugins/lusona --check`: all exited 0.
- `mise exec -- python3 scripts/package.py --output tmp/lifecycle-package`: passed. Native `claude plugin validate` for plugin and marketplace passed. `git diff --check` passed.
- Independent reviewer `/root/lifecycle_review`, model `gpt-6.1-sol`, found transfer acceptance and user-direction handling defects; evaluator corrected both with regression tests. Independent re-review closed the transfer findings and manual evidence integration. It found a stale suite lock; the lock was refreshed and the actual freeze command then passed. Reviewer independently verified all four lock hashes; R1–R4 are closed, with no static findings. Audit remains undecided pending matched behavioral evidence. Policy review found no ownership or cleanup-authority defect.
- No installation, native Windows, live Claude lifecycle or agent-team trial has run. Behavioral acceptance remains unmet. No processes were terminated or commits made.

### Trial preparation and remaining validation

- [Durable evidence/preparation](../evidence/2026-11-15-task-lifecycle/README.md) retains frozen matched inputs and controlled task fixtures. Six trials remain unrun; no paid call or fixture process has started.
- Observed configuration: Claude Code 2.1.325, model alias `opus`, effort `xhigh`. Proposed resources remain pending in the native question. Model alias resolution must match within each pair.
- Prepared fixture cases test policy actions with observed fixture state; native Claude team shutdown remains an integration gap. Do not count fixtures as native host evidence or mark AC8 complete from unit checks.
- `mise exec -- python3 evals/loop-conformance/run.py freeze --plugin plugins/lusona --out tmp/lifecycle-suite-freeze --host claude --model opus --effort xhigh --timeout 600 --judge-model opus --judge-effort xhigh --max-trials 6` passed after the suite-lock correction; freeze makes no actor call.
- Lifecycle leaves completed their assignments and report no background operations or descendants. This host exposes interrupt/follow-up controls but no shutdown/close control; completed agent records cannot be claimed removed. All lifecycle leaves have returned their final results and report no active operations.

## Current handoff

- Authorized: implementation, user invocation on 2026-11-15. Targeted TDD selected. Trial resources are pending the native question. Grouped local checkpoint commits are authorized by the user on 2026-11-16; push and publication remain unauthorized.
- Next action: run the retained matched trials after the pending resource decision. User decision pending for six trials, 10 minutes each, 60 minutes total, $10 total cap, configured Claude model. Only trials wait on this decision. Implementation is authorized; do not request it again. Keep queue in Review until required behavioral evidence and audit acceptance are satisfied.

### Local test version

User, 2026-11-16: authorized version preparation without push, and will test locally first. Local tag 3.1.0 exists at 2244a6a; prepared 3.1.1 as an untagged local candidate. At version preparation, no commit, tag or push was authorized; the later checkpoint decision below authorizes local commits only. User testing is pending and does not yet satisfy behavioral acceptance.

### Commit checkpoint authority

User requested grouped local commits on 2026-11-16. This authorizes a checkpoint while behavioral validation remains pending; it does not authorize push or publication. Local testing remains with the user.
