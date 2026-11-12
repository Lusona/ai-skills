# Deferral and resumption

Read before deferring a batch item, before continuing a recorded batch, and before stopping or completing a batch.

## Deferral

- Before continuing past an unfinished item, stop or reconcile its writers. Preserve its source changes and baseline identities, and reconcile candidate transfers.
- Record the reason, the excluded dependents, the repair rounds consumed and the next action.
- Release ownership only after the unfinished changes are isolated.
- Deferral is a scheduling flag. It is not Done and does not reset the queue state.
- A deferred item keeps its actual queue state and blocker. It releases execution capacity once its writers stop and its unfinished changes are isolated.
- Unfinished content must not become an input of an independent item. Do not continue on a baseline that contains unfinished work.
- When you cannot isolate the unfinished changes, or cannot prove that restoration loses no other writer's changes, stop all affected work.

## Resuming a recorded batch

Apply these steps to an explicitly selected continuation:

1. Load the fixed membership, authorization and constraints, TDD and completion references, dependency reconciliation, limits, assignments, open rounds, integration phases and current handoff.
2. Recheck the recorded authority against the user's current instructions. Do not enlarge the selection or reset budgets.
3. Keep parked members ineligible until the user reactivates them explicitly. Retain their repair counts, and defer dependents that need them.
4. Inspect the actual leaves, workspace content, destination and returned artifacts.
5. Reattach to or stop each writer that has not stopped before dispatching again. Saved assignment state does not prove completion or that a writer stopped.
6. When the host cannot establish ownership, stop the affected work and report the exact blocker.
7. Recover interrupted candidate transfers and promotions before dispatching dependent work.
8. Reuse completed checks and decisions only when their inputs match. Preserve valid evidence and link it.
9. Refresh the effective host capacity. Keep the requested ceiling. Count each leaf that has not stopped and the coordinator's own occupancy as occupied host capacity.
10. Work in sequence only where unfinished edits stay separated. Working in sequence does not replace required independent review.
11. Update the one current handoff and dispatch the next eligible bounded assignment.
12. Keep unresolved deferrals excluded until the recorded blocker is resolved within authority.

## Stop and completion report

- Report history links of completed items, queue and evidence links of deferred and unfinished items, unresolved decisions and concrete next actions.
- State which outcome applies: all selected complete, selection exhausted with deferrals, interrupted, or unsafe to continue.
- Before handing off, persist the exact recovery inputs and ownership in the batch record. Do not copy task evidence into it.
