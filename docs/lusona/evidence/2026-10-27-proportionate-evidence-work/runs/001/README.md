# Run 001 — frozen paired probe

Completed 2026-10-27 (local date). [Decision and limits](../../README.md).

- [Baseline independent grades](arm-a.json): 5 pass, 1 expected policy mismatch.
- [Candidate independent grades](arm-b.json): 6 pass, no critical regression.
- [Evidence archive](evidence.zip), verified by [SHA-256 manifest](manifest.json).

The archive preserves the original directory layout under `proportionate-work-20261027/`.
Extract it into a scratch directory to follow the independent assessment's relative paths.
`grades/paired-review.md` contains the independent comparison and limited adoption
recommendation; the parent decision remains refine for the observed overhead concerns.

`conditions/` contains both exact instruction/fixture snapshots. `runs/` contains all 12
trials, 14 turns, inputs, command/results, stdout, filtered session traces, linked worker
traces, and before/after artifacts. `suite/`, `design-lock.json`, `candidate-recipe.md`,
`candidate.patch`, `candidate-application.json`, and `baseline-sequence-decision.json`
preserve design and sequencing. Capture and retention helpers are included. Source snapshots,
static check records, and `final-integrity.json` retain the implementation comparison and
canonical-file checks. `preflight/` preserves setup observations separately from behavioral red.

Git internals, bytecode caches, and generated package output are excluded from the archive.
Required-test cache effects are disclosed in the assessment. Root/child session traces retain
only relevant actions and assistant outputs, not complete host sessions. Original absolute
paths and session IDs are provenance, not promises that those paths exist after extraction.
No additional trial, canonical implementation, commit, or publication is implied.
