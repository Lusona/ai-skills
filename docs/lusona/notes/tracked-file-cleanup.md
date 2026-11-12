# Notes: tracked-file-cleanup

Context: direct cleanup without a spec. The user asked on 2026-11-12 to look for outdated and
redundant committed files and chose what to remove and correct.

## 2026-11-12 — Remove evidence archives and unlinked notes; use "TDD level"

### Question and scope

- Agreement (user, 2026-11-12, native question tool):
  - Delete the 11 `*.zip` archives under `docs/lusona/evidence/` and add a restore reference to
    each topic README.
  - Delete 6 notes with no inbound link: `changelog-last-four-versions`,
    `implementation-queue-creation`, `readme-rules-draft`, `readme-translation-sync`,
    `rules-cohesion-1-4-0` and `spec-and-notes-triggers`.
  - Correct the handoff of `final-reply-required-labels.md`, which said "uncommitted".
  - Replace "TDD policy" with "TDD level" in the `specify` description, the spec and status
    templates, `CONTRIBUTING.md` and `INSTALL.md`.
- Not selected, left in place: `notes/voice-pass/`, `notes/skills-rules-review-matrix.md`, and
  the rule inventory with `scripts/check_rule_inventory.py` and its test.
- TDD level: `none`. The selected option stated "I would use none and run the check scripts and
  tests" (user, 2026-11-12, native question tool).

### Evidence

- Method: `tmp/cleanup/survey.py` lists, for each tracked record, its size, the tracked files
  that name it, broken relative links and identical files. Its output before the change is
  `tmp/cleanup/before.txt` and after is `tmp/cleanup/after.txt`; both are scratch.
- Result:
  - Tracked files went from 430 (13,737 KB) to 413 (5,308 KB), before this record was added.
    The archives were 8,424 KB.
  - Each of the 7 evidence topics has a "Removed archives" section with path, byte count,
    SHA-256 and the command `git show 9f2260f:<path>`. Every archive blob at `9f2260f` equals
    the removed file, and `9f2260f` is on `origin/main`. 14 links to the archives now point to
    those sections. The manifests and `artifacts.sha256` are unchanged.
  - The 6 notes exist unchanged at `9f2260f` under `docs/lusona/notes/`.
  - The broken-link section of the survey is identical before and after: the removals added no
    broken link.
  - All exit 0 after the change: `sync_shared.py --check`, `check_voice.py`,
    `check_skill_template.py`, `check_contract.py`, `check_instructions.py`,
    `check_rule_inventory.py`; 229 script tests in 7 files; `evals/evidence-aware/test_run.py`
    (8), `evals/loop-conformance/test_run.py` (60), `test_checks.py` (75), `test_compare.py`
    (15); `scripts/test-work-record.sh`; `scripts/test-work-record.ps1` under PowerShell 7.6.10
    (187 assertions); `scripts/package.py` built `lusona-3.0.0.zip`; the English README link
    check; `git diff --check`.
- Limitations:
  - The archives remain in the repository history, so a clone does not get smaller.
  - No agent run used the changed `specify` description. Installation and interactive behavior
    were not tested.
  - "TDD policy" remains in `evals/loop-conformance/` (rubric, scenarios, calibration, tests)
    and `evals/regression-requirements/cases.md`. Those files are hashed suite inputs; changing
    them changes the suite lock.

### Conclusion and decisions

- Additions by the coordinator to the approved list, same term change:
  `plugins/lusona/skills/architect/SKILL.md:76`, `.github/pull_request_template.md:9`, and one
  sentence in the 3.0.0 changelog entry for the renamed spec template heading.
- Deviation: the work was done by the coordinator without a leaf.
- Found and not changed:
  - `evals/loop-conformance/reference/` holds 2 stored references that the suite README states
    are not comparable with the current suite.
  - Spec 20261111 records 1,026 inventory rows and 1,004 content lines; the check printed
    1,167 rows and 1,141 content lines on 2026-11-12.
  - `INSTALL.md` records a 1.4.0 installation check with "thirteen skills". No 3.0.0
    installation check is recorded.
  - Spec `20261030-require-durable-workflow-records` has no history entry.

## Current handoff

- Authority: the four selections above, TDD `none`; grouped local commits (user, 2026-11-12,
  conversation: "group and commit"). Push and publication are not authorized.
- State: committed on `main` in the two commits that follow `d7d16a2`: the term change first,
  then the removals with this record.
- Next action: none for this cleanup.
