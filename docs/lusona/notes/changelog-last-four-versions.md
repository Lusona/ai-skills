# Notes: changelog-last-four-versions

## 2026-11-04 — Changelog for the latest four source versions

- Authority: user invoked `lusona:implement` to add a changelog, then explicitly selected
  versions 2.0.0, 1.5.0, 1.4.0, and 1.3.2 and TDD `none` with Git-history, link, and packaging checks.
- Outcome: a concise root `CHANGELOG.md` with verified user-facing changes, linked from all
  five READMEs and included in the portable catalog. Preserve existing translation edits.
- Boundary: 2.0.0 is the current source version without a Git tag; distinguish it from tagged
  versions and avoid inferring publication dates. Exclude unrelated uncommitted translation fixes
  from historical release claims. The user subsequently authorized grouped local commits;
  pushing and publication remain unauthorized.
- Verification: trace entries to tag ranges and actual diffs; validate local links and anchors,
  run whitespace checks, build a fresh package, check the archived changelog, and run existing
  packaging tests. Independent review checks history accuracy and integration.
- Ownership: `/root/changelog_history` owns changelog content; the coordinator owns integration,
  verification, and this record. TDD `none` permits implementation before verification.

### Result and verification

- Created [CHANGELOG.md](../../../CHANGELOG.md) with four version entries and immutable Git
  comparison links. Tagged version dates use each commit's local date; the tags themselves
  were created retrospectively, so no publication dates are inferred.
- History boundaries: `ebca32b..61ec6da` (1.3.2), `61ec6da..95d0bae` (1.4.0),
  `95d0bae..545b6e0` (1.5.0), and `545b6e0..5e39db8` (current 2.0.0).
  The author checked logs, actual diffs, manifests, and retained evidence.
- Added one changelog link to each README, marking the English destination in the translations.
  Included the changelog in the package builder's explicit file list and matching test fixture.
- Independent reviewer `/root/east_asian_review` checked the four ranges, version dates,
  actual changelog, README additions, and packaging integration; no actionable findings or
  meaningful user-facing omissions were identified. The coordinator inspected the artifact.
- Passed: `git diff --check`; all 315 local links and anchors across the five READMEs and
  changelog; requested headings and cited Git objects; fresh package build with
  `python3 scripts/package.py --output tmp/changelog-last-four-versions-20261105`;
  all 10 tests from `python3 scripts/test_package.py`. Extracted and archived changelog bytes
  match the source, and project records are excluded from the package.
- Limits: external HTTP availability, installation, interactive behavior, and publication
  were not tested. No new release, tag, commit, push, or publication was created.

## Current handoff

- Authorized work is complete and verified. The user authorized grouping and committing the
  changes; the changelog, README links, packaging integration, and this record form one local
  commit after the translation commit. Existing translation changes and their notes were preserved.
- Next action: None for this request.
