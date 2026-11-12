# Workspaces and baselines

Read before the first production edit of a batch item, before choosing an item's workspace, and before transferring an item's changes.

## Workspaces

- Before production edits, inspect the repository's and host's capabilities. Give each item a separate workspace: a worktree or an isolated copy.
- Document-only assignments can share the project tree when ownership is disjoint and records are created by the helper with date prefixes.
- Tasks within one item share its workspace only when they have no unresolved shared behavior, their writes are disjoint and they share no mutable check resource.
- Keep scratch material in the location project instructions permit.

## Baselines

- Identify the required starting content: the revision when present, staged and unstaged changes, untracked files, deletions and binary content.
- Do not treat a clean checkout of HEAD as the complete starting content.
- Retain a baseline identifiable by content. Distinguish user-owned starting content from batch-owned edits.
- Record workspace paths, ownership, baseline identity, dependencies and the method to reconstruct the item delta.
- Check content identity with repository tools or retained manifests or snapshots, including paths, bytes and file modes.
- A branch name or a plain status listing does not establish content identity.

## Unrelated changes and transfer

- Do not move, stash, overwrite, clean or commit unrelated changes to obtain a baseline.
- Commit only when project authorization permits it.
- Without commits, keep the uncommitted edits. Transfer the attributable item delta relative to its baseline, including binaries and deletions.
- Never substitute a whole workspace copy that would overwrite changes in the destination.
- When required inputs or ownership cannot be established, defer the affected work.
- Without isolation, work in sequence only where unfinished edits stay separated. Otherwise stop the batch.
