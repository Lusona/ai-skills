# Commits and integration

Read before staging, committing, rebasing or integrating changes.

## Authority

- Commit locally during authorized implementation or refactoring, unless the user opts out or repository instructions prohibit it.
- Other work needs commit authority from the user.
- Push, publication, pull requests, external tickets, amending commits, and rewriting shared, published or another contributor's history each need separate authority.
- A successful commit records a verified increment. Human acceptance and delivery remain separate completion conditions.
- A workflow that integrates attributable file changes without commits needs no Git operation.

## Commit boundaries

- Commit after a coherent increment passes its required checks.
- Complete the selected TDD sequence and required verification before committing.
- Keep incomplete or failing work uncommitted unless the user explicitly requests a checkpoint commit.
- Group related implementation, tests, configuration and documentation by purpose and dependency.
- An increment may span files or tasks. Each commit leaves the project building and its required checks passing.
- Do not create one commit per file, task, skill or queue state change.
- A change with one verified increment is one commit.
- Include the related change records, verification evidence and queue updates in the increment's commit. Include a completion record only when the saved evidence shows its completion condition is met.
- Saving a record or a recovery checkpoint does not require a commit.
- Do not create preparatory or follow-up commits only for workflow records.
- When required review, acceptance or delivery happens after the implementation commit, put the remaining record updates in one closeout commit, if commit authority covers it.
- Do not mark completion before its condition is met to fit a commit boundary.
- A requested documentation deliverable may have its own commit when authorized.

## Staging

- As coordinator, stage and commit after integrating leaf work. Leaves do not stage or commit to a shared index.
- Inspect working-tree and staged changes before staging.
- Stage only this increment's files or hunks. Inspect the staged diff before committing.
- Preserve unrelated edits and staged changes. Never stage or commit them with an add-all or commit-all command.
- Commit the content that passed verification, including when shared files need partial staging.
- Save verification evidence before committing. Report the resulting hash in the reply.
- Record a hash only to identify reviewed or integrated content, or when project rules require it. Add it to the next record update that other work requires.
- Do not amend or create a commit only to record another commit's hash.
- When a check or commit operation cannot complete, report it. Do not claim success.

## Message format

- Use Conventional Commits: `type(scope): imperative summary`. The scope is optional.
- Explain why in the body.
- Choose the type for the increment's outcome. Accompanying workflow records do not make a fix or feature a `docs` commit.
- Mark a breaking change with `!` and a `BREAKING CHANGE:` footer that states the impact.

## Integration

- Within authorized Git integration, use `git merge --ff-only` when the target can advance directly.
- Check the incoming commits for merge commits. A successful fast-forward alone does not establish linear history.
- Do not add merge commits to the target unless the user explicitly requests that topology.
- When branches diverge, rebase agent-owned, unpublished commits onto the current target, then fast-forward.
- Authorized integration includes this rebase unless project instructions prohibit it. This rule does not authorize commits or integration where those are forbidden.
- Do not rebase another contributor's work or shared or published commits without explicit authority.
- Do not force-push as part of a rebase.
- As coordinator, serialize rebasing and integration, stop affected writers, and preserve unrelated changes.
- After a rebase or conflict resolution, inspect the resulting diff and rerun the affected verification.
- Refresh the commit identities and the review evidence that changed inputs invalidate.
- Confirm the target has not advanced before the final fast-forward.
- When a conflict needs a consequential behavior or scope decision, ask the user. Inside a batch, defer the item under the batch rules.
- Use squash integration only when the user explicitly selects it or the project's workflow requires it. Verify the resulting content and record its new identity.
- Do not discard the commit boundaries between verified increments only to avoid resolving a divergence.
- Apply this policy to new integration. Do not rewrite existing target history to remove old merges.
- When permitted operations cannot produce the requested linear result, report the exact blocker. Do not create a merge commit instead.
