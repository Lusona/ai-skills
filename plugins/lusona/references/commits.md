# Commit verified increments

- During authorized implementation, make local commits after coherent increments pass their
  required checks, unless the user opts out or repository instructions prohibit it. Group
  related implementation, tests, configuration, and documentation by purpose and dependency.
  An increment may span files or tasks; each commit must leave the project usable. Do not
  create one commit per file, task, skill stage, or workflow-state transition. A small
  change can be one verified commit.
- Include related change records, verification evidence, queue updates, and any completion
  records already justified by the evidence in the implementation increment's commit.
  Saving a record or recovery checkpoint does not require committing it. Do not create
  preparatory or follow-up documentation commits solely for workflow bookkeeping.
  If required review, acceptance, or delivery occurs after the implementation commit,
  consolidate remaining record updates into one closeout commit when commit authorization
  covers it. Do not mark completion early to fit a commit boundary. Documentation that is
  itself the requested deliverable can have its own commit when authorized.
- Complete the selected TDD sequence and required verification before committing. Keep
  incomplete or failing work uncommitted unless the user explicitly requests a checkpoint
  commit. Report any checks or commit operation that could not complete; do not claim success.
- The coordinator manages staging and commits after integrating delegated work; subagents do
  not race on the shared index. Inspect working-tree and staged changes, stage only this
  increment's files or hunks, and inspect the resulting staged diff before committing.
  Preserve unrelated edits and staged changes; never include them through a blanket add or
  commit. Ensure the committed content is what passed verification, including when shared
  files require partial staging.
- Use the contract's Conventional Commits format and explain why in the body. Choose the
  type for the increment's outcome; accompanying workflow records do not make a fix or
  feature a documentation commit. Save verification evidence before committing and report
  the resulting hash in the conversation. Save a hash only when needed to identify reviewed
  or integrated content or when project rules require it; include it in the next otherwise
  needed record update. Do not amend or create a commit solely to record another commit's hash.
- A successful commit records a verified increment. Human acceptance and delivery remain
  separate completion conditions. Pushing, publishing, amending commits, and rewriting shared
  or published history require separate authorization. For integration, apply the rebase
  authority and linear-history rules below.


Use Conventional Commits: `type(scope): imperative summary`, with an optional useful scope
and a body explaining why. Choose the type for the change. Mark breaking changes with `!`
and a `BREAKING CHANGE:` footer explaining the impact.

## Linear integration

- Within authorized Git integration, prefer `git merge --ff-only` when the target can
  advance directly. Check the incoming commits as well: a fast-forward can import existing
  merge commits, so fast-forward success alone does not establish linear history. Do not
  introduce merge commits into the target unless the user explicitly requests that topology.
- If branches diverge, rebase agent-owned, unpublished commits onto the current target,
  then fast-forward. This is included in authorized integration unless project instructions
  prohibit it; it does not authorize commits or integration where those actions are forbidden.
  Do not rebase another contributor's work or shared/published commits without explicit
  authority, and do not force-push as an implicit part of rebasing.
- The coordinator serializes rebasing and integration, stops affected writers, and preserves
  unrelated changes. Inspect the resulting diff and rerun affected verification after a rebase
  or conflict resolution. Refresh commit/content identities and review evidence when changed
  inputs invalidate it; confirm the target has not advanced before the final fast-forward.
  Conflicts requiring a consequential behavior or scope decision follow the normal question
  or batch-deferral rules.
- Squash integration is an alternative when explicitly selected or required by the project's
  established workflow. Verify the resulting content and record its new identity. Do not
  silently discard meaningful commit boundaries merely to avoid resolving a divergence.
- Apply this policy to new integration; do not rewrite existing target history to remove old
  merges. If permitted operations cannot produce the requested linear result, report the exact
  blocker instead of falling back to a merge commit. No Git operation is required for a
  no-commit workflow that integrates attributable file changes.
