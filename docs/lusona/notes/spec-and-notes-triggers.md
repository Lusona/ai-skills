# Notes: spec-and-notes-triggers

Context: direct rule change without a spec, after the user observed that specs are rarely
created now; evidence from the `ror-starter-kit` project (3 notes, 0 specs, no queue).

## 2026-11-03 — Is there a bias toward notes over specs?

### Question and scope

- Question: whether the rules route direct changes to notes instead of specs, and whether
  that costs anything visible in the records.
- Scope: `references/retention.md`, `references/queue.md`, `references/workflow-guide.md`
  routing, `skills/explore`, `skills/implement`, `skills/refactor`, `templates/work.md`,
  root `README.md`.

### Evidence

- Method: read the three `ror-starter-kit` notes and the commits they own; traced the
  rules that decide the record type.
- Result: the only non-user path to a spec is Specify, which routes on unclear behavior.
  Explore settles the request, implement treats a clear request as needing no Specify, so
  the owner defaults to notes. The `result-kernel` change (18 files, new `ApplicationService`
  and `ApplicationJob` base classes) meets the shared-contract independent-review trigger;
  its notes record no review. Its handoff names a follow-up defect with no queue row, because
  the proposal rule applied only to tracked work and no queue existed.
- Limitations: whether a review happened in session is not recorded either way. No defect
  was observed in the delivered changes.

### Conclusion and decisions

- Conclusion: the low spec count is the 2026-11-03 decision working as decided. The visible
  cost comes from two rules that record type did not cover: review triggers unchecked at
  implement entry, and follow-ups from untracked work having no landing place.
- Decision, 2026-11-03 (user): keep notes as the default for clear direct work (option A)
  and apply two fixes instead of changing spec frequency:
  1. Implement and refactor decide at entry whether the change meets an independent-review
     trigger and name the required review in the handoff; a change that requires independent
     review requires a spec so the reviewer has recorded acceptance criteria (retention).
  2. The proposal rule applies to untracked work too: a follow-up found during notes-only work
     adds an Ideas row linking the notes, creating the queue from its template when absent, or
     is named in the reply as unowned when saving is restricted.
- Rejected: B (every implement/refactor records a spec) and C alone (spec on review
  triggers without the proposal fix).
- Independent review (read-only subagent, 2026-11-03): one blocking finding, the notes and
  spec templates still listed the spec triggers as a closed list; fixed by pointing both at
  retention. Applied non-blocking findings: the spec trigger names the content triggers only
  (security boundaries, persistent data, shared contracts, coordinated writers), so a blanket
  repository review rule does not turn option A into B; acceptance criteria are recorded
  before implementation starts; discussion is exempt from the proposal rule; skills keep a
  pointer plus the entry decision, re-made when scope grows; a delegated worker returns the
  Ideas row to its coordinator; restricted saving reports through a permitted channel.
  Not applied: a provisional completion condition on raw Ideas rows; the three statements of
  the Ideas-row rule (queue, retention, work template) follow existing precedent.
- Checks: `python3 scripts/check_instructions.py`; `python3 -m unittest
  scripts.test_instructions scripts.test_package`; `python3 scripts/package.py`;
  `claude plugin validate plugins/lusona`. All pass. Not run: marketplace validation
  (unchanged), work-record helper checks (unchanged), live installation or invocation.
- Known consequence: "shared contracts" raises spec frequency in library repositories
  regardless; the notes-only repositories gain a `docs/lusona/work.md` the first time a
  follow-up appears.

## Current handoff

- Authorized work: rule edits complete and independently reviewed; uncommitted. This change
  was recorded under the rules in effect when it started (notes, no spec).
- Next action: user reviews the diff; commit requires a separate request.
