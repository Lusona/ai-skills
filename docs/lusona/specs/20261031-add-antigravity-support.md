# Spec 20261031-add-antigravity-support: Add Antigravity support

Created: 2026-10-31
Updated: 2026-10-31

Kind: feature
Work item: [Work queue](../work.md)

## Agreement

User requested Google Antigravity support through `lusona:specify`, then authorized
implementation through `lusona:implement` and selected “All surfaces; targeted TDD”.

Outcome: users of the selected Antigravity surfaces can install and invoke all canonical
Lusona skills with their shared resources available. Proposed delivery is native plugin
compatibility metadata, portable-package support and validation, installation/use/update/removal
instructions, and corresponding README guidance in all maintained languages.

Selected surfaces: Antigravity App, CLI, and standalone IDE (explicit user selection).
Supported platform claims must identify the documented environment and actually tested versions.
Keep `plugins/lusona/` canonical; do not maintain duplicate skill definitions or add a separate
individual-skill copier. Native full-directory plugin support is the recommended approach,
based on the official documented format. Implementation must validate its actual behavior.

### Acceptance criteria

- AC1: Antigravity recognizes the native plugin as `lusona`, displays Lusona Skills, and uses
  the same version as the existing native manifests. No version bump is implied by specification.
- AC2: The documented GitHub, local-checkout, and portable-package paths expose all canonical skills
  on selected surfaces and preserve access to shared README, references, templates, scripts,
  and assets. Relative resource paths resolve from loaded skills, not the consuming project.
- AC3: INSTALL.md covers requirements, installation, skill discovery/invocation, updates and
  removal for each selected surface, with official source links and verification dates.
  Public README guidance and translations identify Antigravity and link the installation steps.
  A top-level repository URL must not be claimed to install the nested plugin unless verified.
- AC4: Installation does not create consuming-project records. Updates and removal preserve
  project records and unrelated host configuration/plugins.
- AC5: Packaging includes Antigravity metadata and required resources, excludes project data,
  and retains existing host packages and manifest identity/version checks.
- AC6: Static/package validation is distinguished from live Antigravity verification. Record
  the host/version and results for each claimed tested surface; report unavailable/unrun checks
  explicitly and do not equate package success with installed or interactive compatibility.

Out of scope: marketplace submission/publication, live host configuration changes during
specification, custom agents/hooks/MCP integrations, redesigning workflow behavior, historical
record migration, broad unrelated documentation cleanup, commit, push, or release.

### TDD and definition decisions

TDD: `targeted`, explicitly selected by the user. Test first for Antigravity metadata
inclusion in the portable package, shared-resource preservation, manifest identity/version
alignment, and project-data exclusion. No new installer is planned; use native host operations.
Scope and criteria accepted through the implementation request and explicit surface selection.
No further implementation approval required. Commit, push, and publication remain outside scope. The user subsequently authorized version
1.4.0 and verification/documentation of direct GitHub installation.

## Evidence and constraints

Inspected INSTALL.md, scripts/package.py, current manifests, and canonical skill layout.
There are 13 canonical skills. Existing manifests are version 1.3.2; derive expected membership
from source rather than outdated prose counts. Skills depend on resources above their individual
folders, so isolated skill copies do not establish Lusona compatibility.

Official documentation inspected 2026-10-31:

- [Agent skills](https://antigravity.google/docs/skills): App/CLI/IDE discovery and invocation
  are documented separately. Do not assume installation in one surface configures another.
- [Plugins](https://antigravity.google/docs/plugins/): documents native plugin management and
  standalone IDE local/global plugin locations.
- [Build plugins](https://antigravity.google/docs/build-plugins/): documents a multi-provider
  `.antigravity-plugin/plugin.json` location with components at plugin root, and
  `agy plugin validate --strict` for native validation.

At specification time, these sources supported the proposed full-directory approach; runtime
behavior was untested and only an `agy` shim had been identified. Implementation verification
subsequently established CLI 1.4.12 and the native lifecycle results recorded below.

## Verification and completion

After implementation authority and TDD selection: run relevant package behavior tests,
manifest/schema and identity/version validation, all resource link checks, existing-host
regression checks, and native Antigravity strict validation when available. For any surface
claimed runtime-tested, retain actual installation/discovery/invocation evidence in an isolated
project: status can load the shared core; specify can access templates/helpers and create its
spec/queue in the consuming project. Check updates/removal preserve project records. Any
unavailable required host verification remains an explicit completion gap, not a passing result.
Retain open verification limitations without claiming successful integration for untested surfaces.

## Current handoff

Implementation authorized for App, CLI and IDE with targeted TDD. Native metadata, root
reference, package integration, installation documentation, and all README translations are
implemented. User subsequently authorized version 1.4.0, aligned across all native manifests
and public source-version labels. Eight package tests pass, including targeted red/green
for metadata, resource integrity, root references and project-data exclusion.

Native CLI 1.4.12 strict validation passed for the source and portable plugin (13 skills).
Isolated lifecycle verification covered install/list, bundled helper execution, fixture update,
uninstall, and preservation of project records and unrelated configuration. Public GitHub root and tree URL installations passed on CLI 1.4.12: enabled 1.3.2 via
Claude compatibility, all 13 skills and 54 canonical files preserved, no project records.
Instructions now prefer the explicit plugins/lusona tree URL. Native 1.4.0 remains unpublished;
that version has not been tested through public GitHub. Evidence summary is consolidated with
all original results retained in its archive. See [evidence](../evidence/2026-10-31-antigravity-support/README.md).

Independent review found a packaged-test-runner omission, corrected with red/green coverage;
focused review accepted the repair and extended lifecycle evidence. Subsequent cohesion review
found generated-record links pointing into nonexistent project-local plugin procedures; those
links were corrected and helper regression checks pass. The later discussion/visual retention
clarifications are tracked in [the rule matrix](../notes/skills-rules-review-matrix.md).

Remaining AC2 checks: App/IDE installation and discovery, and model-driven status/specify
invocation/loading shared core in a disposable project. These have not been run; static/native
lifecycle checks do not establish them. Work remains Review rather than Done.

Next action: perform the remaining live-host checks when an appropriate test environment is
available. GitHub documentation/evidence cleanup is complete; package/link and eight regression
checks pass. No commit, push,
publication, or real-user-configuration installation is authorized by this follow-up. Parent
owns records; verification/documentation workers returned results without active operations.
The host exposes no worker shutdown control; completion does not claim termination.

## English README synchronization — 2026-10-31

User edited README.md to put installation hosts in alphabetical order and use
`agy plugin install https://github.com/lusona/ai-skills.git`, then requested translation
synchronization. Updated German, Spanish, Japanese and Simplified Chinese README files;
English remained byte-for-byte unchanged during this task. Antigravity explanatory text is
placed under Antigravity in the translations (it remains below Xcode in the user-edited English).
Also restored omitted Cursor details, measurement/experiment guidance, material-evidence
retention, and privacy/terms links to match the English content.

Verification: shell command blocks, host and skill-table order, local links and anchors match;
workers checked inline-code and Mermaid-structure parity. Package build/link checks and
`git diff --check` passed. Editors: /root/translate_de_es and /root/translate_ja_zh; parent
checked source preservation and structural parity. No installation/interactive testing was
performed for this documentation task. User intends to test after publication and considers
amend/force-push only if subsequent issues require it; no Git mutation was performed here.
The separate root-native-manifest installation behavior remains unverified.

## Closeout — 2026-11-03

The user marked this item Done ("mark in review items as done") with the remaining AC2 checks
unrun: App and IDE installation and discovery, and model-driven `status`/`specify` invocation
in a disposable project. These surfaces remain unverified and are recorded as explicit limits.
The queue row is removed; archived state:
[history](../history/2026-11-week-01.md#2026-11-03--add-antigravity-support).
