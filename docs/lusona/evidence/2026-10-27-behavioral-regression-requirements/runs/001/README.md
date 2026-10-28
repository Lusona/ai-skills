# Run 001 — contributor evidence assessment

## Declared design

Declared before the contributor-role assessment on 2026-10-27.

- Question: can the documented requirements support proportionate case selection and
  identify sufficient, incompatible, incomplete, and inapplicable behavioral evidence?
- Inputs: frozen contribution guidance and five synthetic evidence packets. A separately
  frozen answer key is available only to the evaluator. Snapshots and hashes are retained
  with this run before dispatch.
- Method: a fresh contributor-role subagent reads only the permitted exercise inputs and
  returns its selections, assessments, evidence references, and limits. A separate reviewer
  grades that response against the key and inspects the implementation against AC1–AC7.
- Expected result: the assessment distinguishes a valid comparison, incompatible conditions,
  setup failure presented as red, a pass claim lacking independent evidence, and an editorial
  change eligible for static verification. At least one packet exercises multi-turn evidence.
- Budget: one assessment of the five packets and one independent grading/review assignment.
  No installed-host or CLI behavioral trials, external services, or runtime policy changes.
  A necessary correction must preserve this run and declare any further assessment separately.
- Stop: after the assessment and independent review return, or when a prerequisite prevents
  a valid assessment. Preserve failures and limitations; do not silently retry to obtain a pass.
- Actor: `gpt-6-luna`, medium reasoning, fresh context (`fork_turns: none`). Evaluator:
  `gpt-6.1-sol`, high reasoning, a separate fresh context. Both use this session's collaboration
  tools; an exact host-build identifier is not exposed and is not inferred from installed CLIs.

## Coverage and limits

This is an in-session assessment of written fixture evidence, not a baseline/candidate trial
of runtime skill behavior. The embedded fixture results are fictional. Expected outcomes and
the key are withheld from the assessor's assignment. Access separation is instructional, not
an OS read-isolation boundary. One assessment establishes only this exercise's observed result.
No timing, token, or total-cost comparison is planned.

## Observations

- Frozen inputs and settings: [conditions](conditions.json), [assignment](assignment.txt),
  [contribution guidance](inputs/CONTRIBUTING.txt), [packets](inputs/cases.txt), and
  [evaluator-only key](inputs/review-key.txt).
- Actual assessor: `/root/regression_assessment`; [complete response](assessment.md) and
  [provenance](assessment-provenance.json). It returned one assessment; no retry occurred.
- Independent evaluator: `/root/regression_review`; [complete grading and diff review](review.md)
  and [provenance](review-provenance.json). It had no implementation or assessment role.
- [Actual implementation diff](implementation.patch) and [repository checks](checks.md)
  are retained separately from synthetic packet evidence.

| Packet | Observed assessment | Independent grade |
| --- | --- | --- |
| A | Accepts the limited matched comparison and relevant coverage | Pass |
| B | Rejects comparative improvement under mismatched conditions and incomplete responsibility coverage | Pass |
| C | Rejects setup failure as red and identifies unrun work, but gives incomplete recovery advice | Partial fail: coverage and diagnosis pass; recovery fails |
| D | Rejects the pass claim without independent grades; requests grading of retained captures | Pass |
| E | Accepts editorial-only static verification without invented trials | Pass |

## Reconciliation and conclusion

The coordinator accepts the independent grades: four packets pass and Packet C partially
fails. Its original assessment and the frozen key remain unchanged. The corrected advice
for Packet C is to resolve the already-broken selected test-first sequence or obtain an
authorized revised approach before further trials, preserving the failed attempt and
chronology. A new budget and later baseline/candidate captures do not retroactively make
earlier edits test-first. This correction is coordinator reconciliation, not a second
successful assessor trial.

The contribution guidance already states that sequencing rule; independent review found
no actionable implementation defects. The bounded AC7 exercise required recorded expected
and observed assessments, not universal assessor success. It is complete with this explicit
limitation. The result supports usability for the demonstrated distinctions, not reliable
adherence across agents or flawless recovery recommendations. No further trial was run.

The assessor reports no excluded reads, but its complete tool transcript was not retained;
the absence of key access is not independently proven. Exact final responses and their
hashes are retained. The evaluator verified source/input/output hashes, actual diff identity,
links, archive contents, and declared verification limits.

Next action: none for this exercise. The change record owns implementation completion;
future work must not cite this run as five clean passes or as runtime/installation evidence.
