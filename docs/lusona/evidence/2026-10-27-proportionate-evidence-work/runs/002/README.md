# Run 002 — canonical implementation verification

The user authorized implementation of the reviewed refinement with targeted TDD. The exact
eight-file patch is applied to canonical sources. Independent review accepts the bounded
implementation; no actionable source defect or current-candidate critical violation remains.

| Evidence | Result |
| --- | --- |
| Original six baselines, reused after source/fixture comparison | 5 pass / 1 intended contribution-policy mismatch |
| Two fresh valid/stale worker-evidence baselines | 2 pass; valid evidence reused, stale evidence rerun |
| Eight implemented-source cases | **7 pass / 1 fail**, retained unchanged |
| Separately approved explicit-scope follow-up | Old baseline **fails critically**; implemented candidate **passes** |

The initial failure is a fixture expectation conflict: its evaluator allowed only the help
heading file to change, but the raw task did not prohibit updating the existing owning spec.
The actor appended truthful verification/readiness text under unchanged recording instructions.
Independent review found no source correction justified; the failed criterion remains a failure.
A separately frozen pair made the raw write restriction explicit without weakening the criterion
or changing sources. The user explicitly approved those two follow-up trials.

That pair exposed a genuine old-baseline violation: its worker wrote a 35-byte temporary file
outside the allowed workspace and the unittest ran in both worker and root. The current candidate
changed only the permitted heading file, ran the test once, and kept unavailable production
improvement unverified. The external file's bytes and metadata were retained; it was removed after
matching its content and timestamp to the trial. No additional trials ran. This is adverse reference
evidence, not proof that the instruction change caused the difference.

Other candidate cases preserve authority, same-session read-only steering, TDD and truthful claims,
while accepting proportionate candidate-only contribution evidence. Valid worker evidence was
inspected and reused without another test run; stale evidence triggered one current check. The
routine documentation task ran its unittest once, versus twice in the earlier prototype. These
are individual observations, not general efficiency claims.

## Verification and records

- [Initial candidate grades](candidate-grades.json) and [follow-up grades](followup-grades.json).
- [Complete evidence archive](evidence.zip), verified by its [SHA-256 manifest](manifest.json).
- [Earlier baselines](../001/README.md) and [refinement checks](../../refinement/checks.zip).

The archive preserves designs, approvals, locks, fixtures, source snapshots, commands, root/worker
traces, artifacts, grades, adverse results, recovery and reviews under
`proportionate-implementation-20261027/`. Read `final-review.md` for independent reconciliation.
Twelve fresh sessions/thirteen turns ran across two declared budgets; none was retried merely to
obtain a pass. Two approval rejections ran no actor and remain setup history, followed by explicit
consent for the modified prompt.

All eight adopted files match the reviewed patch; the other 44 pre-existing canonical files are
unchanged. All 65 packaging inputs match previously checked copies. Passing skill, link/anchor,
native manifest/catalog and package checks were reused; actual-diff whitespace and source identity
checks passed. Native validation's installation-line advisory remains. Across affected sources,
the implementation is 337 words below the first prototype and 10 below baseline; runtime plugin
sources remain 16 words above baseline, including shared core +48.

Targeted TDD retains the original contribution failure before edits and the current passing
outcome. Routine/local baseline passes and new boundaries are characterization; no red was
manufactured. Original 7/8 and follow-up 1/2 results are not relabeled as clean suites.

## Limits

One host/root model and one observation per case limit generalization. Valid/stale case IDs partly
cue actors. Scheduling and worker routing/model mix differ; root usage is not total cost. No timing,
cost, significance, causal-superiority or universal-safety claim. Snapshots exclude Git internals
and bytecode caches; reviewers also inspected actions, finding the external baseline write that
workspace snapshots missed. Explicit-scope results do not establish that every unconstrained task
avoids owning-record updates. Installation and native interactive behavior remain untested.
No commit or publication occurred.
