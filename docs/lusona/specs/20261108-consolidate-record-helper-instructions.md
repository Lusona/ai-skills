# Spec 20261108-consolidate-record-helper-instructions: Consolidate record-helper instructions

Created: 2026-11-08
Updated: 2026-11-09

Kind: refactor
Work item: [Historical completion](../history/2026-11-week-02.md#2026-11-08--consolidate-record-helper-instructions)

## Agreement

User invoked `lusona:refactor` for rules following repeated explicitness and consistency passes.
The bounded structural target is duplicated helper invocation guidance in retention, naming,
and closeout. All three already require following `references/work-record.md`; that reference
owns shell selection, path resolution, commands, and argument contracts. Consolidate only this
boilerplate, preserving domain decisions and mandatory helper use. No contradictions are confirmed
in this target. No broader policy rewrite, scripts/templates, public documentation, versions,
installation, commits, or publication were included in the original increment. The subsequent
version-and-commit request below extends delivery authority. Preserve unrelated untracked notes.

Shared procedure contracts require independent review. This record supplies the agreement before
implementation. Scope selection is a routine bounded increment within the requested refactor.

### Acceptance criteria

- [x] AC1: Helper invocation mechanics have one maintained owner in `references/work-record.md`;
  retention, naming, and closeout retain explicit mandatory helper-use and required-read pointers.
- [x] AC2: Every removed obligation remains available through the existing loading path: shell/WSL,
  plugin-relative resolution, absolute project paths, commands, dates, preservation, and error handling.
- [x] AC3: Domain rules for record identity, retention/authority, completion evidence, history links,
  and queue removal remain unchanged. No helper runtime or saved format changes.
- [x] AC4: Baseline and candidate characterization, instruction/package checks, native validation,
  whitespace checks, and independent diff review pass. Installation and interactive use are untested.

### TDD policy

- Level: targeted, explicitly selected by the user in this session.
- Named coverage: instruction availability and preservation across helper callers and their required
  reference. Add a source-traced characterization matrix before edits and repeat it on the candidate.
- This is editorial behavior-preserving restructuring: characterization starts green; no manufactured
  failing test. CONTRIBUTING.md permits content/link checks for this class of change.
- Regression: existing instruction and package tests plus package link validation. No new wording-match
  tests or runtime-helper tests are required because scripts, templates, and command contracts do not change.

## Evidence

Baseline: revision `a7097284f9a5d35c3e4d31849bc1b9a644c932bf`; canonical plugin 2.0.3.
The invoked workflow source is installed Lusona 2.0.2. Canonical sources are the edit target.
Initial unrelated untracked file: `docs/lusona/notes/instruction-removal-component-previews-verification-caching.md`.

- `python3 scripts/check_instructions.py`: passed.
- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 passed.
- Structural assessment: delegated leaf `rule_structure`, maintenance engineer, read-only.
  Retention, naming, and closeout already explicitly require the helper reference; no new loading
  prerequisite is needed. The following characterization was added and inspected before edits.

| Boundary | Baseline source coverage | Baseline result / candidate preservation condition |
| --- | --- | --- |
| Role/loading | Core README loading; retention:84, naming:17, closeout:22 | Pass: all callers require work-record; keep those links and coordinator-only closeout |
| Mandatory use | retention:80–81, naming:12–16, closeout:18–19 | Pass: keep each operation's mandatory helper use |
| Shell/WSL/policy | work-record:3–8, 17–28 | Pass: available shell selects helper, WSL uses Bash, execution policy remains binding |
| Paths | work-record:6–15, 36–37; retention:96–99; closeout:37 | Pass: loaded-plugin resolution, absolute explicit project roots, shell filesystem paths |
| Commands/dates | work-record:34–49; naming:31–32; closeout:34–38 | Pass: argument contracts, local-today defaults, actual historical completion date |
| Preservation/errors | work-record:52–59; naming:34–46; retention:96–99 | Pass: no overwrite and existing created/conflict/error actions |
| Notes meaning/authority | retention:6–32, 96–99 | Pass: saving restrictions and initialization distinct from evidence/completion |
| Closeout sequence | closeout:3–16, 38–42 | Pass: coordinator records evidence, verifies preservation/links before removing row |

Line numbers refer to the baseline. Candidate review must trace the actual removed text to
retained owners rather than merely match phrases. No live agent-behavior improvement is claimed.

### Candidate verification

- Diff limited to retention, naming, and closeout: removed duplicated path-resolution text and
  shell examples, retained mandatory helper use and explicit required-read links. Naming retains
  `init-change` and `init-adr` inline so the following command rules remain unambiguous.
- Writer's eight-boundary characterization: pass; coordinator inspected the actual diff and
  unchanged helper reference. Independent review passed; see below.
- `python3 scripts/check_instructions.py`: passed after edits.
- `python3 -m unittest scripts.test_instructions scripts.test_package`: 21 passed after edits.
- `python3 scripts/package.py --output tmp/consolidate-record-helper-instructions-package`:
  passed manifest identity/version, catalog path, link, and package selection checks.
- `claude plugin validate plugins/lusona` and `claude plugin validate .claude-plugin/marketplace.json`:
  passed; manifest inputs unchanged by this refactor. Plugin validation gave advisory installation
  documentation advice, not a failure.
- `git diff --check`: passed for implementation and final record closeout edits.
- Installation, interactive agent compliance, PowerShell execution, and live host use not tested.
  No scripts/templates or command contracts changed; static characterization is the selected
  editorial verification, not a claim of improved agent behavior or measured latency.

### Independent review

Reviewer `review_consolidation`, a separate read-only leaf, inspected the actual three-file diff
and unchanged helper reference against AC1–AC4. Zero actionable findings. All eight baseline
boundaries passed: loading, mandatory use, shell/policy, paths, commands/dates, preservation/errors,
notes authority, and closeout sequence. Reviewer independently reran the instruction checker,
21 instruction/package tests, and whitespace check; all passed. No corrections required.
Coordinator accepted the result after reconciling the diff and recorded evidence.

### Version and commit follow-up — 2026-11-09

The user requested “bump the version and commit”. Applied patch version 2.0.4 to all five
native manifests and all five README version labels; added the dated untagged-source changelog
entry. Local commit is authorized; push/publication remains outside scope. The coordinator
reviewed the actual metadata diff; the earlier independent review remains valid for the
unchanged three-file instruction refactor.

- `python3 -m unittest scripts.test_package`: 10 tests passed after the bump.
- `python3 scripts/package.py --output tmp/lusona-2.0.4-release`: passed; archive 2.0.4 produced.
- Claude plugin and marketplace validations: passed.
- `agy plugin validate plugins/lusona --strict` and the packaged plugin equivalent: passed.
- Installation and interactive behavior remain untested.

## Current handoff

- Authorized work: bounded consolidation and 2.0.4 metadata update completed; local commit authorized.
  No push/publication authority.
- Changes: three canonical reference files, 40 net lines removed. Helper reference, scripts,
  templates and command contracts unchanged. Release metadata updated as recorded above.
  No broader contradiction audit claimed.
- Remaining work: none for this bounded increment; verification limits are recorded above.
- Workers: `rule_structure` and `review_consolidation` returned completed assignments, with no
  active operations, children, or write ownership. Host exposes no shutdown/close control;
  capacity release is not claimed.
- Next action: coordinator commits the verified increment; no installation or publication requested.
