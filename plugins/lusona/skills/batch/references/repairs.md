# Repair rounds

Read before charging, dispatching, cancelling or resuming a repair round for a batch item, and before retrying after an environment failure.

## Budget

- The recorded repair budget counts corrective rounds after the first bounded attempt.
- The count spans all responsibilities and owners of the item.
- Increasing the budget requires explicit new authority. Changing leaves, responsibilities or labels does not reset it.

## What starts a round

- A round starts when a failed implementation outcome, required check, review, integration or unresolved bounded investigation needs another approach.
- Expected red and green steps of a task's TDD sequence are not failed batch attempts. An unsuccessful task outcome that needs a new approach is.
- An initial investigation needs a bounded question, a finite set of experiments and a stopping condition. When it ends unresolved, another approach charges a round to the same item.
- When a consequential decision or authority is missing, defer the item at once. Do not charge or dispatch a round that assumes the missing decision or authority.
- On an environment failure, do not close the item. Retry only after the environment has changed, and charge each retry as a round.

## Charging and running a round

- Before dispatch, persist the round's charge, the triggering finding reference, the declared bounded set of corrections or experiments, the owners, and the expected checks and review.
- One round covers that declared set and its checks and review.
- Run fixes within one round concurrently only when they are independent, within the batch pool.
- Diagnostic investigation of the declared failure belongs to that round.
- Do not add a correction or experiment outside the declared set to an open round.
- A failed round that needs a different correction or experiment consumes the next round. This includes a new actionable failure found during verification.

## Interruption, cancellation and exhaustion

- Keep an interrupted round charged. Resume its declared set only after you stop or reattach its writers and confirm that its recorded inputs match the actual content.
- Cancel a reserved charge only with evidence that no work was dispatched. Retain that cancellation and its evidence reference.
- Keep a round charged when its progress is uncertain.
- When the rounds are exhausted, defer the item and its unfinished dependents. Retain attempts, findings and the next action in the owning records.
- On a requested suspension, stop dispatch and reconcile active writers. Before handing off, checkpoint the reserved intent, the charge, the actual dispatch status and the retained candidate.
- Suspension does not reset rounds.
