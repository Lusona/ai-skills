# Selective delegation for status and explore

Created: 2026-11-11
Updated: 2026-11-11

## 2026-11-11 — Delegation overhead

The user reports that status is especially slow and asks to rethink delegation.
This is a discussion proposal; no workflow policy has been changed.

### Evidence and existing decision

- [Shared role rule](../../../shared/every-task.md) mandates delegation at every task size.
- [Status](../../../plugins/lusona/skills/status/SKILL.md) explicitly delegates inventory and inspection; [explore](../../../plugins/lusona/skills/explore/SKILL.md) explicitly delegates research and analysis.
- [Delegation](../../../plugins/lusona/references/delegation.md) requires assignment preparation, model routing, result reconciliation and lifecycle handling. A single sequential leaf satisfies the rule, so delegation does not necessarily provide parallel execution.
- [Rewrite drafting record](skill-rewrite-drafting/README.md) records the 2026-11-10 decision to delegate at every task size and notes earlier orientation exceptions. The user's latency concern challenges that policy's suitability for routine status and discussion.
- Inspection confirms mandatory delegation, not its share of elapsed latency. No runtime timing, installation or interactive behavior test was performed.

### Alternatives and recommendation

1. Keep mandatory delegation and tune model routing. Preserves specialist separation but retains serial assignment and reconciliation overhead.
2. Exempt status and explore entirely. Removes mandatory handoffs but also excludes useful delegation for independent inventories or research.
3. Recommended: allow direct execution by default. Delegate for required independent review, independently executable parallel work, or specialist capability/context isolation needed for a bounded outcome. Do not dispatch solely to satisfy a role or task-size rule. Preserve required review and coordinator ownership of questions, integration and shared state.

For status, read the requested records directly; split independent inventories only when useful concurrent work exists. For explore, keep discussion and ordinary analysis local; delegate bounded research when it benefits from parallel execution or specialist isolation. A faster leaf alone does not remove the handoff.

Any adopted change must reconcile AGENTS.md, the shared role block, the delegation reference and skill-specific mandatory dispatch instructions. Regenerate shared regions from their source. Keep assignment and lifecycle requirements for actual dispatches.

## 2026-11-11 — Accepted texts and implementation

A second session (Claude Code) proposed three texts for the same report; the user accepted
them there ("accept the three texts, TDD none"). They are narrower than alternative 3 above:
only `status` and `explore` assign work to the coordinator, and the other 12 skills still
delegate at every task size.

### Agreement

- Role line in `shared/every-task.md`: "Delegate specialist work at every task size, except
  work the skill assigns to the coordinator".
- `skills/status/SKILL.md`: "As coordinator, do the assessment yourself: read the records,
  queue, history and diffs, and run checks that write nothing. Delegate only an audit of product
  source code that the question depends on."
- `skills/explore/SKILL.md`: "As coordinator, conduct the conversation yourself, and reason
  from the conversation, the project records and the files the user names. Delegate research
  that needs other sources: a web search, product source code the user did not name, or a
  prototype."
- TDD level: `none` (user, 2026-11-11, conversation).
- Decisions revised in part: decision 4 of spec 20261110 and decision 16 Q3 of spec 20261111,
  recorded as [decision 28](../specs/20261111-loop-principles-and-skill-rewrite.md#decisions-and-uncertainty).

### Evidence

- Applied with exact-match replacements by the coordinator, without a leaf: the three texts
  were accepted verbatim and left no implementation decision. `python3 scripts/sync_shared.py
  --source shared plugins/lusona` regenerated the block in all 14 skills; the block has 293
  words (limit 300).
- Checks after the edit, all exit 0: `sync_shared.py --check`, `check_voice.py`,
  `check_skill_template.py`, `check_contract.py`, `check_instructions.py`; unit tests
  `test_sync_shared` (18), `test_voice` (49), `test_skill_template` (64), `test_contract` (65),
  `test_instructions` (16), `test_package` (14); `scripts/package.py --output
  tmp/delegation-texts-pkg` built `lusona-3.0.0.zip`; `git diff --check` clean.
- One observation before the change, not a measurement: in the Claude Code session the
  `status` inspection leaf took 109 seconds, 88,442 tokens and 19 tool calls.
- Limits: no agent run used the new text. Whether `status` and `explore` stop dispatching, and
  how much time that saves, is not observed. The loop-conformance suite was not run; no
  `status` or `explore` scenario in it requires delegation (check C11).
- Observation (2026-11-11, Claude Code, plugin loaded from the checkout): one `status` run
  for overall status loaded the new Role and `status` sentences and made 0 Agent calls; it read
  the records and ran the five check scripts itself. Elapsed time and tokens were not measured.
  The user confirmed in the conversation ("confirm") that this run counts as the observation.
- Not changed: `README.md:153-156` and its four translations still say the coordinator
  delegates "at every task size" with no exception; `CHANGELOG.md` has no line for this change;
  `AGENTS.md` and `references/delegation.md` were read and do not contradict the new texts.

## Current handoff

- Authority: the three texts above, TDD `none` (user, 2026-11-11, conversation). Commits, the
  README sentence, the changelog and a suite run are not authorized.
- State: closed on 2026-11-11 and recorded in
  [history](../history/2026-11-week-02.md#2026-11-11--selective-delegation-for-status-and-explore).
  The change is in the working tree, uncommitted.
- Next action: none for this item. The README sentence and the changelog line are an Ideas row
  in the [work queue](../work.md).
- Delegated assessment: /root/delegation_assessment, read-only workflow policy reviewer, gpt-6.1-sol with medium reasoning and bounded context. Returned complete with source findings; parent inspected and reconciled them. No writes or child agents. Host reported completed when interrupted. No close control is exposed, so host-capacity release is unconfirmed; the completed agent remains addressable.
