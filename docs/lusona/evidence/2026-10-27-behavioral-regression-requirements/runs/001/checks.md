# Implementation checks — 2026-10-27

Coordinator checks on the actual working tree, separate from fictional packet results:

| Check | Observed result |
| --- | --- |
| `mise exec claude@2.1.310 -- claude plugin validate plugins/lusona` | Exit 0, validation passed. Existing non-failing advisory: plugin README lacks a marketplace install line. |
| `mise exec claude@2.1.310 -- claude plugin validate .claude-plugin/marketplace.json` | Exit 0, validation passed. |
| `mise exec python@3.12.13 -- python scripts/package.py --output tmp/behavioral-regression-requirements/package` | Exit 0; generated the current 1.2.0 local archive. |
| Archive inspection with Python `zipfile` | Packaged CONTRIBUTING bytes equal source; its linked evidence procedure is included; evals, project records, and scratch files are excluded. |
| Changed contributor/exercise Markdown links, anchors, final newlines, and requested wording constraints | Passed across CONTRIBUTING, pull request template, and all three exercise files. |
| `git diff --check` | Exit 0. |
| Source hash comparison against the pre-implementation manifest | Existing files changed only within this task's contributor/PR and work-record scope; prior unrelated working-tree changes remain intact. |

The archive is a generated local check artifact, not a release. No executable or runtime
skill behavior changed in this implementation. Evaluation-runner tests were not rerun
because that code and its existing fixtures/rubric were unchanged. No installed-host or
CLI behavioral trial was run; in-session agents assessed synthetic written records.
Installation and interactive behavior have not been tested.
