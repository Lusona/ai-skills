# Decision revisions

Read when new input contradicts an accepted decision, before recording the outcome of revisiting it, and before applying a follow-up request that changes the objective.

## Follow-up input

- Treat a follow-up request as a scope change to the current objective, not as a new objective. Preserve progress and apply the change.
- A follow-up replaces the objective only when it cancels or replaces it explicitly, or requests an incompatible one.

## State the conflict

New input includes a requirement, a specification, a measurement or an experiment result.

- Do not reject the new input because an accepted decision exists.
- Do not continue as if the decision did not exist.
- State the decision, its source, the conflict and the affected assumptions.
- Write the same statement in the reply and in the owning record. When saving is prevented, state it in the reply only.
- As a leaf, return the statement to the coordinator. Do not ask the user.

## Revisit with the user

1. Give the user the options and a recommended answer.
2. Reach one outcome with the user: kept, revised in part, or superseded.
3. Revisiting a decision does not authorize the change. Changes to accepted outcomes, contracts, TDD level or consequential commitments need the user's decision.
4. Record the outcome before work that depends on the decision continues.
5. Continue work that the conflict does not affect, within existing authority.

## Record the outcome

Record every outcome in the record that owns the decision: the decision list of a spec, an ADR for a consequential architecture decision, or notes.

| Outcome | Record |
| --- | --- |
| Kept | The decision, the conflicting input, the date and the source of the user's answer. |
| Revised in part | The changed part, the new text, the date and the source. Keep the replaced text and its rationale, marked as revised. |
| Superseded | Mark the old decision superseded, with the date, the source and a link to the replacing decision. Keep its rationale. |

- The source names who decided, when and through which channel, for example "user, 2026-11-11, native question tool".
- Do not delete superseded text or rationale.
- In an ADR, set `Status: superseded` and fill `Superseded by`. In the replacing ADR, fill `Supersedes`.

## Reconcile

1. Find the records, assignments and handoffs that depend on the revised decision.
2. Update those within your write ownership to the revised decision.
3. Report the corrections that other owners must make, naming each record and owner.
4. Resume work under the revised decision.

- When a record still states a superseded decision, follow the revision and correct or report that record.
