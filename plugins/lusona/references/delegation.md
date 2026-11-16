# Delegation

Read before dispatching an assignment and after each leaf result. Read before final handback, task completion or handoff with owned agents or background operations. Read when deciding whether independent review is required. Read as a leaf before returning a result.

## Roles

- An assignment that names you a leaf makes you a leaf. A separate host task or a prohibition on further delegation does not.
- Your role follows the responsibilities the assignment names.
- As a leaf, read Assigned leaves, Assignment results and Task lifecycle. Apply each other section only when the assignment grants the responsibilities that section covers.

## Coordinator duties

- Ask the user questions, dispatch assignments, reconcile results, integrate, verify and write shared state.
- Delegate the specialist outcome, not only an inspection.
- One leaf working in sequence satisfies delegation.
- When all agent slots are occupied, wait for working leaves. Reuse or release finished leaves; occupied slots do not make delegation unavailable.
- Apply the host's capacity accounting.
- Only the coordinator writes shared queues, batch records and the handoffs saved in them.
- Keep parallel assignments independent of each other. Keep integration and verification with the coordinator.

## Assignment contract

Give each assignment these items:

- The role: name the recipient a leaf.
- The workflow responsibilities and the persona.
- The bounded outcome and its completion checks.
- Write ownership and authority.
- Any delegation grant: the number of leaves the recipient may dispatch.
- The TDD level and its source.
- The workflow and domain skills that apply to the assignment.
- The paths of the procedures and references the leaf must read, each with its trigger, or their current text.
- The Assignment results fields below.

Supply context this way:

- Name the source of each supplied text, and of text the leaf demonstrably inherits. That text satisfies the read requirement.
- Reuse unchanged instructions across skills and assignments. Supply missing or changed text when the role, operation or source changes.
- Do not assume a leaf has the text because the plugin is installed or an anchor link exists. Another leaf reading it does not establish that this leaf has the text.
- Give bounded context instead of full history. Keep accepted intent, constraints, evidence, correction counts and recovery inputs.
- Include only the procedures that apply to the assignment.

## Model routing

- Before each dispatch, select the least capable available model that is adequate for the assignment, and a supported reasoning setting.
- Judge adequacy by uncertainty, coupling, failure consequences and verification strength. File count alone does not establish complexity.

| Tier | Choose when |
| --- | --- |
| `fast` | The assignment leaves no implementation decision to the leaf, scope is isolated, and checks can establish correctness |
| `standard` | Work requires implementation judgment within established boundaries |
| `deep` | Work involves uncertainty outside established boundaries, interacting invariants, or consequential failure |

- A tier names the leaf's model capability. The `fast` tier is not a host's fast mode, which keeps the model and changes output speed and cost.
- Map tiers to models and reasoning settings with the consuming project's instructions. Without a mapping, select from the host's exposed models by their capability descriptions.
- Pass the model and reasoning setting explicitly through the host's dispatch controls. A tier label in the assignment does not select a model.
- Do not invent model identifiers or assume unsupported controls.
- Preserve explicit user model choices and host restrictions.
- Inherit a setting when a user model choice or host restriction requires it, or when its control is unavailable. Still select the other supported settings. Report when inheritance prevents the selected routing.
- Selecting the current model is valid when it is adequate and no less capable model is adequate.
- Routing selects the leaf's model. It does not change the coordinator's model.
- Choose a context mode compatible with the selected model and reasoning setting.
- When the host prohibits overrides with full-history forks, supply a bounded assignment with the needed instructions and inputs.
- On hosts with `fork_turns` and that restriction, use `"none"` or a supported positive turn count. Omitted or `"all"` inherits the coordinator's model and reasoning settings.
- When you drop a selected override to keep full history, report it.
- Record routing in the owning change or batch record only when the dispatch uses a model or reasoning override.
- Reassess routing at dispatch and escalation. A planned task needs no tier or rationale of its own.
- Tiers never reduce required verification or expand scope.

## Independent review

- Independent review is required when user or repository rules require it, or when the change affects security boundaries, persistent data or shared contracts, or has multiple coordinated writers.
- Decide at entry, and again when scope grows.
- Give the reviewer the agreement, the actual diff and the verification evidence, without the implementer's conclusions.
- A persona change is not independence. Reuse a leaf for review only when it did not write the change and has not received the implementer's conclusions.
- When required review is unavailable, report it as unmet.
- Repair findings within authority and verify the repair.

## Assigned leaves

- Execute the bounded assignment. Return results before waiting or ending.
- Do not interview the user or start another workflow skill on your own.
- Additional work requires a new assignment.
- Before returning, reconcile owned work under Task lifecycle and include delegated results in your result.
- Domain skills add to the assigned scope without expanding responsibility or authority.
- Report missing or contradictory context, questions and recommended next actions to the coordinator.
- Return findings for the coordinator to save, unless you have write ownership of the record.
- With write ownership of a change record or notes, update that record's current handoff. Return other handoff changes to the coordinator.
- Before cooperating with shutdown, preserve the result and apply Task lifecycle to owned work.

## Assignment results

Return these fields, with `none` where a field does not apply:

- Status: `complete`, `blocked` or `incomplete`.
- Outcome: the accomplished scope and the changed paths and artifacts.
- Verification: checks and results, naming required checks that failed or did not run.
- Remaining work and concerns: unfinished scope, findings, limits and blockers.
- Recovery: retained work, active operations and leaves, their lifecycle dispositions under Task lifecycle, and the next action or input.
- Correction rounds: for correction or diagnostic work, each round, its material progress, and the consecutive and total counts for the failure. Inside a batch, give the charged rounds under the repair budget.

| Status | Meaning |
| --- | --- |
| `complete` | Assigned scope and required checks satisfied |
| `blocked` | Unavailable input, decision, permission, dependency or capability prevents progress; report attempts and the resumption prerequisite |
| `incomplete` | Work or verification remains without a named blocking prerequisite |

- Statuses describe the assignment. They are not queue states, coordinator acceptance, exit codes or lifecycle states.
- A complete review may report defects.
- An implementation with unmet required checks is not `complete`.

## Evaluate results

1. Preserve each result and its recovery evidence.
2. Inspect it against the assignment. Decide acceptance separately from the leaf's status.
3. Check the reported results; do not accept a status label as evidence. When a required check is missing, or the result contradicts the assignment or its evidence, apply step 4.
4. Missing or malformed reports, idle notifications and crashes are not success. Ask a reachable leaf for missing information, or reconcile artifacts and host evidence. Leave the result unresolved until that information or evidence establishes it.
5. Map a legacy `DONE` to `complete` only after the evidence checks. Map `NEEDS_CONTEXT` and `BLOCKED` to `blocked`. Assess `DONE_WITH_CONCERNS` against the assigned scope and required checks. Do not edit the legacy report.
6. Verify the completed scope, resolve concerns, supply or defer blocked prerequisites, and schedule bounded continuation of incomplete work.
7. Reconcile results against acceptance and the TDD and verification rules. Serialize dependent work and checks that use mutable resources.
8. Reuse a valid check result when its inputs are unchanged. Rerun the check for changed inputs, failures, missing or unreliable evidence, or a named unresolved risk. Independently required checks and review still apply.

For blocked work:

- Supply the missing context, fix the environment, select a more capable model when the reassessed routing selects a higher tier and no user model choice or host restriction prevents it, or split a separable outcome.
- Ask the user only for decisions or authority you cannot supply.
- Do not retry a blocked assignment with unchanged inputs and approach.
- Before transferring edits to another leaf, stop the previous writer and transfer ownership explicitly. Do not let two leaves write the same files.
- Preserve edits and evidence. Give the successor the current state, the remaining outcome, the authority and the TDD level.

## Task lifecycle

Apply after each leaf result and before final handback, task completion, deferral, interruption or handoff.

### Ownership and inventory

- Account for known agents, shells and background commands within your responsibility. Include inherited, reassigned and earlier-session work, even when you launched nothing.
- Identify each operation by its task ID or equivalent host handle. Inspect its last observed state and available controls.
- As a leaf, reconcile your owned operations and granted descendants. Return any unresolved descendant to the coordinator with its identity and recovery information.
- As coordinator, reconcile returned survivors and operations assigned to you. Do not assume that receiving a result ends this responsibility.
- Stop only operations attributable to this task and within its authority. Do not stop unrelated user processes, shared services or another task's agents.
- When ownership or stopping authority is unclear, report the uncertainty. Ask only for the missing decision; as a leaf, return it to the coordinator.

### Resolve or retain

- Preserve results and recoverable work before stopping an operation.
- Continue or wait for work the authorized assignment still requires, within its existing limits.
- Stop or close owned operations no longer required, using supported host controls. Confirm the resulting state through host evidence.
- Do not stop a command again when its exit is confirmed. Do not keep a persistent leaf idle in case more work appears.
- For a persistent Claude Code team member, request shutdown and verify acknowledgment or host-confirmed termination.
- For an agent outside a team, inspect host evidence rather than assuming automatic exit. Do not invent a team cleanup operation.
- Retain a running operation only for an authorized continuing purpose with an explicit owner. Record its identity, purpose, owner and next observation or stop condition.
- Transfer ownership only when the recipient accepts it or the user directs the transfer. Ending a turn does not transfer ownership.
- Report retained work as an intentional handoff, not as terminated work or released capacity.

### Confirm and report

- Distinguish report delivery, assignment completion, write-ownership release and host-capacity release.
- Do not treat a final report, idle notification, shutdown request or completed status alone as termination evidence.
- When a completion notification reports running child work, keep lifecycle reconciliation open. Resolve or explicitly report that work before claiming full completion.
- Track pending or rejected shutdowns and resolve the stated reason within existing limits. Do not retry indefinitely or invent a reset of correction limits.
- When inspection, shutdown or confirmation is unavailable, report the operation's identity, owner and last observed state. Name the missing capability and next action.
- Preserve unresolved operations and recovery information in the existing handoff. Distinguish finished deliverables from unresolved cleanup; do not claim termination or released capacity.
- Continue unrelated authorized work while an operation remains unresolved.
- Do not infer a running process from a retained UI entry or unmatched transcript call alone.
- Do not delete transcripts, workspaces or team directories as a substitute for termination evidence.
