---
name: <skill>
description: <Action> <object> and produce <output>. Use when <unresolved need that selects this skill>. Not for <adjacent need>; use <other-skill>.
---

<!--
Author notes (delete this comment in a real skill).
- name equals the directory name (K1). The description has three parts in this order:
  action and output; "Use when ..."; "Not for ...; use <skill>" naming an existing skill.
- The two generated regions are written by the sync script from the repository-level
  shared sources (draft: drafts/shared/every-task.md and drafts/shared/final-reply.md).
  Do not edit text between the markers; edit the source and rerun the sync script.
  Region layout: begin marker line, source text without its final newline, end marker line.
- Link a plugin-level reference as [x](../../references/x.md) and a reference used only by
  this skill as [x](references/x.md). Never name a plugin-level file by a bare path.
- Every link to a reference sits in a trigger sentence: "Before <action>, read [x](...)".
- Voice: V1-V9. Imperative, trigger stated, no hedges, sentences of at most 40 words,
  file average at most 15 words per sentence (scripts/check_voice.py).
- Do not restate a rule from the every-task block; add only what this skill changes or adds.
- Principles: do not cite P1-P8 by ID. Their instructions sit here:
  - P1 non-sequential: description "Use when" / "Not for"; Establish names skills for
    unresolved needs; valid next actions under Final reply.
  - P2 refinement: Establish reads carried state; <Procedure> and record writes it.
  - P3 decisions as inputs: every-task block, Decisions line.
  - P4 recorded invalidation: reference revisions, linked from the Decisions line.
  - P5 evidence: block Evidence line; Persona and judgment Evidence field.
  - P6 authority: block Authority line.
  - P7 continue bounded work: block Progress line.
  - P8 next action: final-reply region.
-->

# <Skill title>

<!-- lusona:begin every-task -->
<!-- lusona:end every-task -->

## Persona and judgment

- Persona: <role, for example implementation engineer>.
- Responsibility: <the outcome this skill owns, and what it does not own>.
- Decision criteria: <how to choose between options inside this skill's authority>.
- Evidence: <what counts as evidence for this skill's claims; what does not>.
- Failure modes: <2-5 concrete mistakes to check for before replying>.

## Establish <input>

<!--
Read carried state before acting (P2): outcome, accepted decisions, authority, TDD level and
source, evidence and uncertainty. Name the owning record and where to find it. State what to do
when the input is missing or contradicts an accepted decision (the block's Decisions rule
applies; add only skill-specific handling). Name other skills for unresolved needs (P1).
-->

- Read <owning record or request>. Before <record operation>, read [<reference>](../../references/<reference>.md).
- Before <substantive work>, read the applicable domain skills available in the session; report a missing required one.
- When <input> is missing, <action>.
- When <need outside this skill> is unresolved, use [<skill>](../<skill>/SKILL.md).

## <Domain> practices

<!--
Optional. Omit only when the skill has no domain checks; record the omission in the skill
inventory. Each item: a trigger and an action.
-->

- When <condition>, <check>.

## <Procedure> and record

<!--
The steps this skill performs, in order only where order matters for correctness or
dependencies. End with what to record and where (P2, P4), linking the reference that owns
the record format.
-->

1. <Step with an observable result>.
2. Before <operation>, read [<reference>](../../references/<reference>.md).
3. Record <results, evidence, decisions, handoff> in <owning record>.

## Final reply

<!-- lusona:begin final-reply -->
<!-- lusona:end final-reply -->

Valid next actions for <skill>:

- <Condition>: <next action>, owner <user | coordinator | skill>.
- <Condition>: use [<skill>](../<skill>/SKILL.md) for <need>.
