# Work queue

States: Ideas → Ready → Doing → Review → Done. Ready does not authorize execution.

## Active queue

| Item / change | State | Completion condition | Current blocker or next action |
| --- | --- | --- | --- |
| Add `setup` and `init-queue` to the contract inventory of `scripts/check_contract.py` (K1, K3), which lists the skills and helper commands at baseline `34186da` and therefore does not guard the two additions ([evidence](specs/20261112-add-setup-skill.md#evidence)) | Ideas | Not defined; needs a TDD selection | User decides whether to pursue |
| On Codex CLI, `specify` implemented a request worded "Change greet.py so that ..." and did not name the source of the TDD level (trial X2-t1, 3 failed checks; the request worded as a definition passed in X2-t2); decide whether the routing rule in `specify` or the source rule in `tdd.md` needs a change or a conformance scenario ([evidence](evidence/2026-11-12-setup-skill/README.md)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| State that the TDD gate covers refactoring, and give the notes path its `docs/lusona/` prefix in retention ([findings](specs/20261109-loop-conformance-suite.md#open-items-and-limits)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Repeat the loop conformance run on an unchanged plugin to measure run-to-run variation ([limits](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#limits)) | Ideas | Not defined; about $40 of Claude-reported spend per run | User declined for now on 2026-11-09 |
| Claude Code investigated the `investigate-bug` defect itself in 5 / 5 trials instead of delegating (C11); decide whether the delegation rule, the scenario (cause found with one command), or the check should change ([interpretation](evidence/2026-11-09-loop-conformance-pilot/runs/003/README.md#interpretation)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Claude Code edited the project `docs/lusona/README.md` without asking in 2 of 5 `old-records` trials (C8 3/5); decide whether a rule on unrequested edits to project records is needed ([run](evidence/2026-11-11-rewrite-suite-run/README.md)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Unify record-owner and handoff terms; remove remaining retention and closeout duplicates ([findings](specs/20261109-consolidate-restated-rules.md#findings-outside-this-scope)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |
| Add the missing next-action items to two skills (audit item P8): `review` has none for a missing input (`skills/review/SKILL.md:45` asks about an ambiguous scope) and `batch` has none for a complete scope (`skills/batch/SKILL.md:110`, outcome "all selected complete") ([gaps](../skill-audit.md#13-known-gaps-in-enforcement)) | Ideas | Not defined; needs a spec and a TDD selection | User decides whether to pursue |

Completed outcomes are recorded in [history](history/2026-11-week-02.md) and earlier
completions in [2026-11-week-01](history/2026-11-week-01.md), [2026-10-week-05](history/2026-10-week-05.md) and
[2026-10-week-04](history/2026-10-week-04.md).

## Icebox

No parked work.
