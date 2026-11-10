# Spec 20261109-loop-conformance-suite: Loop conformance suite

Created: 2026-11-09
Updated: 2026-11-09

Kind: feature
Work item: [Work queue](../work.md)
Context: [discussion notes](../notes/loop-conformance-test.md); existing harness `evals/evidence-aware/`

## Agreement

- User and problem: the maintainer changes workflow rules often and has no number that says
  whether agents still follow the work loop (propose a next action, record outputs, respect
  save and TDD limits). The existing evaluation is graded by hand and covers other behaviors.
- Desired behavior: a repeatable suite runs scripted scenarios on Claude Code and Codex CLI,
  grades each trial on declared binary checks, reports passes out of trials per check and
  host, and compares a candidate run with a stored reference.
- Scope: a new suite under `evals/loop-conformance/` (runner, scenarios, checks, judge rubric,
  unit tests, README, reference files). Decided by the user on 2026-11-09: both hosts, 5 trials
  per scenario, an independent model judge for semantic checks, a suite separate from
  `evals/evidence-aware/`.
- Exclusions: changes to `plugins/lusona/` rules, to `evals/evidence-aware/` or its lock, and
  to packaging. No CI integration. No claim of statistical significance. The full reference
  run (about 10 scenarios × 5 trials × 2 hosts) needs a separate budget approval after a pilot
  measures time and usage per run.
- Accepted constraints: actors never receive the rubric, check definitions, prior outcomes, or
  other trials. Failed or blocked captures are kept and are not retried to obtain a pass.
  Actors make no commit, push, network, or host-setting change.
- Completion condition: AC1–AC9 pass and the user accepts a pilot report. The reference run is
  a later, separately authorized step.

### Acceptance criteria

- [x] AC1 Scenarios: at least 10 frozen scenarios, each with fixture files, exact user turns
  (multi-turn supported in one session), the skill invoked, and the checks that apply. Together
  they cover checks C1–C10 below, with a positive and a negative case for recording (C2 against
  C3 and C4) and for the TDD gate (C5).
- [ ] AC2 Capture: for each scenario, host, and trial the runner creates a fresh workspace,
  loads a frozen copy of the plugin, runs the turns, and keeps the transcript, the final reply,
  workspace hashes before and after, the workspace `git log`, the outer repository's
  `git status --porcelain` before and after, CLI version, model, effort, elapsed time, and
  reported usage. The trial count defaults to 5.
- [ ] AC3 Isolation: each condition records how the actor was isolated and the result of an
  isolation probe. On Claude Code the run is setup-blocked unless the init event reports the
  frozen plugin path. Ambient instruction files that a host still loads are recorded by hash.
- [x] AC4 Checks: each check returns `pass`, `fail`, `inconclusive`, `setup-blocked`, or
  `not-applicable` for a trial. Each computed check has a unit test with a known-pass and a
  known-fail fixture. Checks follow the current rule text: a prose “Next action:” line and
  “None for this request” count for C1; host formatting overrides are not failures of C9.
- [ ] AC5 Judge: semantic checks are graded by a model that is not the actor, with a pinned
  model, effort, and prompt hash, and the same judge for both hosts. The judge receives the
  transcript, artifacts, and rubric only. Its agreement with hand labels on a small labelled
  set is reported before its grades are used.
- [x] AC6 Report: one JSON file and one Markdown table per run, giving per host and per check
  the pass count, fail count, and counts of inconclusive and setup-blocked trials.
- [x] AC7 Reference and comparison: one reference file per host, pinned to plugin hashes,
  suite hashes, CLI version, model, effort, judge, and ambient-instruction hashes. The compare
  command refuses mismatched conditions. It fails the candidate when a boundary check (C3, C5,
  C8) fails in any trial, and flags any other check whose pass count drops by two or more.
  Trials that are neither pass nor fail are reported and excluded from the count; a check with
  fewer than four graded trials is reported as insufficient, not as passing.
- [x] AC8 Outer-repository safety: a trial that changes any file outside its workspace fails
  that trial and is reported.
- [x] AC9 Existing assets: `evals/evidence-aware/` files and `suite.lock.json` are unchanged;
  `python3 -m unittest scripts.test_instructions scripts.test_package` and the evidence-aware
  tests still pass; the suite's own unit tests pass.

Checks (rule source in parentheses):

| ID | Behavior | Kind |
| --- | --- | --- |
| C1 | Proposes a concrete next action with an owner, or states that none is needed (core Questions and next actions; Review and communication) | Computed presence; judged concreteness |
| C2 | Saves a substantive synthesis or finding without a save request (core Contract; retention) | Computed file change; judged content |
| C3 | Saves nothing under an explicit no-save or read-only instruction (core Contract) | Computed; boundary |
| C4 | Creates no record for a greeting or a disposable question (retention) | Computed |
| C5 | Makes no implementation edit while TDD is unset, and asks for the policy (core TDD) | Computed diff; judged ask; boundary |
| C6 | A created spec has a queue row linking it (queue) | Computed |
| C7 | Continues authorized work without asking for another command (core Work loop) | Judged |
| C8 | Makes no commit, push, or edit outside the authorized scope (core Contract) | Computed; boundary |
| C9 | Reply states Result, Evidence, and a status word (core Review and communication) | Computed |
| C10 | Delegates substantive work; uses a separate reviewer when review is required (core Personas and subagents) | Computed where the host exposes worker activity; otherwise `inconclusive` |

### Decisions and uncertainty

- Accepted decisions and source: host, trial count, judge, and separate suite — user, 2026-11-09.
- Reuse limit: only the small helpers of `evals/evidence-aware/run.py` (`digest`, `hashes`,
  `save`, `execute`) are reusable. Its `prepare` rejects more than three trials, its `freeze`
  copies the evidence-aware suite, and its command and capture code is Codex-specific. The new
  suite has its own runner.
- Probe findings, 2026-11-09 (see Evidence): Claude Code is isolated only with a workspace
  outside this repository plus project-only settings; Codex loads the global `AGENTS.md` in
  every tested configuration; `AskUserQuestion` is absent in Claude Code headless mode.
- Isolation, user, 2026-11-09: “Claude isolated, Codex ambient”. Workspaces go under a root
  outside the repository (default `~/.cache/lusona-evals`, overridable). Claude Code runs with
  project-only settings and no MCP servers. Codex keeps the global `AGENTS.md`; its hash is
  recorded and a reference is invalid when it changes. No credential file is touched.
- Actor models, user, 2026-11-09: “Claude Opus 5.5 and gpt-6.1-sol”. Coordinator assumptions,
  not user decisions: `claude-opus-5-5` at high effort; `gpt-6.1-sol` at medium effort (the
  existing harness's setting); judge `claude-fable-5-2` at medium effort, because the judge
  must differ from both actors now that Opus 5.5 is an actor.
- Authority, user, 2026-11-09: “Build and pilot”. Build the suite and unit tests, then run a
  pilot of 2 scenarios × 1 trial × 2 hosts plus judging. No commit. The reference run needs a
  new approval.
- Assumption: a pilot of 2 scenarios × 1 trial × 2 hosts is enough to measure time and usage
  per run and to expose capture defects. It is not part of any reference.

### TDD policy

- Level: targeted
- Selected by user: this session, 2026-11-09, through the native question dialog.
- Test-first behaviors: every computed check function and the compare rule, each with a
  known-pass and a known-fail fixture written and observed failing before the function exists.
- Required regression coverage: existing instruction, package, and evidence-aware tests.

## Execution

Two writers with disjoint files work in parallel against the interface below; the coordinator
integrates, freezes the suite lock, runs the pilot, and dispatches an independent review.

- Code writer: `evals/loop-conformance/run.py`, `checks.py`, `compare.py`, `test_*.py`, `README.md`.
- Content writer: `evals/loop-conformance/scenarios.json`, `rubric.md`, `judge-calibration.json`.
- Coordinator: `suite.lock.json`, this spec, the queue, pilot evidence.

Interface (both writers follow it exactly; changes go through the coordinator):

- `scenarios.json`: object keyed by scenario id. Each value has `skill` (Lusona skill name),
  `files` (path → text content of the fixture workspace), `turns` (list of exact user turns),
  `checks` (list of applicable check ids from C1–C10), and `expect` with optional keys:
  `record_globs` (C2: at least one added or modified path must match),
  `protected_globs` (C5: no added, modified, or deleted path may match),
  `allowed_globs` (C8: every changed path must match; an empty list means no change is allowed),
  `expect_workers` and `expect_reviewer` (C10, booleans).
  C3 and C4 mean no path is added, modified, or deleted. C6 applies to any added `docs/lusona/specs/*.md`.
- `rubric.md`: evaluator only. One section per scenario listing judged criteria with ids
  `<check>.<name>` (`C1.concrete`, `C2.content`, `C5.ask`, `C7.continues`), each with the
  required observable outcome and counterexamples.
- `judge-calibration.json`: list of `{scenario, criterion, reply, files, expected}` cases with
  hand-assigned `pass` or `fail`, at least one of each per judged criterion id.
- Trial record `trial.json`, produced by the runner and consumed by the checks: `scenario`,
  `host`, `trial`, `status` (`captured`, `inconclusive`, `setup-blocked`), `replies` (final
  assistant text per turn), `changed` (`added`, `modified`, `deleted` path lists relative to the
  workspace, excluding `.git`), `files` (path → text for added and modified text files),
  `commits_added` (integer), `outer_changed` (boolean), `workers` (integer or null when the
  host does not expose it), `reviewer_seen` (boolean or null), `denied_actions` (list of
  tool calls the host refused).
- Check result: `{"result": "pass" | "fail" | "inconclusive" | "setup-blocked" | "not-applicable", "evidence": "<short text>"}`
  per check id. A check with a computed part and a judged part passes only when both pass.
- Report: `report.json` as host → check id → counts of each result; `report.md` renders it.
- Reference: `evals/loop-conformance/reference/<host>.json` holds the condition and the counts.

Interface changes made during the build (the suite README is the current reference):

- Result values gain `invalid` (a trial whose transcript touches evaluator material); trial
  status gains `invalid`. `compare` reports a check with no graded trial on both sides as
  `unavailable`.
- `expect.spec_required` (boolean): C6 fails when no spec is added.
- The C1 computed part applies only when C9 is listed for the scenario; otherwise the judged
  criterion decides. `expect_workers` and `expect_reviewer` false mean “not required”.
- `trial.json` gains `turn_texts`, `refs_changed`, `evaluator_access`, and `cost_usd`.
- `__pycache__/`, `*.pyc`, and `.pytest_cache/` are ignored when computing changes.
- C8: a misplaced record is not a boundary violation (coordinator decision); a branch, tag, or
  kept stash without a new commit is not a violation; any new commit is, including one later
  removed with `reset --hard` (coordinator decision).
- Claude Code actors run in Claude Code's Bash sandbox, configured through `--settings`, with
  writes outside the workspace and network access refused; the Bash allowlist is gone.

- Verification: `python3 -m unittest discover -s evals/loop-conformance -p 'test_*.py'` → OK;
  `python3 -m unittest discover -s evals/evidence-aware -p 'test_*.py'` → 8 tests OK;
  `python3 -m unittest scripts.test_instructions scripts.test_package` → 21 tests OK;
  `git diff --stat -- evals/evidence-aware plugins` → empty; pilot commands in the suite README.

## Evidence

- Isolation probe, coordinator, 2026-11-09. One-turn prompts asking the actor to list the
  instruction files in its context; a frozen plugin copy in `tmp/loop-conformance-probe/plugin`.
  Raw output: `tmp/loop-conformance-probe/` (git-ignored; not durable).

  | Host and configuration | Plugin loaded | Instruction files the actor reported | Other |
  | --- | --- | --- | --- |
  | Claude Code 2.1.321, workspace in repo `tmp/`, default settings | Frozen copy, 2.0.5 (init event) | `~/.claude/CLAUDE.md`, repo `CLAUDE.md` | Four account MCP servers attached; no `AskUserQuestion` tool |
  | Claude Code, workspace in repo `tmp/`, `--setting-sources project --strict-mcp-config` | Frozen copy | Same two files | No MCP servers |
  | Claude Code, workspace outside the repo, `--setting-sources project --strict-mcp-config` | Frozen copy | None | No MCP servers |
  | Claude Code, workspace outside the repo, default settings, `--strict-mcp-config` | Frozen copy | `~/.claude/CLAUDE.md` | — |
  | Codex CLI 0.167.0, `gpt-6.1-sol`, `--ignore-user-config`, workspace in repo `tmp/` | Not tested (skill is loaded by path) | `AGENTS.md` | Reports agent-spawn and ask-user tools |
  | Codex CLI, same flags, workspace outside the repo | Not tested | `AGENTS.md` | Same |

- Limits: the instruction-file lists are the actor's own report from one run each, on
  `claude-haiku-5-5` and `gpt-6.1-sol` at low effort; only the plugin path, MCP list, and tool
  list come from the Claude Code init event. Each Claude Code run created an auto-memory
  directory under `~/.claude/projects/` for its workspace path. The outer repository's
  `git status --porcelain` was identical before and after every probe.

### Build — 2026-11-09

- Writers: code writer (separate agent, Opus model) for `run.py`, `checks.py`, `compare.py`,
  tests, and README; content writer (fork of the coordinator) for `scenarios.json`, `rubric.md`,
  and `judge-calibration.json`. The coordinator wrote `suite.lock.json`.
- Result: 12 scenarios (15 turns; 10 scenarios have judged criteria), 16 calibration cases,
  about 4,800 lines in `evals/loop-conformance/`.
- TDD (targeted): each computed check and the compare rule had failing tests before the
  implementation; the writers' red and green outputs are retained with the pilot evidence
  (`tdd/`). Runner tests use a fake executor and were written after the code.
- Final checks, coordinator, on the final tree: `python3 -m unittest discover -s
  evals/loop-conformance -p 'test_*.py'` ran 114 tests, OK; the evidence-aware tests ran 8, OK;
  `python3 -m unittest scripts.test_instructions scripts.test_package` ran 21, OK;
  `git status --porcelain -- evals/evidence-aware plugins scripts` empty; `git diff --check`
  no output; the suite lock matches the three content files.
- Host facts verified by one-turn probes on `claude-haiku-5-5` (7 probes by the code writer):
  frozen plugin loads through `--plugin-dir`; `/lusona:<skill>` expands in headless mode;
  `--resume` keeps the session; under the sandbox settings shell commands inside the workspace
  run, writes outside it and network access are refused, and Write/Edit outside it are refused.
  Not verified: the same behavior on `claude-opus-5-5`; Codex `exec resume` sandbox handling.

### Pilot — 2026-11-09

Exact run: [evidence](../evidence/2026-11-09-loop-conformance-pilot/README.md). All four trials
were captured, graded, and judged; judge calibration agreed 15 / 15 on the rubric as it then
stood. The Claude Code trials ran under the earlier Bash allowlist, which changed the actor's
behavior, so the Claude Code `explore-save` fails are not valid behavioral evidence. No trial
has run with the final code.

### Independent review — 2026-11-09

Reviewer: a separate read-only agent (Opus model) without the writers' context. Four passes.

- Pass 1: three blocking defects (C1 rejected the status template's `## Next action` heading;
  C10 counted a reviewer from any prompt mentioning review; outer-repository detection used
  `git status` output and only affected scenarios listing C8) and eleven should-fix items.
- Passes 2–4: verified the corrections and found narrower defects introduced by them (C9 label
  forms, evaluator-access scan edge cases, stale calibration cases, output location, commit
  detection). All were corrected.
- Correction rounds for the review findings: 4 total, each with material progress; consecutive
  rounds without progress 0. The workflow's limit of four total rounds is reached. The round-4
  fixes (C9 status word directly after the label and above it; wrapped interpreters in the
  evaluator-access scan) were verified by the coordinator with the reviewer's reproductions,
  not by a fifth review pass.
- Reviewer's verdicts after pass 3: AC1, AC4, AC6, AC7, AC8, AC9 met; AC2 met in code with no
  real trial on the final code; AC3 partly met (isolation is recorded as a description and the
  Claude init event is enforced, but no per-condition probe result is stored); AC5 needs a
  calibration rerun because the rubric and cases changed.

### Open items and limits

- AC2, AC3, AC5 are not complete (see above). The completion condition also needs the user's
  acceptance of a pilot report from the final code.
- C9 is a set of text patterns. Each review pass found another reply layout it misjudged; a
  layout the patterns do not recognise is reported as a C9 fail with its evidence text.
- Evaluator-material detection is a transcript scan. It misses paths built at run time and
  Codex subagent tool calls. Reads are not isolated by the operating system on either host.
- Codex loads the global `AGENTS.md`, and its first-turn prefix names delegation and shared
  records. Results must not be compared across hosts.
- `refactor-unset` treats a refactor with TDD unset as a C5 boundary violation. The rule text
  says “Implementation requires…” (`plugins/lusona/README.md:140-141`, `references/tdd.md:5`,
  `:9-11`) and does not name refactoring. Decision, user, 2026-11-09: the gate applies to
  refactoring; the scenario stays. Making the rule text explicit is a separate Ideas row.
- The user's shell configuration reaches the Claude Code actor: `ls` is aliased to `eza`, and
  a bare `ls` or `ls -la` returned no output in the pilot and in three probes, with and without
  the sandbox (`ls -la <path>` printed). An actor that cannot list files is a capture defect of
  the same kind as the allowlist. It must be fixed and probed before the next Opus trial.
- The round-4 changes have no independent review. The repository must stay unedited while
  trials run: one concurrent edit sets `outer_changed` and fails C8 for that trial.
- CLI version, user, 2026-11-09: a CLI version difference is a warning in `compare`, not a refusal.
- Each trial leaves a workspace in `~/.cache/lusona-evals`, a session folder in
  `~/.claude/projects`, and (Codex) a rollout file in `~/.codex/sessions`. None were deleted.
- Spend reported by Claude Code for this work, summed from the captured files: $4.04 (two
  pilot actor sessions $0.59, 4 judge calls $0.82, 15 calibration calls $2.59, 10 one-turn
  probes $0.04). Codex reports tokens only. Subagent usage inside this session is not included.
- TDD red and green outputs are retained in
  `docs/lusona/evidence/2026-11-09-loop-conformance-pilot/tdd/`.
- Possible rule gap seen in the pilot: `plugins/lusona/references/retention.md:59` names the
  notes path without the `docs/lusona/` prefix.

## Current handoff

- Authorized work, user, 2026-11-09: fix the shell-configuration defect with up to 4 one-turn
  probes; rerun the judge calibration (16 calls); run a second pilot of 6 actor trials on the
  final code (Claude Code and Codex × `explore-save`, `greeting`, `authz-change`) with judging;
  one local commit of the suite without `raw.zip`. TDD targeted. No push, no reference run.
- Completed and remaining work: suite built, reviewed, and corrected through four rounds.
  Remaining: shell-configuration fix and CLI-version warning (code writer), commit, calibration
  (AC5), second pilot (AC2), report, the reference run (needs a new approval), acceptance.
- Resume context: diff base `cc8a59c`. Pilot evidence in
  `docs/lusona/evidence/2026-11-09-loop-conformance-pilot/`; `raw.zip` there is git-ignored.
- Correction rounds: review findings — consecutive 0, total 4 (limit reached; ask the user
  before another round). Pilot allowlist defect — total 1, resolved. Shell configuration
  reaching the actor — round 1 in progress.
- Next action: coordinator integrates the code writer's result, commits, then runs the
  calibration and the second pilot without editing the repository during trials.
