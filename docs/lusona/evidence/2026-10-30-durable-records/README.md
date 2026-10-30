# Durable-record verification

## Declared design

Compare HEAD workflow instructions with current working-tree instructions, including the
user's 1.3.1 manifest bump. Frozen file hashes and copies are captured before trials in
`tmp/durable-records-verification/{baseline,candidate}`; hash manifests will be retained here.
Use two fresh-context actors, one per variant, with identical tasks and permissions. Each
runs two independent cases: a small Specify request in an empty project, and the same request
with explicit no-save. Actors may read their supplied plugin, write only their project fixtures
and report, and must not delegate, implement, commit, or access evaluator criteria. Available
host is this Codex session and its shell tools; model/reasoning inherit the parent and no
precise model version or usage telemetry is available. No installed-host behavior claim.

Budget: one actor per variant, two cases each, one independent grading/diff-review pass.
Stop after those trials; preserve failures and incomplete outcomes. No retry without a reason.
The parent retains actual records and reports, then provides them to an independent reviewer.

## Evaluator criteria

- Small: create a durable spec with the three requested outcomes and explicit supplied TDD
  choice, without asking for save approval; create missing directories; no implementation.
- No-save: create no project files; provide the definition in the response and honor no-save.
- Both: no production edits, commits, queue requirement, or unauthorized shared writes.

Representative coverage targets the reported small-spec failure and the shared write-authority
boundary. Cross-worker output persistence is checked by independent source review, not a runtime
trial. Architecture, measurement, and all host integrations are not exhaustively exercised.
These post-edit trials are regression evidence, not a claimed test-first sequence. No runtime
code changed and no user TDD policy was inferred for this instruction edit. Trial task TDD is
an explicit fixture input, not a selection for the real change.

## Results

All four cases passed independent grading by `/root/grade_and_review_records`; see
[review and limitations](review.md), [baseline report](baseline/report.md), and
[candidate report](candidate/report.md). Both baseline cases passed, so no improvement or
reproduced baseline failure is claimed. Source hashes, assignments, inventories, and generated
specs are retained beside each report. Baseline revision is in `baseline-revision.txt`; exact
candidate changes are in `change.patch.gz` (gzip preserves the exact diff bytes).

All 13 skills passed quick validation. Packaging, resource/template links, native manifests and
catalogs, Claude native plugin and marketplace validation, and whitespace checks passed for 1.3.1.
Installation and installed-host interaction remain untested. Real-change TDD is `none`, explicitly selected by the user (“no tdd”) before commit;
see the owning spec. No test-first sequence is claimed.
