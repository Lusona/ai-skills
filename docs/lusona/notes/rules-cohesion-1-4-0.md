# Rules cohesion review — 1.4.0

Date: 2026-10-31. User requested version bump and cohesion/consistency findings, then authorized
the reported repairs with “fix them”.
Independent reviewer: /root/rules_cohesion (read-only); parent reproduced the finding.
Scope: canonical shared README, references, skills, templates and relevant record helpers.

## Findings

P2: templates/spec.md:14 and templates/notes.md:11 contain plugin-relative procedure links.
The record helpers copy these into consuming-project specs/notes; ../references then resolves
to docs/lusona/references, which installation does not create. Reproduced with init-change and
init-notes in tmp/rules-cohesion-project: both targets are absent. templates/evidence.md:5 has
the same static pattern; no evidence-template generation trial was run.
Recommended correction: keep plugin-only instructions out of saved records, or resolve the
links to a stable accessible source. Do not copy plugin procedures into every consuming project.

No confirmed contradictions found in authority, TDD, delegation, or queue lifecycle. Architect's
handoff-update wording is less explicit than parent-only shared rules, but assigned-leaf rules
resolve it; this is a wording improvement, not a second defect.

## Review verification

All five native manifests and five README source-version labels now say 1.4.0. Eight package
tests, portable build/link checks, whitespace check, and packaged-root Antigravity strict
validation passed (13 skills, no findings). No new live-host UI verification was performed;
existing Antigravity App/IDE/model-invocation gaps remain. At review time no rules had been repaired.

## Authorized correction and evidence

Scope: remove broken plugin-procedure links from saved record templates. The same pattern
was also found in templates/work.md. All four links are removed; the record instructions
remain, and canonical plugin instructions retain the procedure links. No plugin procedures
are copied into consuming projects. TDD: targeted, retaining the user's selected policy for
this work; test saved-record link integrity before changing templates.

Regression: scripts/test-work-record.sh now checks relative Markdown links from actual
helper-generated specs and notes, plus work/evidence templates copied to their consuming-project
locations. Before the fix, `bash scripts/test-work-record.sh` failed with
`AssertionError: Broken saved-record links`, listing spec → ../references/queue.md,
notes → ../references/evidence.md, evidence → ../references/evidence.md, and
work → ../references/queue.md. After the fix it printed `Work-record behavioral checks passed.`
This exercises relocated helper output as well as nested evidence output without a plugin
installation inside the consuming project.

Additional checks passed:
- `python3 -m unittest discover -s scripts -p test_package.py`: 8 tests.
- `python3 scripts/package.py --output tmp/template-link-verification/package`: built 1.4.0
  portable catalog and ZIP with link validation.
- `git diff --check`: no whitespace errors.

PowerShell is unavailable, so its helper was not executed; both helpers use the same corrected
templates. Existing saved records are not automatically migrated. Antigravity interactive
verification gaps remain unchanged. Changes are uncommitted; no publish was performed.

Next action: none for this template defect; resume the remaining Antigravity verification
from its existing owning spec and queue entry.
