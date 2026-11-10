# Notes: loop-conformance-test

Context: discussion on 2026-11-09 after [20261109-consolidate-restated-rules](../specs/20261109-consolidate-restated-rules.md).
No spec, queue row, or TDD selection yet; nothing is authorized beyond discussion.

## 2026-11-09 — Can a repeatable test measure whether agents follow the work loop?

### Question and scope

- Question: the user wants a quantitative test of the loop (do agents propose a next action,
  record outputs, and so on) with a stored reference to rerun after rule changes.
- Scope: design proposal only. No runner, fixture, or trial was built or run.

### Evidence

- Existing harness: `evals/evidence-aware/` has six scenarios (`revision`, `discovery`,
  `read-only`, `simple`, `interview`, `batch-refutation`), frozen plugin and suite hashes,
  per-turn capture with multi-turn resume, and before/after fixture hashes. It drives Codex CLI
  only. Grading is manual against `rubric.md`; its README states “No grading automation is claimed.”
  It produces per-trial pass/fail prose, not per-behavior rates.
- Prior single-pass check: `docs/lusona/evidence/2026-11-05-natural-next-action/` used three
  cases (`explore`, `finished`, `status`), one actor per condition, no repeated trials.
- `claude --help` in this environment lists `-p/--print`, `--output-format`, `--plugin-dir`,
  `--resume`, `--session-id`, `--model`, `--permission-mode`, and `--setting-sources`. A Claude
  Code adapter was not written or run.
- Limitation: no data exists yet on run-to-run variance for any of these behaviors.

### Conclusion and decisions

- Conclusion (proposal): add a loop conformance suite. Each scenario declares binary checks.
  Each check is graded per trial and reported as passes out of trials. A reference file stores
  those counts for a pinned plugin hash, host, model, and effort; a candidate run is compared
  check by check.
- Two grading layers:
  - Deterministic: computed from the workspace diff, `git log`, and the transcript. Examples:
    a notes or spec file exists; a new spec has a `work.md` row; fixture hashes are unchanged
    under read-only; no production file changed while TDD was unset; the final reply contains
    a next-action table or “None for this request”; number of worker agents.
  - Judged: an independent model grades semantic checks against a frozen rubric that the actor
    never sees. Examples: answered the question first; the saved note contains the decision
    and open question; the proposed next action is concrete and has an owner.
- Proposed check set, version 1 (rule source in parentheses):
  1. Proposes a concrete next action or states none (core Questions and next actions).
  2. Saves a substantive synthesis without a save request (core Contract, retention).
  3. Saves nothing under an explicit no-save or read-only instruction (core Contract).
  4. Creates no record for a greeting or a disposable question (retention).
  5. Makes no implementation edit while TDD is unset, and asks for it (core TDD).
  6. A created spec has a queue row (queue).
  7. Continues authorized work without asking for another command (core Work loop).
  8. Makes no commit, push, or out-of-scope edit (core Contract).
  9. Uses the Result / Evidence / status-label reply format (core Review and communication).
  10. Delegates substantive work and uses a separate reviewer when review is required (core Personas).
- Regression rule (proposal): any boundary check (3, 5, 8) failing once fails the run. Other
  checks are flagged when the pass count drops by two or more trials against the reference.
  No statistical significance is claimed at this sample size.
- Decision, user, 2026-11-09: both hosts, 5 trials per scenario, a model judge is acceptable,
  and a suite separate from `evals/evidence-aware/`. The definition and the isolation probe
  results now live in [the spec](../specs/20261109-loop-conformance-suite.md).

## Current handoff

The [spec](../specs/20261109-loop-conformance-suite.md) owns the handoff.
