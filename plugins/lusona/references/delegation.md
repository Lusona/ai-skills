# Delegation

Leaves read Assigned leaves and Assignment results; coordinators read all sections. Reuse current
text under [core loading rules](../README.md#loading-rules). Coordinators also read
[model routing](model-routing.md) before dispatch and [worker lifecycle](worker-lifecycle.md)
after results; leaves need neither without those responsibilities.

## Assigned leaves

Execute the bounded assignment; return results before waiting/ending. Do not interview users or
self-assign another workflow skill/phase. Additional work requires a new assignment; children require
an explicit grant. Domain skills supplement assigned scope without expanding responsibility or authority.
Route missing/contradictory context, questions, and recommended next actions to the coordinator;
it reconciles findings, asks users through the permitted native tool, and alone writes shared
queues/saved handoffs. Preserve the result and stop owned work before cooperating with shutdown;
report unfinished operations preventing safe shutdown.

## Assignment results

Final reports contain these fields (`none` where applicable):

- Status: `complete`, `blocked`, or `incomplete` as defined below.
- Outcome: accomplished scope; changed paths/artifacts.
- Verification: checks/results; required checks failing or unrun.
- Remaining work and concerns: unfinished scope, findings, limits, blockers.
- Recovery: retained work, active operations/children, next action/input.
- Correction rounds: for correction/diagnostic work, each round, material progress, resulting
  consecutive/total counts for the failure under [correction limits](corrections.md).

| Status | Meaning |
| --- | --- |
| `complete` | Assigned scope and required checks satisfied |
| `blocked` | Unavailable input, decision, permission, dependency, or capability prevents progress; report attempts and resumption prerequisite |
| `incomplete` | Work/verification remains without a named blocking prerequisite |

Statuses describe assignments, not queue state, coordinator acceptance, exit codes, or lifecycle.
A complete review may find defects; unmet required checks prevent implementation `complete`.

## Assignment contract

Delegate the substantive specialist outcome, not merely inspection. Supply persona, bounded outcome,
completion checks, write ownership, authority, explicit TDD/source, relevant workflow/domain skills,
role-specific core sections, and Assignment results. Supply accessible paths with explicit loading
instructions or current text; identify supplied/inherited sources and fill gaps under Loading rules.
Installation and anchor links do not prove context inheritance or section-only host loading.
Prefer bounded context to full history: retain accepted intent, constraints, evidence, failure counts,
and recovery inputs; include only applicable procedures. Independent reviewers receive agreement,
actual diff, and verification evidence without implementer conclusions.

## Evaluate and reconcile results

Coordinator acceptance is separate from worker completion or capacity release. Verify completed scope,
resolve concerns, supply/defer blocked prerequisites, and schedule bounded incomplete continuation.
Reconcile against acceptance and [verification rules](tdd.md); serialize dependencies/mutable checks.
Reuse adequate checks on unchanged inputs; rerun for changed inputs, failures, missing/unreliable
evidence, or concrete unresolved risks. Independently required checks/review still apply.

Missing/malformed reports, idle notifications, and crashes are not success. Ask reachable workers for
missing information or reconcile artifacts/host evidence; leave unresolved until established.
Map legacy `DONE` to `complete` only after evidence checks; `NEEDS_CONTEXT`/`BLOCKED` to `blocked`;
assess `DONE_WITH_CONCERNS` against completion criteria without rewriting history.

For blocked work, supply missing context, fix environment, select a stronger model when allowed and
reasoning is insufficient, or split oversized separable outcomes. Ask users only for decisions/authority
the coordinator cannot supply. Do not retry unchanged blocked inputs/approach. Before transferring
edits, stop the previous writer and explicitly transfer ownership; avoid overlapping writers. Preserve
edits/evidence; supply current state, remaining outcome, authority, and TDD to the successor.
