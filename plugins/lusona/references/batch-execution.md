# Batch execution

Read for explicitly authorized unattended batch work, as coordinator or assigned delegate.

These exceptions apply when the user explicitly authorizes unattended work on a fixed
selection of queue outcomes. Record the selection, decision authority, applicable TDD,
completion conditions, concurrency limit, and finite per-item repair budget before execution.
Selecting work for discussion or planning alone is not batch implementation authority.
Apply these rules to each delegated skill's questions, queue handling, delegation, and
next action; other contract and repository requirements remain binding.
After each result, apply the [work loop](../README.md#work-loop) to each affected outcome
and schedule its next eligible bounded action. Do not synchronize items into workflow phases;
shared dependencies, ownership, and required review still determine eligibility.

- The parent coordinator may settle routine details using existing project decisions and
  documented conservative assumptions within delegated authority. Record the basis and
  authority of those decisions; do not present them as direct user answers. Reconcile related
  definitions before accepting shared assumptions or making dependent architecture decisions.
  Reconcile architecture outputs before dependent implementation decisions or assignments. Independent settled work can
  advance without waiting for the whole batch; disjoint files do not prove independence.
- Definition, architecture, and implementation delegates return potential dependencies,
  shared assumptions, unresolved shared behavior, and newly discovered coupling to the parent
  rather than settling them locally, and record the basis of delegated routine decisions.
  Each shared decision has one owner with all affected definitions as inputs; architecture
  runs in parallel only across compatible scopes. An unresolved potentially shared concern
  blocks affected design and implementation, not unrelated reconciled work.
- For a missing consequential decision, authority, or applicable TDD policy, return the gap
  to the parent. Record the question and defer affected work and its dependents; continue
  eligible independent work. Delegates do not start user interviews. The parent reports
  deferred questions for resumption. Host approval rules still apply, and unanswered
  requests never count as consent. Unset TDD still permits independent definition and planning.
- There is one parent coordinator and one concurrency pool across responsibilities and nested work,
  capped by host capacity. A delegated skill performs its assigned role and returns evidence
  to the parent; it does not independently start another assignment, spawn more agents, or manage
  shared state. Additional delegation requires a parent grant from that same pool. The parent
  alone updates queue/shared handoffs and integrates results. Workers may create records
  within their assigned ownership using the helper and must report naming conflicts.
  Review delegates remain read-only; the parent schedules authorized repairs separately.
- Workers report each assignment result as soon as it is available. The parent applies
  [incremental reporting](../skills/batch/references/execution.md#incremental-reporting),
  persisting the result and recovery pointers before further dispatch or waiting, and updating
  the item's `docs/lusona/work.md` row only when its state, blocker, or next action changed.
  Queue updates and eligible per-item closeout do not wait for batch-wide consolidation.
- Multiple selected items may be Doing or in Review concurrently. A deferred item keeps its
  truthful queue state and blocker but releases execution capacity after its writers stop
  and unfinished changes are safely isolated. Do not continue on a baseline contaminated by
  unfinished work; stop if safe attribution or isolation cannot be established. New coupling
  stops affected work for reconciliation before rescheduling.
- Repairs and investigations obey the recorded per-item budget across assignments and
  resumptions; changing agents or roles does not reset it. Exhaustion defers affected work.
  The parent proceeds through authorized work without new role approvals and closes an item
  only when its completion conditions, required checks, and independent review pass. Explicit
  human acceptance and delivery requirements remain binding. Report unavailable independent
  review rather than substituting a persona change.

Keep evidence in its owning change record, ADR, or existing separate plan; batch coordination references those records.
Existing commit authority and repository restrictions apply, with staging and commits owned
by the parent after verified integration. Batch authorization does not grant publication,
deployment, or other external actions beyond the user's explicit scope.
