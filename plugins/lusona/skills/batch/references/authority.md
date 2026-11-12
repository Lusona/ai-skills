# Batch authority and decisions

Read before recording a batch's authorization and before settling a routine decision inside a batch. Also read before deferring an item for a missing decision, authority or TDD level, or for new input that contradicts an accepted decision.

## Authorization

- A batch needs the user's explicit authorization of unattended work on a fixed selection of queue items.
- Selecting work for discussion or planning alone does not authorize batch implementation.
- Before execution, record the selection, decision authority, applicable TDD, completion conditions, requested assignment ceiling and per-item repair budget in the batch record.
- Apply the batch rules to the questions, queue handling, delegation and next action of each skill the batch dispatches.
- Host approval rules still apply. An unanswered request never counts as consent.
- Existing commit authority and repository restrictions apply. As coordinator, stage and commit only after verified integration.
- Batch authorization does not grant publication, deployment or other external actions beyond the user's explicit scope.

## Routine decisions

- As coordinator, settle routine details from existing project decisions and recorded assumptions within the delegated authority. An assumption that changes an accepted outcome, contract or TDD level is not routine.
- Record the basis and authority of each such decision. Do not present it as a user answer.
- Reconcile related definitions before accepting shared assumptions or making dependent architecture decisions.
- Reconcile architecture outputs before dependent implementation decisions or assignments.
- Give each shared decision one owner, with all affected definitions as inputs.
- Run architecture in parallel only across compatible scopes.
- While a shared decision, shared assumption or possible coupling is unresolved, hold the design and implementation it affects. Continue unrelated reconciled work.

## Scheduling

- After each result, compare each affected item's result with its intended outcome and schedule its next eligible bounded action.
- Do not hold an item until other items finish the same responsibility. Shared dependencies, ownership and required review still decide eligibility.
- Advance independent settled work without waiting for the whole batch. Disjoint files do not prove independence.
- More than one selected item can be Doing or in Review at the same time.
- Proceed through authorized work without asking the user for a new approval when an item moves to another responsibility.

## Missing and contradicted decisions

- For a missing consequential decision, authority or TDD level, record the question and defer the affected item and its dependents.
- When new input contradicts an accepted decision, record the decision, its source and the conflict in the batch record for the user. Defer the affected item and its dependents.
- Continue eligible independent work.
- Unset TDD still permits independent definition and planning.
- At stop or completion, report the deferred questions and recorded conflicts to the user for resumption.

## Completion

- When independent review is unavailable, report it as unmet. A persona change does not replace it.
- Keep evidence in its owning change record, ADR or existing execution record. The batch record links those records.
