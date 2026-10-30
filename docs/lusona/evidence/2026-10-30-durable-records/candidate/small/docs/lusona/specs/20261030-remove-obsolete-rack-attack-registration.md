# Spec 20261030-remove-obsolete-rack-attack-registration: Remove obsolete Rack::Attack middleware registration

Created: 2026-10-30
Updated: 2026-10-30

Kind: refactor

## Agreement

- User and problem: The requester identifies the Rack::Attack middleware registration as obsolete and requests a separate bounded work item.
- Structural outcome: Remove that registration while preserving the rest of the middleware configuration and successful application startup.
- Scope and exclusions: Define this change only. Do not implement it. Future implementation is limited to the registration removal and relevant verification; dependency removal and other middleware changes are excluded.
- Accepted constraints: Preserve all other middleware ordering, as explicitly required by the user.
- Completion condition: Definition is complete when scope, criteria, and the selected TDD policy are recorded. Implementation completion requires AC1–AC3 and supporting verification.

### Acceptance criteria

- [ ] AC1: The obsolete Rack::Attack middleware registration is removed.
- [ ] AC2: All other middleware retain their existing ordering.
- [ ] AC3: Application startup succeeds without the removed registration.

### Decisions and uncertainty

- Accepted decisions and source: Scope, criteria, definition-only authority, and targeted TDD were supplied directly in the request.
- Unresolved decisions: None blocking definition. Application source location and startup verification command remain uninspected and must be established if implementation is authorized.

### TDD policy

- Level: targeted
- Selected by user: Explicit request, “TDD choice is targeted for startup coverage.”
- Test-first behaviors: Application startup at the affected middleware boundary. Reuse adequate startup coverage; add missing characterization coverage before production edits, keeping behavior-preserving checks green. Do not manufacture a failing test.
- Required regression coverage: Successful startup without the registration and preservation of all other middleware ordering.

## Evidence

- Checks and outcomes: Inline definition check found no contradictory criteria, ambiguous scope, or missing consequential decisions.
- Remaining verification and limitations: No application source inspection, implementation, startup tests, or middleware-order verification was performed; these belong to future authorized implementation.
- Changes: This definition only; no production files changed.

## Current handoff

- Authorized work: Definition only, from the explicit request; implementation is not authorized.
- Completed and remaining work: Definition complete; AC1–AC3 remain unimplemented and unverified.
- Next action: None for this definition request. Upon explicit implementation authorization, the implementation owner should locate the registration and startup coverage, then apply the selected targeted TDD policy and verify AC1–AC3.
