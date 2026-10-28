# Contributing to Lusona

Contributions to the skills, documentation, tooling, and host integrations are welcome.
Start with the [README](README.md) for the workflow and
[installation guide](INSTALL.md) for local setup.

## Bugs and feature requests

Search [existing issues](https://github.com/lusona/ai-skills/issues) before opening one.
Use the bug report form for defects and the feature request form for proposed changes.
For a larger change, open an issue to discuss the outcome and scope before implementing it.
You can send small documentation fixes as a pull request without an issue.

For bugs, include the host and plugin versions, installation source, reproduction steps,
expected behavior, and actual behavior. For agent behavior, include the prompt and a
short transcript when possible. Remove credentials, private code, and personal data
from examples and logs.

For features, explain the problem, who encounters it, and what a successful result
would look like. Include alternatives or workarounds you have considered.

## Make a change

Fork the repository, clone your fork, and create a branch for one bounded change.
Read `AGENTS.md` before editing; it also applies when you use an agent to contribute.

By submitting a contribution, you agree to license it under this project's
[MIT License](LICENSE). Only contribute material you have the right to submit, and
retain any required third-party notices.

- Edit canonical workflow sources under `plugins/lusona/`.
- Keep skills focused, preserve explicit TDD and authorization boundaries, and give
  the agent a concrete next action.
- Resolve bundled resources relative to the loaded skill. A `docs/lusona/` path in
  workflow instructions refers to the consuming project.
- Keep consuming-project records and generated packages out of your contribution.
  Use repository-local `tmp/` for scratch files and package output.
- Keep the Spanish, German, Simplified Chinese, and Japanese READMEs in sync with
  `README.md` when changing public documentation. Use natural technical prose in
  each language; preserve command names, paths, and authorization rules. Check
  translated section links and keep the language links in each README.
- Keep the native manifests' plugin names and versions aligned. Coordinate release
  version changes with maintainers rather than bumping versions for each pull request.

## Verify your change

Use `mise` for tools when available. The package builder requires Python 3; native
plugin validation requires Claude Code.

From the repository root:

```bash
git diff --check
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

The package builder checks manifest identity and versions, catalog paths, resource
links, and package contents. It writes to `tmp/lusona-package/` and refuses to
overwrite an existing output directory. For another build, use a fresh directory:

```bash
python3 scripts/package.py --output tmp/my-change-package
```

For changes to the work-record helper, run its behavioral checks:

```bash
bash scripts/test-work-record.sh
```

Run the PowerShell helper's behavioral checks in Windows PowerShell 5.1 or PowerShell 7:

```powershell
powershell.exe -NoProfile -File scripts/test-work-record.ps1
```

Use `pwsh` instead of `powershell.exe` for PowerShell 7. Both helpers share templates
and must preserve the command and file-safety contract. Test native Windows separately
from PowerShell on macOS/Linux; passing on one platform does not establish the others.

For script behavior changes, add or update tests that exercise the affected behavior.
Record an explicitly selected TDD policy (`none`, `targeted`, or `strict`) and its
user or standing-preference source; `none` still requires verification.
Documentation changes need relevant content and link checks. Apply the behavioral
evidence requirements below when instructions change skill behavior. Packaging checks
alone do not establish host integration; report unavailable checks explicitly.

### Behavioral evidence

Keep verification proportionate to the observable change and affected boundaries.
These requirements are maintained here; an existing suite or evidence record can
satisfy them without creating another runner or duplicating its records.

1. **Choose proportionate coverage.** Describe the observable change, affected boundaries, and
   coverage rationale. Include positive and relevant negative/boundary cases; preserve
   multi-turn sequences in the same trial session for steering, authority, or resumption.
   Justify representative coverage across shared responsibilities; cases may overlap; not every
   host must run. Low-risk, noncomparative behavior changes may use relevant candidate-only
   checks. Matched baseline/candidate evidence is required for named test-first behaviors,
   comparative improvement claims, and consequential shared boundaries (authority, TDD,
   completion, trust, persistent data, cross-worker ownership). File count alone does not
   determine risk. Editorial behavior-preserving changes may use content/link checks with a
   rationale.
2. **Declare verification before trials.** Freeze applicable cases, outcome criteria, exact
   inputs, candidate revisions/hashes and local modifications, host/version, model/reasoning,
   capabilities/permissions, finite budget, and stopping condition. When comparison is required,
   pin an unchanged baseline captured before relevant edits or recoverable from a snapshot.
   Match relevant conditions except the intended change; disclose mismatches and limit claims.
   Keep evaluator materials separate; actors receive raw tasks and authorized resources without
   rubrics, prior outcomes, or desired answers.
3. **State TDD separately.** Record the explicitly selected `none`, `targeted`, or `strict`
   policy and its user or standing-preference source. Separate named test-first behaviors from
   regression coverage. For test-first behaviors, observe intended baseline failure before
   relevant edits, then obtain matched candidate evidence. Passing baselines are
   characterization; setup failure, textual disagreement, or weakened criteria is not red.
   Resolve infeasible sequencing before substituting an approach. Later evidence cannot
   establish a missed sequence. Behavior-preserving clarification needs no manufactured failure;
   `none` still requires verification.
4. **Grade independently.** A person or agent independent of the actor grades retained
   conversation, actual actions, and artifacts against frozen criteria. Judge semantic outcomes
   and boundaries, not wording, headings, tool order, or question counts. One qualified reviewer
   may assess both diff and outcomes; role labels alone do not require another reviewer.
   Supplement with deterministic checks where useful. Retain grader identity, exact evidence,
   rationale, and unresolved disagreement. Process exit or actor success claims do not prove
   behavioral success.
5. **Report all outcomes and limits.** Use `pass`, `fail`, `inconclusive`, or `setup-blocked`
   for attempted trials; identify planned but unrun trials. Setup errors, missing capabilities,
   timeouts, incomplete captures, and unresolved grading cannot count as passing evidence or
   red. Observed authority or scope violations fail the applicable trial. Include unfavorable
   and incomplete results, unrun required checks, and host/model limits. Preserve earlier
   attempts; record retry/budget-change reasons and authority. Do not infer missing usage, total
   cost, or statistical significance.
6. **Retain reviewable support.** Link exact runs/artifacts with provenance and access for
   inspection. Material evidence or a durable reference must survive scratch cleanup; disposable
   `tmp/` cannot be its only home. Large transcripts need not enter Git. Follow [evidence
   retention](plugins/lusona/references/evidence.md) for material decision evidence; routine
   verification stays with its owner. Record redactions, unavailable evidence, and resulting
   limits.

Contribution summaries identify TDD/source, coverage rationale, applicable condition identifiers
and independent grades, all outcomes including incomplete/unrun work, exact evidence, and
limits. Comparison identifiers apply only to comparisons. Editorial summaries give the
behavior-preserving rationale and static results instead of trial metadata.

## Open a pull request

Explain the problem, resulting behavior, scope, and verification evidence. Link the
related issue when there is one, and call out installation or interactive behavior
you have not tested. Keep unrelated edits in separate pull requests.

Use Conventional Commits for commit messages, with a body explaining why the change
is needed, for example `docs: clarify Xcode installation`. If you use an agent,
authorize commits explicitly; the repository instructions prohibit unrequested commits,
pushes, and publication.

The `@lusona/core` team owns review across the repository. Maintainers may request
changes to scope, behavior, or verification before merging.
