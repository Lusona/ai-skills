# Work queue

States: Ideas → Ready → Doing → Review → Done. Ready does not authorize execution.

## Active queue

| Item / change | State | Completion condition | Current blocker or next action |
| --- | --- | --- | --- |
| State that the TDD gate covers refactoring, and give the notes path its `docs/lusona/` prefix in retention ([findings](specs/20261109-loop-conformance-suite.md#open-items-and-limits)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Repeat the loop conformance run on an unchanged plugin to measure run-to-run variation ([limits](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#limits)) | Ideas | Not defined; about $40 of Claude-reported spend per run | User declined for now on 2026-11-09 |
| Direct completion checkpoint, examples, mechanical validation and decision-point checks ([spec](specs/20261109-direct-instruction-checkpoints.md) missing from disk and history; [run 007](evidence/2026-11-09-loop-conformance-pilot/runs/007/README.md)) | Review | AC1–AC5 and independent review pass | Superseded on 2026-11-10 by user decision: folded into the standard skill template item below, which removes its hooks and validator. Closes with that item |
| Standardize all 14 skills on one template with an inline every-task rule block, move other core rules into trigger-based references, and remove the uncommitted hooks and validator ([spec](specs/20261110-standard-skill-template-and-inline-rules.md)) | Ideas | AC1–AC13 verified, checks pass, independent review, one C9 suite run reported, user accepts the run result | Architect decision (ADR) on A1–A5; implementation needs user authorization; U4 (run budget) at the suite run |
| Claude Code investigated the `investigate-bug` defect itself in 5 / 5 trials instead of delegating (C11); decide whether the delegation rule, the scenario (cause found with one command), or the check should change ([interpretation](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#interpretation)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Unify record-owner and handoff terms; remove remaining retention and closeout duplicates ([findings](specs/20261109-consolidate-restated-rules.md#findings-outside-this-scope)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |

Completed outcomes are recorded in [history](history/2026-11-week-02.md) and earlier
completions in [2026-11-week-01](history/2026-11-week-01.md), [2026-10-week-05](history/2026-10-week-05.md) and
[2026-10-week-04](history/2026-10-week-04.md).

## Icebox

No parked work.
