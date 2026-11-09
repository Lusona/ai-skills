# Changelog

Changes in recent source versions. Dates for tagged versions use the tagged commit's
local date, not a verified publication date. Versions 2.0.4, 2.0.3, 2.0.2, 2.0.1, and 2.0.0 are untagged;
the entries distinguish source updates from published releases.

## 2.0.4 — Current source, untagged

Local source update prepared on 2026-11-09. Publication and installation are not implied.

- Consolidate record-helper invocation guidance in its existing reference, preserving
  mandatory helper use and record-specific rules for retention, naming, and closeout.

## 2.0.3 — Untagged source snapshot

Local source update prepared on 2026-11-08. Publication and installation are not implied.

- Make workflow roles explicit in assignments and newly prepared evaluation runs.
- Load worker lifecycle instructions when responsible for workers or their results,
  including inherited responsibilities, without requiring them for unrelated local work.

## 2.0.2 — Untagged source snapshot

Local source update prepared on 2026-11-08. Publication and installation are not implied.

- Check that removed or replaced behavior preserves required obligations, while
  respecting intentionally retired behavior.
- Establish telemetry coverage before inferring that an unrecorded event did not occur.
- Assess verification results against the operation's contract, including application
  errors that a process exit code alone may not expose.
- Preserve reusable execution steps after substantial setup discovery in existing
  project instructions or scripts, within write authority and safe replay limits.

## 2.0.1 — Untagged source snapshot

Version metadata changed on 2026-11-05. Publication and installation are not implied.

- Require every command to provide a concrete next step or explicitly state that
  none is warranted and why, including after a completed assessment.
- Make Explore proactively offer useful questions, alternatives, and recommendations,
  and save reusable synthesis during discussion within existing write permissions.
- Align completion routing and translated documentation with the shared rule.

## 2.0.0 — Untagged source snapshot

Version metadata changed on 2026-11-03. Includes subsequent changes through
2026-11-04 ([`5e39db8`](https://github.com/Lusona/ai-skills/commit/5e39db8a5d507aca4360c222cc4f5d2ba3ef234f)).

- Consolidate shared rules and load evidence and handoff procedures when needed,
  reducing repeated instructions across skills.
- Make record selection explicit: direct implementation and refactoring can use
  notes; requested or existing specs and changes requiring independent review
  for security boundaries, persistent data, shared contracts, or coordinated
  writers require a spec and queue row. Keep unresolved follow-ups discoverable
  in the queue, including those found during untracked work.
- Make Result, Evidence, and Next action the standing reply format. When work
  remains, show the next action, owner, required inputs, and authority in a
  one-row table; completed requests retain a plain next-action line.
- Clarify coordinator and worker ownership of queues, handoffs, closeout, and
  review findings, and align conflicting instructions.

[Changes since 1.5.0](https://github.com/Lusona/ai-skills/compare/545b6e05146844911dd91a9f8ecb1f276c0dc9aa...5e39db8a5d507aca4360c222cc4f5d2ba3ef234f)

## 1.5.0 — 2026-11-03

- Add the `design` skill for UI mockups, screen flows, and Mermaid diagrams,
  including a single settled design or alternatives for an unresolved choice.
- Document browser inspection, accepted visual references, binding requirements,
  and fallbacks when browser opening or screenshot capture is unavailable.
- Reorganize the README around the shared work loop and useful starting points,
  with updated Spanish, German, Simplified Chinese, and Japanese translations.

[Changes since 1.4.0](https://github.com/Lusona/ai-skills/compare/95d0bae37231b76046c699ec32ebcb1299792ba1...545b6e05146844911dd91a9f8ecb1f276c0dc9aa)

## 1.4.0 — 2026-10-31

- Add native Antigravity manifests, package validation, and installation guidance
  for the CLI, App, and standalone IDE.
- Document that Antigravity installation from the repository-root GitHub URL
  includes repository project records; canonical-directory and portable-package
  installations exclude those records.
- Use fenced Mermaid Markdown consistently for diagram presentation, retention,
  and review. Preserve consequential rejection reasons while discarding rejected
  draft assets.
- Remove plugin-relative links from templates where they break after records are
  saved in a consuming project.

[Changes since 1.3.2](https://github.com/Lusona/ai-skills/compare/61ec6da486fc4fc2701c2b0a156548606f9fbf34...95d0bae37231b76046c699ec32ebcb1299792ba1)

## 1.3.2 — 2026-10-31

- Require a queue row whenever a spec is created, updated, or used. Create a
  missing queue and reconcile the selected item without resetting its lifecycle
  state, Icebox placement, or archived history.
- Keep planning out of Doing and require accepted scope, acceptance criteria,
  explicit TDD, and no blocking definition questions before Ready. Queue
  membership does not authorize implementation.
- Allow direct work without a spec to retain notes without mandatory tracking;
  existing tracked work remains tracked.

[Changes since 1.3.1](https://github.com/Lusona/ai-skills/compare/ebca32b23dbf4a48c1ec9c4ce1f084e65c4b511a...61ec6da486fc4fc2701c2b0a156548606f9fbf34)
