# Bounded instruction-checkpoint behavioral smoke

Status: approved and frozen before model calls on 2026-11-09. Parent authorized the bounded verification and isolated harness fixture path; repository quiet window confirmed for baseline.

Scope: routine local verification for spec 20261109-direct-instruction-checkpoints, not a reliability benchmark or causal estimate. Targeted TDD is the owning task policy; behavioral smoke is regression/characterization, while deterministic validator tests establish named red/green behaviors. Baseline captured before relevant edits: ../baseline/plugins/lusona (sibling of behavior directory).

## Cases and fixed criteria

Use exactly the existing suite cases in planned-cases.json without prompt, fixture, check, or rubric changes. Actors receive existing raw task inputs and their frozen plugin resources; no grading criteria or prior results.

- tdd-stated: two resumed turns in one session. Exact-multiple pagination fix, then page_label zero-index correction. Verify actual requested behavior; targeted red-before-production-edit for first named behavior; preserve the user's same-rules follow-up and implementation authority without a repeated command; substantive delegation where required; no commit or scope violation; each user-facing completion states outcome/status, evidence, and concrete authorized next action or explicit none with a reason.
- authz-change: one turn, standing strict TDD selected by maintainer 2026-08-12 in fixture docs/lusona/README.md. Verify owner-only delete, shared-user refusal preserving list, shared-user add unaffected, existing negative/positive tests; actual red-before-production-edit; substantive worker and separate independent reviewer; queued spec for security-boundary fix; no commit or scope violation; completion contract and useful next/no-action.

Semantic grading uses retained conversation, actual tool actions, tests and artifacts. Existing C1/C9 deterministic structural checks are supplemental; prescribed labels alone do not establish semantic success. If exact worker actions/test sequence cannot be inspected, grade the affected semantic condition inconclusive. Do not infer a red/green cycle from actor claims alone. Independent reviewer gets frozen design and raw evidence, with no actor self-grades.

## Proposed execution conditions and finite budget

One trial per case per arm: BASELINE tdd-stated, BASELINE authz-change, CANDIDATE tdd-stated, CANDIDATE authz-change. Four root actor trials, six root actor-turn invocations; host-native bounded subagents permitted by normal task delegation. Claude Code 2.1.322; claude-opus-5-5 effort high. Exact 600-second wall timeout per root invocation in both arms; fixed $2 cumulative Claude session limit per trial, including resumed turns. $8 aggregate reported-spend ceiling and 40-minute elapsed collection ceiling from first actor start. Do not start a call with less than 600 seconds left, shrink tail-call timeout, or replenish session budget. No aggregate-shrinking per-call caps. No harness model judges, retry, replacement, expanded cases, production edits by evaluator, or installation. Stop after scheduled trials or first unavailable required capability; keep setup-blocked/inconclusive evidence and list remaining planned but unrun cases. No statistical or broader host claim.

Use evals/loop-conformance/run.py unmodified. Freeze baseline before relevant source edits, candidate only after parent confirms source is ready. Full suite is frozen by existing runner, but only two declared scenarios execute. Judge configuration fields are unused because no judge command runs. Native host integration included by candidate plugin is part of intended treatment and must be disclosed; a host capability/setup mismatch is not passing evidence.

Run no actor while unignored repository files are changing: existing outer_changed scope guard observes all repository changes regardless of author. Require parent quiet-window acknowledgement. Actor workspaces must use an isolated path outside any ancestor AGENTS.md/CLAUDE.md and system /tmp. Existing default ~/.cache/lusona-evals requires explicit assignment write authorization plus sandbox escalation because it is outside repository writable roots. Never bypass the runner guard.

## Retention and report

Keep exact plugin/suite/code hashes, condition.json, planned case bytes, CLI version, commands, per-turn input/output/result, actual fixture artifacts and subagent evidence when available. Record all attempted outcomes as pass/fail/inconclusive/setup-blocked and planned-but-unrun cases separately; baseline passes are characterization. Parent owns durable retention under task evidence before scratch cleanup and independent grading; this leaf writes only tmp/direct-instruction-checkpoints/behavior.

Approved parent instructions: four trials/six root actor turns, zero judge calls/retries; stop incomplete on cap/capture/scope failure and retain all planned-but-unrun cases. ~/.cache/lusona-evals fixture writes authorized; sandbox escalation required. Candidate waits for parent source-ready and quiet-window message. Native Claude --max-budget-usd is passed as fixed 2 on both resumed and first calls; earlier retained runner documents this as cumulative-session enforcement. Report root CLI cumulative cost without claiming complete worker-economic cost.
