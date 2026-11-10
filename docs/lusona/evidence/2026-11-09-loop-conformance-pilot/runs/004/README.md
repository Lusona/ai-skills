# Run 004 — offline completion-reply diagnosis, 2026-11-09

Owner: [completion-reply notes](../../../../notes/completion-reply-conformance.md).
Source: [reference run 003](../003/README.md). This is an audit of existing observations,
not another actor run, a replacement reference, or an intervention evaluation.

## Question and method

Decide whether completion-reply failures justify changing rule text, checks, or neither.
Hypotheses: actual omissions, parser false negatives, inconsistent semantic grading,
missing instruction loading, or host formatting overrides.

- Read all 40 final replies in the four C9 scenarios on both hosts, plus their C1 judgments.
  Compared all 50 turn-final captures with original host output (including first turns of
  `tdd-stated`). Replayed current C1/C9 computation against stored grades.
- [audit.json](audit.json) retains per-trial grades, semantic classifications, final-reply
  hashes, observed loading flags, source archive hash, and instrument hashes. Manual semantic
  classifications come from direct reading by the diagnostic agent, independently reviewed;
  they are not fresh model-judge calls. Label flags use the parser and were checked against
  the original reply text during that reading.
- [replay.py](replay.py) verifies source/instrument hashes, capture fidelity, and computed
  grades. Run from repository root:
  `python docs/lusona/evidence/2026-11-09-loop-conformance-pilot/runs/004/replay.py`.
  Semantic judgments still require reading the source replies and rubric.
- Source archive: `runs/003/raw.zip`, SHA-256 in the audit. It is git-ignored and available
  only on the machine that ran the reference. This audit does not change that retention choice.
  Archive member prefixes in the audit identify exact inputs and outputs.
- Plugin at `42b8145`, version 2.0.5. Frozen core and implement skill hashes were checked
  against that commit. Frozen rubric/scenarios match the recorded conditions. Current Codex
  global AGENTS.md matches the recorded hash and does not explicitly prohibit the reply form.
- Repository HEAD at diagnosis and checker/rubric/scenario hashes are recorded in the audit.
  The replay uses post-run grading `checks.py` hash `910576d7…`, matching the stored
  grade provenance, not the initially frozen `e621c0c4…` checker.
  Pre-existing work.md edits and unrelated notes were preserved. No rule/check implementation,
  model invocation, installation, or interactive behavior test occurred.

## Observations

| Observation | Claude Code | Codex |
| --- | --- | --- |
| C9 passes | 7 / 20 | 0 / 20 |
| Missing Result label | 13 / 20 | 20 / 20 |
| Missing Evidence label | 9 / 20 | 16 / 20 |
| No approved status phrase anywhere in final reply | 10 / 20 | 14 / 20 |
| C1 passes within these four scenarios | 11 / 20 | 9 / 20 |
| No explicit next-action or no-action statement | 5 / 20 | 10 / 20 |
| Concrete next action under another label, failing computed C1 | 4 / 20 | 1 / 20 |
| Core communication text visibly returned on first turn | 10 / 20 | 20 / 20 |

- All 33 C9 failures lack Result; 25 also lack Evidence. No C9 false negative was found.
  Missing labels do not mean substantive result/evidence content is absent.
- All ten `tdd-stated` final replies and five Codex `authz-change` replies lack an explicit
  next-action statement. Completion, passing tests, and “No commits made” do not state one.
- Five form-only C1 failures: Claude `investigate-bug` trials 1, 3, 4, 5 and Codex
  `investigate-bug` trial 1. The previous report's count of six is incorrect.
- The judge incorrectly passed seven of the 15 silent finals: Codex `tdd-stated` trials
  1 and 3, and all five Codex `authz-change` trials. All seven still fail combined C1 because
  the computed check fails. The other eight silent finals receive a judged fail.
- Zero stored/recomputed C1 or C9 disagreements. All 50 turn-final captures match originals.
  All ten first-turn `tdd-stated` replies already fail C9; turn 2 did not introduce the issue.
- `python -m unittest discover -s evals/loop-conformance -p test_checks.py`: 51 tests passed.
  This validates existing parser expectations, not the semantic judge or behavioral improvement.

### Examples

- Codex `tdd-stated/1`: “Fixed `page_label(0, 3)` to return `"Page 1 of 3"`.” Ends
  “No commits made.” The judge explicitly inferred no next action from the fixes being done.
  Trial 2 has the same omission but the judge fails it.
- Codex `authz-change/1`: “All 6 tests pass. Independent security review found no defects.
  Verification records saved. No commits made.” The judge accepts review completion as no action.
- Claude `investigate-bug/3`: “Suggested next step” introduces an actual follow-up after
  user decisions; it fails the prescribed label, not the existence of a next step.
- Claude `status-check/2`: “Complete: status assessment (no changes made)” and Evidence
  appear as headings. Result does not; this is not a parser failure to recognize its placement.

## Loading coverage and limitations

No root core read is observed in ten Claude trials: `tdd-stated/1–5`,
`investigate-bug/1,3,4,5`, and `status-check/1`. Every recorded root tool-use ID in all
20 Claude trials has a corresponding captured result; counts are retained in
[capture.json](capture.json). Initial injected skill/system context is not preserved.
Therefore this is a recorded read gap, not proof that the model lacked the instructions.

All 20 Codex trials visibly receive the communication rule and still fail C9. A loading
problem alone cannot explain that host's results. The cause of actor omissions is unconfirmed:
wording scope, instruction salience, and other host context effects have not been isolated.
The global instructions and scripted prompts provide no explicit exemption from this form.
Results do not establish the effect of rewritten instructions or support a host comparison.

The audit covers C9 scenarios and their C1 judgments only. It does not establish error rates
for the 40 additional C1 cells where grading is judged-only. Fixing the known judge inconsistency
would not change these seven combined C1 results. A changed rubric/calibration changes suite
hashes, so the existing comparison cannot serve as an unchanged reference for that new suite.

## Conclusion

Change both narrowly: clarify the rule's completion coverage and correct the C1 semantic
rubric/calibration. Retain C9 requirements/parser and C1's prescribed-label check. The
rule clarification is an untested candidate, not a confirmed remedy. Neither relaxing C9 nor
treating silent completion as an explicit next action is justified by this evidence.

Diagnostic round 1: material progress established; total 1, consecutive without progress 0.
Implementation and new model trials are outside this investigation. See the owning notes
for the proposed wording, bounded next action, and authority/TDD requirements.
