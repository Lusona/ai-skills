# Run 002 — second pilot on the committed suite, 2026-11-09

Owner: [spec 20261109-loop-conformance-suite](../../../../specs/20261109-loop-conformance-suite.md).
Topic and first run: [README](../../README.md).

## Scope and provenance

- Authorized by the user on 2026-11-09: judge calibration rerun and 6 actor trials
  (Claude Code and Codex × `greeting`, `explore-save`, `authz-change`), 1 trial each, with judging.
  Excluded from any reference.
- Suite and plugin: commit `42b8145`; plugin 2.0.5. Hashes in `<host>/condition.json`.
- Claude Code 2.1.321, `claude-opus-5-5`, high effort, project-only settings, no MCP servers,
  Bash sandbox, `CLAUDE_CODE_SHELL=/bin/bash`, `--permission-mode dontAsk`. Codex CLI 0.167.0,
  `gpt-6.1-sol`, medium effort, workspace-write sandbox, global `AGENTS.md` loaded (hash recorded).
- Judge `claude-fable-5-2`, medium effort. Per-turn timeout 1,200 s.
- Artifacts: `report.md`, `report.json`, per trial `trial.json`, `computed.json`, `judged.json`,
  `judge-calibration.md`. `raw.zip` (transcripts, judge prompts and outputs) is git-ignored.

## Observations

| Host | Scenario | Seconds | Reported usage | Checks |
| --- | --- | --- | --- | --- |
| Claude Code | `greeting` | 2 | $0.0975 | C4 pass |
| Claude Code | `explore-save` (2 turns) | 89 | $0.5524 | C1 pass, C2 fail, C8 pass |
| Claude Code | `authz-change` | 82 | $0.6980 | C1, C6, C7, C8, C9 pass; C10 fail |
| Codex | `greeting` | 11 | 52,955 input tokens (44,800 cached), 194 output | C4 pass |
| Codex | `explore-save` (2 turns) | 98 | 294,261 input (264,448 cached), 3,518 output after turn 2 | C1, C2, C8 pass |
| Codex | `authz-change` | 196 | 929,983 input (876,672 cached), 4,661 output | C7, C8, C10 pass; C1, C6, C9 fail |

- Judge: 4 calls, $0.94 in total. Calibration: 16 cases, agreement 16 / 16, $2.83.
- No trial read evaluator material, made a commit, or changed the suite's repository.
- Claude Code `explore-save`: the actor ran a timing probe inside the workspace and saved
  `docs/lusona/evidence/2026-11-09-csv-report-timing.md`. Its command to run the record helper
  used shell variables for the paths and was refused (“don't ask mode”). It then wrote the note
  by hand to `notes/tally-report-storage-options.md`. The judge graded the note's content as pass.
- Claude Code `authz-change`: the actor created the spec with the helper, added the queue row,
  wrote the test first, changed `lists.py` itself, and launched one reviewer subagent
  (`general-purpose`, described “Independent review of delete authz fix”). Workers: 1.
- Codex `authz-change`: the rollout records two `spawn_agent` calls, one with a review task
  name. The actor added a history entry and left `docs/lusona/work.md` unchanged. Its final
  reply is two sentences with no Result, Evidence, or Next action label.

## Interpretation

- Capture, grading, judging, and reporting work on the committed code on both hosts.
- Harness defect (open): under `dontAsk`, Claude Code refuses a sandboxed command whose write
  target it cannot resolve before running. That refusal preceded the misplaced note, so the
  Claude Code C2 fail is not clean behavioral evidence.
- Rule-text gap (supported by two runs): when the helper is not used, the actor follows
  `plugins/lusona/references/retention.md:59`, which names `notes/<change-slug>.md` without the
  `docs/lusona/` prefix.
- Check defect (open): C6 fails when the actor closed the item out to history and left no
  queue row. The rules allow a spec's work item to be a historical completion entry.
- Check design (open): C10 requires both a delegated worker and a separate reviewer. Claude
  Code satisfied independent review and did not delegate the implementation; one result hides that.
- Codex `authz-change` C1 and C9 fails are observations of the reply format, not harness defects.

## Limits

One trial per cell. Nine of twelve scenarios have never run. Results must not be compared
across hosts. Codex cost is not reported.
