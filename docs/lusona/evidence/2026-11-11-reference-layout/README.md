# Reference layout and path form — 2026-11-11

Owner: [spec 20261111-loop-principles-and-skill-rewrite](../../specs/20261111-loop-principles-and-skill-rewrite.md),
work item W4 (experiment half), open questions A6 (layout) and A7 (path form).
Method reference: [run 008](../2026-11-09-loop-conformance-pilot/runs/008/README.md#method-and-provenance)
and the actor launch in [`evals/loop-conformance/run.py`](../../../../evals/loop-conformance/run.py).

## Decision and scope

- Decision informed: which skill directory layout (A6) and which path form in skill text (A7)
  make each host read a reference file at the trigger the skill states. The ADR is written
  later by architect; this record does not write it.
- Metric: per trial, whether the reference file reached the root agent through tool output,
  and whether the first path the agent tried for it worked.
- Population: one fixture skill per condition, one task prompt, two hosts. Package build:
  copies of the current working tree with layout variants applied.

## Declared trial design

Declared 2026-11-11 before any actor or probe run. Later deviations are listed under
[Deviations](#deviations) with reasons.

### Hypotheses

- H1 (A6): both layouts load. With a Markdown link that resolves from the skill directory,
  the agent reads the reference at the trigger on both hosts, for L1 (plugin-level
  `references/`, link `../../references/x.md`) and L2 (per-skill `skills/<skill>/references/`,
  link `references/x.md`).
- H2 (A7): a bare path `references/x.md` that names a plugin-level file (L1-bare) does not
  resolve on the first attempt from the loaded skill directory, because the file is at
  `../../references/x.md` relative to it. The agent either searches and recovers, or does not
  read the file.
- H3 (A7): a bare path that names a per-skill file (L2-bare) resolves like the L2 link.
- H4 (package): `scripts/package.py` keeps `skills/<skill>/references/` (it copies `skills/`
  whole), drops a plugin-level `shared/` directory, fails on a Markdown link into `shared/`,
  and does not check bare paths.

### Fixture

One fixture plugin per condition under `tmp/w4/fixtures/<condition>/`, plugin name `w4fix` in
every condition (same slash command, no naming confound). Each has
`.claude-plugin/plugin.json` and one skill `skills/release-note/SKILL.md`:

```markdown
---
name: release-note
description: Write a release note into RELEASE.md. Use when the user asks for a release note.
---

# Release note

Write the release note to `RELEASE.md` in the project root.

Before writing the release note, read <REF>.

Use the version and changes the user gives. Do not ask questions.
```

`<REF>` per condition:

| Condition | Reference file location | `<REF>` text in SKILL.md |
| --- | --- | --- |
| L1-link | `references/release-format.md` (plugin level) | `[the release-note format](../../references/release-format.md)` |
| L1-bare | `references/release-format.md` (plugin level) | `` `references/release-format.md` `` |
| L2-link | `skills/release-note/references/release-format.md` | `[the release-note format](references/release-format.md)` |
| L2-bare | `skills/release-note/references/release-format.md` | `` `references/release-format.md` `` |

The reference holds the only statement of the format, with a marker unique to the condition:

```markdown
# Release-note format

The first line of every release note is exactly: `Format-ID: W4REF-<condition>-<8 hex>`
After it, a level-2 heading with the version, then one bullet per change.
```

The marker appears nowhere else: not in SKILL.md, the prompt, the workspace or any other
fixture file. No `references/` directory exists in the workspace.

Workspace per trial: `tmp/w4/ws/<host>-<condition>-<n>/`, a new git repository with one
committed file `CHANGES.txt` (`1.4.0: fixed the login timeout`). The fixture plugin is a
sibling of the workspaces under `tmp/w4/`, not inside them.

Task prompt (same text on both hosts):
`Write the release note for version 1.4.0. Change: fixed the login timeout.`

### Hosts and invocation

- Claude Code (CLI 2.1.322): `claude -p` with the suite's flags (`--plugin-dir <fixture>`,
  `--setting-sources project`, `--strict-mcp-config`, the suite's sandbox `--settings`,
  `--permission-mode dontAsk`, `--allowedTools Read Edit Write Skill Task Agent Bash`,
  `--output-format stream-json --verbose`), plus `--max-budget-usd 1.50` per trial, model
  `claude-opus-5-5`, effort `high` (the suite reference condition), environment as in
  `run.py` (`CLAUDE_CODE_*` removed, `CLAUDE_CODE_SHELL=/bin/bash`). Prompt starts with
  `/w4fix:release-note `, as the suite invokes skills.
- Codex CLI (0.167.1): `codex exec --ignore-user-config --sandbox workspace-write --json
  --model gpt-6.1-sol -c model_reasoning_effort="medium" -C <ws> --skip-git-repo-check -`
  (the suite reference model and effort). Native plugin installation (`codex plugin add`)
  writes to the global `~/.codex` configuration and is excluded by the assignment, so Codex
  gets the suite's method in a shorter form: the prompt starts with
  `Use the release-note skill at <absolute fixture path>/skills/release-note/SKILL.md.` and a
  blank line. Codex results therefore show how the agent resolves paths from a SKILL.md path
  it was given; installed-plugin behavior stays untested. The suite's phrase "and applicable
  linked instructions" is left out so the prompt does not ask for linked files.

### Setup probes (counted in the budget, recorded like trials)

- P1 isolation, both hosts: `tmp/w4` is inside this repository, whose `CLAUDE.md` points to
  `AGENTS.md`, which says "Resolve bundled resources relative to the loaded skill". That
  sentence instructs the behavior A7 measures. In a fresh `tmp/w4/ws/probe-<host>` repository
  each host is asked, without tools, to list every instruction file whose content is in its
  context and quote its first heading. Decision declared now: if the repository `CLAUDE.md` or
  `AGENTS.md` reaches a host and no flag within the assignment suppresses it, that host's
  actor trials are not run and the question returns to the coordinator (a work root outside
  `tmp/w4` breaks the write ownership; running with the leak invalidates A7).
- P2 pilot: one Claude trial of L1-link, counted as trial 1 of that condition if valid. It
  also shows whether the host gives the skill's base directory in the expanded skill text.

### Conditions and trials

4 conditions × 2 hosts. Maximum 5 trials per condition and host: 20 Claude, 20 Codex.
Order: round-robin over conditions (trial 1 of L1-link, L1-bare, L2-link, L2-bare, then
trial 2, ...), Claude and Codex runs alternating by round. Cost rule declared now: if the
pilot costs more than $0.80, the maximum is 3 trials per condition and host.

### Measured outcome (per trial)

From tool calls and tool output shown to the root agent (Claude: `tool_use` / `tool_result`
in stream-json; Codex: `command_execution` command and `aggregated_output`):

- `returned`: the condition's marker string appears in tool output shown to the root agent
  (marker check; the reference has one unique line, so run 008's 3-line rule cannot apply).
- `first_path`: the path in the first tool call whose input names `release-format`.
- Class: **resolved** = the first call naming `release-format` returned the marker;
  **recovered** = the marker was returned, but not by that first call;
  **not read** = the marker never returned.
- `searches_before`: count of listing or search calls (`ls`, `find`, `rg --files`, `Glob`,
  `Grep`, `grep -r`) before the marker was returned.
- `applied` (secondary): `RELEASE.md` first line equals the format line with the marker.
- Cost: Claude `total_cost_usd` from the result event; Codex token usage (cost not reported).

A trial whose host process fails before the skill is loaded, or whose Claude init event does
not list the `w4fix` plugin, is `setup-blocked`; it is kept and not retried.

### Decision criteria

Per host, a condition **works** when at least 4 of 5 trials (3 of 3 under the cost rule) are
resolved, **fails** when at most 1 of 5 (0 of 3) are resolved, otherwise **mixed**.

- A6: if L1-link and L2-link both work on both hosts, loading does not decide the layout and
  the ADR decides it on other grounds (duplication, package, catalog). If only one works on
  a host, the evidence supports that layout.
- A7: if L1-bare fails or is mixed on a host while L1-link works, a bare path naming a
  plugin-level file is not supported on that host; skill text needs a link that resolves
  from the skill directory. If L1-bare works on both hosts, the bare form is acceptable for
  loading, and the package link check gap (H4) remains the only argument against it.
  L2-bare versus L2-link answers whether a bare path is acceptable when it resolves from the
  skill directory.

### Budget and stopping

- Total $20 Claude-reported spend: probes and pilot up to $2, Claude trials the rest.
  Before each Claude trial, the runner stops if spent + $1.50 (the per-trial cap) exceeds $20.
- Codex: cost not reported; trials capped at the Claude trial count per condition; token
  counts recorded.
- Curtailment: a condition-host series stops early once its classification (works / fails /
  mixed) cannot change with the remaining trials. No other early stop; no retries.
- `~/.codex/config.toml` is hashed before and after the Codex runs.

### Package build

`scripts/package.py` builds from its own repository root, so each variant is a copy of the
working tree (tracked and untracked, non-ignored files) at `tmp/w4/pkg/<variant>/`, built
with the copied script to `tmp/w4/pkg-out/<variant>/`:

- P0: unchanged copy (L1, current).
- P-L2: `references/tdd.md` copied to `skills/implement/references/tdd.md`; the implement
  skill gets a link `references/tdd.md`.
- P-shared: a file `shared/block.md` added at plugin level, once without a link (P-shared-a)
  and once with a Markdown link `../../shared/block.md` from the implement skill (P-shared-b).
- P-bare: the implement skill names `references/does-not-exist.md` as a bare path.

Recorded per variant: build exit status and message, and whether each added file is in the zip.

## Method and provenance

- Repository HEAD `34186da` with an uncommitted working tree (git status at start: 15 modified,
  11 untracked paths, including `scripts/package.py`, sha256 `1a300869…`). Fixtures do not
  depend on the plugin sources; the package builds use copies of that working tree.
- Hosts: Claude Code 2.1.322 (`claude-opus-5-5`, effort `high`); Codex CLI 0.167.1
  (`gpt-6.1-sol`, effort `medium`). Authenticated sessions already present; nothing installed.
- Instruments: [`w4.py`](w4.py) (fixtures, workspace, launch, per-trial analysis; sha256
  `9d6b91e5…` at run time, `e6f5c410…` after the analysis fix in deviation 7; it contains one
  absolute local path, in `claudeMdExcludes`) and [`drive.py`](drive.py) (round-robin, budget guard, curtailment; `b1b45910…`).
  They run from `tmp/w4/` (paths are relative to the script). Per-trial rows:
  [`rows.json`](rows.json) (`213ea4eb…`; repository path replaced by `<repo>`, home by `~`). Raw stdout, stderr, commands, fixtures and the driver
  log: `raw.zip` (`1ec77f6e…`, git-ignored, holds absolute local paths; exists only on the
  machine that ran the trials).
- Reproduce: `cd tmp/w4 && python3 w4.py fixtures && python3 drive.py && python3 w4.py analyze`.
- Validity check: no trial transcript contains `ai-skills/AGENTS.md` or `ai-skills/CLAUDE.md`
  (only probe P1 run 1, before the fix below). Every trial is `captured`; the Claude init event
  listed plugin `w4fix` with the path of the condition's own fixture directory in all 16
  Claude trials (checked from the init event's `plugins[].path`).
- Claude's expanded skill text is not in the stream-json output, so whether the host states the
  skill's base directory cannot be read directly. In every Claude trial the first reference
  read used an absolute path under the fixture's skill directory, which shows the agent had
  that directory.

### Setup probe results

| Probe | Result | Cost |
| --- | --- | --- |
| P1 Claude, run 1 | Leak: actor listed `~/.claude/CLAUDE.md` and the repository `CLAUDE.md` (`# Repository instructions`); said `AGENTS.md` content was not in context | $0.0834 |
| P1 Claude, run 2, with `claudeMdExcludes` | Only `~/.claude/CLAUDE.md` (user global instructions: reply style, plain language, accuracy rules) | $0.0815 |
| P1 Codex | Only the global `AGENTS.md` (`# Global instructions`, same user style rules); repository `AGENTS.md` not loaded (workspace has its own `.git`) | 16,662 input / 113 output tokens |
| P2 pilot (claude-L1-link-1) | Resolved; $0.0994 ≤ $0.80, so 5 trials per condition stayed the maximum | counted as a trial |

## Deviations

1. After P1 Claude run 1, `--settings` gained
   `"claudeMdExcludes": ["<repo>/CLAUDE.md", "<repo>/AGENTS.md"]` (a per-invocation setting; no
   global change). P1 run 2 confirmed the repository file no longer reached the actor. All
   Claude trials ran with it. This differs from the suite's settings only by this key.
2. `--setting-sources project` did not stop the user `~/.claude/CLAUDE.md` from loading. It
   holds reply-style, plain-language and accuracy rules (for example "Do not invent file
   names ... Check, or say you cannot"). It was not excluded. Whether it also reached actors in
   the suite's runs was not verified; the suite condition records "Ambient instruction files:
   none" for Claude.
3. Codex `exec` added a `[projects."<workspace>"] trust_level = "trusted"` entry to the global
   `~/.codex/config.toml` for each workspace, despite `--ignore-user-config` (17 entries under
   `tmp/w4/ws/`; sha256 before `969fe460…`, after the Codex probe `bdc7a940…`, after all
   Codex runs `2d5cd843…`; other processes may also write this file). The suite's earlier
   runs left the same kind of entries. The entries were not removed: the file is outside this
   item's write ownership.
4. Other host-side leftovers outside the repository: 18 Claude session directories under
   `~/.claude/projects/-home-jg-code--lusona--ai-skills-tmp-w4-ws-*` and 17 Codex rollout
   files under `~/.codex/sessions` that name `tmp/w4/ws`. Not removed (outside write ownership).
5. Curtailment stopped every series at 4 trials (classification fixed: 4/4 or 0/4 resolved),
   so no condition reached a fifth trial. The Codex count equals the Claude count in every
   condition.
6. Package variants P-L2b and P-L2c were added after P-L2 failed, to separate "per-skill
   folder is not packaged" from "moved file's own links break". They are unplanned
   (exploratory) variants.
7. Analysis fix after the run: the search-call pattern missed a command directly after a quote
   (`"ls -la"`, `"rg --files ..."`), so `searches_before` was undercounted. The pattern now
   accepts a leading quote and `rows.json` was regenerated. Classes do not use this field and
   did not change.

## Observations

`searches_before` (listing or search calls before the marker): 0 in all resolved trials;
Claude L1-bare 1, 2, 1, 2; Codex L1-bare 2 in each trial.

| Condition | Host | Trials | Reference read: resolved / recovered / not read | Rule applied in RELEASE.md | Cost |
| --- | --- | --- | --- | --- | --- |
| L1-link | Claude Code | 4 | 4 / 0 / 0 | 4/4 | $0.411 |
| L1-bare | Claude Code | 4 | 0 / 1 / 3 | 1/4 | $0.501 |
| L2-link | Claude Code | 4 | 4 / 0 / 0 | 4/4 | $0.419 |
| L2-bare | Claude Code | 4 | 4 / 0 / 0 | 4/4 | $0.427 |
| L1-link | Codex | 4 | 4 / 0 / 0 | 4/4 | 285,574 in (251,520 cached) / 1,279 out tokens |
| L1-bare | Codex | 4 | 0 / 4 / 0 | 4/4 | 413,356 in (366,080 cached) / 2,011 out |
| L2-link | Codex | 4 | 4 / 0 / 0 | 4/4 | 271,965 in (241,536 cached) / 1,316 out |
| L2-bare | Codex | 4 | 4 / 0 / 0 | 4/4 | 271,808 in (246,400 cached) / 1,266 out |

Spend: Claude $1.923 in total (trials $1.758, probes $0.165) of the $20 budget. Codex reports
no cost: 16 trials plus 1 probe, 1,259,365 input tokens (1,117,824 cached) and 5,985 output
tokens in total.

- L1-bare, both hosts: the first attempt was always `<skill dir>/references/release-format.md`
  (does not exist). Claude then listed the skill directory and the workspace; in 3 of 4 trials
  it stopped there, wrote `RELEASE.md` without the format, and said in its reply that the file
  does not exist. In trial 4 it searched the fixture root, read the plugin-level file, and
  suggested moving it into the skill directory. Codex searched the fixture root with
  `rg --files` in all 4 trials (trial 1 also searched `~/.codex/skills`), then read the file:
  about 35,000 more input tokens per trial than the link conditions.
- Link conditions and L2-bare: the first read used the correct absolute path in all 24 trials,
  with no search before it.

### Package build (H4)

Copies of the working tree under `tmp/w4/pkg/<variant>/`, built with the copied
`scripts/package.py --output tmp/w4/pkg-out/<variant>`:

| Variant | Change | Build | Files in zip |
| --- | --- | --- | --- |
| P0 | none (L1) | pass | 78 files |
| P-L2 | `references/tdd.md` copied to `skills/implement/references/tdd.md`, linked as `references/tdd.md` | **fail**: `Broken resource link: …/skills/implement/references/tdd.md: retention.md` | none (partial output directory left) |
| P-L2b | as P-L2, link `retention.md` rewritten to `../../../references/retention.md` | **fail**: `…/tdd.md: ../README.md#questions-and-next-actions` | none |
| P-L2c | as P-L2b, also `../README.md` rewritten to `../../../README.md` | pass | 79 files; `plugins/lusona/skills/implement/references/tdd.md` present |
| P-shared-a | `shared/block.md` at plugin level, not linked | pass | 78 files; `shared/` absent |
| P-shared-b | as P-shared-a, linked `../../shared/block.md` from `implement` | **fail**: `Broken resource link: …/skills/implement/SKILL.md: ../../shared/block.md` | none |
| P-bare | `implement` names `references/does-not-exist.md` as a bare path | pass | 78 files (bare path not checked) |

## Interpretation and decision

- H1 supported: L1-link and L2-link both work on both hosts (4/4 resolved each).
- H2 supported: L1-bare fails on both hosts (0/4 resolved). The consequence differs by host:
  Claude Code did not apply the referenced rule in 3 of 4 trials; Codex recovered by search in
  4 of 4, at about 50% more input tokens.
- H3 supported: L2-bare resolved 4/4 on both hosts, same as L2-link.
- H4 supported, with one addition: `skills/<skill>/references/` is packaged; `shared/` is
  dropped, and a link into it fails the build; bare paths are not checked. Moving a reference
  into a skill directory breaks the reference's own relative links (`retention.md`,
  `../README.md`) until they are rewritten; the link check catches this.

A6 (layout), supported answer: loading does not decide between L1 and L2; both load at the
trigger on both hosts when the path in the skill text resolves from the skill directory. The
choice rests on other grounds the ADR weighs: L2 duplicates a reference used by several skills
(or needs `../<other-skill>/references/` links); L1 keeps one copy. Any shared source must sit
inside a packaged folder (`skills`, `templates`, `scripts`, `references`, `assets`, `hooks`) or
be added to `package.py`; `shared/` is not packaged. Confidence: moderate (4 trials per cell,
one fixture, all-or-none results).

A7 (path form), supported answer: on both hosts the agent resolves a path in skill text relative
to the skill directory, whether written as a Markdown link or a bare path. A bare
`references/x.md` that names a plugin-level file does not resolve and is rejected for L1. A
bare path is equivalent to a link only when the file is inside the skill directory, and
`package.py` validates links only. Confidence: moderate for the resolution behavior (consistent
24/24 and 0/8); low for generalization (see limits).

Experiment disposition: **adopt** "write every reference path relative to the skill directory"
(links `../../references/x.md` for L1, or `references/x.md` for L2); **reject** bare
`references/x.md` for plugin-level files. Layout choice: **inconclusive** from loading;
decided by the ADR on duplication and packaging.

### Limits

- Setup-blocked: Codex loading from an installed plugin (`codex plugin add` writes the global
  configuration, which the assignment excludes). Its prompt gave the
  absolute SKILL.md path; results show path resolution from a given path, not native skill
  discovery. Claude used `--plugin-dir`, not an installed marketplace plugin.
- One small fixture, one trigger at the start of the task, one model and effort per host.
  Triggers reached later in a long task, references named inside other references, and the
  every-task block's own wording are untested.
- 4 trials per cell; the curtailment rule stopped at 4. No significance claim.
- Claude's injected skill text is not visible in the transcript; the base directory is
  inferred from the absolute paths the agent used.
- The user `~/.claude/CLAUDE.md` and the global Codex `AGENTS.md` (same text: reply style,
  plain language, accuracy rules) were in context. These rules and the fixture's "Do not ask
  questions" may shape what Claude did after the failed read (3 of 4 wrote without the format
  and reported the missing file; 1 searched). They cannot make a first read succeed, so the
  0/4 resolved count is unaffected.

### Open questions (for the ADR)

- L1 versus L2 (or both): duplication and cross-skill links versus one copy; not decided by
  loading.
- Where the shared block source lives, given `shared/` is not packaged (new packaged folder,
  `package.py` change, or a location under `references/` or `scripts/`).
- Whether `package.py` should also check bare `references/...` paths in skill text, since the
  bare form for plugin-level files fails at runtime and the build does not catch it.
- `--setting-sources project` does not stop `~/.claude/CLAUDE.md` from loading in Claude Code
  2.1.322; whether this affects the suite's isolation claim is not checked here.
- Whether to remove the 17 Codex trust entries for `tmp/w4/ws/*` from `~/.codex/config.toml`
  (user's file; not changed here).

## Next action

Architect (W4 second half) writes the ADR for A2-A8 using this record; owner: coordinator.
