# Delegation

Read only the sections required for your responsibility: assigned leaves must read Assigned
leaves and Assignment results; coordinators read all sections. These are mandatory procedures,
not optional examples. Reuse current supplied or loaded text under
[core loading rules](../README.md#loading-rules). Coordinators also read
[model routing](model-routing.md) before dispatch and [worker lifecycle](worker-lifecycle.md)
after results; leaves need neither without those responsibilities.

## Assigned leaves

The worker applies the supplied assignment instructions within its scope as an assigned leaf; no
recursive delegation is required. Do not spawn children without an explicit grant or interview
the user. If required context is unavailable or contradictory, return the specific gap and
necessary question to the coordinator. Return the assignment result before waiting or ending;
do not self-assign another workflow skill, start another phase, or claim more work without a new
assignment.
Domain skills may supplement the supplied workflow within the assigned scope; they do not grant
another responsibility or wider authority. The coordinator reconciles findings, handles user
questions through the permitted native tool, and chooses authorized follow-up; it alone owns
shared queue and saved handoff updates.
The worker cooperates with shutdown after preserving the result and stopping owned work;
report any unfinished operation that prevents safe shutdown.


## Assignment results

Delegates return these fields in their final report, using `none` where applicable:

- Status: `complete`, `blocked`, or `incomplete`.
- Outcome: what was accomplished within the assigned scope, with changed files or artifact links.
- Verification: checks performed and their results; required checks not run or not passing.
- Remaining work and concerns: unfinished scope, findings, limitations, and any blocker.
- Recovery: retained work, active operations or child workers, and the next action/input needed.
- Correction rounds: for assigned correction or diagnostic work, each round run, whether it made
  material progress, and the resulting consecutive and total counts for the failure.

A blocked result identifies what prevented completion, what was tried, and what would
enable progress.

These statuses describe assignment outcomes, not queue states, coordinator acceptance,
process exit codes, or worker lifecycle. A completed review can report defects; an
implementation with an unmet required check cannot report `complete`.

| Status | Meaning |
| --- | --- |
| `complete` | Assigned scope and required checks are satisfied |
| `blocked` | Progress requires an unavailable input, decision, permission, dependency, or environment capability |
| `incomplete` | Execution ended with assigned work or required verification remaining, without a named blocking prerequisite |

## Assignment contract

The coordinator delegates the substantive specialist outcome, not just preliminary inspection.
Supply the relevant Lusona workflow skill, applicable domain skills, required role-specific core
sections, specialist persona, bounded outcome, completion checks, write ownership, authorization,
TDD policy, and Assignment results
in each assignment. Include accessible resource paths or the necessary excerpts; do not
assume a worker inherits the coordinator's conversation or has read a skill merely because
it is installed. For domain skills, supply the current instructions or accessible paths with explicit
loading instructions. A complete, current copy of the required core sections supplied or demonstrably
inherited
satisfies [core loading rules](../README.md#loading-rules); identify its source and supply
missing required sections. Prefer bounded context over full conversation history; preserve
accepted intent, constraints, authority/TDD source, relevant evidence, failure counts, and
recovery inputs. Supply only procedures for the worker's responsibility. Anchor links identify
sections; they do not prove a host loads only those sections. Supply the actual required text
or accessible paths with explicit section instructions. Keep independent reviewers free of
implementer conclusions; provide agreement, actual diff, and verification evidence.

## Evaluate and reconcile results

Coordinator acceptance is separate: verify a complete result and resolve material concerns;
supply or defer a blocked prerequisite; schedule bounded continuation for incomplete work.
Serialize dependencies and mutable checks, verify returned evidence, and stop previous writers
before transferring ownership. Worker completion does not establish acceptance or release capacity.

A missing or malformed report, idle notification, or host-reported crash is not success.
Request missing information from a reachable worker or reconcile artifacts and host evidence;
keep the assignment unresolved until its outcome is established. For older reports, map
`DONE` to `complete` only after checking the evidence, `NEEDS_CONTEXT`/`BLOCKED` to `blocked`,
and assess `DONE_WITH_CONCERNS` against the same completion criteria. Do not rewrite history.

For a blocked result, missing context calls for more information; an environment failure calls
for an environment fix. Select a stronger model when more reasoning is needed and allowed;
split separable outcomes when the assignment is too large. Ask the user only for unresolved
decisions or authority that the coordinator cannot supply within the existing authorization.
Do not retry a blocked assignment without changing its input or approach.

Before reassigning edits, stop the previous writer and transfer ownership explicitly.
Preserve useful evidence and existing edits; give the new delegate the current state,
remaining outcome, and effective authorization and TDD policy. Avoid concurrent writers
to the same scope. A delegate's `complete` does not replace coordinator verification.
