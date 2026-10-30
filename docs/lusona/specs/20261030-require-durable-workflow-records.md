# Spec 20261030-require-durable-workflow-records: Require durable workflow records

Created: 2026-10-30
Updated: 2026-10-30

Kind: bug fix

## Agreement

The user reported that Specify left a small change only in conversation, citing optional
saving language. Workflow outputs must remain available for future action without a separate
save request. Update canonical instructions and their supporting templates and documentation.

- AC1: Specify saves every definition, including small changes, using the helper and naming
  rules; missing directories or a queue do not waive saving.
- AC2: Consequential architecture decisions require ADRs; substantive exploration and
  investigation notes and material decision evidence are saved before handoff or completion.
- AC3: Shared instructions, implementation/refactoring, review findings, and templates do not
  offer conversation-only exceptions for substantive outputs. Reuse existing owners and keep
  records concise. Explicit user no-save/read-only restrictions and write permissions prevail.

User subsequently reported success, bumped the plugin to 1.3.1, and authorized verification
and a local commit. No runtime code changes, installation, push, or publication are authorized.
No new architecture decision is needed for this instruction correction.

## Verification

- All 13 canonical skills passed skill-creator `quick_validate.py`.
- Package `tmp/durable-records-1.3.1-verification/lusona-1.3.1.zip` built successfully:
  resource links, template links, native manifest identities/versions, and catalogs passed.
- All three native manifests use 1.3.1. Claude plugin and marketplace validation passed.
- `git diff --check` passed before final evidence recording.
- Matched baseline/candidate small-spec and explicit no-save fixtures executed. Both variants
  saved the small spec and kept the no-save project empty. This is regression evidence, not
  evidence of comparative improvement or a test-first sequence.
- [Declared trials, exact reports, artifacts, and provenance](../evidence/2026-10-30-durable-records/README.md).
- No runtime code changed; no real-change TDD policy was inferred. Fixture TDD was explicitly
  supplied as a trial input. Installation and installed interactive integration remain untested.

## Current handoff

Authority: user requested mandatory records, authorized fresh-context reimplementation,
reported success, supplied version bump 1.3.1, and requested verification then commit.
Implementation: canonical skills, shared procedures/templates, and all five public README
translations updated. Required records reuse existing owners; explicit no-save/read-only
limits and delegated read-only reviewer ownership are preserved.
Current state: implementation, static validation, independent diff review and trial grading
complete. No substantive defects; all four cases pass with evidence limits recorded.
Parent owns records and commit. No active implementation worker.
TDD: `none`, explicitly selected by the user with “no tdd” after verification. This removes
the test-first requirement; completed regression and static checks remain required evidence.
Next action: create the authorized local Conventional Commit. No push or publication.
