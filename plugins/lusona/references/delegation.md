# Delegation

Read before dispatching an assignment, after each leaf result, and before closing or handing off responsibility for leaves. Read when deciding whether independent review is required. Read as a leaf before returning a result.

## Roles

- An assignment that names you a leaf makes you a leaf. A separate host task or a prohibition on further delegation does not.
- Your role follows the responsibilities the assignment names.
- As a leaf, read Assigned leaves and Assignment results. Apply each other section only when the assignment grants the responsibilities that section covers.

## Coordinator duties

- Ask the user questions, dispatch assignments, reconcile results, integrate, verify and write shared state.
- Delegate the specialist outcome, not only an inspection.
- One leaf working in sequence satisfies delegation.
- Occupied capacity is not unavailability. Wait for working leaves; reuse or release finished ones.
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
- Installation, an anchor link, or another leaf's read does not prove that the leaf has the text.
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
- Under a delegation grant, before returning, stop each leaf you dispatched and include its results in your result. Report any leaf you could not stop.
- Domain skills add to the assigned scope without expanding responsibility or authority.
- Report missing or contradictory context, questions and recommended next actions to the coordinator.
- Return findings for the coordinator to save, unless you have write ownership of the record.
- With write ownership of a change record or notes, update that record's current handoff. Return other handoff changes to the coordinator.
- Before cooperating with shutdown, preserve the result and stop owned work. Report each operation that you cannot finish or pause in a recoverable state.

## Assignment results

Return these fields, with `none` where a field does not apply:

- Status: `complete`, `blocked` or `incomplete`.
- Outcome: the accomplished scope and the changed paths and artifacts.
- Verification: checks and results, naming required checks that failed or did not run.
- Remaining work and concerns: unfinished scope, findings, limits and blockers.
- Recovery: retained work, active operations and leaves, and the next action or input.
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
3. A status label alone is not evidence. When a required check is missing, or the result contradicts the assignment or its evidence, apply step 4.
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

## Leaf lifecycle

Apply after each result and before closing or handing off responsibility for leaves. This includes inherited, reassigned or earlier-session leaves, even when you dispatch no new leaf.

- You own lifecycle decisions for the leaves you dispatched. The leaf that dispatched leaves under a delegation grant owns their lifecycle.
- After each result, either assign concrete authorized follow-up work with explicit ownership, or release the leaf through the host's shutdown or close mechanism.
- Do not keep a persistent leaf idle in case more work appears.
- Inspect the actual agent type and its available controls.
- For a persistent Claude Code agent team member, request shutdown and wait for acknowledgment or host-confirmed termination.
- A Claude Code agent outside a team ends by itself. Observe the host result; do not invent a team cleanup operation.
- On other hosts, use the exposed lifecycle controls.
- Confirm termination or closure through host evidence. An idle notification, a final report or a sent shutdown request does not prove shutdown.
- Track pending or rejected shutdowns and resolve the stated reason. Do not report capacity as released before the host confirms it.
- When shutdown or its confirmation is unavailable, report the limitation and the surviving leaf's identity. Do not claim cleanup, and do not delete transcripts, workspaces or team directories as a substitute.
- At batch completion, deferral, interruption or handoff, reconcile every leaf within that responsibility.
- Preserve unfinished work before shutdown. Record surviving leaves, ownership and pending lifecycle actions in the existing handoff.
- Assignment completion, release of write ownership and release of host capacity are separate facts.
