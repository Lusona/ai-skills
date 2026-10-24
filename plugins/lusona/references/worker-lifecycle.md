# Worker lifecycle

Coordinators read after each assignment result and before closeout or handoff.

The coordinator owns lifecycle decisions for dispatched workers, including coordinating
any granted children. After each result:

1. Preserve the result and recovery evidence, inspect it against the assignment, and decide
   acceptance separately from the worker's status. Missing checks or material contradictions
   require follow-up; a status label alone is insufficient evidence.
2. Either assign concrete authorized follow-up work with explicit ownership, or release the
   worker through the host's supported shutdown/close mechanism. Do not leave a persistent
   teammate idle merely in case more work appears. Reuse must preserve required reviewer independence.
3. Confirm termination or closure through host evidence. An idle notification, final report,
   or sent shutdown request does not prove shutdown. Track pending or rejected shutdown and
   resolve the stated reason; do not report capacity released before the host confirms it.

Inspect the actual agent type and available controls. For Claude Code teammates, request
shutdown and wait for acknowledgment or host-confirmed termination. Ordinary subagents may
end automatically; observe the host result instead of inventing a team cleanup operation.
For other hosts, use the exposed lifecycle controls. If shutdown or confirmation is unavailable,
report the limitation and surviving worker identity; do not claim cleanup or delete transcripts,
workspaces, or team directories as a substitute. Apply the host's actual capacity accounting.

At batch completion, deferral, interruption, or handoff, reconcile every dispatched worker
and granted child. Preserve unfinished work before shutdown, and record surviving workers,
ownership, and pending lifecycle actions in the existing handoff when one is needed.
Assignment completion, write-ownership release, and host-capacity release are separate facts.
