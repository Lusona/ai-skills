# Start and resume prompts

Read before asking the user to resolve a batch's selection, authority or TDD level, and before giving guidance on starting or resuming a batch.

## Starting a batch

- Ask for the exact queue titles or IDs, the authorized scope, and an explicit TDD level or its existing source.
- Do not promise background execution. The host's tools determine concurrency and session continuity.

Example for named items:

> Use Lusona's batch skill for only the current queue items "Invitation expiry" and
> "Expired invitation message". Authorize definition, necessary architecture, implementation, and independent review. Resolve routine details within existing project
> decisions; defer consequential gaps. Use targeted TDD for the expiry boundary and expired
> invitation behavior. Do not commit, push, or publish.

Example for the whole Active queue with 5 assignments:

> Use Lusona's batch skill for all current queue items through implementation and
> independent review, using each item's recorded TDD and completion conditions. Resolve
> routine details within existing project decisions; defer consequential gaps or missing
> TDD. Request five concurrent assignments subject to host capacity. Do not commit, push,
> or publish. Exclude newly discovered work.

## Resuming a batch

- Change records and ADRs keep their requirements and evidence. Existing execution records stay valid.
- Continue a recorded batch only on an explicit request that names its record.
- Use the actual batch record path from the earlier run.
- Resuming keeps the recorded authority. It does not enlarge the selection or reset repair budgets.
- In Claude Code, `/lusona:batch` selects the skill. In Codex, use its skill interface.

Example:

> Use Lusona's batch skill to resume docs/lusona/batches/invitation-updates.md.
> Continue its remaining authorized scope, recorded TDD, and remaining repair budget.
> Reconcile the current handoff and active ownership before dispatching work.
