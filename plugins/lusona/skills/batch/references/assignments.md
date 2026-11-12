# Assignments and results

Read before dispatching a batch assignment, and when a batch assignment result arrives.

## Before dispatch

- Persist each assignment's dispatch intent in the batch record before starting it: owner, responsibility, scope, dependencies, baseline, pool slot, any delegation grant and any charged round.
- Stop the writers of the affected scope before reassignment, deferral or integration. A stop request does not prove that the writer stopped.
- Before dispatch, for each leaf that has not stopped, record the scope it holds in the batch record or stop the leaf.

## Results as they arrive

Handle each available result as it arrives. Do not wait for all dispatched leaves.

When a serialized operation is in progress, first complete it or, for an integration, record its next phase. Then, before further dispatch or waiting:

1. Inspect the result and its evidence.
2. Persist the assignment outcome and recovery references in the batch record.
3. When the item's state, blocker or next action changed, update its row in `docs/lusona/work.md`. Do not rewrite an unchanged row.
4. Limit the row to the actual queue state, the current blocker or next action, and the owning evidence link.
5. Refresh the affected pointers of the current batch handoff. Do not copy task evidence or add an activity log.

- When evidence is missing, record the pending verification or the missing report as the next action. A completion notification does not establish success.
- Record the returned status and owning evidence references before releasing the assignment's write scope.
- Record result status, coordinator acceptance and host lifecycle evidence separately.
- Decide for each idle leaf whether to reuse it or shut it down. Reconcile any leaf that a leaf with a delegation grant reports as not stopped.

## Item state

- A leaf's `complete` describes its assignment, not the queue item.
- Keep remaining implementation, integration, checks, review, acceptance or delivery visible in the row.
- Apply the queue state criteria and completion gates. Close and archive an item once its gates pass, even while unrelated items continue.
- Reporting a result does not integrate changes, release write ownership or release host capacity. Apply integration and leaf lifecycle separately.
- On hosts without asynchronous notifications, collect results at assignment boundaries. Do not promise immediate background updates.
