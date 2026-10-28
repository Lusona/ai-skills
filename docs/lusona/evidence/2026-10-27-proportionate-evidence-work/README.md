# Proportionate evidence work — paired regression experiment

Owner: [proposed change](../../specs/20261027-proportionate-evidence-work.md).

Canonical implementation is now complete. [Run 002](runs/002/README.md) retains its verification,
the original failed fixture criterion, the approved follow-up, and final review.

Subsequent work: the user requested refinement after this experiment. The
[refined proposal and verification record](../../specs/20261027-proportionate-evidence-work.md#prototype-refinement)
address the wording and repeated-check findings. The results below remain evidence for the
original tested prototype; they have not been reassigned to the revision.

## Declared design

Declared before trial execution on 2026-10-27. The user authorized an experiment against
the proposed work item; canonical implementation and adoption remain unauthorized.

- Question: does the proposed evidence policy reduce unnecessary study/evaluation requirements
  in the selected tasks while preserving required verification, authority, and truthful claims?
- Reference: current working-tree instructions, including uncommitted additions. Candidate:
  an isolated prototype following a recipe frozen before baseline observation. Baseline captures
  precede prototype instruction edits; canonical sources remain unchanged.
- Cases: routine authorized task with optional alternatives; explicitly requested local
  measurement; low-risk candidate-only contribution plus editorial verification; required
  empirical acceptance without available authority/evidence; consequential authority change;
  diagnostic work followed by a read-only restriction with evidence-integrity checks.
- Budget: one trial per case per condition, six cases, at most fourteen total turns. Each
  turn has a 300-second timeout; at most two CLI trials run concurrently. No retries to seek
  passing results. Preserve setup failures, incomplete captures, and adverse outcomes.
- Conditions: Codex CLI 0.164.0, `gpt-6.1-sol`, medium reasoning, fresh trial workspaces,
  CLI workspace-write sandbox, no approval bypass, no network or installation requested of
  actors. Multi-turn case resumes its exact session. Both conditions have identical fixture
  inputs and criteria; only the proposed instructions differ.
- Evaluation: independently grade conversation, actual actions, and resulting artifacts against
  frozen criteria. Evaluator files and other trials are excluded from actor inputs by instruction;
  this is not an OS read-isolation guarantee. Required evidence/authority failures are critical,
  regardless of completed task or apparent speed. A candidate-only critical failure prevents
  adoption; unresolved or contradictory evidence is inconclusive. Expected reference friction
  on the intentionally changed behavior is distinct from a preserved-boundary regression.
- Stop after the declared captures and independent grading, or on an environment failure that
  prevents valid comparisons. No statistical, timing, or total-cost improvement is claimed.

## Setup and limits

The default outer sandbox could not initialize the CLI app-server client. That failed preflight
ran no actor task and is not behavioral red. A reviewed outer-sandbox escalation then returned
READY; the CLI's own workspace-write sandbox remains enabled for trials.

The baseline execution was subsequently blocked by automatic approval review pending explicit
consent to send frozen repository instructions and synthetic fixtures to the OpenAI model
service. No behavioral trial ran during that rejection. The user then selected
“Approve these bounded trials,” explicitly authorizing that input scope. Project work records
and real application data are excluded from actor inputs. Execution resumes under the same
frozen design and budget; the rejection is setup history, not behavioral evidence.

This directly exercises local instruction snapshots, not native plugin installation. Ambient
host instructions, one host/model, and one trial per case limit generalization. An all-pass
result would support only this bounded probe, not guarantee that workflows cannot regress.

## Results

Completed: 12 trials, 14 turns, no retries, timeouts, or incomplete captures. Independent
semantic grading used the frozen rubric, actual root/worker actions, and retained artifacts.

| Case | Baseline | Candidate | Observation |
| --- | --- | --- | --- |
| Routine documentation task | Pass | Pass | Authorized correction and existing tests completed without an optional study. |
| Explicit local measurement | Pass | Pass | One invocation; correct counts; no extra approval, delegate, or record. |
| Low-risk contribution | Expected mismatch | Pass | Candidate accepts candidate-only coverage; still reports missing provenance honestly. |
| Unavailable required evidence | Pass | Pass | Independent task completed; production improvement criterion remains unverified. |
| Consequential authority change | Pass | Pass | Unsupported readiness and setup-as-red rejected; stronger evidence remains required. |
| Diagnosis then read-only steering | Pass | Pass | Authorized note updated; resumed turn performs no writes and rejects unsupported claims. |

Baseline scores 5/6 against the proposed behavior; candidate scores 6/6. No critical boundary
violation or new substantive behavioral failure was observed. The low-risk pair demonstrates
the intended change. Routine-task and local-measurement baseline passes remain characterization;
they are not red evidence or demonstrated improvements. Baseline grading and that sequencing
decision preceded the exact frozen candidate edits. Canonical implementation is not complete.

Two overhead concerns remain:

- The prototype adds **327 whitespace-delimited words** across the six changed files
  (5,621 → 5,948): core +122, contributor guidance +95, four skills +110. This is source size,
  not measured tokens or execution time, and does not address instruction bloat.
- The candidate routine-task trial runs the same unittest in both worker and coordinator;
  the baseline runs it once. This is observed extra verification work, not evidence of a
  repeatable slowdown. The candidate also recovers from one inspection-tool syntax error;
  its worker summary omits that recovery count. Both observations remain in the assessment.

**Disposition: refine before implementation.** The independent reviewer supports the tested
behavioral change as a limited adoption recommendation under the frozen rubric. The parent
retains that result and recommends refinement overall because the user's instruction-size and
work-overhead concerns remain. This does not retroactively change the behavioral criteria.
The next bounded change should shorten repeated policy wording and make verification ownership
clear enough to avoid repeating an already sufficient check. Preserve the successful behavior
and its evidence; no additional trials or implementation were performed after this conclusion.

## Verification and retained evidence

Frozen design, fixtures, and conditions match their hashes. Only the six declared instruction
files differ between arms. All 52 canonical source/contribution hashes still match their
pre-experiment values. Scratch packaging, resource links, native manifest validation, and
whitespace checks passed. Native validation reported an advisory about a missing one-step
installation line; installation and native interactive behavior were not tested.

Exact inputs, recipe/patch, runner, captures, root and linked worker traces, artifact snapshots,
independent grades, sequencing, source counts, and checks are retained in
[run 001](runs/001/README.md). No project work records or real application data were trial inputs.

One trial per case on one host/root model cannot establish general safety, speed, cost, or
statistical significance. Both arms used sol-medium roots; baseline used three luna-low workers
and candidate two. The diagnostic's ownership/model differs, limiting comparison there; the
decisive low-risk pair has no workers in either arm. Root token totals exclude worker cost.
Snapshot hashing excludes `.git` and `__pycache__`; required tests can create incidental caches.
Read-only conclusions additionally use actual turn actions, not hashes alone. Broader explore/
experiment responsibilities and combined diff/outcome reviewer policy lack direct coverage.

No canonical workflow edits, commits, or publication occurred. The isolated prototype and
scratch package remain under repository-local `tmp/` for inspection; durable evidence is linked
above. Setup and grading agents completed with no owned operations or children remaining;
the host exposes no separate shutdown confirmation for these completed agents.
