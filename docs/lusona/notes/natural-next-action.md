# Notes: natural next action

## 2026-11-05 — Proactive exploration and explicit stopping

The user reports that `explore` rarely offers or records results on its own and asks
for a natural next step in every command, or an explicit statement when none exists.
They also report better rule adherence in Claude than ChatGPT; no transcripts or
comparative measurements were supplied.

### Agreement and decisions

- Edit canonical shared instructions, with early explicit triggers in `explore` and
  concise shared decision rules. Preserve one source for Claude and OpenAI hosts.
- Save reusable discussion synthesis when useful, without waiting for a save request
  or the end of discussion. Respect no-save/read-only/destination constraints.
- Recommend a concrete question, direction, or action; continue already authorized
  work. A complete assessment may have a proposed follow-up requiring new authority.
- Say that no next step is warranted when understanding is sufficient; do not invent
  work, require a decision, or create a spec/queue merely for discussion.
- This refines the completed-request wording recorded in
  [next-action-table](next-action-table.md); the selected table format is unchanged.
- Documentation only. No executable implementation or user-selected TDD policy; no
  test-first claim. The user subsequently authorized cleanup and grouped local commits;
  push, publication, and installation remain outside this request.

### Changes and evidence

Updated core questions/retention/presentation rules, Explore, discussion template,
completion routing, and the corresponding paragraph in all five public READMEs.
A conflicting routing row previously allowed further proposals only when asked.

Static verification passed: instruction checker, 11 instruction tests, 10 packaging
tests, Explore skill validator, package build with resource links and manifest checks,
Claude plugin and marketplace validation, and whitespace check. Claude validation
included nonblocking installation-line advice; mise emitted cache-write warnings.

[Bounded behavioral evidence](../evidence/2026-11-05-natural-next-action/README.md)
owns the declared cases, snapshots, captures, independent grades, and limits.
Independent review found no actionable defects. Candidate cases: 3 pass. Baseline:
Explore and Status pass; Finished fails only the explicit reason-for-stopping criterion.
The original failure to save or offer a next step was not reproduced.
Installation and live interactive Claude/ChatGPT behavior are untested. No claim of
cross-host improvement follows from these checks.

## Current handoff

- Authorized work: instruction edits and proportionate verification, from the current
  user request, followed by cleanup and grouped local commits. Coordinator owns
  integration and records; specialist edit is complete.
- Remaining: none for the authorized source edits and bounded checks. All assigned
  workers completed; no active operations or ownership remain.
- Proposed next action: compare the same realistic exploration in live Claude and
  ChatGPT sessions using this revision, retaining outputs and saved records. This
  broader host comparison was not performed; installation/publication remain outside
  the current authority.

## 2026-11-05 — Version 2.0.1

User authorized a version bump to distinguish the updated instructions across sessions.
Updated all four canonical native manifests, the root Antigravity reference, the five
public README version labels, and the changelog. Historical version references and
frozen behavioral snapshots remain unchanged. This metadata update follows the
behavioral trial; its archived candidate manifests still identify version 2.0.0.
The user subsequently authorized a local release-metadata commit. No installation,
push, or publication was performed.

Verification: 2.0.1 package build, all 10 packaging tests, Claude plugin and
marketplace validation, and whitespace checks passed. All five manifest versions
were verified as 2.0.1.
Next action: update/reload installed copies before live host testing; the version
bump alone does not change already loaded sessions.
