# Work queue

States: Ideas → Ready → Doing → Review → Done. Ready does not authorize execution.

## Active queue

| Item / change | State | Completion condition | Current blocker or next action |
| --- | --- | --- | --- |
| State that the TDD gate covers refactoring, and give the notes path its `docs/lusona/` prefix in retention ([findings](specs/20261109-loop-conformance-suite.md#open-items-and-limits)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Repeat the loop conformance run on an unchanged plugin to measure run-to-run variation ([limits](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#limits)) | Ideas | Not defined; about $40 of Claude-reported spend per run | User declined for now on 2026-11-09 |
| Claude Code investigated the `investigate-bug` defect itself in 5 / 5 trials instead of delegating (C11); decide whether the delegation rule, the scenario (cause found with one command), or the check should change ([interpretation](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#interpretation)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Claude Code edited the project `docs/lusona/README.md` without asking in 2 of 5 `old-records` trials (C8 3/5); decide whether a rule on unrequested edits to project records is needed ([run](evidence/2026-11-11-rewrite-suite-run/README.md)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| State the `status` and `explore` exception in the delegation sentence of `README.md` (line 154) and its four translations, and add a changelog line for the change ([notes](notes/selective-delegation-for-status-and-explore.md), [history](history/2026-11-week-02.md#2026-11-11--selective-delegation-for-status-and-explore)) | Ideas | Not defined; needs the user's authorization and a TDD selection | User decides whether to pursue |
| Unify record-owner and handoff terms; remove remaining retention and closeout duplicates ([findings](specs/20261109-consolidate-restated-rules.md#findings-outside-this-scope)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |

Completed outcomes are recorded in [history](history/2026-11-week-02.md) and earlier
completions in [2026-11-week-01](history/2026-11-week-01.md), [2026-10-week-05](history/2026-10-week-05.md) and
[2026-10-week-04](history/2026-10-week-04.md).

## Icebox

No parked work.
