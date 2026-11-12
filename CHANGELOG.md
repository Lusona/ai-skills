# Changelog

Changes in recent source versions. Dates for tagged versions use the tagged commit's
local date, not a verified publication date. Versions 3.0.0, 2.0.5, 2.0.4, 2.0.3, 2.0.2, 2.0.1, and 2.0.0 are untagged;
the entries distinguish source updates from published releases.

## 3.0.0 — Current source, untagged

Local source update prepared on 2026-11-11. Publication and installation are not implied.

- Rewrite all 14 skills in one section layout. Skill names and commands do not change.
- Put the rules that apply to every task, and the reply format, inside each `SKILL.md`.
  Both are generated from one source file each by `scripts/sync_shared.py`. No skill requires the
  plugin README any more; it is human documentation and a catalog.
- Every task reply states a status (Complete, In progress, Needs input or Paused), the
  evidence, and the next action with its owner, or states that none remains and why.
- The coordinator delegates specialist work at every task size, except work the skill assigns
  to the coordinator. `status` does its assessment as coordinator and delegates only an audit
  of product source code that the question depends on. `explore` reasons from the
  conversation, the project records and the files the user names, and delegates research that
  needs other sources. The other 12 skills assign no work to the coordinator.
- A task reply keeps the required labels and fields unless a user or host instruction
  explicitly requires an incompatible format. A preference for brevity does not remove them.
  Before, any user or host formatting instruction overrode the form.
- Add eight loop principles to the workflow guide. A new requirement that contradicts an
  accepted decision leads to a revisit with the user and a recorded outcome, described in
  the new `revisions` reference.
- Merge references: `model-routing` and `worker-lifecycle` into `delegation`, `handoff`
  into `retention`, `work-record` into `naming`, and `interview-examples` into `interviews`.
  `batch-execution`, `batch-use` and the batch `execution` reference are replaced by eight
  references in `skills/batch/references/`.
- Rename templates to `name.ext.template` (for example `templates/spec.md.template`). The
  record helpers read the new names; their commands, output and exit codes do not change.
- Rename template labels. In the batch template, the field "Repair allowance" is now
  "Repair budget", the table headers "Allowance and source" and "Remaining allowance" are now
  "Budget and source" and "Remaining budget", and the column "Relevant items" is now "Items".
  In the product template, the field "Useful horizon, if established" is now "Horizon, if
  established". In the spec template, the heading "TDD policy" is now "TDD level"; the
  `specify` description, the status template, `CONTRIBUTING.md`, `INSTALL.md` and the pull
  request template use the same term. Records created from earlier templates stay readable.
- Use one term for each concept: "repair budget", "queue state", and "execution record" for
  an existing file in `docs/lusona/plans/`. The terminology table in the workflow guide
  defines these, plus accepted decision, settled decision, skill prompt and continuation
  directive.
- Describe Icebox as a section of the queue, not a queue state. A parked row keeps its
  queue state.
- State conditions as tests. Words such as "relevant", "useful", "safe" and "small" are
  replaced by a condition the agent can check, or deleted. `scripts/check_voice.py` fails
  on a list of banned terms, and `scripts/sync_shared.py` fails when the every-task block
  exceeds 300 words.

## 2.0.5 — Untagged source snapshot

Local source update prepared on 2026-11-09. Publication and installation are not implied.

- State save restrictions, spec queue tracking, batch incremental reporting, and task
  conditions once each; other files point to the owning rule and keep their local consequence.
- Use the core Contract's condition, "when saving is prevented", wherever a procedure says
  what to do when a record cannot be saved.
- List sequencing and a long run whose earlier context will be summarized among the core
  conditions for adding tasks, matching the spec template.
- Make the batch deadline "before further dispatch or waiting" cover inspecting and
  persisting a result as well as updating its queue row.

## 2.0.4 — Untagged source snapshot

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
