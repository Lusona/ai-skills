# Repository instructions

- Canonical workflow sources live in `plugins/lusona/`. Edit them directly;
  do not edit generated packages or duplicate sources in consuming projects.
- Preserve bounded tasks, explicit TDD, native question tools when permitted, and a
  concrete next action in every skill. Keep context and process small.
- Write direct instructions with an action and trigger. Give each shared policy one
  authoritative definition; repeat short local instructions when they make a skill easier
  to execute. Replace overlapping wording, and avoid reference chains that obscure the action.
  Avoiding duplication is a design preference, not a rule that overrides clarity.
- Edit the every-task block and final reply in repository-level `shared/`, never inside the
  generated `<!-- lusona:begin NAME -->` regions of a `SKILL.md`. Regenerate the regions with
  `python3 scripts/sync_shared.py --source shared plugins/lusona`; add `--check` to verify.
  `shared/` is not packaged, and no packaged file links to it.
- Resolve bundled resources relative to the loaded skill. Paths under `docs/lusona/`
  refer to data in the consuming project, not to this plugin repository.
- Keep native plugin manifests' identity and version aligned. Catalog plugin paths are
  relative to this repository root. Exclude project data from packages.
- Use `mise` for required tools when available. Keep scratch files and generated packages
  in repo-local `tmp/`, never system `/tmp`.
- Validate changed skills, native manifests/catalogs, links, and packaging as appropriate.
  Say when installation or interactive behavior has not been tested.
- Before accepting a new or changed skill, reference, template, shared text or record helper
  command, audit it with [docs/skill-audit.md](docs/skill-audit.md).
- The coordinator delegates substantive specialist work to bounded subagents and owns
  questions, reconciliation, integration, verification, and shared state. Give each
  subagent a persona, minimal context, and disjoint write ownership. Local execution is
  the fallback when delegation is prohibited or unavailable; it never satisfies required
  independent review. Keep queue and handoff updates with the parent.
- Target context handoff before 50% usage when measured; otherwise checkpoint at task
  boundaries without inventing a percentage. Preserve authorization across handoffs.
- Do not commit, push, or publish unless requested. Preserve unrelated changes.
- Use Conventional Commits with a body explaining why when commits are authorized.
