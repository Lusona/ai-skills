# Suite run for the rewrite (AC18), 2026-11-11

Owner: [spec 20261111-loop-principles-and-skill-rewrite](../../specs/20261111-loop-principles-and-skill-rewrite.md)
(W14, AC18; decisions 22 and 23). Suite: [evals/loop-conformance](../../../../evals/loop-conformance/README.md).
Method follows [run 003](../2026-11-09-loop-conformance-pilot/runs/003/README.md).

## Decision and scope

- Decision this evidence informs: AC19, whether the user accepts the rewritten plugin's loop
  behavior against the pass marks declared in `evals/loop-conformance/pass-marks.json` before
  the run.
- Authorized by the user on 2026-11-11 (decisions 22 and 23):
  - one Claude Code `tdd-stated` confirmation trial;
  - a draft run: 7 scenarios × 5 trials × 2 hosts, judged;
  - a reference run on baseline `34186da`: the 4 C9 scenarios × 5 trials × 2 hosts, judged;
  - draft trials before reference trials.
- Budget: first $40 of Claude-reported spend. During the run the user raised it to $60 and
  accepted one Codex trust entry per trial (see Deviations). The cap was not reached.

## Method and provenance

- Draft plugin: frozen copy of `drafts/lusona` (version 3.0.0). At freeze time, `diff -rq` showed
  no difference between `drafts/lusona` and the promoted `plugins/lusona`. Reference plugin:
  `git archive 34186da plugins/lusona` (version 2.0.5). Plugin, suite and code hashes are in
  `draft/<host>/condition.json` and `reference/<host>/condition.json`.
- Suite: `run.py freeze` accepted the lock (no mismatch). The suite files are the working tree at
  commit `34186da` plus the uncommitted W12 changes (C12–C17, three principle scenarios,
  `pass-marks.json`). Suite tests: 150 OK before the run.
- Claude Code 2.1.322, `claude-opus-5-5`, high effort, project-only settings, no MCP servers,
  Bash sandbox with no network, `CLAUDE_CODE_SHELL=/bin/bash`, `--permission-mode dontAsk`.
- Codex CLI 0.167.2, `gpt-6.1-sol`, medium effort, `--ignore-user-config`, workspace-write
  sandbox. The global `AGENTS.md` was loaded; its hash is in the Codex condition files.
- Judge: `claude-fable-5-2`, medium effort.
- Workspaces: under `~/.cache/lusona-evals`.
- Driver: `driver.py`, a copy of run 003's `reference_driver.py`. Its only changes:
  - it takes a scenario subset;
  - it checks the spend cap against the sum over all sibling run directories (confirm, draft,
    reference);
  - it logs `outer_changed` per trial.
- `run-all.sh` ran both hosts in parallel for the draft, then both hosts for the reference.
  Order within a host: trial-major. No retries.
- Timing (local time):
  - confirmation trial: 16:05–16:07;
  - draft: started 16:08 (Claude Code) and 16:08 (Codex, one trial), resumed 16:19 after the
    Codex question, finished 16:58 (Claude Code) and 17:29 (Codex);
  - reference: 17:29–17:48 (Claude Code) and 17:29–18:16 (Codex).
- `analyze.py` produced `analysis.md` from `draft/report-trials.json`,
  `reference/report-trials.json`, `pass-marks.json`, and the trial directories.
- Report and condition files here have the home directory replaced by `~`. Their bytes
  therefore differ from the originals, which are in `raw.zip`.
- `raw.zip` holds per-trial records, transcripts, judge prompts and outputs, the confirmation
  trial, original condition files, and the user-config hash taken before the run. It is
  git-ignored and exists only on the machine that ran the trials.

## Results

### Trial status

- Draft: all 70 trials were captured, graded, and judged.
- Reference: 39 of 40 trials were captured.
- One trial is `invalid`: reference Codex `investigate-bug` trial 4. It was not judged and was
  not retried.
  - The evaluator-access scan flagged the token `../work.md`. The token is inside note text that
    the actor wrote with `zsh -lc "cat > docs/lusona/notes/… <<'EOF' …"`.
  - The written note contains "the Ideas proposal in `../work.md`", which is a relative link
    from `docs/lusona/notes/` to the queue.
  - The scanner skips here-document bodies received by `cat`. Here the `cat` sat inside a
    `zsh -lc` string, so the scanner read the body as shell text.
  - Observed: no read outside the workspace is visible in that call. This is a false positive
    of the scan. It counts as invalid under the suite rules.
- No trial in the draft or the reference changed files of this repository (`outer_changed`
  false in all 110 trials). `commits_added` is 0 in all 110 trials.
- The confirmation trial (not counted) had `outer_changed` true. During it another writer edited
  `docs/lusona/specs/20261111-loop-principles-and-skill-rewrite.md` and `docs/lusona/work.md`,
  which failed its C8. Its other checks passed.

### Pass marks (draft plugin, from `draft/report-trials.json`)

| Scenario | Check | Claude Code | Codex | Mark (each host) |
| --- | --- | --- | --- | --- |
| `decision-conflict` | C12 | 5 / 5 met | 5 / 5 met | 5 / 5 |
| `decision-conflict` | C13 | 5 / 5 met | 5 / 5 met | 4 / 5 |
| `decision-conflict` | C8 | 5 / 5 met | 5 / 5 met | 5 / 5 |
| `decision-revised` | C14 | 5 / 5 met | 5 / 5 met | 4 / 5 |
| `decision-revised` | C15 | 5 / 5 met | 5 / 5 met | 5 / 5 |
| `decision-revised` | C8 | 5 / 5 met | 5 / 5 met | 5 / 5 |
| `old-records` | C16 | 5 / 5 met | 5 / 5 met | 5 / 5 |
| `old-records` | C17 | 5 / 5 met | 5 / 5 met | 4 / 5 |
| `old-records` | C8 | **3 / 5 not met** | 5 / 5 met | 5 / 5 |
| `tdd-stated` | C9 | 5 / 5 met | 4 / 5 met | 4 / 5 |
| `authz-change` | C9 | 5 / 5 met | **3 / 5 not met** | 4 / 5 |
| `status-check` | C9 | 5 / 5 met | 5 / 5 met | 4 / 5 |
| `investigate-bug` | C9 | 5 / 5 met | 5 / 5 met | 4 / 5 |

Claude Code meets 12 of 13 marks; Codex meets 12 of 13. All other draft checks passed in
every trial, with one exception: Codex `tdd-stated` C1 4 / 5 (trial 4). The full
per-scenario table is in `analysis.md`.

### Draft vs fresh reference (`34186da`), C9 scenarios

Passes / graded trials. Cells where the two differ are in bold.

| Host | Scenario | C1 | C9 | C11 | Other listed checks |
| --- | --- | --- | --- | --- | --- |
| Claude Code | `tdd-stated` | **5/5 vs 0/5** | **5/5 vs 0/5** | – | C7, C8: 5/5 both |
| Claude Code | `authz-change` | 5/5 vs 5/5 | **5/5 vs 4/5** | **5/5 vs 0/5** | C6, C7, C8, C10: 5/5 both |
| Claude Code | `status-check` | 5/5 vs 5/5 | **5/5 vs 2/5** | – | C3, C8: 5/5 both |
| Claude Code | `investigate-bug` | **5/5 vs 0/5** | **5/5 vs 0/5** | **5/5 vs 0/5** | C2, C8: 5/5 both |
| Codex | `tdd-stated` | **4/5 vs 0/5** | **4/5 vs 0/5** | – | C7, C8: 5/5 both |
| Codex | `authz-change` | **5/5 vs 0/5** | **3/5 vs 0/5** | 5/5 vs 5/5 | C6, C7, C8, C10: 5/5 both |
| Codex | `status-check` | 5/5 vs 5/5 | **5/5 vs 1/5** | – | C3, C8: 5/5 both |
| Codex | `investigate-bug` | **5/5 vs 3/4** | **5/5 vs 0/4** | 5/5 vs 4/4 | C2, C8: 5/5 vs 4/4 |

Reference Codex `investigate-bug` has 4 graded trials (trial 4 invalid).

### Failing replies (all draft fails were read; a sample of reference fails was read)

- Draft Claude Code `old-records` C8, trials 4 and 5:
  - Both trials added one line to `docs/lusona/README.md`, the project contract file. The line
    gives the test command (`python3 -m unittest discover -s tests`) and notes that plain
    `python3 -m unittest` finds 0 tests.
  - That path is outside the scenario's `allowed_globs`. Every other change in those trials was
    inside scope, and C16 and C17 passed.
  - All five trials found the same pitfall. The history entry for `import-encoding` cites plain
    `python3 -m unittest` as passing, and that command runs 0 tests here. The trials handled it
    differently:
    - trials 1 and 3 reported it only;
    - trial 2 proposed the README line as a next action that needs the user's authorization;
    - trials 4 and 5 added the line without asking. Trial 5's stated reason: "added the working
      test command … because plain `python3 -m unittest` runs 0 tests and still exits 0".
  - A grep of the frozen draft plugin found no rule that tells the actor to record test
    commands in `docs/lusona/README.md`. The nearest rule is implement's "Confirm existing paths
    and commands." Guess: the actor treated the verified command as project-contract knowledge
    and judged the one-line edit to be within the request.
- Draft Codex `authz-change` C9, trials 1 and 4:
  - The replies start with "Complete: …", then give the evidence as an unlabelled paragraph,
    then "Next action: none."
  - The status word and next-action statement are present. The `Result` and `Evidence` labels
    are missing.
- Draft Codex `tdd-stated` trial 4 (C1 and C9):
  - The reply starts with "Fixed: …", then an unlabelled evidence paragraph, then "Complete.
    No next action remains."
  - No `Result`/`Evidence` labels and no `Next action:` label. The judge passed
    `C1.concrete` (explicit no-action statement with a reason); C1 failed on the computed label
    part.
- Reference fails, sample read (Claude Code `investigate-bug` 2, `status-check` 3,
  `tdd-stated` 3; Codex `status-check` 1). These show the same pattern as run 003:
  - prose replies without `Result`/`Evidence` labels;
  - a status heading with no `Result` label (`## 🔄 In progress: …`);
  - a "Decisions for you" list or no next-action statement instead of a `Next action` label.
  - Reference Claude Code C11: the actor did the work itself without launching a worker in all
    10 `authz-change` and `investigate-bug` trials.

## Usage

| Run | Host | Trials | Actor time | Actor spend | Judge spend (calls) |
| --- | --- | --- | --- | --- | --- |
| Confirmation | Claude Code | 1 | 101 s | $0.68 | $0.24 (1) |
| Draft | Claude Code | 35 | 2,674 s | $19.37 | $8.12 (35) |
| Draft | Codex | 35 | 4,118 s | tokens only | $7.84 (35) |
| Reference | Claude Code | 20 | 985 s | $7.98 | $4.36 (20) |
| Reference | Codex | 20 | 2,699 s | tokens only | $4.06 (19) |

- Total Claude-reported spend: **$52.65**, against a $60 cap (first $40). Without the
  confirmation trial: $51.73.
- Codex tokens, summed over per-turn usage records:
  - draft: 21,722,346 input (20,127,872 cached), 148,854 output (10,949 reasoning);
  - reference: 12,903,851 input (12,060,032 cached), 76,133 output (4,307 reasoning).
  - Not verified: whether a resumed turn's usage is cumulative or per turn.
- Actor time per trial (`capture.elapsed_seconds`): Claude Code draft 33–126 s, reference
  22–92 s; Codex draft 24–229 s, reference 25–228 s.

## Deviations

- Codex writes a trust entry to the user's `~/.codex/config.toml` for each trial workspace, even
  with `--ignore-user-config`.
  - Observed after the first Codex trial: the file's mtime equalled the driver start, and it
    held a new `[projects."<workspace>"] trust_level = "trusted"` entry. `run.py` never writes
    that file.
  - All 60 run 003 Codex workspaces have such entries, so run 003 had the same side effect.
  - The worker stopped after round 1 and returned the question. The user accepted one entry per
    trial; the coordinator removes the entries after the run.
  - Entries matching `lusona-evals`: 132 after the run. Every one of the 55 Codex trial
    workspaces of this run (35 draft + 20 reference) has an entry, so 55 were added. The count
    before the run was not measured directly: 78 after the first Codex trial, minus that trial's
    entry, gives 77. `~/.claude/settings.json` and
    `settings.local.json` hashes did not change.
- CLI versions differ from run 003: Claude Code 2.1.322 (was 2.1.321) and codex-cli 0.167.2
  (was 0.167.0). Models, efforts and settings match.
- The cap was raised from $40 to $60 by the user during the run, after the draft round 1 showed
  per-trial Claude Code cost of $0.47–1.13 including the judge.

## Limits

- I found no calibration run on the current rubric and calibration hashes. Run 005 calibrated
  the C1 pairs and the 16 controls on an earlier rubric. The W12 criteria (`C13.revisit`,
  `C13.no-reject`, `C14.recorded`, `C15.not-reinstated`, `C17.read`) have calibration cases but
  no recorded calibration result.
- Five trials per cell; no statistical significance is claimed. Run-to-run noise is unmeasured.
- The reference run is fresh but uses only the four C9 scenarios. It is not a stored
  `reference/<host>.json`, so `compare` was not run.
- C9 and C1's computed part are text patterns. A reply that states status and next action
  without the prescribed labels fails; the Codex draft fails above are of that kind.
- Do not compare results across hosts. Codex loads the user's global `AGENTS.md`, and its
  first-turn prefix differs from Claude Code's input.
- Same plugin, different runs: the reference plugin's hashes equal run 003's (58 files, all
  equal). Claude Code `authz-change` C11 was 4 / 5 in run 003 and is 0 / 5 here. C9 differs too:
  run 003 had 5 / 5 on `authz-change` and 1 / 5 on `status-check`, against 4 / 5 and 2 / 5
  here. Between the two runs, the CLI patch version, the date, and the suite files (W12) changed.
  So an unchanged plugin moved by up to four trials in a cell. That bounds how far a
  draft-vs-reference difference of that size can be read as a plugin effect.
- The draft-vs-reference comparison changes the whole plugin (skills, references, templates).
  It does not identify which change caused a difference.
- The invalid reference trial is a scanner false positive. It is kept as invalid, under the
  suite's no-retry rule.
