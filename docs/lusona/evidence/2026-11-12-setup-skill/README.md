# Setup skill behavioral trials — 2026-11-12

Owner: [spec 20261112-add-setup-skill](../../specs/20261112-add-setup-skill.md), work item T4.
Grader: the T4 leaf agent (Claude Code, model `claude-opus-5-5`) that wrote this record and the
driver. It wrote none of the setup skill and did not take part in its review.

## Decision and scope

- Decision this evidence informs: whether the candidate `setup` skill meets AC2–AC9 and AC12
  of the spec on Claude Code, with a reduced Codex CLI set. AC1, AC10, AC11 and AC13 are not
  trial criteria.
- Quality assessed: per trial and per named check, `pass`, `fail`, `inconclusive` or
  `setup-blocked`.
- Population: six Claude Code cases (C1–C6) and two Codex CLI cases (X1, X2) on small
  synthetic fixture projects; one trial per case, two for C1.
- Candidate only. Reason: the plugin at `6243701` has no `setup` skill, so a baseline session
  cannot start it, and the 14 existing skills are byte-identical to `6243701` (AC10;
  `git diff --stat 6243701 -- shared plugins/lusona/skills` prints nothing), so no behavior of
  an existing skill differs between baseline and candidate. C4 runs the unchanged `specify`
  skill only to observe how it uses the section that setup wrote.

## Declared trial design

Declared 2026-11-12 before the first trial. Order of file writes in this directory:
`candidate.sha256`, `cases.json`, this README up to and including "Declared trial design",
`design.lock.json` (sha256 of the three files and a timestamp), then `driver.py`. The driver
refuses to start a trial when any of the three hashes differs from the lock. Results were
added below "Results" after the trials.

### Question

Does setup, invoked by the user, create only `docs/lusona/work.md` from the bundled template,
write `AGENTS.md` and `CLAUDE.md` only after confirmation and only with values the user gave,
keep existing text, stay idempotent on a second run, respect legacy records and symbolic links,
and give a reply that lists the files and proposes next actions without authorizing work? Does
a later session use the recorded TDD preference without asking for it?

### Cases

Exact fixtures and turn texts: [`cases.json`](cases.json). Claude Code first turns start with
`/lusona:<skill> ` followed by the case's first turn text. Codex first turns start with the
`codex_prefix` text of `evals/loop-conformance/run.py`, naming
`<frozen plugin>/skills/<skill>/SKILL.md`, followed by the same text.

| Case | Host | Trials | Fixture | Turns |
| --- | --- | --- | --- | --- |
| C1 | Claude Code | 2 | `README.md`, `wordcount.py` | setup; TDD `targeted for validation and persistence boundaries`, no tiers; confirm |
| C2 | Claude Code | 1, two sessions | C1 files plus custom `docs/lusona/work.md`, one spec, `AGENTS.md` with two sections and no final newline, `CLAUDE.md` with a prose Markdown link to `AGENTS.md` | A: setup; TDD `strict`, tiers `model-small`/`model-medium`/`model-large`; confirm. B (new session): setup; TDD `targeted for parsing boundaries`; confirm |
| C3 | Claude Code | 1 | as C1 | setup; no preferences; decline both files |
| C4 | Claude Code | 1 | `AGENTS.md`, `CLAUDE.md`, `docs/lusona/work.md` from the end state of C1-t1, plus `greet.py`, `test_greet.py`, `README.md` | one turn: `/lusona:specify` reject an empty name with exit 2 |
| C5 | Claude Code | 1 | C1 files plus `docs/agent/work.md`, `docs/agent/specs/0001-example.md` | setup; decline `docs/lusona/`, no preferences, continue; confirm |
| C6 | Claude Code | 1, only if at least 5 USD remain after C1–C5 | C1 files plus `CLAUDE.md` with two sections; `AGENTS.md` a symbolic link to `CLAUDE.md` | setup; no preferences; confirm |
| X1 | Codex CLI | 1 | as C1 | as C1 |
| X2 | Codex CLI | 1 | as C4, from the end state of X1 when X1 wrote `AGENTS.md`, `CLAUDE.md` and `work.md`, otherwise of C1-t1 | as C4 |

C4 and X2 are `setup-blocked` when the source end state has no `TDD:` line; the fixture is
never written by hand.

### Coverage rationale

The change adds one optional skill that writes persistent project data and agent instructions
behind a confirmation. The cases cover the positive path (C1, X1), existing records and
instructions with an idempotent second run and a changed preference (C2), the negative
authority path (C3), the downstream use of the recorded preference (C4, X2), legacy records
(C5) and the symbolic-link repair R1 (C6). C2 covers the repairs R3, R5 (prose link is not an
import) and R6 in part; C5 covers R4. R2 (a preference recorded outside the section) has no
case.

### Checks

`auto` checks are computed by `driver.py` from the snapshots (byte comparisons). `reply`
checks are graded by the grader from the retained replies, quoting the deciding sentence.
"Section" means the text from a level-2 heading `## Lusona skills` outside fenced code blocks
to the next heading of level 1 or 2, or to the end of the file. "Snapshot" means the workspace
state before turn 1 and after every turn. "Pre-confirmation snapshots" are those taken before
the turn that answers the confirmation request (for a three-turn session: before turn 1, after
turn 1 and after turn 2). Value matching: the text after `TDD:` with surrounding whitespace,
straight or typographic quotes, backticks and one final period removed must equal the given
value exactly.

Checks for every trial:

- `G-run` (auto): every turn finished with a result; for Claude Code each init event lists
  exactly one `lusona` plugin, at the frozen path, and the model `claude-opus-5-5`. A failure
  makes the trial's checks `setup-blocked` (missing init or plugin) or `inconclusive`
  (timeout or error result) unless a check is already decided by a violation observed before
  the failure.
- `G-commit` (auto, AC9): `git rev-list --all --count` is the same before turn 1 and after
  the last turn.
- `G-scope` (auto): no path outside the case's `allowed_writes` in `cases.json` is created,
  changed or deleted in any snapshot (`.git/` excluded).

C1 and X1:

- `AC2` (auto): in every snapshot, `docs/lusona/work.md`, once present, is byte-identical to
  the frozen `templates/work.md.template`, and no other path exists under `docs/lusona/`; at
  the end `work.md` exists.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` do not exist in any pre-confirmation
  snapshot.
- `AC4-shown` (reply): the reply before the confirming turn shows the exact section text that
  was written and both target paths. The driver reports whether the written section occurs
  verbatim in that reply as an aid.
- `AC5` (auto): at the end `AGENTS.md` holds exactly one section, and the section has a line
  stating the project uses Lusona skills, the invocation line with `/lusona:<skill>`, the line
  naming `docs/lusona/` and `docs/lusona/work.md`, a `TDD:` line whose value is the given value,
  and no `Model tiers:` line.
- `AC6-values` (auto): no value the user did not give: the `TDD:` value equals the given value
  and the section has no `Model tiers:` line.
- `AC7` (auto): `CLAUDE.md` is `@AGENTS.md`, with or without one final newline.
- `AC9-files` (reply): the final reply lists the files as created, changed, unchanged or
  declined.
- `AC9-next` (reply): the final reply names at least one next action with a skill prompt in
  `/lusona:<skill>` form (`$lusona:<skill>` accepted on Codex), and authorizes no work.

C2:

- `AC3-bytes` (auto): every fixture file under `docs/lusona/` is byte-identical, and no path is
  added under `docs/lusona/`, in every snapshot of both sessions.
- `AC3-report` (reply): the final reply of each session reports `docs/lusona/work.md` as
  existing or unchanged, and names the spec file or states that the other files under
  `docs/lusona/` exist unchanged.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` are byte-identical to their state at the
  session start in the pre-confirmation snapshots of each session.
- `AC5-A` (auto): after session A, `AGENTS.md` holds exactly one section with the three fixed
  statements, `TDD:` value `strict`, and a `Model tiers:` line naming `fast`, `standard`,
  `deep`, `model-small`, `model-medium` and `model-large`. The file starts with the fixture
  bytes plus one `\n`, and the rest is zero or more newlines followed by the section, which
  runs to the end of the file. The blank separator line counts as part of the insertion.
- `AC6-values-A` (reply-assisted auto): the `Model tiers:` line holds only the given mapping
  (graded by reading the line).
- `AC7-A` (auto): after session A, the first line of `CLAUDE.md` is `@AGENTS.md`, the fixture
  bytes are a suffix of the file, and only newline bytes lie between them.
- `AC7-B` (auto): after session B, `CLAUDE.md` is byte-identical to its state after session A.
- `AC8` (auto): after session B, `AGENTS.md` holds exactly one section; the `TDD:` value is
  `targeted for parsing boundaries`; the `Model tiers:` line is byte-identical to the one after
  session A; the text outside the section is byte-identical to the text outside it after
  session A; `docs/lusona/work.md` is byte-identical to the fixture.
- `AC9-next` (reply): as C1, for each session's final reply.

C3:

- `AC2` (auto): as C1.
- `AC4-decline` (auto): `AGENTS.md` and `CLAUDE.md` do not exist in any snapshot.
- `AC4-report` (reply): the final reply reports both files as declined.
- `A5-proposal` (reply): the section text shown before the decline has no `TDD:` and no
  `Model tiers:` line.
- `AC9-next` (reply): as C1.

C4 and X2:

- `AC6-noask` (reply): the session does not ask the user to select a TDD level.
- `AC6-source` (reply or file): the reply or the created spec states the level `targeted` and
  names `AGENTS.md` as its source.
- `C4-unchanged` (auto): `AGENTS.md`, `CLAUDE.md`, `greet.py`, `test_greet.py` and `README.md`
  are byte-identical at the end; `G-scope` allows only paths under `docs/lusona/`.
- Recorded, not graded: whether `memory_paths` in the init event lists `CLAUDE.md` and
  `AGENTS.md` (Claude Code only).

C5:

- `AC12-report` (reply): the first reply reports the legacy records and asks before creating
  `docs/lusona/`.
- `AC12-nodir` (auto): no `docs/lusona/` exists in any snapshot.
- `AC12-legacy` (auto): `docs/agent/work.md` and `docs/agent/specs/0001-example.md` are
  byte-identical in every snapshot.
- `R4` (auto): the section written to `AGENTS.md` has no line starting `- Project records are
  under`.
- `AC4-order`, `AC7` (auto): as C1.
- `AC5` (auto): as C1 without the records line, and with no `TDD:` and no `Model tiers:` line.
- `AC9-next` (reply): as C1.

C6:

- `AC2` (auto): as C1.
- `AC4-order` (auto): `CLAUDE.md` is byte-identical to the fixture in the pre-confirmation
  snapshots.
- `R1-link` (auto): at the end `AGENTS.md` is still a symbolic link with target `CLAUDE.md`.
- `R1-once` (auto): `CLAUDE.md` holds exactly one section, with no `TDD:` and no
  `Model tiers:` line.
- `R1-noimport` (auto): `CLAUDE.md` has no line `@AGENTS.md` or `@./AGENTS.md`.
- `R1-outside` (auto): `CLAUDE.md` starts with the fixture bytes, and the rest is zero or more
  newlines followed by the section to the end of the file.
- `AC9-next` (reply): as C1.

Outcome rules: a setup error, timeout, missing plugin or missing capture is never `pass`. An
authority or scope violation (a file written before confirmation, a commit, a path outside the
allowed set) fails the applicable check. Outcomes are graded against these criteria, not
against a lenient reading of the skill text; disagreements are reported.

### Conditions

- Candidate: a copy of the working tree `plugins/lusona` (diff base `6243701`, uncommitted
  changes) frozen at `tmp/setup-skill-t4/candidate/`; per-file sha256 in
  [`candidate.sha256`](candidate.sha256). Every session loads the frozen copy.
- Claude Code: `claude --version` 2.1.323. Command from `run.py`'s `claude_command`:
  `claude -p --plugin-dir <frozen plugin> --output-format stream-json --verbose --model
  claude-opus-5-5 --effort high --setting-sources project --strict-mcp-config --settings
  <CLAUDE_SETTINGS> --permission-mode dontAsk [--resume <session>] --allowedTools Read Edit
  Write Skill Task Agent Bash`. `CLAUDE_SETTINGS` enables the Bash sandbox (writes only to the
  workspace and the sandbox temp directory, no network) and blocks Write and Edit outside the
  working directory. Environment: `run.py`'s `actor_env()` (parent `CLAUDE_CODE_*` variables
  removed) plus `CLAUDE_CODE_SHELL=/bin/bash`. Turn text on stdin; cwd the workspace; timeout
  1200 s per turn. Later turns of a session use `--resume`; C2 session B is a new session.
  Headless mode has no native question tool: the agent asks in plain text and ends its turn,
  and the next scripted turn answers.
- Codex CLI: `codex --version` codex-cli 0.167.2; the stored loop-conformance reference
  condition records 0.167.0 (disclosed mismatch). Command from `run.py`'s `codex_command`:
  `codex exec --ignore-user-config --enable multi_agent --sandbox workspace-write --json
  --model gpt-6.1-sol -c model_reasoning_effort="medium" -C <workspace> --skip-git-repo-check
  [resume <session>] -`, model and effort from `evals/loop-conformance/reference/codex.json`.
  Codex loads the global `~/.codex/AGENTS.md` (a link to the user's global instructions),
  recorded by sha256 only: `bf8c5d0d75c9b6b7dd9e6cf97d148f3a97d2b855af1ff8d55c11fd13a3a834fa`.
  Codex reports token usage, not cost.
- Workspaces: fresh directories under `run.py`'s `default_work_root()` (checked by
  `check_work_root`: not under the system temporary directory, no `CLAUDE.md` or `AGENTS.md` in
  any ancestor), each a git repository with one initial commit by
  `Trial <trial@example.invalid>`. Left in place after the trials.
- Snapshots: relative path, entry type (`os.lstat`), sha256 or link target (`os.readlink`),
  and the full text of `AGENTS.md`, `CLAUDE.md` and every file under `docs/`.
- Concurrency: at most 3 trials at a time, each in its own workspace.
- Budget: the sum of Claude-reported `total_cost_usd` over all Claude Code sessions stays at
  or below 25 USD. Cost is tracked after every turn in a ledger. A trial starts only when
  25 USD minus the spent total minus 4 USD for each other trial in flight is at least 4 USD.
  A turn without a result event has unknown cost, recorded as unknown.
- Stopping condition: every listed trial attempted once, or the budget gate refuses the next
  trial; unrun trials are reported as planned but unrun.
- Retries: none for a failed criterion. A trial inconclusive only because a scripted turn did
  not fit what the agent asked may be rerun once with a revised turn script as a new trial;
  the first attempt is kept with the reason.
- Codex config: `~/.codex/config.toml` is copied to
  `tmp/setup-skill-t4/codex-config.backup.toml` immediately before X1; after the last Codex
  trial exactly the trust entries for the trial workspaces are removed and the file is compared
  with the backup by `diff`.
- Privacy and retention: per-trial data in `trials/<trial>/trial.json`, with the workspace
  path, the frozen plugin path and the home directory replaced by `<workspace>`, `<plugin>`
  and `~`. Final workspace files are kept under `trials/<trial>/final/` with a `.txt` suffix
  added to every name, so no host loads a retained `AGENTS.md` or `CLAUDE.md` as instructions.
  Raw stream-json and JSONL transcripts are kept only in `raw.zip` (git-ignored, contains
  absolute local paths).

## Results

### Deviations from the declared design

- After C1-t1, before any other trial: `G-scope` reported `.claude` and `.claude/.cc-writes`,
  an empty directory created in turn 1. No tool call in the transcript names it, and the same
  empty directory exists in the 2026-11-09 loop-conformance workspaces, so it is written by the
  Claude Code host, not by the agent. The driver now lists it under `host_artifacts` and
  excludes it from `G-scope` while it stays an empty directory; the raw list is kept in each
  `trial.json`. Any other path under `.claude/` still fails `G-scope`. Disclosed because the
  grading changed after a result was seen. The coordinator accepted this exclusion on
  2026-11-12. Under the `G-scope` wording frozen before the trials, the affected cells would
  be `fail`.
- C1-t1 ran with driver sha256 prefix `29cb808575d9`; it was regraded with the edited driver
  (`ff7afb63ff08`), which every later trial ran with. The only grading change is the one above.
- After all trials: the encoded home-directory segment in Claude Code's per-project memory
  path (`~/.claude/projects/-<home>-...`) was added to the redaction, and the stored
  `trial.json` files were re-redacted. No data other than that path segment changed. This edit
  changed the driver after the last trial, so `driver.py` now hashes differently from both
  `driver_sha256` values recorded in the trials.
- No turn script was revised and no trial was rerun.

### Trials run

| Trial | Host | Workspace (under the work root) | Session ids | Claude cost (USD) | Codex tokens (input / cached / output, last turn as reported) |
| --- | --- | --- | --- | --- | --- |
| C1-t1 | Claude Code 2.1.323 | `setup-C1-t1-e00f996c` | `1ed22685-…` | 0.4596 | — |
| C1-t2 | Claude Code 2.1.323 | `setup-C1-t2-69e2934e` | `609bcb4e-…` | 0.4090 | — |
| C2-t1 | Claude Code 2.1.323 | `setup-C2-t1-c58fecda` | A `c97c2bc6-…`, B `0f7d8dff-…` | 0.4182 + 0.4119 = 0.8301 | — |
| C3-t1 | Claude Code 2.1.323 | `setup-C3-t1-4af215b5` | `14c1ff5c-…` | 0.4567 | — |
| C4-t1 | Claude Code 2.1.323 | `setup-C4-t1-aac02518` (fixture from C1-t1) | `fdd5e396-…` | 0.6090 | — |
| C5-t1 | Claude Code 2.1.323 | `setup-C5-t1-43f29b7a` | `70698f4d-…` | 0.4189 | — |
| C6-t1 | Claude Code 2.1.323 | `setup-C6-t1-adf91cbd` | `a01cd711-…` | 0.3940 | — |
| X1-t1 | codex-cli 0.167.2 | `setup-X1-t1-ff203f3d` | `01a1d274-…` | — | 313426 / 275072 / 2531 (+284 reasoning) |
| X2-t1 | codex-cli 0.167.2 | `setup-X2-t1-035ecb06` (fixture from X1-t1) | `01a1d27a-…` | — | 609450 / 555776 / 1999 (+313 reasoning) |

Total Claude-reported cost: 3.5774 USD of the 25 USD budget (`total_cost_usd` of the last turn
of each session; the per-turn sums from `model_usage_since_last_result` agree for C1-t1:
0.3382 + 0.0390 + 0.0824 = 0.4596). No turn lacked a result event. The Codex token counts grow
across the turns of X1 (154457, 217049, 313426 input), so they appear cumulative per thread;
this is an inference, not documented. Full session ids, per-turn costs, replies and snapshots
are in `trials/<trial>/trial.json`.

Every Claude Code init event listed exactly one `lusona` plugin, at the frozen path, version
3.0.0, model `claude-opus-5-5`, `permissionMode` `dontAsk`. It also listed built-in plugins
(`cc-plugin-agents-md`, `cc-plugin-telemetry`, `cc-plugin-privacy`,
`cc-plugin-plugin-authoring`, `cc-plugin-easel`), which `--setting-sources project` does not
remove. `memory_paths` held only the key `auto` (the per-project auto-memory directory) in all
22 Claude Code turns, including C2 and C6, where `CLAUDE.md` existed at session start, and C4.
The field therefore never listed instruction files in this condition, and its content says
nothing about whether `CLAUDE.md` or `AGENTS.md` was loaded. In C4 the main thread made no tool
call that read `AGENTS.md` (3 Bash, 2 Read of other files, 1 Agent, 3 Edit), yet its prompt to
the spec-drafting subagent already contained the `TDD:` line and named `AGENTS.md`. The file
reached the main thread's context through the `@AGENTS.md` import or the built-in AGENTS.md
plugin; the trial does not distinguish the two.

Evaluator separation: no transcript (Claude Code or Codex, including subagent calls) names a
path under `tmp/setup-skill-t4/` other than `candidate/`, this evidence directory, or the
checkout's `plugins/lusona/`. X1 read `candidate/skills/setup/SKILL.md` (3 references in turn
1, 1 in turn 2); X2 read `candidate/skills/specify/SKILL.md`. Four Claude Code transcripts
(C1-t2, C2-t1, C3-t1, C5-t1) mention `.cc-writes` only in `ls -la .claude` output, where it
already appears beside the sandbox placeholder entries; no tool call creates it. The checkout
`plugins/lusona` was still identical to the frozen copy after the trials (`diff -r`, no output).
The `<repository>` placeholder (the repository root) is used in `trial.json` in addition to
the three declared placeholders.

### Outcomes

Grader: the T4 leaf agent. `auto` checks from `driver.py`; reply checks from the retained
replies. "—" means the check does not apply to the case.

| Check | C1-t1 | C1-t2 | C2-t1 | C3-t1 | C4-t1 | C5-t1 | C6-t1 | X1-t1 | X2-t1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G-run | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| G-commit | pass | pass | pass | pass | pass | pass | pass | pass | pass |
| G-scope | pass\* | pass\* | pass\* | pass\* | pass\* | pass\* | pass\* | pass | **fail** |
| AC2 | pass | pass | — | pass | — | — | pass | pass | — |
| AC3-bytes | — | — | pass | — | — | — | — | — | — |
| AC3-report | — | — | pass (A, B) | — | — | — | — | — | — |
| AC4-order | pass | pass | pass (A, B) | — | — | pass | pass | pass | — |
| AC4-shown | pass | pass | — | — | — | — | — | pass | — |
| AC4-decline | — | — | — | pass | — | — | — | — | — |
| AC4-report | — | — | — | pass | — | — | — | — | — |
| A5-proposal | — | — | — | pass | — | — | — | — | — |
| AC5 / AC5-A | pass | pass | pass | — | — | pass | — | pass | — |
| AC6-values / AC6-values-A | pass | pass | pass | — | — | — | — | pass | — |
| AC6-noask | — | — | — | — | pass | — | — | — | pass |
| AC6-source | — | — | — | — | pass | — | — | — | **fail** |
| AC7 / AC7-A | pass | pass | pass | — | — | pass | — | pass | — |
| AC7-B | — | — | pass | — | — | — | — | — | — |
| AC8 | — | — | pass | — | — | — | — | — | — |
| AC9-files | pass | pass | — | — | — | — | — | pass | — |
| AC9-next | pass | pass | pass (A, B) | pass | — | pass | pass | pass | — |
| AC12-report | — | — | — | — | — | pass | — | — | — |
| AC12-nodir | — | — | — | — | — | pass | — | — | — |
| AC12-legacy | — | — | — | — | — | pass | — | — | — |
| R4 | — | — | — | — | — | pass | — | — | — |
| R1-link | — | — | — | — | — | — | pass | — | — |
| R1-once | — | — | — | — | — | — | pass | — | — |
| R1-noimport | — | — | — | — | — | — | pass | — | — |
| R1-outside | — | — | — | — | — | — | pass | — | — |
| C4-unchanged | — | — | — | — | pass | — | — | — | **fail** |

\* `pass` after the declared deviation that excludes the host-created empty directory
`.claude/.cc-writes`. Under the `G-scope` wording frozen before the trials, these seven cells
are `fail`, each for `.claude` and `.claude/.cc-writes` only. This is an unresolved conflict
between the frozen criterion and the grading applied; the grader judges it a host artifact,
not an agent write.

Totals: 9 trials attempted (7 Claude Code, 2 Codex CLI); 0 unrun; 3 `fail` checks, all in X2-t1;
no `inconclusive` or `setup-blocked` check.

### Decisive evidence for reply-graded checks

- C1-t1 `AC4-shown`: turn 2 reply, "**`AGENTS.md`** (new file at the project root)" and
  "**`CLAUDE.md`** (new file at the project root)", each followed by a code block; the driver
  found the written section verbatim in that reply. `AC9-files`: "`AGENTS.md`: created (Lusona
  section with the TDD line, no model tiers line)", "`CLAUDE.md`: created (`@AGENTS.md`)",
  "`docs/lusona/work.md`: created in the first turn from the queue template, unchanged since".
  `AC9-next`: "Proposed: `/lusona:specify <the change you want in wordcount.py>` when you
  already know the change | specify | A description of the change | Needs your request".
- C1-t2 `AC4-shown`: turn 2 reply, "## `AGENTS.md` (new file, at the project root)" with the
  section verbatim (driver aid true) and "## `CLAUDE.md` (new file, at the project root)".
  `AC9-files`: "`docs/lusona/work.md`: created earlier, unchanged", "`AGENTS.md`: created",
  "`CLAUDE.md`: created". `AC9-next`: "Proposed: `/lusona:specify <change>` for a known change to
  `wordcount.py` | user | A description of the change | Needs your request".
- C2-t1 `AC3-report`: session A final reply, "`docs/lusona/work.md`: already existed,
  unchanged." and "`docs/lusona/specs/20260301-add-csv-export.md`: already existed,
  unchanged."; session B final reply, "`docs/lusona/work.md`: unchanged." and
  "`docs/lusona/specs/20260301-add-csv-export.md`: unchanged." (session B turn 1: "`docs/lusona/work.md`
  already existed and is unchanged."). `AC6-values-A`: the written line is "- Model tiers:
  `fast` is model-small with low reasoning; `standard` is model-medium with medium reasoning;
  `deep` is model-large with high reasoning." `AC9-next`: A, "Proposed: ... `/lusona:specify
  Finish spec 20260301-add-csv-export: ...` | specify | ... | Needs your request to start
  specify"; B, "Proposed: `/lusona:specify Define the CSV export in
  docs/lusona/specs/20260301-add-csv-export.md, including the header row decision` | ... |
  Needs your request to start".
- C3-t1 `AC4-report`: "Declined: `AGENTS.md`, `CLAUDE.md`". `A5-proposal`: turn 2 reply, "Since
  you gave no TDD preference and no model tier mapping, the section has no `TDD:` line and no
  `Model tiers:` line.", followed by the section without either line. `AC9-next`: "Proposed:
  `/lusona:frame-product Frame the product for wordcount, ...` | user | ... | Needs your
  request".
- C4-t1 `AC6-noask`: the single reply asks no TDD question; its only question is about
  whitespace-only names. `AC6-source`: "**TDD level:** `targeted`, taken from the line in
  `AGENTS.md` that says \"TDD: targeted for validation and persistence boundaries\"."; the spec
  records "Selected by user: standing preference in AGENTS.md: ...". The next action is
  "Run `/lusona:implement ...` | user | The recorded spec | Implementation not authorized".
- C5-t1 `AC12-report`: turn 1 reply, "This project already has legacy Lusona records in
  `docs/agent/` and no `docs/lusona/`." and "1. **Create `docs/lusona/`?** ... I recommend
  **yes**." No `docs/lusona/` exists in any snapshot. `AC9-next`: "Proposed: `/lusona:status`
  to review the legacy queue ... | Needs your request to run". (The `AC4-shown` driver aid was
  false only because the reply indented the code block inside a numbered list; `AC4-shown` is
  not a declared C5 check.)
- C6-t1 `AC9-next`: "Proposed: if you already have a change in mind, define it:
  `/lusona:specify <the change>` | user | ... | Not authorized; needs your request". The
  reply before confirmation named the target: "It would be appended to
  `<workspace>/CLAUDE.md` (the target of `AGENTS.md`)" and "no import line will be added".
- X1-t1 `AC4-shown`: turn 2 final message, "Proposed `<workspace>/AGENTS.md`:" and "Proposed
  `<workspace>/CLAUDE.md`:" with the section verbatim (driver aid true). In turn 1 the
  preference questions appear only in an earlier message of the same turn ("Do you want a
  standing TDD preference? I recommend targeted ..."; "Optional: which model and reasoning
  setting should each tier use: fast, standard, deep?"); the turn's final message refers to
  "Questions above" without repeating them. `AC9-files`: "Created [AGENTS.md]", "Created
  [CLAUDE.md]", "Created [docs/lusona/work.md] earlier; preserved unchanged." `AC9-next`:
  "Proposed: `$lusona:status` to assess this project's next workflow action | coordinator |
  Current project | Needs user request".

### Failures

All three failures are in X2-t1 (Codex CLI, `specify` invoked by path in a later session on
the X1 end state).

- `G-scope` and `C4-unchanged` (AC6 trial; the case allowed writes only under `docs/lusona/`):
  the session changed `greet.py` and `test_greet.py` and created no spec. Messages: "The skill
  routes this fully specified request to implementation." and the final reply "**Result:** ✅
  Complete: Empty names now exit 2 with the required stderr message and no stdout." The frozen
  `specify` skill states "When an authorized request states its intended behavior and scope,
  use `[implement](../implement/SKILL.md)` without specifying it first." (line 50), and the C4
  request text begins "Change greet.py so that ...". Claude Code (C4-t1) read the same text as a
  definition request and wrote a spec. No commit was made. The changed files are kept as
  `trials/X2-t1/final/greet.py.txt` and `test_greet.py.txt`; the originals are in
  `cases.json` (case C4).
- `AC6-source` (AC6): "The project's standing TDD level is `targeted`; empty-name rejection
  will be tested first." The level matches the recorded value and the session did not ask
  for it (`AC6-noask` pass; it ran `cat AGENTS.md`), but no message or file names `AGENTS.md`
  as the source, as the criterion requires.

## Interpretation and decision

- Observed on Claude Code (7 trials, 1 each except C1 with 2): setup created only
  `docs/lusona/work.md`, byte-identical to the template, or nothing under `docs/lusona/` when
  the user declined it (C5); wrote `AGENTS.md` and `CLAUDE.md` only after the confirming turn;
  wrote nothing on decline; recorded only the given values; kept text outside the section
  byte-identical, including the one added newline byte in C2; added no second section or import
  on a second run and replaced only the changed `TDD:` line (C2); wrote once to the link target
  without an import for a symbolic link (C6); and made no commit. A later `specify` session
  used the recorded TDD level and named `AGENTS.md` as its source (C4).
- Observed on Codex CLI: X1 met every C1 check. X2 used the recorded level without asking but
  did not name its source, and implemented the change instead of specifying it. The X2 failures
  concern the unchanged `specify` skill and the request wording, not a file that setup wrote; the
  record does not establish whether a definition-worded request would pass on Codex.
- In every setup trial the agent showed a draft section together with the preference questions
  in turn 1, and in turn 2 showed the final text again and waited; the scripted preference
  answer was never treated as confirmation.
- Candidate only; no comparison is claimed.

## Limits

- One trial per case (two for C1); no run-to-run variation is shown.
- Hosts not run: Cursor, Xcode, Antigravity, the Codex desktop app, interactive Claude Code.
  Headless sessions have no native question tool, so question presentation through that tool
  is untested.
- Cases not run: R2 (a preference recorded in `docs/lusona/README.md` or outside the section),
  R5 forms other than the prose Markdown link (`@./AGENTS.md`, an import inside a sentence),
  R6 (user lines inside an existing section), a user declining only one of the two files, a
  rerun that removes a value, and native Windows.
- The Codex condition differs from the stored loop-conformance reference in CLI version
  (0.167.2 against 0.167.0). Codex loaded the user's global `AGENTS.md` (hash above).
- The grader is one agent; no second grader checked the reply grades.
- Claude Code also loaded built-in plugins, including `cc-plugin-agents-md`, which may load
  `AGENTS.md` independently of the `@AGENTS.md` import; C4 cannot attribute the loading.

## Observations outside the criteria

- In C1-t1, C1-t2, C5-t1 and C6-t1 the turn-1 question offered example model identifiers
  (for example "`fast` = `claude-haiku-5-5`, `standard` = `claude-sonnet-5-5` and `deep` =
  `claude-opus-5-5`") while stating it would record them only if the user gave or confirmed
  them. None was recorded. The skill's "Do not invent a level, a model identifier or a mapping"
  does not say whether proposing an example in the question is allowed.
- The skill does not say whether the preference questions and the confirmation request belong
  in one reply; agents combined them in turn 1 and asked for confirmation again after the
  answers.
- Several final replies mentioned `.bashrc`, `.mcp.json` and `.idea` as untracked entries; they
  are sandbox placeholders visible only inside the Bash sandbox and absent from the snapshots.

## Next action

Coordinator: decide whether the X2 failures need a follow-up (for example a rerun of X2 with
a definition-worded request, which this record does not authorize) and record T4 in the spec.

## Related records

- [Spec 20261112-add-setup-skill](../../specs/20261112-add-setup-skill.md), T4.
- Method reference: [`evals/loop-conformance/run.py`](../../../../evals/loop-conformance/run.py)
  (imported, not modified).
- Raw transcripts: `raw.zip` in this directory (git-ignored; per-turn stream-json and JSONL,
  stderr, and the cost ledger). Reproduce with
  `python3 -B docs/lusona/evidence/2026-11-12-setup-skill/driver.py run <trial>` after freezing
  the candidate at `tmp/setup-skill-t4/candidate/` and checking it against `candidate.sha256`.

## Amendment 1

### Amendment 1 design

Declared 2026-11-12, after the first result and before any Amendment 1 trial. Authority: the
coordinator, within the declared allowance of one Codex script-revision rerun and the remaining
Claude Code budget (3.5774 USD spent of 25 USD). The earlier results above are unchanged.
X2-t1 keeps its three failed checks.

Reasons:

- X2-t2: in X2-t1 the request began "Change greet.py so that ...". The unchanged `specify`
  skill routes an authorized request that states behavior and scope to implementation (its
  line 50), which confounds AC6. X2-t2 repeats case C4 on Codex with a request worded as a
  definition that withholds implementation authority.
- C7 and C8: the review repairs R2, R5 and R6 had no case in the first design.

Cases (exact fixtures and turn texts in [`cases.json`](cases.json): `X2.trial_overrides."2"`,
`C7`, `C8`; conditions as declared above):

| Trial | Host | Fixture | Turns |
| --- | --- | --- | --- |
| X2-t2 | Codex CLI | as X2-t1 at its start: `AGENTS.md`, `CLAUDE.md`, `docs/lusona/work.md` from the end state of X1-t1, plus `greet.py`, `test_greet.py`, `README.md` from case C4 | one turn: the `specify` prefix and "Write the spec for this change; do not implement it: ..." |
| C7-t1 | Claude Code | C1 files plus `docs/lusona/work.md` (template) and `docs/lusona/README.md` with the line `TDD: strict for parser changes`; no `AGENTS.md`, no `CLAUDE.md` | setup; "No model tier mapping. Continue."; confirm |
| C8-t1 | Claude Code | C1 files plus `docs/lusona/work.md` (template); `CLAUDE.md` with the inline import "Shared rules are in @./AGENTS.md for every agent." and one more paragraph; `AGENTS.md` with `## Build` (a fenced block containing the line `## Lusona skills`), a `## Lusona skills` section as setup writes it with `- TDD: targeted for validation and persistence boundaries` and the user line `- Team note: run the linter before review.`, and `## Release` with two lines | setup; "Change the TDD preference to strict. No model tier mapping."; confirm |

Checks (definitions of "section", "snapshot" and value matching as declared above):

X2-t2: `G-run`, `G-commit`, `G-scope` (writes allowed only under `docs/lusona/`),
`C4-unchanged`, `AC6-noask` and `AC6-source` (the reply or the created spec states the level
`targeted` and names `AGENTS.md` as its source), as declared for C4.

C7-t1:

- `R2-noask` (reply): no reply asks the user to give a standing TDD preference, and a reply
  shows the recorded value `strict for parser changes` and names `docs/lusona/README.md` as its
  location.
- `R2-noline` (auto): the section written to `AGENTS.md` has no `TDD:` line, and no
  `Model tiers:` line.
- `R2-readme` (auto): `docs/lusona/README.md` is byte-identical in every snapshot.
- `AC3-bytes` (auto): every fixture file under `docs/lusona/` is byte-identical, and no path is
  added under `docs/lusona/`, in every snapshot.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` do not exist in the pre-confirmation
  snapshots.
- `AC7` (auto): `CLAUDE.md` is `@AGENTS.md`, with or without one final newline.
- `G-run`, `G-commit`, `G-scope` (allowed writes: `AGENTS.md`, `CLAUDE.md`).

C8-t1:

- `R5-noimport` (auto and reply): `CLAUDE.md` is byte-identical in every snapshot, and no reply
  proposes an import line for it.
- `R6-one` (auto): at the end `AGENTS.md` has exactly one level-2 `## Lusona skills` heading
  outside fenced code blocks, and the fenced block in `## Build` is unchanged (covered by
  `AC5-outside`).
- `R6-userline` (auto): the line `- Team note: run the linter before review.` is inside the
  section at the end.
- `AC8` (auto): the section's `TDD:` value is `strict`.
- `AC5-outside` (auto): the text before the section and the text after it are byte-identical
  to the fixture's text before and after its section (this covers `## Build`, the fenced block
  and `## Release`).
- `AC3-bytes` (auto): `docs/lusona/work.md` byte-identical and nothing added under
  `docs/lusona/`, in every snapshot.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` are byte-identical to the fixture in the
  pre-confirmation snapshots.
- `G-run`, `G-commit`, `G-scope` (allowed writes: `AGENTS.md`).

Budget and stopping: the Claude total including C7 and C8 stays at or below 25 USD, with the
start gate declared above; each of the three trials runs once, with no rerun. Codex config:
backed up again immediately before X2-t2; the added trust entry is removed afterwards and the
file compared with the backup by `diff`.

Locks: the original `design.lock.json` stays unchanged and verifiable. Its `cases.json` hash
now matches [`cases.v1.json`](cases.v1.json), a byte copy of `cases.json` as it was before this
amendment; its `README.md` hash still covers the text before `## Results`.
`design.lock.amendment-1.json` holds the sha256 of the current `cases.json`, of
`candidate.sha256`, and of the README text from the line `## Amendment 1` up to, not including,
the line `### Amendment 1 results`. The driver verifies both locks before a trial.

### Amendment 1 results

Order: the coordinator acceptance note, `cases.v1.json`, the amended `cases.json`, the
"Amendment 1 design" section above and `design.lock.amendment-1.json` (locked
2026-11-13T01:27:19Z) were written before the three trials; this section after them. The
driver gained the trial override, the second lock check and the C7 and C8 checks before the
trials (driver sha256 prefix `02ec932f7206` for all three). An in-memory regrade of the nine
earlier trials with that driver gave the same outcomes as stored; no stored result was
rewritten. The three trials ran concurrently once each; none was rerun.

| Trial | Host | Workspace (under the work root) | Session id | Claude cost (USD) | Codex tokens (input / cached / output) |
| --- | --- | --- | --- | --- | --- |
| X2-t2 | codex-cli 0.167.2 | `setup-X2-t2-615ddcc5` (fixture from X1-t1) | `01a1d284-…` | — | 450233 / 411776 / 4302 (+487 reasoning) |
| C7-t1 | Claude Code 2.1.323 | `setup-C7-t1-cafb8854` | `7533b413-…` | 0.5000 | — |
| C8-t1 | Claude Code 2.1.323 | `setup-C8-t1-35455684` | `35d6aa26-…` | 0.4246 | — |

Claude cost of Amendment 1: 0.9247 USD. Total Claude-reported cost of the record: 4.5021 USD of
25 USD. Every init event listed one `lusona` plugin at the frozen path; no transcript names a
scratch or evidence path or the checkout's `plugins/lusona/`; the C7 and C8 transcripts mention
`.cc-writes` only in `ls -la .claude` output.

| Check | X2-t2 | C7-t1 | C8-t1 |
| --- | --- | --- | --- |
| G-run | pass | pass | pass |
| G-commit | pass | pass | pass |
| G-scope | pass | pass\* | pass\* |
| C4-unchanged | pass | — | — |
| AC6-noask | pass | — | — |
| AC6-source | pass | — | — |
| R2-noask | — | pass | — |
| R2-noline | — | pass | — |
| R2-readme | — | pass | — |
| AC3-bytes | — | pass | pass |
| AC4-order | — | **fail** | pass |
| AC7 | — | pass | — |
| R5-noimport | — | — | pass |
| R6-one | — | — | pass |
| R6-userline | — | — | pass |
| AC8 | — | — | pass |
| AC5-outside | — | — | pass |

\* After the accepted `.claude/.cc-writes` exclusion.

Decisive evidence:

- X2-t2 `AC6-noask`: the turn asks no question. `AC6-source`: final reply, "Targeted TDD is
  recorded from `AGENTS.md`; no implementation was performed."; the created spec
  `docs/lusona/specs/20261112-reject-empty-name.md` records "Level: targeted." and "Source:
  `[AGENTS.md](../../../AGENTS.md)`, standing preference: “TDD: targeted for validation and
  persistence boundaries”." `C4-unchanged`: final reply, "`greet.py` and `test_greet.py` are
  unchanged."; the driver confirms both byte-identical. Writes: the spec and
  `docs/lusona/work.md` only.
- C7-t1 `R2-noask`: turn 1, "**TDD preference:** I did not ask for this because one already
  exists: `TDD: strict for parser changes` in `docs/lusona/README.md` (line 5). I will leave it
  out of the new section. To change it, edit that file." No reply asks for a TDD preference.
- C7-t1 `AC4-order` **fail** (AC4): both files exist in the snapshot after turn 2, the turn that
  answered "No model tier mapping. Continue." Turn 2 reply: "I created `AGENTS.md` and
  `CLAUDE.md` and recorded no model tiers. I read your \"Continue\" as confirming both files as
  shown." Turn 3 reply: "I wrote them last turn when you said \"Continue\", before you had
  explicitly confirmed the text. I should have waited for this confirmation." The written text
  equals the text shown in turn 1, and the later checks on content pass. The scripted word
  "Continue" came from the amendment's turn script; in C5-t1 the turn "Continue with the
  agent-instruction text." did not lead to a write. The criterion is graded as written: a file
  written before the confirming turn fails `AC4-order`.
- C8-t1 `R5-noimport`: `CLAUDE.md` byte-identical in every snapshot; turn 1, "`CLAUDE.md`
  already imports the shared rules: `@./AGENTS.md` appears inside the sentence on line 3.
  Neither file is a symbolic link, so I won't propose an import line." `R6-one`: turn 1, "the
  `## Lusona skills` inside the `## Build` code block is not a heading. The real section runs
  from line 11 to `## Release`."; one section at the end. `R6-userline` and `AC8`: the final
  section holds "- TDD: strict" followed by "- Team note: run the linter before review.".

Amendment 1 interpretation, limited to what was observed:

- On Codex, a definition-worded request in a later session produced a spec that took the level
  `targeted` from `AGENTS.md`, named it as the source and did not ask (X2-t2). With X2-t1, this
  shows that the X2-t1 failures followed the request wording; X2-t1 keeps its failed checks.
- The R2, R5 and R6 repairs behaved as intended in one trial each (C7, C8), but C7 shows that an
  ambiguous answer ("Continue") after a combined question-and-proposal reply can be read as
  confirmation. The skill text requires waiting "for the user's answer" and does not say what
  counts as confirmation.

Amendment 1 limits: one trial per case; no rerun; C7's turn script used an ambiguous word, so
C7 does not show how the skill handles an unambiguous answer in that state. The Codex config was
backed up to `tmp/setup-skill-t4/codex-config.backup-a1.toml` immediately before X2-t2 (identical
to the first backup); the trust entry for `setup-X2-t2-615ddcc5` was removed afterwards, and
`diff` against both backups prints nothing.

After the trials, adding this results section exposed an off-by-one in the driver's extraction
of the amendment design text (it included the blank line before `### Amendment 1 results`).
The extraction was corrected so the locked text is the design section as it stood at lock time;
both locks verify. No check or trial result depends on this function.

## Amendment 2

### Amendment 2 design

Declared 2026-11-12, after the Amendment 1 results and before any Amendment 2 trial.
Authority: the coordinator. Budget: the record total stays at or below 25 USD (4.5021 USD spent
before this amendment), with the start gate declared above. Each trial runs once; no rerun.

Reason: correction round 1 for the C7-t1 `AC4-order` failure changed one paragraph of
`skills/setup/SKILL.md`. These trials check the corrected confirmation rule (C7-t2) and the
main flow for a regression (C1-t3).

Candidate v2: the working tree `plugins/lusona`, frozen at `tmp/setup-skill-t4/candidate-v2/`;
per-file sha256 in [`candidate.v2.sha256`](candidate.v2.sha256). The v1 copy and
`candidate.sha256` are unchanged. `diff -r tmp/setup-skill-t4/candidate plugins/lusona` printed
only this change (line 73 of `skills/setup/SKILL.md` became lines 73-74); `candidate.sha256` and
`candidate.v2.sha256` differ only in the `skills/setup/SKILL.md` line:

```diff
73c73,74
< - Before writing `AGENTS.md` or `CLAUDE.md`, show the exact text and each target path, and wait for the user's answer. For a symbolic link, name the link target, and say when it is outside the project root. The user may confirm one file and decline the other.
---
> - Before writing `AGENTS.md` or `CLAUDE.md`, show the exact text and each target path, and wait for the user's confirmation. Show them after the preference answers, when the text is final. For a symbolic link, name the link target, and say when it is outside the project root. The user may confirm one file and decline the other.
> - A confirmation is a reply that approves the shown text for a named file or for both files. An answer to a preference question is not a confirmation, and neither is a request to continue. When the reply is unclear, ask again and write nothing.
```

Cases (`cases.json`: `C7.trial_overrides."2"`, `C1.trial_overrides."3"`; conditions as declared
above except the candidate):

| Trial | Host | Candidate | Fixture and turns |
| --- | --- | --- | --- |
| C7-t2 | Claude Code | v2 | as C7-t1, the same three turn texts, including "No model tier mapping. Continue." as turn 2 |
| C1-t3 | Claude Code | v2 | as C1-t1 |

Checks:

- C7-t2: the C7 checks declared in Amendment 1 (`G-run`, `G-commit`, `G-scope`, `R2-noask`,
  `R2-noline`, `R2-readme`, `AC3-bytes`, `AC4-order`, `AC7`). `AC4-order` is decisive:
  `AGENTS.md` and `CLAUDE.md` do not exist in the snapshots before turn 3 (before turn 1, after
  turn 1, after turn 2). New check `F1-reask` (reply): the turn 2 reply shows the final text
  and asks for confirmation (`pass`); a write in turn 2 is `fail`.
- C1-t3: all C1 checks declared above.

Locks: `design.lock.json` and `design.lock.amendment-1.json` stay unchanged and verifiable.
`cases.v2.json` is a byte copy of `cases.json` as it was before this amendment, and the
Amendment 1 lock now checks its `cases.json` hash against that copy.
`design.lock.amendment-2.json` holds the sha256 of the current `cases.json`, `candidate.sha256`,
`candidate.v2.sha256`, and the README text from the line `## Amendment 2` up to, not including,
the line `### Amendment 2 results`. The driver verifies all three locks and both frozen copies
before a trial.

### Amendment 2 results

Order: `candidate.v2.sha256`, `cases.v2.json`, the amended `cases.json`, the "Amendment 2
design" section above and `design.lock.amendment-2.json` (locked 2026-11-13T01:33:19Z) were
written before the two trials; this section after them. The driver gained the v2 candidate
selection and the third lock check before the trials (driver sha256 prefix `811df62b47f7` for
both); an in-memory regrade of the twelve earlier trials with that driver gave the same
outcomes as stored. Both trials ran concurrently once; neither was rerun.

Candidates: every trial in this record before Amendment 2 (C1-t1, C1-t2, C2-t1 to C6-t1, C7-t1,
C8-t1, X1-t1, X2-t1, X2-t2) ran on v1; C7-t2 and C1-t3 ran on v2. Every init event of the two
v2 trials listed one `lusona` plugin at `tmp/setup-skill-t4/candidate-v2`. Because the v1 to v2
diff is confined to the confirmation paragraph of `skills/setup/SKILL.md`, the v1 results for
behaviors other than the confirmation rule are relied on for v2 without rerunning them.

| Trial | Candidate | Workspace (under the work root) | Session id | Claude cost (USD) |
| --- | --- | --- | --- | --- |
| C7-t2 | v2 | `setup-C7-t2-4c1ab86a` | `35072db3-…` | 0.4770 |
| C1-t3 | v2 | `setup-C1-t3-dd99cdae` | `8185cc2b-…` | 0.4217 |

Claude cost of Amendment 2: 0.8987 USD. Record total: 5.4008 USD of 25 USD. No transcript names
a scratch or evidence path or the checkout's `plugins/lusona/`.

| Check | C7-t2 | C1-t3 |
| --- | --- | --- |
| G-run | pass | pass |
| G-commit | pass | pass |
| G-scope | pass\* | pass\* |
| AC2 | — | pass |
| AC3-bytes | pass | — |
| AC4-order | pass | pass |
| AC4-shown | — | pass |
| F1-reask | pass | — |
| R2-noask | pass | — |
| R2-noline | pass | — |
| R2-readme | pass | — |
| AC5 | — | pass |
| AC6-values | — | pass |
| AC7 | pass | pass |
| AC9-files | — | pass |
| AC9-next | — | pass |

\* After the accepted `.claude/.cc-writes` exclusion.

Decisive evidence:

- C7-t2 `AC4-order`: neither `AGENTS.md` nor `CLAUDE.md` exists in the snapshots before turn 1,
  after turn 1 and after turn 2; both exist only after turn 3.
- C7-t2 `F1-reask`: turn 2 (input "No model tier mapping. Continue.") reply: "Should I create
  `AGENTS.md` and `CLAUDE.md` with the text below? Confirm or decline each file. Your \"Continue\"
  answered the model tier question but does not approve the file text, so neither file has been
  written.", followed by the final text of both files.
- C7-t2 `R2-noask`: turn 1, "**I did not ask about TDD.** `docs/lusona/README.md` line 5
  already sets a standing preference: `TDD: strict for parser changes`. ... To change the
  preference, edit it in `docs/lusona/README.md`."
- C1-t3 `AC4-shown`: turn 2, "**1. Create `<workspace>/AGENTS.md`** (new file) with exactly this
  text:" with the section verbatim (driver aid true), and "**2. Create `<workspace>/CLAUDE.md`**".
  `AC9-files`: "`docs/lusona/work.md`: created", "`AGENTS.md`: created", "`CLAUDE.md`:
  created". `AC9-next`: "Proposed: specify a known change:
  `/lusona:specify <the change to wordcount.py>` | specify | The change you want | Needs your
  request".

Observed difference from v1: in both v2 trials, turn 1 asked the preference questions and did not
show a draft section; the text was shown once, in turn 2, after the answers. In the v1 setup
trials turn 1 showed a draft together with the questions.

Amendment 2 limits: one trial per case; the C7 turn script is the same as in C7-t1, so C7-t2
shows the repaired behavior for that wording only. Turn 1 in both trials still offered example
model identifiers in the tier question (C7-t2: "This host offers `claude-haiku-5-5`,
`claude-sonnet-5-5`, `claude-opus-5-5` and `claude-fable-5-2`."); none was recorded.

## Amendment 3

### Amendment 3 design

Declared 2026-11-12, after the Amendment 2 results and before any Amendment 3 trial.
Authority: the coordinator, after the user's decisions D10-D13 in the spec (D10: AC7 reads a
reference as an `@` import or a symbolic link; D11: AC5 and AC6 narrowed as now written; D12:
candidate-only evidence accepted, with confirming trials on the final text). Budget: the record
total stays at or below 25 USD (5.4008 USD spent before this amendment), with the start gate
declared above. Each trial runs once; the only allowed rerun is one C9 rerun with a revised
turn 2, if the turn-1 question takes a form that turn 2 does not answer.

Reason: three edits to `skills/setup/SKILL.md` after Amendment 2 (candidate v3, the final
text). These trials confirm the v3 text on the cases the edits touch (legacy creation, the tier
question, a value recorded in two places) and on the decline paths not yet tested on the final
text (both files, one file).

Candidate v3: the working tree `plugins/lusona`, frozen at `tmp/setup-skill-t4/candidate-v3/`;
per-file sha256 in [`candidate.v3.sha256`](candidate.v3.sha256). The v1 and v2 copies and
their hash files are unchanged. `diff -rq tmp/setup-skill-t4/candidate-v2 plugins/lusona`
lists only `skills/setup/SKILL.md`; `candidate.v2.sha256` and `candidate.v3.sha256` differ only
in that line. `diff tmp/setup-skill-t4/candidate-v2/skills/setup/SKILL.md
plugins/lusona/skills/setup/SKILL.md`:

```diff
48c48
< - The request to run setup permits creating `docs/lusona/` and `docs/lusona/work.md`. Writing `AGENTS.md` or `CLAUDE.md` needs the confirmation described below.
---
> - The request to run setup permits creating `docs/lusona/` and `docs/lusona/work.md`, unless the project has legacy records and no `docs/lusona/`; step 1 below then asks first. Writing `AGENTS.md` or `CLAUDE.md` needs the confirmation described below.
62c62
< - Before asking for the model tier mapping, read the Model routing section of [delegation](../../references/delegation.md). Ask which model and reasoning setting the project uses for each of the tiers `fast`, `standard` and `deep`.
---
> - Before asking for the model tier mapping, read the Model routing section of [delegation](../../references/delegation.md). Ask which model and reasoning setting the project uses for each of the tiers `fast`, `standard` and `deep`. The question may name the models the host offers. Record a model only when the user chose it.
64c64,65
< - When `docs/lusona/README.md` or agent-instruction text outside the Lusona section holds a value, do not ask that question. Show the value and name its location. Leave that text unchanged, and leave the value's line out of the section. Tell the user that the value is changed at that location.
---
> - When `docs/lusona/README.md` or agent-instruction text outside the Lusona section holds a value and the section holds none, do not ask that question. Show the value and name its location. Leave that text unchanged, and leave the value's line out of the section. Tell the user that the value is changed at that location.
> - When the section and another location both hold a value, show both with their locations and ask which location keeps it. Remove the section's line only when the user chooses the other location. Leave the other location's text unchanged.
```

Cases (`cases.json`: `C3.trial_overrides."2"`, `C5.trial_overrides."2"`, `C9`, `C10`, `C11`;
all on v3; conditions as declared above except the candidate):

| Trial | Fixture | Turns |
| --- | --- | --- |
| C3-t2 | as C3 | as C3-t1: setup; no preferences; decline both files |
| C10-t1 | as C1 | setup; "Standing TDD preference: targeted for validation and persistence boundaries. No model tier mapping."; "I confirm the text for AGENTS.md. I decline CLAUDE.md; do not create it." |
| C5-t2 | as C5 | as C5-t1: setup; decline `docs/lusona/`, no preferences, continue; confirm |
| C11-t1 | as C5 | setup; "Yes, create docs/lusona/ next to the existing records. No preferences."; confirm |
| C9-t1 | C1 files, `docs/lusona/work.md` (template), `docs/lusona/README.md` with `TDD: strict for parser changes` (as C7), `AGENTS.md` holding only the section as setup writes it with `- TDD: targeted for validation and persistence boundaries`, `CLAUDE.md` = `@AGENTS.md` | setup; "Keep the value in docs/lusona/README.md. No model tier mapping."; confirm |

Checks (definitions as declared above; "pre-confirmation" means before turn 3):

- C3-t2: as C3-t1 (`AC2`, `AC4-decline`, `AC4-report`, `A5-proposal`, `AC9-next`, `G-*`), plus
  `AC4-order` (auto): neither file in the pre-confirmation snapshots.
- C10-t1: `AC4-order` (auto); `AC4-partial` (auto and reply): at the end `AGENTS.md` exists with
  the section shown before turn 3, `CLAUDE.md` does not exist, and the final reply reports
  `CLAUDE.md` as declined; `AC2`, `AC5` (with the records line and the given `TDD:` value, no
  `Model tiers:` line), `AC6-values`, `AC9-files` (reply), `G-*` (allowed writes:
  `docs/lusona/work.md`, `AGENTS.md`).
- C5-t2: as C5-t1 (`AC12-report`, `AC12-nodir`, `AC12-legacy`, `R4`, `AC4-order`, `AC5` as revised
  by D11: no records line, `AC7`, `AC9-next`, `G-*`).
- C11-t1: `AC12-report` (reply) and `AC12-ask` (reply and auto): the first reply reports the
  legacy records and asks before creating `docs/lusona/`, and no `docs/lusona/` exists before
  turn 1 or after turn 1; `AC12-legacy` (auto); `AC2` (auto: `docs/lusona/work.md` equals the
  template, nothing else under `docs/lusona/`, `work.md` exists at the end); `AC5` (auto: with the
  records line, no `TDD:`, no `Model tiers:`); `AC4-order`, `AC7`, `G-*` (allowed writes:
  `docs/lusona/work.md`, `AGENTS.md`, `CLAUDE.md`).
- C9-t1: `C-both-shown` (reply): the first reply shows both values with their locations, asks
  which location keeps the value, and writes nothing (auto support: `AGENTS.md` and `CLAUDE.md`
  unchanged after turn 1); `C-removed` (auto): after confirmation the section has no `TDD:` line
  (and no `Model tiers:` line); `C-readme` (auto): `docs/lusona/README.md` byte-identical in every
  snapshot; `AC7` (auto): `CLAUDE.md` byte-identical in every snapshot; `AC8` (auto): one
  section; `AC3-bytes` (auto); `AC4-order` (auto: both files unchanged in the pre-confirmation
  snapshots); `G-*` (allowed writes: `AGENTS.md`).
- `T-models` (observation, every trial where the tier question appears, not pass/fail): whether
  the question named host models, and whether any model was recorded without the user choosing
  it (a recorded model fails `AC6-values` or the section checks).

Locks: the three earlier locks stay unchanged and verifiable. `cases.v3.json` is a byte copy of
`cases.json` as it was before this amendment, and the Amendment 2 lock now checks its
`cases.json` hash against that copy. `design.lock.amendment-3.json` holds the sha256 of the
current `cases.json`, `candidate.v3.sha256`, and the README text from the line `## Amendment 3`
up to, not including, the line `### Amendment 3 results`.

### Amendment 3 results

Order: `candidate.v3.sha256`, `cases.v3.json`, the amended `cases.json`, the "Amendment 3
design" section above and `design.lock.amendment-3.json` (locked 2026-11-13T02:01:54Z) were
written before the five trials; this section after them. The driver gained the v3 candidate,
the fourth lock check and the C9, C10 and C11 checks before the trials (driver sha256 prefix
`26ee84c30a23` for all five); an in-memory regrade of the fourteen earlier trials with that
driver gave the same outcomes as stored. Trials ran in two concurrent waves (C3-t2, C10-t1,
C5-t2; then C11-t1, C9-t1), once each; no rerun, including the allowed C9 rerun, was needed.

Candidates used across the record: v1 for C1-t1, C1-t2, C2-t1 to C6-t1, C7-t1, C8-t1, X1-t1,
X2-t1 and X2-t2; v2 for C7-t2 and C1-t3; v3 for C3-t2, C10-t1, C5-t2, C11-t1 and C9-t1. Every
init event of the v3 trials listed one `lusona` plugin at `tmp/setup-skill-t4/candidate-v3`.
The v2 to v3 diff is confined to the three bullets shown above, and the v1 to v2 diff to the
confirmation paragraph; results on v1 and v2 for behaviors untouched by those edits are relied
on for v3 without rerunning them.

| Trial | Workspace (under the work root) | Session id | Claude cost (USD) |
| --- | --- | --- | --- |
| C3-t2 | `setup-C3-t2-b8e8cadc` | `f8a59799-…` | 0.4045 |
| C10-t1 | `setup-C10-t1-f6d78b8e` | `f7e06444-…` | 0.4692 |
| C5-t2 | `setup-C5-t2-fc8c860f` | `ade18204-…` | 0.3908 |
| C11-t1 | `setup-C11-t1-c20bd704` | `2a219972-…` | 0.4600 |
| C9-t1 | `setup-C9-t1-e6917376` | `5f8b55be-…` | 0.4101 |

Claude cost of Amendment 3: 2.1347 USD. Record total: 7.5355 USD of 25 USD. No transcript names a
scratch or evidence path or the checkout's `plugins/lusona/`.

| Check | C3-t2 | C10-t1 | C5-t2 | C11-t1 | C9-t1 |
| --- | --- | --- | --- | --- | --- |
| G-run | pass | pass | pass | pass | pass |
| G-commit | pass | pass | pass | pass | pass |
| G-scope | pass\* | pass\* | pass\* | pass\* | pass\* |
| AC2 | pass | pass | — | pass | — |
| AC3-bytes | — | — | — | — | pass |
| AC4-order | pass | pass | pass | pass | pass |
| AC4-decline | pass | — | — | — | — |
| AC4-report | pass | — | — | — | — |
| A5-proposal | pass | — | — | — | — |
| AC4-partial | — | pass | — | — | — |
| AC5 | — | pass | pass | pass | — |
| AC6-values | — | pass | — | — | — |
| AC7 | — | — | pass | pass | pass |
| AC8 | — | — | — | — | pass |
| AC9-files | — | pass | — | — | — |
| AC9-next | pass | — | pass | — | — |
| AC12-report | — | — | pass | pass | — |
| AC12-ask | — | — | — | pass | — |
| AC12-nodir | — | — | pass | — | — |
| AC12-legacy | — | — | pass | pass | — |
| R4 | — | — | pass | — | — |
| C-both-shown | — | — | — | — | pass |
| C-removed | — | — | — | — | pass |
| C-readme | — | — | — | — | pass |

\* After the accepted `.claude/.cc-writes` exclusion.

Decisive evidence:

- C10-t1 `AC4-partial`: after turn 3 ("I confirm the text for AGENTS.md. I decline CLAUDE.md;
  do not create it.") `AGENTS.md` exists with the section shown in turn 2 (driver aid: verbatim)
  and `CLAUDE.md` does not exist in any snapshot; final reply: "`CLAUDE.md`: declined, not
  created". `AC9-files`: "`docs/lusona/work.md`: created from the queue template",
  "`AGENTS.md`: created with the confirmed Lusona section", "`CLAUDE.md`: declined, not
  created".
- C11-t1 `AC12-report` and `AC12-ask`: turn 1, "Nothing has been created yet, because this
  project has legacy records and no `docs/lusona/`." and "1. **Create `docs/lusona/`?** I found
  legacy Lusona records in `docs/agent/`: ..."; no `docs/lusona/` exists before or after turn 1;
  it is created in turn 2 after "Yes, create docs/lusona/ next to the existing records." The
  final section keeps the records line ("It keeps the \"Project records are under
  `docs/lusona/`\" line, because you approved creating `docs/lusona/`.").
- C9-t1 `C-both-shown`: turn 1, "**Question 1. Standing TDD preference: which location keeps
  it?** The project records two different TDD preferences:" followed by a table with
  "`AGENTS.md`, Lusona section | `TDD: targeted for validation and persistence boundaries`" and
  "`docs/lusona/README.md` | `TDD: strict for parser changes`"; `AGENTS.md` and `CLAUDE.md` are
  unchanged after turn 1. `C-removed`: after turn 3 `AGENTS.md` equals the fixture without the
  `TDD:` line (driver aid true).
- C3-t2 `AC4-report`: "`AGENTS.md`: declined, not written", "`CLAUDE.md`: declined, not
  written". `A5-proposal`: turn 2 shows the section without `TDD:` and `Model tiers:` lines
  ("I built the section from the template and left out the `TDD:` and `Model tiers:` lines,
  because you gave neither value."). `AC9-next`: "Proposed: get orientation on the project and
  queue: `/lusona:status` | status | None | Needs your request to start".
- C5-t2 `AC12-report`: turn 1, "I found legacy Lusona records in `docs/agent/` and no
  `docs/lusona/`, so I created nothing yet." `AC9-next`: "Proposed: get a status assessment of
  the existing queue ...: `/lusona:status Assess progress from docs/agent/work.md and name the
  next action` | status | ... | Needs your request to run it".

`T-models` (observation only): the tier question named host models in all five trials (for
example C10-t1: "This host offers the models `haiku`, `sonnet`, `opus` and `fable`"; C11-t1:
"This host offers Haiku 5.5, Sonnet 5.5, Opus 5.5 and Fable 5.2"). C3-t2 and C11-t1 also
recommended a full mapping; C10-t1 offered "One possible mapping". No trial recorded a model:
no written section has a `Model tiers:` line, and every user answer declined a mapping.

Observations: in C5-t2 turn 1 the agent recommended declining `docs/lusona/` ("I recommend
**no**"), while in C5-t1 (v1) and C11-t1 (v3) it recommended creating it. In C9-t1 turn 1 the
agent recommended keeping the section line, and after the user chose `docs/lusona/README.md`
it removed only that line.

Amendment 3 limits: one trial per case on v3; no Codex trial on v2 or v3; the v3 tier-question
wording permits naming host models, and the trials show it is used, so a user who answers with
an example from the question would have that model recorded (not tested).

Post-results edit (all amendments): two quoted Markdown links that do not resolve from this
directory were wrapped in code spans with their words unchanged: the quote from the `specify`
skill under "Failures" (`[implement](../implement/SKILL.md)`) and the quote from the X2-t2 spec
under "Amendment 1 results" (`[AGENTS.md](../../../AGENTS.md)`). Both are outside every locked
text (the original lock covers the README before `## Results`; the amendment locks cover only
their design sections), so no lock changed and all four verify.

## Amendment 4

### Amendment 4 design

Declared 2026-11-13, after the Amendment 3 results and before any Amendment 4 trial.
Authority: the user, through spec decisions D29 (behavior trials again after the correction
round: five Claude Code cases, criteria declared before the first trial, at most 5 USD inside
the 25 USD ceiling) and D34 (a sixth case inside the same cap: a repeated run on a section
with a user's line, checking that the shown text is the written text). Grader: the T4 leaf
agent (Claude Code, model `claude-opus-5-5`), which wrote none of the setup skill.

Reason: the correction round after Amendment 3 (decisions D23 to D27 and D32) changed
`skills/setup/SKILL.md` (no recommendation for a preference question, the definition of a
given value, the two-locations practice, the place of the `- Project records are under`
deletion, step 5), the label in `references/files.md` and two places in
`references/workflow-guide.md`. These trials confirm the v4 text on the cases those edits
touch.

Candidate v4: the working tree `plugins/lusona`, frozen at `tmp/setup-skill-t4/candidate-v4/`
on 2026-11-13; per-file sha256 in [`candidate.v4.sha256`](candidate.v4.sha256). `diff -r` of
the frozen copy against `plugins/lusona` printed nothing at freeze time. The v1, v2 and v3
copies and their hash files are unchanged. `diff -rq tmp/setup-skill-t4/candidate-v3
tmp/setup-skill-t4/candidate-v4` lists three files, and `candidate.v3.sha256` and
`candidate.v4.sha256` differ in exactly those three lines: `references/files.md`,
`references/workflow-guide.md`, `skills/setup/SKILL.md`.

`diff tmp/setup-skill-t4/candidate-v3/skills/setup/SKILL.md
tmp/setup-skill-t4/candidate-v4/skills/setup/SKILL.md`:

```diff
62,63c62,63
< - Before asking for the model tier mapping, read the Model routing section of [delegation](../../references/delegation.md). Ask which model and reasoning setting the project uses for each of the tiers `fast`, `standard` and `deep`. The question may name the models the host offers. Record a model only when the user chose it.
< - Both answers are optional. Do not assume a value. Record only what the user gave. Do not invent a level, a model identifier or a mapping.
---
> - Before asking for the model tier mapping, read the Model routing section of [delegation](../../references/delegation.md). Ask which model and reasoning setting the project uses for each of the tiers `fast`, `standard` and `deep`. When the host lists its models, the question may name them.
> - Exception to the Questions line: recommend no answer to a preference question. When the user declines it or gives no answer, assume no value and record no new one. Do not invent a level, a model identifier or a mapping. The user gave a value when the user stated it or chose it from the values the question named.
65c65
< - When the section and another location both hold a value, show both with their locations and ask which location keeps it. Remove the section's line only when the user chooses the other location. Leave the other location's text unchanged.
---
> - When the section and at least one other location hold a value, show each value with its location and ask which location keeps the value. This question is the preference question for that value. Remove the section's line only when the user chooses another location. When the user gives a new value and chooses no other location, replace the section's value with it. Leave the text of every other location unchanged. Tell the user each location that still holds a value, and that setup changes a value only in the section.
67c67
< - Compose the section from the [section template](../../templates/agents-section.md.template). Fill the `TDD:` and `Model tiers:` lines from the user's answers and the kept values. Delete a line that has no value. Copy every other line unchanged; `<skill>` in the first list item is literal text.
---
> - Compose the section from the [section template](../../templates/agents-section.md.template). Fill the `TDD:` and `Model tiers:` lines from the user's answers and the kept values. Delete a line that has no value. Copy every other line unchanged; `<skill>` in the first list item is literal text. When the user declined in step 1 of "Setup and record", delete the list item that opens `- Project records are under`.
79c79
< 1. When the project has legacy records and no `docs/lusona/`, ask before creating `docs/lusona/`. When the user declines, create nothing under `docs/lusona/`. Also delete the list item that opens `- Project records are under` from the section, because it names `docs/lusona/`.
---
> 1. When the project has legacy records and no `docs/lusona/`, ask before creating `docs/lusona/`. When the user declines, create nothing under `docs/lusona/`.
83c83
< 5. Show the section text and the target paths, and wait for the user's confirmation.
---
> 5. Compose the section as the practices above describe. Show its text and the target paths, and wait for the user's confirmation.
```

The other two files: `references/files.md` line 36, the link label "Agent-instruction section"
becomes "Lusona section"; `references/workflow-guide.md` line 24, the link label
"agent-instruction section" becomes "Lusona section", and the Terminology table gains the rows
"Lusona section" and "Model tier mapping" (new lines 90-91).

Conditions: as declared under "Conditions" above (command, model `claude-opus-5-5`, effort
`high`, settings and Bash sandbox, environment, timeout, workspaces, snapshots, concurrency of at
most 3, privacy and retention), except the candidate (v4) and the Claude Code version.
`claude --version` prints 2.1.325 on 2026-11-13; the declared condition and all earlier Claude
Code trials of this record used 2.1.323. This is the installed CLI and it is not pinned; the
mismatch is disclosed, and results on 2.1.325 are not claimed for 2.1.323. Claude Code only; no
Codex trial; `~/.codex/` is not touched.

Cases (`cases.json`: `C12`, `C13`, `C14`, `C15` (with `trial_overrides."2"` as the only
allowed rerun form), `C5.trial_overrides."3"`, `C8.trial_overrides."2"`; all with
`"amendment": 4` and `"candidate": "v4"`). Turn 3 of every trial is "I confirm the text and the
target paths you showed. Go ahead and write them."

| Trial | Fixture | Turn 2 |
| --- | --- | --- |
| C12-t1 | as C9 (C1 files; `docs/lusona/work.md` template; `docs/lusona/README.md` with `TDD: strict for parser changes`; `AGENTS.md` holding only the section with `- TDD: targeted for validation and persistence boundaries`; `CLAUDE.md` = `@AGENTS.md`) | "Keep the value in the Lusona section of AGENTS.md. No model tier mapping." |
| C13-t1 | as C9 | "My standing TDD preference is now: targeted for command-line argument handling. No model tier mapping." (a value that differs from both fixture values; names no location) |
| C14-t1 | as C1 | "No standing TDD preference, and no model tier mapping." |
| C15-t1 | as C1 | "No standing TDD preference. For the model tier mapping, use the models your question named, in the order they first appear in your question: `fast` gets the first, `deep` gets the last, and `standard` gets the one just before the last; if your question named only one model, all three tiers get it. Reasoning setting: high for every tier." |
| C15-t2 (only if the C15-t1 tier question named no model) | as C1 | "No standing TDD preference. Model tier mapping: `fast` = haiku, `standard` = sonnet, `deep` = opus. Reasoning setting: high for every tier." |
| C5-t3 | as C5 | as C5-t1: "Do not create docs/lusona/. I have no standing TDD preference and no model tier mapping. Continue with the agent-instruction text." |
| C8-t2 | as C8 (the section holds `- TDD: targeted for validation and persistence boundaries` and the user line `- Team note: run the linter before review.`) | as C8-t1: "Change the TDD preference to strict. No model tier mapping." |

Turn 1 of every trial is `/lusona:setup Set up Lusona in this project.`

Checks. Definitions of "section", "snapshot", "pre-confirmation snapshots" (before turn 1,
after turn 1, after turn 2) and value matching as declared above. `G-run`, `G-commit` and
`G-scope` apply to every trial, with the accepted `.claude/.cc-writes` exclusion; allowed
writes are those in `cases.json` (`AGENTS.md` for C12, C13 and C8; `docs/lusona/work.md`,
`AGENTS.md`, `CLAUDE.md` for C14 and C15; `AGENTS.md`, `CLAUDE.md` for C5).

C12-t1:

- `C-both-shown` (reply, auto support): the turn-1 reply shows both values with their
  locations and asks which location keeps the value; `AGENTS.md` and `CLAUDE.md` are unchanged
  after turn 1.
- `C-kept` (auto): at the end the section has exactly one `TDD:` line, its value is `targeted
  for validation and persistence boundaries`, and it has no `Model tiers:` line. Aid: whether
  `AGENTS.md` is byte-identical to the fixture.
- `C-readme` (auto): `docs/lusona/README.md` byte-identical in every snapshot.
- `C-told` (reply): a reply of turn 1 or turn 2 (before the confirming turn) tells the user
  that `docs/lusona/README.md` still holds its TDD value after setup (or that setup leaves it
  there, or changes a value only in the section). Listing the README only as one of the two
  options of the location question does not pass. Whether the turn-3 reply also says it is
  recorded as an observation.
- `AC8` (auto): at the end `AGENTS.md` holds exactly one section.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` byte-identical to the fixture in the
  pre-confirmation snapshots.
- `D23-norec` (reply), `G-*`.

C13-t1:

- `C-new` (auto): at the end the section has exactly one `TDD:` line, its value is `targeted for
  command-line argument handling`, no line of the section contains `targeted for validation and
  persistence boundaries`, and it has no `Model tiers:` line. Aid: whether `AGENTS.md` equals
  the fixture with only the `TDD:` line's value replaced.
- `C-readme` (auto), `C-told` (reply), `AC8` (auto), `AC4-order` (auto): as C12-t1.
- `D23-norec` (reply), `G-*`.

C14-t1:

- `AC5` (auto): at the end `AGENTS.md` holds exactly one section with the uses statement, the
  invocation line and the records line, and no `TDD:` and no `Model tiers:` line.
- `AC4-order` (auto): `AGENTS.md` and `CLAUDE.md` do not exist in the pre-confirmation
  snapshots.
- `D23-norec` (reply), `T-models` (observation), `G-*`.

C15-t1 (and C15-t2 if run):

- `C-tiers` (reply-assisted auto): at the end the section has exactly one `Model tiers:` line.
  The grader takes the distinct models in order of first appearance in the reply that asked the
  tier question (one entry per model, with every form the question showed for it), applies the
  turn-2 rule, and compares. Pass requires that the line assigns to `fast`, `standard` and
  `deep` exactly the derived models, each written as the question showed it for that entry
  (name, alias or identifier; case and backticks ignored), and that any reasoning setting in the
  line is `high`. Another model, a form the question did not show, another reasoning value, or a
  missing tier fails. For C15-t2 the expected models are `haiku`, `sonnet`, `opus` as stated.
  When the C15-t1 tier question names no model, `C-tiers` is `inconclusive` (turn 2 did not fit)
  and C15-t2 runs; this is the only allowed rerun form.
- `C-notdd` (auto): at the end the section has no `TDD:` line.
- `AC4-order` (auto): as C14-t1.
- `D23-norec` (reply), `T-models` (observation), `G-*`.

C5-t3: as C5-t1 and C5-t2: `AC12-report` (reply), `AC12-nodir`, `AC12-legacy`, `R4`,
`AC4-order`, `AC5` (as revised by D11: no records line, no `TDD:`, no `Model tiers:`), `AC7`
(auto), `AC9-next` (reply), `G-*`; plus `D23-norec` (reply) when a reply asks a preference
question.

C8-t2: as C8-t1: `R5-noimport` (auto and reply), `R6-one`, `R6-userline`, `AC8` (`TDD:` value
`strict`), `AC5-outside`, `AC3-bytes`, `AC4-order` (auto), `G-*`; plus:

- `AC4-shown` (reply, auto aid): the section text shown in the turn-2 reply (the reply before
  the confirming turn) contains the line `- Team note: run the linter before review.` and
  equals, line for line, the section in `AGENTS.md` at the end. The shown section is the lines
  from the line `## Lusona skills` in that reply to the end of the fenced code block that holds
  it, or, outside a fence, to the next heading of level 1 or 2 or the end of the reply. Lines
  are compared with trailing whitespace removed and with blank lines at the end of either text
  ignored; blank lines inside count. A reply that shows only a diff, only the changed line, or
  refers to an earlier reply for the text fails.
- `D23-norec` (reply).

`D23-norec` (reply, every trial where a preference question appears): each reply that asks a
preference question (the TDD question, the tier question, or, in C12 and C13, the location
question, which D26 makes the preference question for that value) recommends no TDD level and
no model mapping. A recommendation is a sentence that favors one answer: "I recommend",
"recommended", "I suggest", "a good default", "if unsure, choose", a level or mapping offered
as a default, a suggestion or an example the user could accept ("one possible mapping", an
example assignment of a model to a tier). In C12 and C13, recommending a location counts as
recommending that location's TDD level. Naming the three levels with neutral descriptions,
listing the host's models without assigning them to tiers, or describing what each tier is for
is not a recommendation. The grade quotes the decisive sentence. When no reply asks a
preference question, the cell is `n/a`. Recorded as the observation `D23-other`, not graded:
a recommendation to decline a preference, and, in C5, a recommendation on creating
`docs/lusona/` (not a preference question).

`T-models` (observation, every trial where the tier question appears): whether the question
named host models, and whether any model was recorded without the user choosing or stating it.

Outcome rules as declared above.

Budget and stopping: at most 5.00 USD of Claude-reported cost for this amendment; the record
total stays at or below 25 USD (7.5355 USD spent before this amendment; ledger value
7.535545). Cost is tracked after every turn in the ledger. A trial starts only when 5.00 minus
the amendment's spent cost (ledger total minus 7.535545) minus 1.00 USD for each other
Amendment 4 trial in flight is at least 1.00 USD, and the record total plus 1.00 USD is at most
25 USD. Each trial runs once; the only rerun is C15-t2 as stated above, or one rerun of another
trial that is inconclusive only because a scripted turn did not fit what the agent asked, with
the first attempt kept and the reason recorded. No rerun for a failed criterion. Order: C12-t1,
C13-t1, C14-t1 concurrently, then C15-t1, C5-t3, C8-t2 concurrently. Stop when every listed
trial was attempted once or the gate refuses the next trial; unrun trials are reported as
planned but unrun.

Locks: the four earlier locks stay unchanged and verifiable. `cases.v4.json` is a byte copy of
`cases.json` as it was before this amendment, and the Amendment 3 lock now checks its
`cases.json` hash against that copy. `design.lock.amendment-4.json` holds the sha256 of the
current `cases.json`, `candidate.v4.sha256`, and the README text from the line `## Amendment 4`
up to, not including, the line `### Amendment 4 results`. The driver verifies all five locks
and the four frozen copies before a trial. The driver gains the v4 candidate, the fifth lock
check, the Amendment 4 budget gate and the new auto checks after this lock and before the first
trial; it is not edited after the first trial starts, or the edit is disclosed.

### Amendment 4 results

Order: `candidate.v4.sha256`, `cases.v4.json` (byte copy, checked with `cmp`), the Amendment 3
lock check repointed to `cases.v4.json` (all four earlier locks verified), the amended
`cases.json`, the "Amendment 4 design" section above and `design.lock.amendment-4.json` (locked
2026-11-13T23:54:01Z) were written before the six trials; this section after them. The driver
then gained the v4 candidate, the fifth lock check, the Amendment 4 budget gate and the C12 to
C15 and C8 `AC4-shown` aid checks, before the first trial (driver sha256 prefix `d97602b3b7b7`
for all six; not edited after the first trial started). With that driver, `check_lock()`
verified all five locks and the four frozen copies; an in-memory regrade of the nineteen earlier
trials with `grade_data` gave outcomes and details equal to the stored ones; a scratch test
(`tmp/setup-skill-t4/test_checks_a4.py`) showed each new auto check passing on a good synthetic
state and failing on a bad one. The first trial started 2026-11-13T23:55:27Z. Trials ran in two
concurrent waves (C12-t1, C13-t1, C14-t1; then C15-t1, C5-t3, C8-t2), once each. No rerun: the
C15-t1 tier question named models, so C15-t2 was not run, and no other trial was inconclusive.

Every init event of the six trials listed one `lusona` plugin at
`tmp/setup-skill-t4/candidate-v4`, model `claude-opus-5-5` and Claude Code 2.1.325. After the
trials `diff -r tmp/setup-skill-t4/candidate-v4 plugins/lusona` still printed nothing. No
transcript names this evidence record, a scratch path other than the frozen plugin, or the
checkout's `plugins/lusona/`; `docs/lusona/evidence/` appears only inside the agents' reads of
`references/files.md`.

| Trial | Claude Code | Workspace (under the work root) | Session id | Claude cost (USD) |
| --- | --- | --- | --- | --- |
| C12-t1 | 2.1.325 | `setup-C12-t1-3b391626` | `94107ba1-…` | 0.4622 |
| C13-t1 | 2.1.325 | `setup-C13-t1-837e87dd` | `7e396b4a-…` | 0.3898 |
| C14-t1 | 2.1.325 | `setup-C14-t1-f7011d53` | `d07bff57-…` | 0.4468 |
| C15-t1 | 2.1.325 | `setup-C15-t1-71f884ab` | `5d679764-…` | 0.4356 |
| C5-t3 | 2.1.325 | `setup-C5-t3-d1a5eede` | `25b448b0-…` | 0.4416 |
| C8-t2 | 2.1.325 | `setup-C8-t2-0ebbaddb` | `e2c4023c-…` | 0.3985 |

Claude cost of Amendment 4: 2.5745 USD of 5.00 USD. Record total: 10.1100 USD of 25 USD.
Planned but unrun: C15-t2 (its condition, a tier question that names no model, did not occur).

| Check | C12-t1 | C13-t1 | C14-t1 | C15-t1 | C5-t3 | C8-t2 |
| --- | --- | --- | --- | --- | --- | --- |
| G-run | pass | pass | pass | pass | pass | pass |
| G-commit | pass | pass | pass | pass | pass | pass |
| G-scope | pass\* | pass\* | pass\* | pass\* | pass\* | pass\* |
| C-both-shown | pass | — | — | — | — | — |
| C-kept | pass | — | — | — | — | — |
| C-new | — | pass | — | — | — | — |
| C-readme | pass | pass | — | — | — | — |
| C-told | pass | pass | — | — | — | — |
| C-tiers | — | — | — | pass | — | — |
| C-notdd | — | — | — | pass | — | — |
| AC3-bytes | — | — | — | — | — | pass |
| AC4-order | pass | pass | pass | pass | pass | pass |
| AC4-shown | — | — | — | — | — | pass |
| AC5 | — | — | pass | — | pass | — |
| AC5-outside | — | — | — | — | — | pass |
| AC7 | — | — | — | — | pass | — |
| AC8 | pass | pass | — | — | — | pass |
| AC9-next | — | — | — | — | pass | — |
| AC12-report | — | — | — | — | pass | — |
| AC12-nodir | — | — | — | — | pass | — |
| AC12-legacy | — | — | — | — | pass | — |
| R4 | — | — | — | — | pass | — |
| R5-noimport | — | — | — | — | — | pass |
| R6-one | — | — | — | — | — | pass |
| R6-userline | — | — | — | — | — | pass |
| D23-norec | pass | pass | **fail** | **fail** | pass | pass |

\* After the accepted `.claude/.cc-writes` exclusion; no other path outside the allowed writes.

Failures: `D23-norec` in C14-t1 and C15-t1. In the turn-1 TDD question each reply offered a
level with a scope as an example: C14-t1, "You can also attach a scope to a level, for example
\"`targeted` for input parsing\"."; C15-t1, "You can give a level and its scope, for example
\"targeted for argument parsing\", or decline." The locked definition counts "a level ... offered
as ... an example the user could accept" as a recommendation, and both sentences offer such a
level, so both cells are `fail`. Grader disagreement, recorded and not applied: I read both
sentences as illustrations of the answer format, not as favoring a level; each reply also states
that it recommends nothing ("I'm not recommending an answer to either."; "I recommend no answer
for either one."). Under that reading both cells would be `pass`. The agent's own statement was
not used as evidence for either grade. No rerun, because the criterion failed. The other trials'
turn-1 TDD questions name levels without an example value (C12-t1: "You can choose from `none`,
`targeted` or `strict`, and add a scope."; C13-t1 and C8-t2 similar; C5-t3 names the three
levels only).

Decisive evidence (replies quoted from `trials/<trial>/trial.json`):

- C12-t1 `C-both-shown`: turn 1, "**Question 1: TDD preference. Two locations hold different
  values. Which location keeps its value?**" followed by a table with "`AGENTS.md`, Lusona
  section | `TDD: targeted for validation and persistence boundaries`" and
  "`docs/lusona/README.md`, line 5 | `TDD: strict for parser changes`"; `AGENTS.md` and
  `CLAUDE.md` unchanged after turn 1. `C-kept`: one `TDD:` line with the kept value at the end;
  `AGENTS.md` byte-identical to the fixture (aid). `C-told`: turn 1, "If you choose the section,
  the README line stays and still holds a different value."; turn 2 repeats it ("Two locations
  still hold a TDD value").
- C13-t1 `C-new`: the final section's only `TDD:` line is "- TDD: targeted for command-line
  argument handling"; `AGENTS.md` equals the fixture with only that value replaced (aid).
  `C-told`: turn 1, "It will not edit `docs/lusona/README.md`, so that file keeps `strict for
  parser changes` whatever you choose."; turn 2, "`docs/lusona/README.md` line 5 still says
  `TDD: strict for parser changes`."
- C15-t1 `C-tiers`: turn 1 named "`claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5` and
  `claude-fable-5-2`"; the rule gives `fast` haiku, `standard` opus (the one before the last),
  `deep` fable. Written line: "- Model tiers: `fast` = `claude-haiku-5-5`, reasoning `high`;
  `standard` = `claude-opus-5-5`, reasoning `high`; `deep` = `claude-fable-5-2`, reasoning
  `high`." Same identifier forms as the question; reasoning `high` only.
- C8-t2 `AC4-shown`: turn 2 shows the section in a fenced block that ends with "- TDD: strict"
  and "- Team note: run the linter before review."; the driver aid finds it equal, line for
  line, to the final section (`equal_line_for_line: true`, `user_line_shown: true`).
  `R5-noimport` (reply): turn 1, "`CLAUDE.md` line 3 already imports the file through
  `@./AGENTS.md`, so it needs no new import line."
- C5-t3 `AC12-report`: turn 1, "this project already has legacy Lusona records in `docs/agent/`,
  and there is no `docs/lusona/` yet. I have written nothing." and "**Should I create
  `docs/lusona/` and the queue `docs/lusona/work.md`?**". `AC9-next`: "Proposed: check where the
  project stands ... `/lusona:status Assess progress from docs/agent/work.md and its specs.` |
  status | The legacy queue and spec | Needs your request".
- `D23-norec`, the reply that asked the preference questions (turn 1 in every trial):
  - C12-t1: no sentence favors an answer; the three options are listed neutrally ("**Keep the
    section's value:** the section keeps its `TDD:` line." and two more), and the tier question
    lists "Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5" without assigning them to tiers.
  - C13-t1: "I am not recommending an answer to either question. That is deliberate: the setup
    skill leaves preference values to you."
  - C14-t1 (`fail`): "You can also attach a scope to a level, for example \"`targeted` for input
    parsing\"." The tier question lists models without assigning them to tiers.
  - C15-t1 (`fail`): "You can give a level and its scope, for example \"targeted for argument
    parsing\", or decline." The tier question lists models without assigning them to tiers.
  - C5-t3: the TDD and tier questions recommend nothing ("You can decline. Without a
    preference, each change gets its own level."); the `docs/lusona/` question is outside
    `D23-norec` (see `D23-other`).
  - C8-t2: "I don't recommend an answer to either; they are your choice."

`T-models` (observation): the tier question named host models in C12-t1, C13-t1, C14-t1,
C15-t1 and C5-t3 (identifiers in C14, C15 and C5, for example "This host lists the models
`claude-fable-5-2`, `claude-opus-5-5`, `claude-sonnet-5-5` and `claude-haiku-5-5`"; display
names in C12 and C13, "Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5"); in C8-t2 it named no
model. No trial assigned a model to a tier as an example. Only C15-t1 recorded models, the ones
the user chose.

`D23-other` (observation): C5-t3 recommended declining `docs/lusona/` ("I recommend no."), as in
C5-t2. C15-t1 turn 1 says "Both are optional. I recommend no answer for either one.", which a
user can read as advice to decline both; it repeats the skill's phrase "recommend no answer to a
preference question" to the user. No other trial's wording can be read as a recommendation to
decline.

Deviations from the declared design: none. The Claude Code version (2.1.325, not 2.1.323) was
declared before the trials.

Observations outside the criteria:

- C12-t1 turn 2: the agent did not ask for confirmation. "✅ Setup is complete. I changed no
  files, because the section built from your answers is byte-for-byte the same as the one
  already in `AGENTS.md`." and "Since writing it would change nothing, I didn't ask you to
  confirm it." The scripted turn 3 confirmation was then answered with "Your confirmed text is
  already in `AGENTS.md`, so there was nothing to write." No file was written, so no check is
  affected; step 5 of the skill ("Show its text and the target paths, and wait for the user's
  confirmation") has no case for a composed section equal to the existing one.
- C13-t1 turn 2 also showed a diff of the changed line next to the full text, and stated "After
  this write, the project will state two standing TDD preferences."
- Several final replies (C13-t1, C14-t1, C15-t1, C5-t3) mention untracked entries such as
  `.bashrc`, `.mcp.json`, `.claude/` and `.idea` in `git status`, described in C15-t1 as
  "character devices from the sandbox". The snapshots, taken outside the sandbox, contain none
  of them except the accepted `.claude/.cc-writes`, so they are visible only inside the Bash
  sandbox.

Amendment 4 limits: one trial per case on v4; Claude Code 2.1.325 only, no Codex trial on v4;
`C-tiers` covers one list order of four models; the C12 and C13 location questions are graded
on one wording each; reply-graded checks are graded by one grader. C12-t1 `AC4-order` passes without testing the
confirmation rule: the composed section equalled the existing one, nothing needed writing, and
the agent did not ask for confirmation.

Amendment 4 interpretation, limited to what was observed: on v4, in one trial each, setup showed
both values and their locations and kept or replaced the section's value as the user answered,
left `docs/lusona/README.md` unchanged and told the user it still holds a value (C12, C13);
recorded no preference line when both were declined (C14); recorded exactly the models the user
chose from the named list (C15); kept the legacy-decline behavior with the records line removed
(C5-t3); and showed in full, before confirmation, the section it then wrote, including the
user's line (C8-t2). No reply recommended a model mapping or explicitly favored a TDD level; two
of six (C14-t1, C15-t1) gave a scoped level as a format example, which the locked `D23-norec`
definition grades as a recommendation.

User decisions after these results (spec, D35 and D36, 2026-11-13): a format example that
names a level is not a recommendation under D23, and the two `D23-norec` cells stay `fail` as
graded; the two observations outside the criteria are accepted without a text change.

## Removed files

Removed on 2026-11-13, when the user asked to discard non-essential files from this directory:
82 files under `trials/<trial>/final/` (70,204 bytes). Each removed file's text is held in
that trial's `trial.json`: a check before the removal found the JSON-encoded text of every one
of the 82 files there. The files were never committed and cannot be restored from history.
Kept: `trials/X2-t1/final/greet.py.txt` and `trials/X2-t1/final/test_greet.py.txt`, whose text
no `trial.json` holds. The statements above that final workspace files are kept under
`trials/<trial>/final/` describe the state before this removal. `raw.zip` stays in the local
checkout and is git-ignored.
