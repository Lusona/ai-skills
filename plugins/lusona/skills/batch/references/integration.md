# Serialized integration

Read before integrating a batch item's candidate, and before recovering an interrupted candidate or promotion.

Record each phase in the batch record with one of these labels: `intent recorded`, `candidate materialized`, `evidence collected`, `promotion intent`, `promotion materialized`, `accepted`, `deferred`.

## Before integration

- A Git rebase changes identities. After one, reconcile recorded baselines, candidate content and affected verification and review evidence before the steps below.

## Steps

1. Stop the writers of the item and of the destination. Identify the source baseline, the exact item delta, the current destination baseline and required dependencies.
2. Check destination drift and attribution before applying anything.
3. Before mutation, record the integration intent, the candidate location, the expected content identities and the recovery method.
4. Preserve the source until acceptance and evidence recording are confirmed.
5. Materialize one attributable candidate at a time. Where the host supports it, hold the candidate outside the accepted destination until checks pass.
6. Record `candidate materialized` with the candidate's actual identity, including uncommitted content. Keep intent and actual result distinguishable.
7. Run required verification and independent review on the materialized candidate.
8. Give reviewers the actual diff, the governing definition and architecture, and the check evidence, without the implementer's conclusions.
9. Record evidence in its owning record and link the candidate identity from the integration entry. Then record `evidence collected`.
10. Do not move the item to Done while a check is unrun or review is unavailable.
11. For an external candidate, record `promotion intent` before transfer: the destination's identity before transfer, the expected identity after transfer matching the reviewed candidate, the attributable delta and the recovery inputs.
12. Keep those writers stopped. Recheck destination drift immediately before transferring the delta.
13. On drift, reconcile the candidate and affected evidence before proceeding.
14. After transfer, record `promotion materialized`. Compare the actual destination content identity with the reviewed candidate.
15. Materializing an external candidate alone never promotes it to the destination.
16. Before recording `accepted`, require the actual destination to match the reviewed candidate and the required evidence to cover the item's final content.
17. For a candidate already materialized in the destination, compare that destination identity without a second transfer.

## Later integrations and drift

- After a later integration, assess the earlier behavior it affects. Rerun affected checks, and obtain review where reviewed behavior changed.
- Do not repeat unrelated unchanged reviews.
- Drift invalidates affected evidence. Reconcile the candidate and the affected evidence before acceptance.

## Failure

- On failure, retain the candidate and its evidence and charge the item's repair budget.
- Hold the failed candidate outside the accepted destination. Alternatively, restore the destination by removing only the candidate's attributable changes, after proving that no other writer's changes will be lost.
- When deferring, record `deferred` and identify the accepted destination content.
- When you cannot prove that restoring the destination loses no other writer's changes, stop the batch.
- When a later regression occurs, retain the earlier completion evidence. Charge corrective attempts to the item that introduced the regression.
- When cause or ownership is uncertain, investigate within the budget of an identified responsible item, or defer the affected work.

## Recovery of interrupted transfers

- An intent is not evidence of transfer. Missing result metadata is not permission to apply again.
- Recover candidate materialization and destination promotion separately.
- Compare each operation's actual target with its recorded identity before transfer and its expected identity after transfer.
- A retained external candidate proves nothing about promotion.
- When the destination matches the promotion's expected result, recover that phase and validate evidence without transferring again.
- When the destination still matches its identity before transfer, promote only after reconfirming ownership, candidate evidence and drift.
- When content matches neither expected state, reconcile drift before transfer or restoration. Stop when the differing content still cannot be attributed to the item or to another writer.
- Never replay a patch without these comparisons.
