# Spec-triggered queue verification

## Declared design

Baseline: Git revision 3be42ff9066df6de79ad46102c758632291ad33f, frozen under
`tmp/spec-queue-verification/baseline/plugin`. Candidate: canonical working tree after edits
settle, frozen before either actor begins. Retain per-file SHA-256 manifests and exact diff.
Two fresh-context actors receive identical task sequences and permissions except variant paths.
They use local shell tools in this Codex host, cannot delegate, access external services,
commit, or read evaluator materials. Exact assignment strings were retained before dispatch.
Model/reasoning inherit the parent; precise runtime model version and usage are unavailable.

TDD: none, continuing user's explicit “no tdd” choice for these workflow instruction changes.
Post-edit trials are regression evidence, not a claimed test-first sequence.

Finite budget: one actor per variant, four independent fixture projects per actor, one
independent diff review and grading pass. Preserve failures; any retry needs a recorded reason.
Each actor executes the draft/edit sequence in one context and reports intermediate artifacts.

## Frozen evaluator cases

| Case | Expected candidate outcome |
| --- | --- |
| Draft then accepted spec | First save creates spec and queue in Ideas with unresolved label. Subsequent explicit label/scope/TDD acceptance updates same spec/row to Ready without duplication or implementation. |
| Existing spec, planning only, missing queue | Create missing row linked to supplied spec; preserve no-execution authority and do not enter Doing. Save useful plan. |
| Direct spec-free implementation | Make requested README correction; save notes containing agreement, explicit TDD/source, evidence and handoff; do not create spec/queue under supplied no-spec/no-queue instruction. |
| Explicit no-save specification | No project files created; provide definition and restriction through response. |

All cases must preserve bounded authority, no production changes outside the named README,
no commits or external services, and no shared writes outside assigned fixture paths. Only
actors' harness reports/snapshots are exempt from fixture no-save restrictions.

Coverage rationale: representative creation/reuse, readiness, planning, optional spec-free
execution, and explicit write-authority boundaries. Source review additionally covers delegated
parent ownership, automatic spec creation from other skills, Icebox/completed/history semantics,
and existing tracked work. No global historical backfill, live installation, or exhaustive host
coverage claimed. Action reports and artifacts are retained; full tool traces are unavailable.

## Results

Independent [review and grading](review.md) found no AC1–AC4 defects. Baseline fails the
spec/queue and missing-queue planning cases; candidate passes all four cases. Both variants
pass direct spec-free work and explicit no-save. Final-source planning follow-up also passes.
These bounded observations establish the tested behavior, not reliability across models/hosts.
Exact assignments, reports, inventories, intermediate and final artifacts are retained in
[artifacts.zip](#removed-archives), under `baseline/` and `candidate/`; hashes identify initial
snapshots and final canonical source. Extract the archive to inspect those paths. On 2026-10-31,
all original artifact bytes were verified against the archive before removing the loose copies.

Static verification passed: all 13 skill validators; package resource/template links, manifests,
catalogs and contents; native Claude plugin and marketplace validation; Bash work-record helper
behavior checks; and git whitespace checks. Final package is
`tmp/spec-queue-final-package/lusona-1.3.1.zip` (scratch, not a release).
Native Claude validation used the existing executable resolved by `mise where claude`; the
worker's mise launcher attempt could not refresh read-only shims. No tools were installed.
PowerShell/native Windows, installation, and installed-host integration were not tested.

## Source timing clarification

After candidate trial snapshot capture, the worker clarified queue.md: repair missing rows
before planning handoff or execution (previously before execution), and require explicit
authority plus closeout for reopening. Trial inputs remain frozen and are not overwritten.
Final-source hashes and the small post-snapshot diff are retained as separate archive entries. A focused
final-source planning case ran after the first actor completed; first-run artifacts are preserved.
This adds one candidate-only follow-up, justified by the changed planning-handoff wording.

## Release verification

The requested patch bump is 1.3.2 across Codex, Claude, and Cursor manifests. Behavioral
trial hashes intentionally retain the tested 1.3.1 metadata; only manifest versions changed
after those trials. Version/package checks passed for 1.3.2: package/resource/template links and catalogs, all
13 skill validators, native Claude plugin and marketplace validation, Bash helper checks, and
reviewed-source hash comparison (only the three manifest versions differ). No skill
instruction content changed after independent review. Installation and publication are outside scope.

## Removed archives

The archives below were removed from the working tree on 2026-11-12 to reduce the checkout
size. Commit `9f2260f` holds each one unchanged. Restore an archive from the repository root
with `git show 9f2260f:docs/lusona/evidence/2026-10-30-spec-queue/<path> > <file>`, then compare its SHA-256 with this table.
Hashes recorded in the manifests of this topic apply to the restored files.

| Path in this topic | Bytes | SHA-256 |
| --- | --- | --- |
| `artifacts.zip` | 42565 | `b1735df32f271e1bdcd70ea56a61d1aa8c5045691f3a3c036125fe458b66d5b9` |
