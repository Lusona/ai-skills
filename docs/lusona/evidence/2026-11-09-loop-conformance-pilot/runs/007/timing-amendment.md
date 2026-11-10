# Candidate collection timing amendment

Declared before candidate collection on 2026-11-09. The user explicitly paused implementation for discussion, then explicitly resumed implementation and required verification with “proceed.” The parent authorized this timing-only continuation. No actor calls occurred during the pause.

The original `design.md`, `collect.py`, baseline condition, baseline captures and `ledger.json` remain unchanged. Candidate collection under the original 2400-second elapsed window is unrun: less than one unchanged 600-second call window remained when continuation was considered. Do not reinterpret the original window as successful completion or silently extend it.

This amendment permits only the two originally planned CANDIDATE trials (`tdd-stated` with its resumed second turn; `authz-change` with one turn). Candidate collection receives a fresh 1800-second elapsed window beginning at the first candidate actor call. Keep every per-call timeout exactly 600 seconds, and skip the next call if less than 600 seconds remain. Do not shorten tail-call timeouts or retry blocked/incomplete trials.

All other scope and resource limits remain fixed:

- Four root actor trials and six root actor calls overall; baseline used two trials and three calls. Exactly two trials and three calls remain.
- $8 aggregate Claude-reported spend overall; baseline used $0.8214538. Aggregate headroom before candidate is $7.1785462.
- Fixed `--max-budget-usd 2` cumulative session limit for each trial, passed unchanged on the resumed turn. Do not replenish the session budget.
- Same Claude Code 2.1.322, `claude-opus-5-5`/high, tool/sandbox permissions, scenarios, fixtures, order within each arm, outcome criteria, raw evidence retention and independent grading.
- Zero model judges, retries, replacement trials or additional cases. Stop incomplete on cap, capture or scope failure. Retain all attempted and planned-but-unrun outcomes.

`continue-candidate.py` is a separate continuation wrapper around the unchanged existing harness APIs; it does not rewrite the original collector or baseline ledger. `continuation-pin.json` pins this amendment, wrapper, original baseline pin and original ledger before candidate calls. Candidate provenance will be pinned separately after the parent confirms final source readiness. `candidate-continuation-ledger.json` owns candidate timestamps, deadline, exact commands and deltas while referencing the original ledger hash and recording overall call/trial/spend totals.

Await parent final source-freeze and repository quiet-window confirmation before freezing or launching candidate. Report this amendment and the user-requested pause/resume with final evidence. This bounded task verification supplies no reliability estimate or statistical improvement claim.
