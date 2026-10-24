# Batch use

Read when giving guidance about starting or resuming a batch.

Use [batch](../skills/batch/SKILL.md) to start or resume explicitly authorized
unattended work on a fixed selection of current queue items. Start with exact queue titles
or IDs, authorized scope, and an explicit TDD policy or its existing source. For example:

> Use Lusona's batch skill for only the current queue items "Invitation expiry" and
> "Expired invitation message". Authorize definition, necessary architecture, implementation, and independent review. Resolve routine details within existing project
> decisions; defer consequential gaps. Use targeted TDD for the expiry boundary and expired
> invitation behavior. Do not commit, push, or publish.

“All current queue items” selects the Active queue and excludes Icebox. Explicitly reactivate
parked outcomes before including them. Batch deferral alone does not park an item.

To select the whole active queue and request five assignments:

> Use Lusona's batch skill for all current queue items through implementation and
> independent review, using each item's recorded TDD and completion conditions. Resolve
> routine details within existing project decisions; defer consequential gaps or missing
> TDD. Request five concurrent assignments subject to host capacity. Do not commit, push,
> or publish. Exclude newly discovered work.

The default requested ceiling is four assignments, or five when selected, reduced by host
capacity including parent occupancy. Assignments and nested grants share that ceiling under
[Batch execution](batch-execution.md). Available host tools determine concurrency and session
continuity; the skill supplies no background execution guarantee.

The parent owns `docs/lusona/batches/<batch-slug>.md`, created from the
[batch template](../templates/batch.md), and the queue and shared handoffs. Change records and ADRs retain their requirements and evidence; existing split records remain valid. Continue a recorded batch explicitly:

> Use Lusona's batch skill to resume docs/lusona/batches/invitation-updates.md.
> Continue its remaining authorized scope, recorded TDD, and remaining repair allowance.
> Reconcile the current handoff and active ownership before dispatching work.

Use the actual batch path from the prior run. In Claude Code, `/lusona:batch` selects
the skill; in Codex, use its skill UI. Resumption follows the skill's linked execution
reference and preserves recorded authority; it does not expand selection or reset budgets.
