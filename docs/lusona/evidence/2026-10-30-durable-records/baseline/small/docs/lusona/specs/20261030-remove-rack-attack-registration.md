# Spec 20261030-remove-rack-attack-registration: Remove obsolete Rack::Attack registration

Created: 2026-10-30
Updated: 2026-10-30

Kind: refactor
Work item: [Work queue](../work.md)

## Agreement

- User and problem: The maintainer requests removal of an obsolete Rack::Attack middleware registration.
- Structural outcome: The application middleware stack no longer registers Rack::Attack.
- Scope: Remove the registration only; preserve all other middleware and their relative ordering. Dependency removal and unrelated middleware changes are excluded.
- Constraints source: The user request.
- Completion condition: All acceptance criteria verified with targeted startup coverage. No separate human acceptance or delivery requirement was requested.

### Acceptance criteria

- [ ] AC1: The obsolete Rack::Attack middleware registration is removed.
- [ ] AC2: Every other middleware retains its relative ordering.
- [ ] AC3: Application startup succeeds without the Rack::Attack registration.

### Decisions and uncertainty

- Accepted scope and criteria were supplied directly by the user.
- No blocking definition questions. Registration location and startup test command must be established in the actual application before implementation.

### TDD policy

- Level: targeted.
- Selected by user: Explicit request for targeted startup coverage.
- Test-first behavior: Application startup. Reuse adequate coverage or add missing startup characterization coverage before changing production code; behavior-preserving coverage starts green and stays green. Do not manufacture a failing test.
- Required regression coverage: Verify application startup and preservation of all other middleware ordering.

## Evidence

- Definition checked for contradictions, scope ambiguity, and missing decisions; none block this definition.
- No application source or tests are available in this new consuming project. Startup and middleware ordering have not been tested. No implementation performed.

## Current handoff

- Authorized work: Definition only; user explicitly prohibits implementation for this request.
- Completed: Agreement, acceptance criteria, and targeted TDD recorded.
- Remaining: Implement and verify AC1–AC3 only after implementation authorization and access to application source.
- Next action: None for this definition request. A future implementer needs implementation authorization and the application source, then locates the registration and existing startup coverage.
