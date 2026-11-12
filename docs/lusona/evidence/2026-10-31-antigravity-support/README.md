# Antigravity support verification

Updated 2026-10-31. Scope: App, CLI and standalone IDE metadata, resource packaging,
installation guidance and bounded native CLI checks. User selected all surfaces and targeted
TDD, subsequently authorized version 1.4.0, and requested direct GitHub installation validation
and evidence cleanup. No commit, push, publication or real-user-configuration installation.

## Current results

| Check | Observed result | Exact evidence in artifacts.zip |
| --- | --- | --- |
| Public GitHub root and tree installation | CLI 1.4.12/Linux; both install enabled Lusona 1.3.2 with 13 skills through Claude compatibility | github-install/project/github-root.txt, github-tree.txt, respective list logs |
| Installed content | Identical root/tree inventories: 55 files, including all 54 canonical source files plus generated plugin.json; no docs or docs/lusona | github-install/project/installed-root-summary.json, github-install/installed-tree-inventory.txt |
| Shared-resource integrity | All 54 canonical files match public revision SHA-256; 19 references, 13 templates, 2 scripts, 1 asset | github-install/public-source-comparison.json |
| Public source identity | main/HEAD 7a339789dab09ec4b5a43ef7d48df9ce9522c529; native 1.4.0 manifests are not published | github-install/project/public-head.txt |
| Current package tests | All 8 tests pass; metadata, root references, full resources, mismatch rejection, exclusion and packaged runner covered | version-1.4.0/package-tests.txt |
| Historical native lifecycle | Native fixture 1.3.2 install/list, helper execution, synthetic 1.3.3 replacement, uninstall, project/config preservation passed | captured-lifecycle/test.py, run.sh, output.txt |
| Root-reference tests | Expected test-first failure then green; packaged-root strict validation discovers 13 skills | root-reference/ logs |

[artifacts.zip](#removed-archives) retains exact commands, outputs, scripts, source identities and
file hashes. Historical observations remain unchanged; their versions are not relabeled 1.4.0.

## GitHub installation decision

Document the explicit canonical directory:

```bash
agy plugin install https://github.com/lusona/ai-skills/tree/main/plugins/lusona
agy plugin list --json
```

The test used the equivalent GitHub owner casing `Lusona`. Root URL installation also passed
via automatic nested-plugin discovery on the published 1.3.2 tree. The explicit tree URL avoids
depending on root discovery after the new native root manifest is published. Native GitHub
installation of unpublished 1.4.0 is not claimed. Local/package installation remains available.

Google's [Plugins guide](https://antigravity.google/docs/plugins/) documents GitHub URL
installation; tree-path selection was verified with the actual CLI. All six installation/readme
documents now use the tree URL. Updates reinstall the same URL. App/IDE guidance retains its
separate discovery checks; successful CLI installation does not prove interactive behavior.

Isolation: bubblewrap mounted the host read-only, masked real ~/.gemini with disposable
configuration, and allowed writes only to scratch configuration/project directories. Network
was enabled for public GitHub reads; host Git credentials were excluded. Exact wrappers and
CLI hash are in github-install/. Initial sandbox DNS failure is retained as a clearly labelled
transcription of the original tool result because the scratch logs were overwritten during the
successful retry. No failure was recreated. One network correction made material progress.
Verifier: /root/validate_antigravity_github. Documentation: /root/github_install_docs.
Parent checked returned logs, hashes and documentation claims.

## Historical test-first and review evidence

- package-red.txt / package-green.txt: four original expected failures before native metadata
  and packaging implementation, followed by passing tests.
- correction1/: independent review found the omitted portable package test runner; its added
  regression failed before the fix, then all five tests passed in source and extracted package.
- captured-lifecycle/: a complete packaged-install repeat preserves the initial missing-scratch-
  directory failure and subsequent success. Original lifecycle-test.py/results remain retained.
- root-reference/: root manifest coverage extended the suite to eight tests, with red/green
  and native validation evidence. A custom marketplace-only probe was not supported.
- workspace-list-result.txt: an empty registry list after manual workspace placement does not
  prove workspace discovery or its absence.
- historical/README-before-github-validation.md preserves the previous detailed summary and
  correction/reviewer history before consolidation. No prior evidence was deleted.

## Current local checks and remaining limits

Current 1.4.0 source/portable strict validation previously passed with 13 skills. Checkout-root
strict validation reports the existing AGENTS.md warning; the portable root excludes repository
instructions/project records and passes. Eight package tests, portable build/resource-link
checks and whitespace checks passed after the GitHub documentation edits. Package output is
reproducible with `python3 scripts/package.py --output <fresh-repo-local-directory>`.

No model-driven status/specify invocation, App/IDE installation/discovery, or Windows/PowerShell
execution was tested. These remain AC2 completion gaps; the queue stays Review. Next action:
perform the outstanding live-host checks in a suitable test environment. No broader evidence
migration was needed; older topic directories remain in place with their references intact.

## Exact .git URL follow-up

`agy plugin install https://github.com/lusona/ai-skills.git` passed on CLI 1.4.12
using the same isolated configuration. Native listing confirms enabled 1.3.2 with all
13 skills through Claude compatibility. Logs and exact probe/wrapper are retained under
`github-install/` in artifacts.zip as `dot-git-*` and `project/github-dot-git.txt`.
This confirms the suffix is accepted; it does not test the unpublished root native manifest.

## Published 1.4.0 installation and documentation correction

User authorized real Antigravity installation after pushing. On CLI 1.4.12, the exact root
`.git` install command exited 0 and enabled native1.4.0 with13skills, but installed docs/lusona
from the repository. Reinstalling the explicit tree/main/plugins/lusona URL exited0 and
replaced it with the canonical native1.4.0 plugin. Native list confirmed enabled1.4.0/13skills;
strict validation reported findings: []; direct filesystem checks confirmed shared resources
and absence of docs. These are observed results from the installation turn, not a fresh rerun.

INSTALL.md host sections now follow Antigravity, Claude Code, Codex, Cursor, Xcode. All five
READMEs use the same verified tree URL; INSTALL verification distinguishes current native
behavior from historical compatibility-based root discovery. Package/link and whitespace
checks pass. UI/model-driven invocation remains untested. No commit or push performed for
this follow-up.

User subsequently explicitly selected the repository-root `.git` command as the primary
installation URL. Restored it in INSTALL.md and all five READMEs; retained the observed
root-install project-record inclusion in INSTALL.md. This supersedes the preceding
documentation URL choice, not the recorded installation observations.

## Removed archives

The archives below were removed from the working tree on 2026-11-12 to reduce the checkout
size. Commit `9f2260f` holds each one unchanged. Restore an archive from the repository root
with `git show 9f2260f:docs/lusona/evidence/2026-10-31-antigravity-support/<path> > <file>`, then compare its SHA-256 with this table.
Hashes recorded in the manifests of this topic apply to the restored files.

| Path in this topic | Bytes | SHA-256 |
| --- | --- | --- |
| `artifacts.zip` | 28746 | `24decce9dc1ccc8e412d7912e32fb9d4ed3a76fb468d1f9de9b67fbe2f0b0650` |
