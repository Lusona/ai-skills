# Notes: contributing-shared-sync

Context: direct documentation change without a spec. The user asked on 2026-11-12 for
instructions that describe how the shared template sync works.

## 2026-11-12 — Describe the shared-text sync in CONTRIBUTING.md

### Question and scope

- Agreement (user, 2026-11-12, native question tool, "CONTRIBUTING.md only"): a new section in
  `CONTRIBUTING.md` with the procedure, and the `--check` command in its verification list.
  `README.md` keeps its three-line paragraph; the four translations are unchanged.
- TDD level: `none` (user, 2026-11-12, native question tool).

### Evidence

- Method: the statements come from `scripts/sync_shared.py`, `scripts/check_skill_template.py`
  and `AGENTS.md`. The coordinator ran the script on a scratch copy of `plugins/lusona` and
  `shared` under `tmp/` and observed each output the section quotes.
- Result (2026-11-12, working tree on `0bac309`):
  - A changed source: `--check` printed "region final-reply differs from source" for each of
    the 14 skills and exited 1; the sync printed `synced skills/<name>/SKILL.md` lines and
    exited 0; `--check` then printed "Shared regions in sync." and exited 0.
  - `every-task.md` at 313 words: "313 words exceeds 300", "nothing written", exit 1.
  - A new source file without markers: "missing region extra" for each skill, "nothing
    written", exit 1.
  - In the repository: `sync_shared.py --check` exit 0; `git diff --check` clean;
    `scripts/package.py` built `lusona-3.0.0.zip`; every relative link in `CONTRIBUTING.md`
    resolves.
- Limitations: the duplicate-region and marker-line rules were not run by hand; they are
  stated from the script and its 18 tests in `scripts/test_sync_shared.py`, which passed on
  2026-11-12 after this change. Rendered Markdown was not inspected.

### Conclusion and decisions

- Deviation: the section was written by the coordinator without a leaf.

## Current handoff

- Authority: the `CONTRIBUTING.md` section, TDD `none`; local commit (user, 2026-11-12,
  conversation: "commit"). Push and publication are not authorized.
- State: committed on `main` in the commit that follows `0bac309`.
- Next action: none for this change.
