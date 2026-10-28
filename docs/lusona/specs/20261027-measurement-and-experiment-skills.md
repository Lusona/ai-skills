# Spec 20261027-measurement-and-experiment-skills: Measurement and experiment skills

Created: 2026-10-27
Updated: 2026-10-27

Kind: feature
Work item: [Draft completion](../history/2026-10-week-04.md#2026-10-27--measurement-and-experiment-skills)

Backfilled at the user's request after the draft was implemented and statically reviewed.
This records the settled conversation agreement and actual results; it does not claim a
pre-implementation signed specification or acceptance of installed behavior.

## Agreement

- User and problem: Lusona users need explicit measurement and intervention-evaluation
  responsibilities, with retained evidence that supports decisions without losing methods
  or prior observations.
- Desired behavior: `measure` establishes decision-relevant magnitude, quality, cost, or
  change. `experiment` evaluates an intervention or alternatives against a declared design.
  Both can arise naturally during authorized work; diagnostic questions remain with `investigate`.
- Scope: add the two canonical skills, a shared evidence procedure and template, and the
  routing, retention, catalog, and version updates needed for a locally reviewable draft.
- Constraints: preserve bounded tasks, explicit TDD, native question guidance, authority,
  concrete next actions, and existing record ownership. Material evidence belongs in the
  consuming project's `docs/lusona/evidence/`; no existing-note migration is required.
  Routine task verification logs stay with their task owner. Canonical sources remain under
  `plugins/lusona/`; generated packages exclude project records and scratch files.
- Completion condition: draft source, independent static review, and validated local package
  for user installation/review. Installation, live host behavior, commit, and publication are
  outside this completed draft scope.

### Acceptance criteria

- [x] AC1: `measure` documents decision, metric, meaningful difference, provenance,
  instrument validity, comparable references, variation, uncertainty, and candidate versus
  verified gains, ending with a bounded next action.
- [x] AC2: `experiment` requires hypothesis, comparison, evaluation criteria, resource budget,
  and stopping conditions before observation; preserves unfavorable/null results and labels
  exploratory changes; concludes adopt, reject, refine, or inconclusive without granting
  production implementation authority.
- [x] AC3: Shared evidence guidance and template preserve methods, provenance, observations,
  visible corrections, and exact supporting runs; distinguish latest comparable results from
  latest runs; link owning records without duplication or forced migration.
- [x] AC4: Core, explore, investigate, retention, and user-facing routing make the new
  responsibilities discoverable within existing authority, preserving diagnostic ownership
  and avoiding mandatory workflow phases.
- [x] AC5: Native manifest identities and version 1.2.0 align; relevant skill, manifest,
  catalog, link, template, packaging, and whitespace checks pass; independent review reports
  no actionable issues. Installation and interactive behavior remain explicitly untested.

### Decisions and uncertainty

- Accepted decisions and source: the user authorized a draft for local installation/review,
  chose the responsibilities and shared evidence home above, and explicitly selected TDD
  `none` in the conversation. The later request authorizes this retrospective spec and history.
- No unresolved definition decision blocks the draft. Whether installed behavior meets the
  user's needs remains for local review; static checks do not establish that behavior.

### TDD policy

- Level: none.
- Selected by user: explicit conversation choice for this draft.
- Test-first behaviors: none required.
- Required verification: applicable static skill and native plugin validation, packaging and
  archive inspection, whitespace checks, and independent review; no behavioral red/green
  sequence is claimed.

## Evidence

- Source inspection: the four new canonical files are
  [measure](../../../plugins/lusona/skills/measure/SKILL.md),
  [experiment](../../../plugins/lusona/skills/experiment/SKILL.md),
  [evidence procedure](../../../plugins/lusona/references/evidence.md), and
  [evidence template](../../../plugins/lusona/templates/evidence.md).
  Related tracked changes update routing, retention, skill catalogs, translated README
  entries, and the three native manifests to 1.2.0. Changes remain uncommitted.
- Prior draft verification, supplied by the coordinator: skill-creator `quick_validate`
  passed for measure, experiment, explore, and investigate using mise Python with
  `PYTHONPATH=$PWD/tmp/vercel-skills-investigation/validation-venv/lib/python3.13/site-packages`.
  The default Python environment lacked YAML support; the supplied environment resolved it.
- Claude plugin and marketplace validation passed, with a nonfailure install-line advisory.
  `python scripts/package.py --output tmp/measure-experiment-draft-1.2.0` passed manifest,
  catalog, link, and template checks. Archive inspection confirmed the four new files match
  canonical sources and excludes `docs/lusona/` and `tmp/`. `git diff --check` passed.
- Independent reviewer `/root/review_draft` found no actionable issues in the draft.
- Artifact: [lusona-1.2.0.zip](../../../tmp/measure-experiment-draft-1.2.0/lusona-1.2.0.zip).
- Backfill verification: spec/history local links and reciprocal anchors resolve; template
  placeholders were removed and whitespace checks pass. Project records remain outside the package.
- Limits: the checks above verify draft structure and package contents. Installation and
  live interactive behavior have not been tested; user acceptance is not claimed. This
  backfill reuses the recorded checks rather than inventing behavioral test evidence.

## Current handoff

- Authorized work: the conversation authorized the local draft and its review/package;
  the follow-up requested backfilling this agreement and history. No commit or publish authority.
- Completed and remaining work: AC1–AC5 are satisfied for the draft scope. The spec and
  linked history entry are backfilled and reconciled; no active queue item was needed.
- Try it: use the local package above with the repository's
  [native installation instructions](../../../INSTALL.md), then review the new measure and
  experiment responsibilities in the chosen host. Expected outcomes are the documented
  contracts above; installed behavior remains to be observed.
- Human acceptance and delivery: local artifact prepared for review; no installed-behavior
  acceptance recorded or required to close the draft scope.
- Next action: user may install and review the local draft using the package and installation
  instructions. Any findings can define a bounded correction; no further implementation is
  authorized merely by this suggested review.
