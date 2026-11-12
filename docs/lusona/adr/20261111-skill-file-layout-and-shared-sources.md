# ADR 20261111-skill-file-layout-and-shared-sources: Skill file layout, reference path form and shared sources

Created: 2026-11-11
Updated: 2026-11-11

Status: accepted
Scope: the skill rewrite in [spec 20261111-loop-principles-and-skill-rewrite](../specs/20261111-loop-principles-and-skill-rewrite.md) (work item W4; open architecture questions A6 and A7, and the source location carried from A1)
Decision authority: user, 2026-11-11, native question tool, recorded as spec decision 13
Supersedes: none
Superseded by: none

## Context

The rewrite moves every-task rules into each `SKILL.md` (S1) and every other rule into a
reference that a skill names with a trigger (S2). Two architecture questions decide where those
files live and how skill text names them:

- A6: plugin-level `references/` (current layout), per-skill `skills/<skill>/references/`, or
  both; and where the shared every-task block and final-reply sources live. A1 moved the source
  location question into A6 (the sync mechanism itself is settled by spec decision 9).
- A7: whether skill text may name a reference by a bare path (`references/x.md`) or needs a
  Markdown link that resolves from the skill directory (S6).

Constraints:

- V8 and `AGENTS.md`: each shared policy has one authoritative definition; other files link it.
- `AGENTS.md` and S6: bundled resources resolve relative to the loaded skill.
- `scripts/package.py` line 82 copies a fixed list of plugin folders (`skills`, `templates`,
  `scripts`, `references`, `assets`, `hooks`). `check_links` (lines 18-22) fails the build on a
  Markdown link `](target)` whose target does not exist relative to the linking file. No check
  reads bare paths in prose or code spans.
- The repository already has one per-skill reference: `skills/batch/references/execution.md`,
  linked from `batch/SKILL.md` and from the plugin-level `references/batch-execution.md`.

Evidence: [reference layout experiment](../evidence/2026-11-11-reference-layout/README.md),
4 conditions × 2 hosts (Claude Code 2.1.322, Codex CLI 0.167.1) × 4 trials, one fixture skill
whose reference holds a unique marker. "Resolved" means the first read of the reference
returned the marker.

| Condition | Claude Code resolved / recovered / not read | Codex resolved / recovered / not read |
| --- | --- | --- |
| L1-link: plugin-level file, link `../../references/x.md` | 4 / 0 / 0 | 4 / 0 / 0 |
| L1-bare: plugin-level file, bare `references/x.md` | 0 / 1 / 3 | 0 / 4 / 0 |
| L2-link: per-skill file, link `references/x.md` | 4 / 0 / 0 | 4 / 0 / 0 |
| L2-bare: per-skill file, bare `references/x.md` | 4 / 0 / 0 | 4 / 0 / 0 |

- In all 8 L1-bare trials the first attempt was `<skill dir>/references/x.md`, which does not
  exist. Claude Code wrote the output without the referenced rule in 3 of 4 trials. Codex found
  the file by search in 4 of 4, at about 35,000 extra input tokens per trial (about 50% more
  than the link conditions).
- In all 24 link and L2-bare trials the first read used the correct path with 0 searches before it.
- Package build on copies of the working tree: per-skill `references/` is packaged (79 files,
  variant P-L2c). A plugin-level `shared/` folder is dropped from the package, and a Markdown
  link into it fails the build (P-shared-b). A bare path to a missing file passes the build
  (P-bare). Copying `references/tdd.md` into `skills/implement/references/` failed the build
  twice on the moved file's own relative links (`retention.md`, `../README.md`) until both were
  rewritten (P-L2, P-L2b).
- Result: loading does not decide between L1 and L2; both resolve on both hosts when the path
  resolves from the skill directory. Paths are resolved from the skill directory on both hosts.

## Decision

Accepted by the user (spec decision 13, 2026-11-11). Hybrid layout:

1. A reference used by more than one skill stays in plugin-level `plugins/lusona/references/`.
   Skill text links it as `[label](../../references/x.md)`.
2. A reference used by exactly one skill lives in `plugins/lusona/skills/<skill>/references/`.
   Skill text links it as `[label](references/x.md)`.
3. Skill and reference text names a plugin-level file only by a Markdown link that resolves
   from the linking file. A bare path naming a plugin-level file (for example
   `` `references/x.md` `` in a skill whose own folder has no such file) is rejected by a
   repository check. Decision 13 does not rule on bare paths to per-skill files; they resolved
   4/4 on both hosts (L2-bare) but the package build does not check them.
4. The shared every-task block source and the shared final-reply source live at the repository
   level, outside `plugins/lusona/`; the exact path is chosen in W5. They are not packaged. A
   development-time sync script generates their text into each `SKILL.md`. No runtime link in
   any packaged file points to them.

A7 answer: on both hosts the agent resolves a path in skill text from the loaded skill
directory, whether written as a link or a bare path. Markdown links are required for
plugin-level files.

Rule for placing and moving a reference. Accepted (decision 13): a reference used by exactly
one skill lives in that skill's `references/` folder; a reference used by 2 or more skills lives
in plugin-level `references/`. The every-task block and final-reply text are generated into each
`SKILL.md` and are not references; the rule does not apply to them.

Placement details (user, 2026-11-11, decision 14 of spec 20261111):

- P-a (revised by the user): "used by a skill" means the skill's `SKILL.md` links the reference
  directly. Reference-to-reference chains do not count and are avoided: a skill that needs a
  reference links it from its own `SKILL.md`. The plugin README does not count (S3: not contract).
- P-b (accepted): when a change moves the count from 1 to 2 (a second skill starts using a
  per-skill reference) or from 2 to 1 (a plugin-level reference loses its second user), the same
  change moves the file and rewrites every relative link in it and to it.

## Alternatives considered

- All references at plugin level (L1 only, the current layout): loads 4/4 on both hosts and
  keeps one copy. Not selected; reason not recorded in decision 13.
- All references per skill (L2 only): loads 4/4 on both hosts, but a reference used by several
  skills needs either one copy per skill, which breaks V8, or links of the form
  `../<other-skill>/references/x.md`, which make one skill depend on another skill's folder
  (experiment interpretation). Not selected.
- Bare paths for plugin-level files: 0/8 resolved on first read; Claude Code skipped the rule
  in 3 of 4 trials. Rejected.
- Shared sources in a packaged plugin folder (for example `references/` or a new folder added
  to `package.py`): one of the options the experiment listed. Not selected; reason not recorded
  in decision 13.
- Shared sources in a plugin-level `shared/` folder: not packaged by `package.py`, and a link
  into it fails the build (P-shared-b). Rejected.

## Consequences

- Benefits and tradeoffs:
  - Each shared policy has one definition (V8): shared references have one copy at plugin
    level; the block and final-reply text have one source each, copied into skills only by
    the sync script.
  - A reference may need to move when the number of skills using it changes; the move costs a
    link rewrite in the moved file and in each file linking it.
  - Generated text in each `SKILL.md` duplicates the shared sources by design; the sync check
    (rewritten in W5) must fail when a `SKILL.md` differs from its sources.
- Compatibility, migration, or recovery needs:
  - Moving a reference into a skill folder requires fixing its relative links: a link one
    level up (`../X`) from plugin-level `references/` becomes `../../../X` from
    `skills/<skill>/references/`, and links to sibling references gain `../../../references/`.
    The package build (`check_links`) catches the broken Markdown links; the experiment hit two.
  - `plugins/lusona/references/batch-execution.md` links into
    `skills/batch/references/execution.md`. Under the counting rule, a per-skill reference
    linked from a plugin-level reference is used by every skill that loads that plugin-level
    reference. Under P-a as decided (direct links only, no chains) this chain is removed: the
    `batch` skill links `execution.md` directly, and `batch-execution.md` does not link it (W9).
  - Reference paths and folder layout are not in the public contract K1-K4 (spec decision 2);
    Not checked: whether a consuming project names a reference path directly.
- Verification implications:
  - `package.py` validates Markdown links only and does not read bare paths (P-bare passed
    with a bare path to a missing file). A new repository check is needed that fails when skill
    or reference text names a plugin-level file by a bare path. The spec's W5 row does not list
    this check; owner assigned by the coordinator (W5 proposed).
  - A Markdown link from a packaged file to the repository-level shared sources already fails
    the build, because `check_links` runs on the built catalog where those sources are absent
    (as in P-shared-b). A bare path to them is not checked; the new check covers it.
  - Not tested: Codex loading from an installed plugin (`codex plugin add` was excluded; Codex
    received the absolute `SKILL.md` path in its prompt), Claude Code from an installed
    marketplace plugin (trials used `--plugin-dir`), triggers reached late in a long task, and
    references named inside other references. Confidence in the loading result is moderate
    (4 trials per cell, one fixture).

## Open questions and next action

- Unresolved questions (not decided by this ADR):
  - A2: relation of the reply template to the every-task block. Decided in W5 or by the user.
  - A3: every-task block size and style limit. Decided in W5 or by the user.
  - A4: whether `## Final reply` and the template check apply unchanged to `batch` and
    `status`. Decided by a pilot draft of `batch` and `status` (W5 or W8) or by the user.
  - A5: leaf role rules. Decided in W5 or by the user.
  - A8: whether templates adopt `name.ext.template` naming. Decided by the user.
  - Exact repository path of the shared sources. Chosen in W5.
- Next action: W5 receives the layout rule, P-a, P-b, the bare-path check and the shared-source
  location constraint.
