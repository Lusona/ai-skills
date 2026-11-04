# Spec 20261030-track-specs-in-work-queue: Track specs in the work queue

Created: 2026-10-30
Updated: 2026-10-31

Kind: bug fix
Work item: [Work queue](../work.md)

## Agreement

User accepted the rule that specs trigger queue tracking; implementation without a spec can
remain untracked while retaining notes and evidence. Existing rules leave tracking discretionary.
No separate specification interview is needed for this accepted bounded instruction change.

- AC1: Every new spec requires a row in `docs/lusona/work.md`; create the queue if absent.
  Spec updates reconcile the same row without duplication. Drafts start Ideas; Ready requires
  accepted scope/criteria and explicit TDD with no blocking questions. Existing lifecycle and
  Icebox/history states must not be reset or reopened by an ordinary edit.
- AC2: Implementation/refactoring using or creating a spec must maintain its queue row,
  repairing a missing row before execution and updating lifecycle state. Planning-only work
  never enters Doing; queue membership does not authorize implementation.
- AC3: Direct implementation without a spec may remain untracked and use notes for agreement,
  decisions, TDD/source, checks/evidence, and handoff. Existing tracked work remains tracked.
  Creating a spec activates AC1 regardless of the skill used.
- AC4: Explicit no-save/read-only restrictions and parent-only shared queue writes remain
  binding. No global scan/backfill or resurrection of completed work is required.

TDD: `none`, carrying forward the user's explicit “no tdd” selection for these workflow
instruction corrections. Verification remains required; no test-first claim.
Authority: user said “let's make it so”; bounded instruction edit and verification authorized.
On 2026-10-31 the user authorized a patch version bump, evidence cleanup, and local commit.
No runtime/helper changes, push, installation, or publication requested.

## Verification plan

Check changed skills, links, manifests/catalogs and packaging. Use matched baseline/candidate
fresh-context trials for spec creation and update, draft readiness, spec-linked planning with a
missing queue, spec-free implementation using notes, and explicit no-save. Review delegated
worker ownership and archived/Icebox state preservation independently in source.
Retain declared inputs, source hashes, actual artifacts/reports, grades and limitations.

## Current handoff

Parent owns queue, this spec, notes reconciliation, and evidence. Worker owns canonical skill
instructions/templates/references and corresponding public documentation. Implementation, checks and independent review complete; AC1–AC4 satisfied. All 13 skill validators,
package/link/manifest/catalog checks, native Claude plugin/marketplace validation, Bash helper
behavior checks, and whitespace checks pass. Candidate cases satisfy queue creation/reuse,
readiness and write-authority boundaries; baseline omits queue tracking. Final-source planning
rerun also passes. See [retained trial evidence](../evidence/2026-10-30-spec-queue/README.md).
Independent review found no concrete defects; all candidate cases passed, including the
final-source planning follow-up. Grades and limitations are retained with the evidence.
Version 1.3.2 package/native validators, all 13 skills, Bash helper checks and archived-evidence
byte verification passed. Reviewed-source hashes match except the three manifest version fields.
Next action: create the authorized local commit.
Installation, PowerShell/native Windows execution, and installed-host interactions not tested.
Version set to 1.3.2. Raw evidence consolidated into a byte-verified archive with readable
results and independent review retained. No push or publication authorized.

## Closeout — 2026-11-03

Completed 2026-10-31 in commit `61ec6da`. The Done queue row is removed; archived state:
[history](../history/2026-10-week-05.md#2026-10-31--track-specs-in-work-queue).
