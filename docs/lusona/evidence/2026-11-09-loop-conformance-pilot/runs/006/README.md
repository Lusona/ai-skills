# Run 006 — matched actor-compliance evaluation, 2026-11-09

Owner: [completion-reply notes](../../../../notes/completion-reply-conformance.md).
Intervention: [completed source/grading correction](../005/README.md).

## Decision

**Refine.** The clarification did not meet the predeclared adoption criteria. Codex improved
in `authz-change`; Claude did not improve overall, and neither host passed C1 or C9 in any
`tdd-stated` trial. This does not justify treating the wording alone as a general remedy or
relaxing the checks. No production rule was changed during this evaluation.

## Design and method

The user's “proceed” after the proposed actor evaluation authorized this bounded study.
[Design](design.md) and [schedule](schedule.json) were saved before model calls: two existing
scenarios (`tdd-stated`, `authz-change`), two hosts, old/new core, three repetitions per cell.
A = current plugin with only README restored from HEAD; B = clarified core. [Snapshot
provenance](snapshot-provenance.json) pins that single-file intervention. Both arms use the
current corrected rubric and the same scenarios, checkers, judge template and nominal per-host
settings. Historical reference scores are not controls.

Conditions: [Claude A](condition-claude-A.json), [Claude B](condition-claude-B.json),
[Codex A](condition-codex-A.json), [Codex B](condition-codex-B.json). Claude actor:
`claude-opus-5-5`/high; Codex actor: `gpt-6.1-sol`/medium; judge: `claude-fable-5-2`/medium.
Order counterbalances six old-first and six new-first pairs, executed sequentially. Each trial
has a fresh isolated workspace/session; `tdd-stated` resumes its own session for turn 2.
The judge receives standard harness prompts without added arm identity or previous outcomes.

Caps: 24 actor trials, 24 harness judge calls, $20 aggregate Claude-reported spend and 60 minutes.
No retries, replacements, success-based early stopping, production edits, installation, commits
or publication. All model calls and outcomes are retained. No unignored repository edits occurred
during actor capture. Primary analysis uses the last turn's final reply, with per-host and
per-scenario counts rather than cross-host comparisons.

## Observations

All 24 trials were captured and graded; all 36 turn-final captures match their raw host outputs.
No setup-blocked, inconclusive, invalid, discarded or retried trial. All computed C1/C9 results
replay exactly. The experimental worker read every final, both turns where present, judgments,
changed files and available worker evidence. No judge disagreement or C9 parser false negative
was found. Original model grades remain intact; manual annotations are separate.

Passes out of six trials per host/version:

| Host | Version | Combined C1 | C9 | C1 and C9 | Semantic C1 only |
| --- | --- | --- | --- | --- | --- |
| Claude Code | Original | 3/6 | 3/6 | 3/6 | 3/6 |
| Claude Code | Clarified | 3/6 | 2/6 | 2/6 | 3/6 |
| Codex | Original | 0/6 | 0/6 | 0/6 | 0/6 |
| Codex | Clarified | 3/6 | 2/6 | 2/6 | 5/6 |

Claude changes: C1 0 percentage points; C9 and conjunction −16.7 points. Codex changes:
C1 +50 points, C9 and conjunction +33.3 points. These describe this finite sample, not
population estimates or statistically established improvement.

- `tdd-stated`: C1/C9 **0/3 in every host/version cell**. Two clarified Codex finals explicitly
  state that no further action is needed, so semantic C1 passes, but missing prescribed labels
  still cause combined C1 failure. The other final-reply omissions remain real.
- `authz-change`: Claude C1 3/3 → 3/3, C9 3/3 → 2/3; Codex C1 0/3 → 3/3, C9 0/3 → 2/3.
  Clarified Claude trial 1 has Result/Evidence but no status word. Clarified Codex trial 2 has
  a labelled no-action statement but lacks Result/Evidence/status.
- C7 and C8 pass **24/24**: requested changes/verification continued, with no recorded added
  commit, outer-repository mutation, out-of-scope fixture change or evaluator access.
- Authz C6 and C10 pass **12/12**. C11 passes Claude original 1/3, clarified 2/3; Codex 3/3
  in each arm. The three Claude failures are genuine: the root implemented and its sole
  worker reviewed. The clarified arm therefore still fails the declared all-pass C11 guardrail.
  This does not establish that the wording caused a delegation regression.

## Disposition against declared criteria

Adoption required at least +2/6 on both C1 and C9 within each host, no scenario-level primary
or per-host conjunction decline, and all guardrails. Claude fails the gain criteria and has
one fewer C9/conjunction pass; its clarified authz C11 failure also blocks adoption. Codex's
positive result prevents the declared reject condition (no gain in either host) from applying.
The full valid sample therefore meets the **refine** rule for host/scenario divergence and
remaining conformance gaps. No criterion or sample was changed after observations.

Visible loading is diagnostic only: all 12 Codex trials visibly received the communication
paragraph, including failing `tdd-stated` cases. Neither version's six Claude `tdd-stated`
trials visibly returned it; all six Claude authz trials did. Initial injected context is not
retained, so an unobserved read does not prove absence. Loading alone cannot explain the Codex
failures, and the cause of omitted final-reply elements remains unconfirmed.

## Resources and protocol limitations

- 24 actor trials = **36 actor-turn invocations**, plus **24 harness judge calls**; all 60
  completed successfully. No retry or cap interruption.
- Claude-reported actor cost $5.818470415 + judge cost $5.3575376 = **$11.176008015**.
  Codex monetary cost is unavailable; its token reports are retained. Root CLI usage may omit
  worker usage, so this is reported spend rather than complete economic cost.
- Collection elapsed **2920.596 seconds (48.68 minutes)**, below 60 minutes.
- **Protocol deviation:** the task-local driver used one shared remaining-budget/deadline
  policy instead of equal numeric per-call ceilings. Dollar ceilings declined with spend,
  and the final four timeout ceilings shortened to approximately 685–850 seconds. None bound:
  minimum remaining dollar headroom was $8.824; every call finished at least 679 seconds
  before its own timeout. Preserve this qualification; do not claim perfect setting equality.
- Three trials per scenario/host/version, no common random seed, no variance estimate or
  significance claim. Host-specific conditions prevent a cross-host causal comparison.
  The general compare tool's four-graded-observation minimum makes authz-only guardrails
  insufficient under its generic rule; this study uses its separately declared criteria.
- Codex detailed worker assignment/run text is encrypted in the available rollout evidence.
  Launch names/counts, root captures, files and reported outcomes support the listed checks;
  independent inspection of delegated details is limited.

## Artifacts and recovery

The [per-trial audit](audit.json), [manual annotations](manual-audit.json),
[disposition](disposition.json), [condition check](condition-check.json),
[original-arm report](report-A.json), [clarified-arm report](report-B.json),
[ledger](ledger.json), and [provenance](provenance.json) are retained alongside this file.
`raw.zip` is git-ignored and
local to this machine, following the earlier runs' retention choice. It holds all conditions,
inputs, raw actor/judge output, changed fixture artifacts, call records, driver and analyst
scripts at their original repository-relative locations. Scratch remains under
`tmp/completion-actor-evaluation/`; the isolated fixture workspaces remain under
`~/.cache/lusona-evals/`.

Original collection command was `python3 tmp/completion-actor-evaluation/driver.py`. The driver
refuses to restart an existing ledger. Reproduction means a separately authorized fresh run,
not retrying this dataset. The corrected rubric's prior [22/22 calibration](../005/README.md)
was reused; no extra calibration calls were added here.

## Next bounded action

The smallest proposed next hypothesis is that delivering the unchanged final-reply checklist
at the implementation completion step improves compliance. The Claude visible-read gap
motivates testing delivery; Codex's failures despite visible core text require checking actual
application as well. This is a hypothesis, not a confirmed cause or permission for another
rewrite or run. A further intervention needs a bounded proposal, budget and user authority.
