# Leaf rules inside a batch

Read as a leaf before starting a batch assignment, and as coordinator before writing one. The coordinator gives this file's path or text in every batch assignment.

- Perform the assigned responsibility and return its evidence to the coordinator.
- Do not start another assignment or manage shared state without an instruction from the coordinator.
- A delegation grant in a batch assignment is part of the batch pool. Dispatch no more leaves than it names.
- Return possible dependencies, shared assumptions, unresolved shared behavior and newly found coupling to the coordinator. Do not settle them locally.
- Record the basis of each routine decision the coordinator delegated to you.
- For a missing consequential decision, authority or TDD level, return the gap to the coordinator. Do not interview the user.
- Create records only within your assigned ownership, using the record helper. Report naming conflicts.
- As a review leaf, stay read-only. The coordinator schedules authorized repairs separately.
- Do not edit the queue, the batch record or the batch handoff.
- When the assignment completes, blocks or ends incomplete, return the assignment result before waiting or ending.
- Use the host's completion notification or message mechanism to return it.
- Do not wait for sibling assignments or for batch consolidation.
- For repair work, report the charged rounds under the batch repair budget.
