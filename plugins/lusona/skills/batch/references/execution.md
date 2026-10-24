# Execution and recovery

Use with [batch](../SKILL.md) and the [batch record](../../../templates/batch.md).
The record owns coordination facts and evidence pointers, not a duplicate queue or task log.
Keep requirements, implementation, review, and check evidence in each change record, linked ADRs,
or existing separate execution records. Replace superseded transient state while retaining facts needed to recover
ownership, authority, transfers, and consumed rounds.

## Workspace and ownership

Before production edits, inspect actual repository and host capabilities and choose separate item
workspaces, using worktrees or isolated copies as appropriate. Document-only assignments may share
the project tree with disjoint ownership and helper-created date-prefixed records. Tasks within an
item may share its workspace only with compatible behavior, disjoint writes, and safe check resources.

Identify the required starting content: revision when present, staged and unstaged changes, untracked
files, deletions, and binary content. Retain a content-identifiable baseline and distinguish user-owned
starting content from batch-owned edits. A clean checkout of HEAD alone may omit required inputs.
Record workspace paths, ownership, baseline identity, dependencies, and the means of reconstructing
the item delta. Check content identity using available repository tools or retained manifests/snapshots,
including paths, bytes and relevant modes; a branch name or plain status listing is insufficient.
Keep scratch material in the location permitted by project instructions.

Do not move, stash, overwrite, clean, or commit unrelated changes to obtain a baseline. Commit only
when project authorization permits it. No-commit work retains uncommitted edits and transfers the
attributable item delta relative to its baseline, including binaries and deletions. Never substitute
a whole workspace copy that would overwrite destination changes. If required inputs or ownership
cannot be established, defer affected work. Without isolation, proceed sequentially only where unfinished
edits can remain safely separated; otherwise stop the batch.

Persist each assignment's dispatch intent, owner, responsibility, scope, dependencies, baseline, slot grant,
and any charged round before starting it. Record the returned status and owning evidence references
before releasing its write scope. Stop old writers before reassignment, deferral, or integration;
a message requesting a stop is not proof of cessation. Only the parent grants nested assignments
from the global pool. No surviving worker may retain an unrecorded claim on a scope.
Apply the shared [worker lifecycle](../../../references/worker-lifecycle.md)
after each result and before batch closeout or handoff. Record result status, coordinator
acceptance, and host lifecycle evidence separately; idle teammates still require a reuse
or shutdown decision. Reconcile granted children as well as direct workers.

## Incremental reporting

Include reporting timing in each assignment: return the shared assignment result to the parent
as soon as the bounded assignment completes, blocks, or ends incomplete, before waiting or ending.
Use the host's completion notification or message mechanism; workers do not wait for sibling
assignments or batch consolidation and do not edit the shared queue or batch handoff.

The coordinator handles available results individually as they arrive, rather than waiting for
all dispatched workers. After any in-progress serialized operation reaches a safe boundary,
inspect the result and its evidence, persist the assignment outcome and recovery references,
and, when the item's state, blocker, or next action changed, update its row in `docs/lusona/work.md`
before further dispatch or waiting. Do not rewrite an unchanged row. Keep the row concise:
truthful lifecycle state, current blocker or next action, and owning evidence link.
If evidence is missing, record the pending verification or missing report as the next action;
do not infer success from a completion notification. Refresh the current batch handoff's affected
pointers so it remains resumable, without copying task evidence or adding an activity log.

A worker's `complete` describes its assignment, not the whole queue outcome. Keep remaining
implementation, integration, checks, review, acceptance, or delivery visible in the row. Apply
the normal state criteria and completion gates; close and archive an outcome once those gates
pass, even while unrelated batch items continue. Reporting a result does not itself integrate
changes or release write ownership or host capacity. Apply the existing integration and worker
lifecycle procedures separately. On hosts without asynchronous notifications, collect available
results at bounded assignment boundaries; do not promise immediate background updates.

## Serialized integration

When integration uses Git branches, apply the shared
[linear integration procedure](../../../references/commits.md#linear-integration).
Rebasing changes identities: reconcile recorded baselines, candidate content, and affected
verification/review evidence before resuming the steps below.

1. Stop relevant writers and identify the source baseline, exact item delta, current destination
   baseline, and required dependencies. Check destination drift and attribution before applying.
   Record integration intent, candidate location, expected content identities, and recovery method
   before mutation. Preserve the source until acceptance and evidence recording are confirmed.
2. Materialize one attributable candidate at a time. Prefer holding a candidate outside the accepted
   destination until checks pass where supported. Record the phase as `candidate materialized` with
   its actual identity, including uncommitted content. Keep intent and actual result distinguishable.
3. Run required verification and fresh independent review on the resulting candidate. Give reviewers
   the actual diff, governing definition/architecture, and check evidence without implementer
   conclusions. Record evidence in its owning document and link its candidate identity from the
   integration record; then record `evidence collected`. Unrun checks and unavailable review block Done.
4. For an external candidate, record `promotion intent` with the accepted destination's pre-transfer
   identity, expected post-transfer identity matching the reviewed candidate, attributable delta, and
   recovery inputs. Keep relevant writers stopped; immediately recheck destination drift before
   transferring that delta. On drift, reconcile the candidate and affected evidence before proceeding.
   After transfer, record `promotion materialized` and compare the actual destination content identity
   with the reviewed candidate. External candidate materialization alone is never destination promotion.
5. Before recording `accepted`, require the actual destination to match the reviewed candidate and
   required evidence to cover final relevant content. For a candidate already materialized directly in
   the destination, compare that destination identity without a second transfer. A later integration
   requires assessing affected prior behavior: rerun affected checks and obtain review where reviewed
   behavior changed. Do not repeat unrelated unchanged reviews. Drift invalidates affected evidence;
   reconcile it before acceptance.
6. For failure, retain candidate and evidence and use the item's repair budget. Hold the failed candidate
   outside the accepted destination, or restore only its attributable changes after proving that no
   other writer's changes will be lost. Record `deferred` when deferring and identify the accepted
   destination content. If safe restoration cannot be established, stop the batch. Retain prior
   completion evidence when a later regression occurs; charge corrective attempts to the introducing
   item. If cause/ownership is uncertain, investigate within an identified responsible item's budget
   or defer affected work.

An intent is not evidence of transfer, and missing result metadata is not permission to apply again.
Recover candidate materialization and destination promotion separately. Compare each operation's actual
target with its recorded pre-transfer and expected post-transfer identities. A retained external candidate
proves nothing about promotion. If the destination matches the promotion's expected result, recover that
phase and validate evidence without retransferring; if it still matches the pre-transfer identity, promote
only after reconfirming ownership, candidate evidence, and drift. If content matches neither expected
state, reconcile drift before transfer or restoration; stop if attribution remains unsafe. Never blindly
replay a patch.

## Finite repair rounds

The initial bounded attempt is followed by at most two corrective rounds per item unless the
user supplies another allowance. The counter spans all responsibilities and owners. A failed implementation
outcome, required check, review, integration, or unresolved bounded investigation needing another
approach starts a round. Before dispatch, persist its charge, triggering finding reference, declared
bounded correction/experiment set, owners, and expected checks/review. Increasing the allowance
requires explicit new authority; changing delegates, responsibilities, or labels does not reset it.

One round covers that declared set and its checks/review; independent fixes within it may run
concurrently under the same global cap. A failed round needing a different correction/experiment,
including a new actionable failure found during verification, consumes the next round. Do not append
unbounded fixes to an open round. Diagnostic investigation of its declared failure belongs to that
round. Ordinary task-local TDD red/green steps are not failed batch attempts; an unsuccessful task
outcome requiring a new approach is.

Initial investigation must have a bounded question, finite experiments, and a stopping condition.
If unresolved, another approach costs a round from the same item. Missing consequential decisions
or authority cause immediate deferral, not speculative rounds. Environment failures prevent completion;
a changed environment may justify a charged retry, never an unbounded loop.

An interrupted round remains charged and resumes its declared correction set only where evidence
supports safe continuation. Cancel a reserved charge only with evidence that no work was dispatched;
retain that cancellation and evidence reference. Uncertain progress remains charged. Exhaustion defers
the item and unfinished dependents, retaining attempts, findings, and next action in owning records.
On a requested suspension, stop dispatch, reconcile active writers, and checkpoint the reserved intent,
charge, actual dispatch status, and retained candidate before handing off. Suspension does not reset rounds.

## Deferral, resumption, and reporting

Before continuing past an unfinished item, stop/reconcile its writers, preserve source changes and
baseline identities, reconcile candidate transfers, and record reason, dependent exclusions, repair
consumption, and next action. Release ownership only after safe isolation. Deferral is a scheduling
flag, not Done and not a queue lifecycle reset. Unfinished content must not become an independent
item's accidental input. If isolation or restoration is unsafe, stop all affected continuation.

For an explicitly selected continuation:

1. Load fixed membership, authorization and constraints, TDD/completion references, dependency
   reconciliation, limits, assignments, open rounds, integration phases, and current handoff.
   Recheck authority against current user instructions; do not enlarge selection or reset budgets.
2. Inspect actual agents, workspace content, destination, and returned artifacts. Reattach to or stop
   surviving writers before redispatch. Saved assignment state does not prove completion or cessation.
   If the host cannot establish ownership safely, stop affected work and report the exact blocker.
3. Recover interrupted transfers as above. Reuse completed checks and decisions only when their inputs match;
   preserve valid evidence and link it. Refresh effective host capacity, retaining the requested cap
   and accounting for surviving workers and parent occupancy. Sequential fallback is allowed where
   safe but does not replace required independent review.
4. Update the one current handoff and dispatch the next eligible bounded assignment. Unresolved
   deferrals remain excluded until the recorded blocker is actually resolved within authority.

At stop or completion, report completed history links, deferred/unfinished queue and evidence links,
unresolved decisions, and concrete next actions. Distinguish completion of every selected outcome,
selection exhausted with deferrals, interruption with resumable work, and inability to continue safely.
Persist exact recovery inputs and ownership before handing off; do not duplicate task evidence here.
