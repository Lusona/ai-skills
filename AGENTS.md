# Repository instructions

- Canonical workflow sources live in `plugins/lusona/`. Edit them directly;
  do not edit generated packages or duplicate sources in consuming projects.
- Preserve bounded tasks, explicit TDD, native question tools when permitted, and a
  concrete next action in every skill. Keep context and process small.
- Resolve bundled resources relative to the loaded skill. Paths under `docs/lusona/`
  refer to data in the consuming project, not to this plugin repository.
- Keep native plugin manifests' identity and version aligned. Catalog plugin paths are
  relative to this repository root. Exclude project data from packages.
- Use `mise` for required tools when available. Keep scratch files and generated packages
  in repo-local `tmp/`, never system `/tmp`.
- Validate changed skills, native manifests/catalogs, links, and packaging as appropriate.
  Say when installation or interactive behavior has not been tested.
- Use bounded subagents for independent work when useful; give each a persona, minimal
  context, and disjoint write ownership. Keep queue and handoff updates with the parent.
- Target context handoff before 50% usage when measured; otherwise checkpoint at task
  boundaries without inventing a percentage. Preserve authorization across handoffs.
- Do not commit, push, or publish unless requested. Preserve unrelated changes.
- Use Conventional Commits with a body explaining why when commits are authorized.
