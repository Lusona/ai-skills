# Loop conformance suite pilot — 2026-11-09

Owner: [spec 20261109-loop-conformance-suite](../../specs/20261109-loop-conformance-suite.md).

## Decision and scope

- Decision this evidence informs: whether the suite's capture, grading, and judging work on
  both hosts, and what one trial costs in time and usage, before a reference run is approved.
- Scope: 2 scenarios (`explore-save`, `tdd-unset`) × 1 trial × 2 hosts, plus judging and the
  judge calibration. Authorized by the user on 2026-11-09 as a pilot excluded from any reference.
- Not a measurement of agent conformance: one trial per cell, and the Claude Code trials ran
  under a permission configuration that was later replaced.

## Method and provenance

- Plugin: frozen copy of `plugins/lusona` at commit `cc8a59c` (2.0.5); hashes in each
  `runs/001/<host>/condition.json`.
- Suite: `evals/loop-conformance/` as of the pilot (untracked working tree). Suite hashes are in
  the condition files. The runner code changed after the pilot (see Limits).
- Claude Code 2.1.321, `claude-opus-5-5`, high effort, `--setting-sources project
  --strict-mcp-config --permission-mode dontAsk` with a Bash allowlist, workspace under
  `~/.cache/lusona-evals`.
- Codex CLI 0.167.0, `gpt-6.1-sol`, medium effort, `--ignore-user-config`, workspace-write
  sandbox. The global `AGENTS.md` was loaded; its hash is in the Codex condition file.
- Judge: `claude-fable-5-2`, medium effort, prompt hash in the condition files.
- Commands: the pilot sequence in `evals/loop-conformance/README.md`, then
  `run.py report` and `run.py judge --calibration`.
- Artifacts: `runs/001/report.md` and `report.json`; per trial `trial.json`, `computed.json`,
  `judged.json`; `runs/001/judge-calibration.md`; `runs/001/raw.zip` holds the per-turn
  transcripts, inputs, judge prompts and outputs, and the calibration calls. The zip contains
  absolute local paths and is git-ignored by the user's decision of 2026-11-09; it exists only
  on the machine that ran the pilot. `tdd/` holds the writers' red and green test outputs.

## Observations

| Host | Scenario | Turns | Seconds | Reported usage | Checks graded |
| --- | --- | --- | --- | --- | --- |
| Claude Code | `explore-save` | 2 | 71 | $0.3748 for the session (turn 1 $0.2885, turn 2 $0.0863) | C1 pass, C2 fail, C8 fail |
| Claude Code | `tdd-unset` | 1 | 20 | $0.2141 | C5 pass, C8 pass |
| Codex | `explore-save` | 2 | 139 | 478,705 input tokens (437,376 cached), 4,270 output, as reported after turn 2 | C1 pass, C2 pass, C8 pass |
| Codex | `tdd-unset` | 1 | 46 | 215,971 input tokens (186,752 cached), 1,541 output | C5 pass, C8 pass |

- Judge calls: 4, each reporting $0.17–$0.25. Calibration: 15 cases, agreement 15 / 15.
- No trial read evaluator material. No trial changed the outer repository's `git status`.
- Claude Code `explore-save`: the allowlist refused a timing probe that wrote under `/tmp`.
  The actor then wrote “Bash was denied in this session”, did not run the record helper, and
  saved `notes/tally-storage-options.md` at the workspace root. The Codex actor ran
  `work-record.sh init-notes` and saved `docs/lusona/notes/tally-storage-options.md`.
- Claude Code `tdd-unset`: the allowlist refused `git ls-files && cat …` and a `grep`.
- Codex `explore-save`: the `--json` stream shows one collaboration item of type `wait`; the
  session rollout file records one `spawn_agent` call. The pilot runner recorded `workers` as null.

## Interpretation and decision

- Capture, grading, judging, and reporting completed for all four trials on both hosts.
- The Claude Code C2 and C8 fails are not valid behavioral evidence: the allowlist changed the
  actor's behavior. The runner now uses Claude Code's Bash sandbox instead of an allowlist.
  That change was verified with two one-turn probes on `claude-haiku-5-5`, not with a rerun of
  this scenario.
- Possible rule gap, unconfirmed: `plugins/lusona/references/retention.md:59` names the notes
  path as `notes/<change-slug>.md` without the `docs/lusona/` prefix, which matches where the
  Claude Code actor saved. A rerun under the sandbox is needed to separate this from the
  allowlist effect.
- The calibration cases were written by the content writer, not labelled by a person. The
  15 / 15 agreement shows that the judge applies the rubric as written.
- Claude Code `total_cost_usd` is cumulative per session; whether it includes subagent usage is
  unverified. Codex reports tokens, not cost.

## Limits

- One trial per cell; no variance estimate.
- The pilot conditions cannot be reused: `run.py` changed after the pilot (sandbox settings,
  Codex worker counting, per-trial cost), so `prepare` and `run` refuse them.
- No scenario with delegation, implementation, or independent review was run; their time and
  usage are unmeasured.

## Next action

Coordinator reports the pilot and the independent review to the user; a rerun of the affected
Claude Code trial and any reference run need the user's approval.
