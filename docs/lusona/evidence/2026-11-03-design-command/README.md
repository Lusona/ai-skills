# Design command verification — 2026-11-03

Owner: [change agreement](../../specs/20261103-add-design-command.md).

## Scope and method

Verify a dedicated design command and accurate public documentation against AC1–AC8.
Targeted TDD was explicitly selected for command discovery and packaging. Representative
candidate-only scenarios cover the new entrypoint; shared authority, TDD, visual retention,
and implement/review contracts are unchanged. No comparative improvement is claimed.

Before implementation, the parent captured the baseline revision and canonical sources.
The test worker froze the two new tests before the initial red run. Before actor dispatch,
the parent froze the isolated candidate plugin, fixture hashes, three cases, outcome criteria,
capabilities, and finite budget. Exact declarations, requests, responses, observations,
source hashes, test logs, and review are retained in [artifacts.zip](artifacts.zip), with
[SHA256](artifacts.sha256). The archive includes the exact frozen test file, source diff,
runtime snapshot overrides, chosen/draft artifacts and unchanged fixtures. Baseline commit:
`7e889a9ea0758261ed2d0bd3bedac89ef1e0622e`. Reconstruct sources from that commit plus
source.patch and the new skill in runtime-overrides; the overrides preserve actor input
bytes before two later line reflows. Rejected UI assets are discarded.

Actor runtime: Codex collaboration tool, gpt-6.1-sol, medium reasoning. Active host version
is not exposed. Browser opening, screenshot capture, network, children, and production edits
were unavailable/prohibited in the isolated actor projects. C1 had three turns; C2/C3 one
each. One independent gpt-6.1-sol/medium reviewer inspects the actual source diff and grades
semantic outcomes and artifacts against the frozen criteria, without implementing changes.
Actors received raw tasks, resources, and write limits, without grading criteria.

Validation tools: installed Python 3.14.9; Claude Code 2.1.317 and Antigravity CLI 1.4.12 managed
by mise. `mise exec` shim creation was read-only, so checks used existing executables;
`mise which` resolved the native CLIs. No runtime installation or configuration change.

## Test sequence and checks

These observations describe the original design-command verification at version 1.4.0.
The subsequent 1.5.0 metadata checks are recorded in the owning spec's Version follow-up.

| Check | Observation | Interpretation |
| --- | --- | --- |
| Canonical discovery before implementation | Four missing-design failures across native directory paths | Valid test-first red |
| Package check before implementation | Builder stopped on workflow-guide link to absent design | Setup-blocked for the intended package-membership assertion; not valid package test-first red |
| Supplemental isolated baseline | Missing-design assertions reached after supplying omitted baseline catalog/support fixtures | Diagnostic support only; ran after implementation and cannot repair the missed sequence |
| Candidate focused checks | 2 tests pass | Discovery and package/resource/ZIP behavior pass |
| Full package suite | 10 tests pass | Existing identity/version/resource/exclusion checks preserved |
| Skill validator | Pass | Frontmatter/naming validation only |
| Claude source/catalog validation | Pass | Source includes an existing README install-line advisory |
| Antigravity strict source/final-package validation | Pass, 14 skills | Native static validation; no live discovery/invocation claim |
| Package construction | Pass | Final package in repository-local scratch, excludes project data |
| Documentation links/version checks | 389 local links pass; five README design entries; native versions aligned at 1.4.0 | Content/link checks, without installation or rendering evidence |
| Existing visual contracts | Producer/consumer skills and both templates byte-match baseline; shared visuals body unchanged | Existing behavior preserved by source comparison |

The parent added the workflow-guide link before the package test ran. The selected package
TDD sequence was therefore missed. Independent review identified this gap. On 2026-11-03,
the user explicitly accepted a one-time exception and closure of the verified change.
Canonical discovery red/green remains valid; the exception does not create package red evidence.
All original setup failures and supplemental runs are retained with their actual timing.

## Behavioral observations

| Case | Result | Evidence and limits |
| --- | --- | --- |
| C1: direct UI comparison, rejection/revision, choice/retention | Pass | Two initial options revised to an in-place failure-placement comparison; B retained with V1–V6 binding items, illustrative items, notes owner, rejection reasons and missing-capture report; rejected assets removed and source unchanged |
| C2: settled single mockup | Pass | One template-based draft, prescribed structure/copy/failure state, fidelity note, absolute path, pending acceptance; original source unchanged; no chosen reference |
| C3: one no-save lifecycle diagram | Pass | Fenced Mermaid includes accepted/expired/rejected paths; project directory empty; no alternatives or ADR |

C2's initial generator assertion was corrected in one bounded recovery round. The
supplemental baseline's omitted fixture setup was corrected in one separate round.
Neither is test-first red evidence. C1 user-directed revision is a declared trial turn.
Independent review found zero source defects and graded C1/C2/C3 pass after inspecting
actual markup, inventory, hashes, owner links, transcript and observations. The parent
corrected one overly strict artifact check that required deleting an empty scratch directory;
the relevant requirement is removing rejected files. No implementation change was required.
All review/correction details are retained in the archive. Artifact archive bytes and CRCs
were verified after retention.

## Limits and next action

Browser rendering, state-switch interaction, screenshot capture, native installation, and
live-host invocation have not been tested. The trials validate path/capture fallbacks and
inspect artifacts statically; they establish no cross-host or visual-fidelity claim.

The user accepted the package TDD exception and closeout on 2026-11-03. The retained review
describes the state before that decision; its original findings and limits remain unchanged.
No next action for the authorized change.
