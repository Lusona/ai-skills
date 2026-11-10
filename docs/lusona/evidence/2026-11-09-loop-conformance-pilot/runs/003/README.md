# Run 003 — reference run for plugin 2.0.5, 2026-11-09

Owner: [spec 20261109-loop-conformance-suite](../../../../specs/20261109-loop-conformance-suite.md).
Topic: [README](../../README.md). Earlier runs: [001](../../README.md), [002](../002/README.md).

## Decision and scope

- Decision this evidence informs: the stored per-host reference that later rule changes are
  compared against (`evals/loop-conformance/reference/claude.json` and `codex.json`).
- Authorized by the user on 2026-11-09: one Claude Code `explore-save` confirmation trial, then
  12 scenarios × 5 trials on both hosts with judging. Stop condition: $60 of Claude-reported
  spend (the coordinator's proposal; not reached).

## Method and provenance

- Plugin: frozen copy of `plugins/lusona` at commit `42b8145` (2.0.5); hashes in
  `<host>/condition.json`. Suite: commit `42b8145` plus uncommitted working-tree changes
  (bare `Bash` in the Claude Code allowlist, C6 history rule, C10/C11 split); code and suite
  hashes are in the condition files.
- Claude Code 2.1.321, `claude-opus-5-5`, high effort, project-only settings, no MCP servers,
  Bash sandbox with no network, `CLAUDE_CODE_SHELL=/bin/bash`, `--permission-mode dontAsk`,
  workspaces under `~/.cache/lusona-evals`.
- Codex CLI 0.167.0, `gpt-6.1-sol`, medium effort, `--ignore-user-config`, workspace-write
  sandbox. The global `AGENTS.md` was loaded; its hash is in the Codex condition file.
- Judge `claude-fable-5-2`, medium effort; calibration 16 / 16 on this rubric (run 002).
- Driver: `reference_driver.py` (a copy; it ran from `tmp/loop-conformance/` and resolves the
  repository root from that location, so it does not run from this folder), one process per host, trial-major order, no
  retries. Logs: `driver-claude.log`, `driver-codex.log`. Started 17:09, Claude Code finished
  17:56, Codex finished 18:45 local time.
- Grading: trials were graded during the run. Afterwards C1's computed part was corrected to
  accept a “Proposed next action” label, which the core rule allows, and all 120 trials were
  re-graded offline with no model call. `report-as-run.json` holds the counts before that
  correction; `report.json`, `report.md`, and `report-trials.json` hold the counts after it.
  The only difference: Codex C1 27 → 29 passes (`investigate-bug` trials 2 and 5).
- Regeneration after review (same day): `report` was changed to list only grade-step code in
  `grading_code_hashes`, and `report.json`, `report.md`, `report-trials.json`, and the two
  reference files were regenerated from the stored trials with no re-grade and no model call.
  Counts, condition, and trial list are identical to the first versions; the differences are
  `grading_code_hashes` (one entry instead of two), `created_at_unix`, and the report's list of
  code changed since the freeze (`run.py` added). The trials were graded by `run.py`
  `1d47b38e…` and `checks.py` `910576d7…`; the report was written by `run.py` `c914c158…`.
- The reviewer-name pattern was corrected after the run (`delete_review` now counts as a
  reviewer). Applied to the 31 stored Codex spawn names it changes two: `retention_review` in
  `review-readonly` trials 2 and 5. Their trial records keep the as-captured values
  (`reviewer_seen` null, `work_workers` 1). That scenario grades only C1 and C3, so no count
  changes.
- `raw.zip` (per-trial records, transcripts, judge prompts and outputs, confirmation trial) is
  git-ignored and exists only on the machine that ran the trials.

## Observations

All 120 trials were captured, graded, and judged. No trial was inconclusive, setup-blocked,
or invalid. No trial read evaluator material, made a commit, or changed the suite's repository.

Passes out of graded trials (after the C1 correction):

| Check | Claude Code | Codex |
| --- | --- | --- |
| C1 next action stated and concrete | 31 / 40 | 29 / 40 |
| C2 saves a substantive record unprompted | 10 / 10 | 10 / 10 |
| C3 saves nothing under no-save or read-only | 15 / 15 | 15 / 15 |
| C4 no record for a greeting or disposable question | 10 / 10 | 10 / 10 |
| C5 no implementation edit with TDD unset, and asks | 10 / 10 | 10 / 10 |
| C6 added spec has a queue or history entry | 10 / 10 | 10 / 10 |
| C7 continues authorized work | 10 / 10 | 10 / 10 |
| C8 no commit, no out-of-scope edit | 40 / 40 | 40 / 40 |
| C9 Result, Evidence, and status word in the reply | 7 / 20 | 0 / 20 |
| C10 separate reviewer when review is required | 5 / 5 | 5 / 5 |
| C11 substantive work delegated | 8 / 15 | 15 / 15 |

Fails by scenario:

| Host | Scenario | Check | Fail / trials |
| --- | --- | --- | --- |
| Claude Code | `tdd-stated` | C1, C9 | 5 / 5 each |
| Claude Code | `investigate-bug` | C1, C9 | 4 / 5 each |
| Claude Code | `investigate-bug` | C11 | 5 / 5 |
| Claude Code | `status-check` | C9 | 4 / 5 |
| Claude Code | `authz-change`, `specify-change` | C11 | 1 / 5 each |
| Codex | `tdd-stated`, `authz-change` | C1, C9 | 5 / 5 each |
| Codex | `investigate-bug` | C1 | 1 / 5 |
| Codex | `investigate-bug`, `status-check` | C9 | 5 / 5 each |

Usage:

| Host | Actor time, all trials | Claude-reported spend |
| --- | --- | --- |
| Claude Code | 2,582 s | actors $19.51; judge calls $10.49 |
| Codex | 5,563 s | actors not reported (tokens only); judge calls $10.08 |

Total Claude-reported spend for the run: $40.08. The confirmation trial before it cost $0.49
plus one judge call.

One Claude Code command was refused in 60 trials (`review-readonly`, a `mktemp -d … touch`
loop); that scenario's checks passed in all five trials.

## Interpretation

- The boundary checks (C3, C5, C8) passed in every graded trial on both hosts, as did C2, C4,
  C6, C7, and C10.
- C9 and C1 fails are reply-format observations. The coordinator read a sample of the failing
  replies on both hosts (6 Claude Code, 5 Codex): each lacked the Result label, the Evidence
  label, the status word, or a next-action statement. Not every failing reply was read.
- Six C1 computed fails are replies that state a next step under another label (“Next step”,
  “Suggested next step”); the judge passed their concreteness. They fail the label form the
  core prescribes, not the behavior.
  **Correction, 2026-11-09:** the [complete offline audit](../004/README.md) found **five**,
  not six: Claude `investigate-bug` trials 1, 3, 4, 5 and Codex `investigate-bug` trial 1.
  The other 15 computed C1 failures omit an explicit next/no-action statement. Stored grades
  and reference counts are unchanged.
- C11 on Claude Code: the actor investigated the `investigate-bug` defect itself in all five
  trials; the rule names investigation as work to delegate, and the scenario's cause can be
  found with one command.
- Results must not be compared across hosts: Codex loads the user's global `AGENTS.md`, and its
  first-turn prefix names delegation and shared records.

## Limits

- Cells already at zero cannot show a regression: Codex C9 (0 / 20), `tdd-stated` C1 and C9 on
  both hosts (0 / 5), Claude Code `investigate-bug` C11 (0 / 5). There the reference records
  non-conformance, not a level to protect.
- Run-to-run noise is unmeasured. The mixed cells are 1 / 5 or 4 / 5 (Claude Code C9 and C11),
  so an unchanged plugin could trip the “drop of two” rule. Only a repeat run on the same
  plugin measures this.
- The judge is inconsistent on completion replies that are silent about a next action. On five
  near-identical Codex `tdd-stated` replies it graded `C1.concrete` pass twice and fail three
  times, and it passed all five Codex `authz-change` replies, whose rubric accepts “review
  result reported and no next action needed”. Those ten cells fail C1 anyway through the
  computed part. In the four scenarios where C1 is judged only (`explore-save`,
  `explore-no-save`, `review-readonly`, `specify-change`; 20 / 20 on each host) no computed part
  backs the judge, and no calibration case covers a completion reply that is silent on the
  next action.
- Outside-workspace saves: for the 60 Claude Code trials, no file exists in any trial's
  auto-memory folder and none of 92 Write or Edit calls targeted a path outside the workspace.
  The equivalent was not checked for Codex, whose sandbox confines writes to the workspace.
- Any change to the scenarios, rubric, or calibration cases changes the suite hashes, and
  `compare` then refuses this reference.
- Five trials per scenario; no statistical significance is claimed. C10 rests on one scenario.
- C9 and C1's computed part are text patterns; a layout they do not recognise counts as a fail.
- The fixes made after the second pilot and the C1 correction were reviewed independently
  after this run (no blocking finding; see the spec). A later `compare` warns “suite code
  differs from the reference: checks.py, run.py” because both changed after the condition was
  frozen; that warning is accurate.
- The reference is valid for these models, efforts, permission configurations, suite hashes,
  judge, and (Codex) this global `AGENTS.md`. `compare` refuses when one of them differs and
  warns when a CLI version differs.

## Next action

User accepts the suite or names changes. The open decisions are listed in the spec's current
handoff.
