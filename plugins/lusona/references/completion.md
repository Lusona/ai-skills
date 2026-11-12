# Completion examples

Read before composing a task's final reply. The examples are hypothetical replies, not evidence that work occurred.

## Complete, no action remains

**Result:** ✅ Complete: Corrected the broken documentation link.

**Evidence:** The target exists and the link checker passes. No review or delivery condition applies.

**Next action:** None for this request. The correction is verified and no follow-up serves the agreed outcome.

## Complete, with a proposed follow-up

**Result:** ✅ Complete: Corrected the requested documentation link.

**Evidence:** The corrected target exists and the link checker passes. The other links in the same guide were not audited.

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Proposed: audit the links in the same guide | coordinator | The guide path and the audit scope | Needs the user's authorization for the audit |

## In progress, with a continuation directive

**Result:** 🔄 In progress: Added input validation to the import command; 2 of 3 acceptance criteria pass. Context use reached 42%, so the handoff is saved in the spec; work continues in this session.

**Evidence:** `pytest tests/test_import.py` passes 14 tests. The empty-file criterion has no test yet. The full suite was not run.

**Decisions:** The empty-file check goes in the existing input validator, not the parser, so all input errors share one error path.

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Write the failing test for empty files, then the fix | implement | Spec acceptance criterion 3 | Authorized |

> When another session continues: resume spec `20261111-import-validation` from its current handoff, add the empty-file test first, then run the full suite.

## Needs input, decision first

**Result:** ❓ Needs input: Choose the TDD level before implementation starts. The spec and acceptance criteria are recorded.

**Evidence:** No checks were run; the change is defined, not implemented.

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Select `none`, `targeted` or `strict`; `targeted` is recommended for the parser change | user | The recorded spec | TDD level not selected |

## Paused

**Result:** ⏸ Paused: The migration change is paused until the staging database is reachable.

**Evidence:** `make test-migration` failed twice with a connection timeout to the staging host. The unit suite passes. The migration is not verified.

| Next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Rerun `make test-migration` once the staging database is reachable | implement | Network access to the staging host, restored by the user | Authorized |
