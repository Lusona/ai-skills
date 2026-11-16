# Claude task lifecycle regression investigation

Created: 2026-11-15
Updated: 2026-11-15

## Report and scope

User reports more shells and subagents remaining after work since the 3.0.0 rewrite; clarified that the observation is in Claude Code background tasks / agent team. No affected session was identified. Investigation only; no process termination or production fix authorized.

## Evidence and findings

- Compared pre-rewrite baseline `34186da` with current HEAD `d43c44c` and working text. Commit `ee7fa2a` merged worker-lifecycle.md into references/delegation.md. Main shutdown, confirmation and survivor-reporting obligations remain at lines 131–147.
- Ownership ambiguity: old worker-lifecycle lines 7–8 covered the responsible agent, including granted children. Current delegation line 135 says “leaves you dispatched,” despite line 133 covering inherited and reassigned leaves.
- Automatic exit assumption strengthened: old wording “may end automatically” became “ends by itself” for a Claude Code agent outside a team (line 140). This source change is confirmed; its effect on the reported survivors is unproven.
- No explicit background-shell inventory/cleanup requirement found in baseline or current instruction prose. Stopping owned work before shutdown exists, but does not define task-completion handling for shells.
- evals/loop-conformance/checks.py:238–260 checks reviewer and worker launches. No survivor/shutdown criterion found in checks, scenarios or rubric. Harness timeout cleanup does not prove successful-run descendant cleanup.
- Local repository transcript inventory: latest two root sessions are 1564f1fc-3741-438b-956b-a2ce49e510bc (Nov 13) and 3b0833a1-da63-49f5-905c-e466b7684350 (Nov 12). Structured tool-call inspection counted respectively 20 and 11 Agent calls, 271 and 108 Bash calls; no explicit run_in_background flag. These counts do not establish active survivors, nor that either is the user’s affected session. Tool-result text includes asynchronous agent-start notices. No live task-state evidence collected.
- Diagnostic leaf `/root/lifecycle_history`, model gpt-6.1-sol, independently compared source history and evaluation coverage. No writes or child agents.

## Conclusion and next action

The rewrite did not remove agent cleanup policy. Two wording changes may weaken its execution, and shells lack an explicit completion rule. Runtime cause remains unconfirmed. No fix, behavior trial or process termination performed.

Next: user identifies one affected session/task, or supplies its current task-list entries. Coordinator then traces each reported survivor from creation through result, follow-up/shutdown and host confirmation, distinguishing actual running tasks from retained UI entries. Do not infer a leak from missing shutdown calls alone.

## Affected-session evidence supplied later

Matched the user’s C1 measurement assignment to the svc-lusona.ai session `459b8507-f0c5-4600-91aa-63437ec82491` and its measurement-leaf transcript. The leaf called SubagentHandback at 2026-11-16 06:32:30 UTC; its tool result confirmed delivery to the caller. The parent then received a task notification whose status was completed but whose summary said the agent was waiting on its own background work. The note explicitly said background work was still running and the agent could resume when it finished. No subsequent message to that leaf was found in the inspected parent transcript.

This establishes report delivery without task quiescence for this example. It does not prove an OS process leak or identify which background operation remained alive. Earlier unmatched tool-call counts are not treated as live processes: transcript structure can omit or move results. The excerpt’s completed-command notifications were insufficient on their own, but the parent host notification confirms unfinished child work at handback.

Next bounded investigation: identify the remaining background task from host task state, determine whether it is still required or stale, and verify its termination before retiring the leaf. Candidate correction: explicit shell/background-task reconciliation before handback, and coordinator handling of completed notifications that still report owned background work. No fix or shutdown performed here.

## Definition handoff

The requested correction is now defined in [reconcile task lifecycle](../specs/20261115-reconcile-task-lifecycle.md). That spec owns scope, criteria, targeted TDD and the next action. The exact surviving operation remains unidentified; the known completion-boundary failure is sufficient to define the correction.
