# Drafts workspace

Rewrite workspace for [spec 20261111](../docs/lusona/specs/20261111-loop-principles-and-skill-rewrite.md).
Nothing here is packaged or loaded by a host. `plugins/lusona/` stays unchanged until promotion (W14).

## Start state

- Decision 11: the earlier workspace was discarded on purpose. Prior draft text is not an input.
- Decision 15: `drafts/lusona/` holds only files the rewrite writes or changes. Contract and package checks run on the whole draft after W9-W10.

## Contents

| Path | Content | Owner |
| --- | --- | --- |
| `shared/every-task.md` | Every-task block source (250 words by `wc -w`, which counts a Markdown link as one word; limit 250, decision 15) | W5 |
| `shared/final-reply.md` | Final-reply source: Result with status, Evidence, next-action table or None form | W5 |
| `skill-template.md` | Skill skeleton for authors | W5 |
| `lusona/skills/implement/SKILL.md` | Pilot skill in the template, with both regions generated | W5 |
| `readme-destinations.md` | Destination of each README inventory row readme-001 to readme-187 | W5 |
| `lusona/templates/`, `lusona/scripts/` | Renamed templates (A8) and record helpers | Other W5 workers |

## Generated regions

- Markers: `<!-- lusona:begin every-task -->` ... `<!-- lusona:end every-task -->` after the H1, and `<!-- lusona:begin final-reply -->` ... `<!-- lusona:end final-reply -->` as the first content of `## Final reply`.
- Layout: begin marker line, the source text without its final newline, end marker line. No blank line is added.
- Source files hold region text only: no heading, no preamble.
- Links in the sources use the form a `SKILL.md` uses for plugin-level references, `../../references/x.md` (ADR 20261111).
- The pilot regions were filled by `tmp/w5b/splice.py` and compared with `diff`: both identical. The sync script (`scripts/sync_shared.py`) is another worker's; it must use the same layout or regenerate the pilot.

## Promotion rule

At promotion, `drafts/shared/` moves to repository-level `shared/` (decision 15, coordinator note c; location constraint from decision 13). It stays outside `plugins/lusona/` and is never packaged; no packaged file links to it. `drafts/lusona/` replaces the matching files in `plugins/lusona/` only with user authorization.

## Principle placement (proposal)

Skills do not cite P1-P8 by ID. Each principle's instruction sits at one place:

| Principle | Instruction location |
| --- | --- |
| P1 Non-sequential | Description "Use when" and "Not for ...; use <skill>"; `## Establish` names skills for unresolved needs; Final reply valid next actions |
| P2 Refinement | `## Establish` reads carried outcome, decisions, authority, TDD, evidence and uncertainty; `## <Procedure> and record` writes them |
| P3 Decisions as inputs | Block, Decisions line |
| P4 Recorded invalidation | Reference `revisions` (new), linked from the block Decisions line |
| P5 Evidence | Block, Evidence line; Persona Evidence field |
| P6 Authority | Block, Authority line |
| P7 Continue bounded work | Block, Progress line |
| P8 Next action | Final-reply region |

The principle table itself goes into reference `workflow-guide` (W9) for routing and terminology, and into the plugin README for humans (W10).

## Proposals

- A2: the reply template is a second generated region, separate from the block, placed first in `## Final reply`. The skill's valid next actions follow the end marker. Reasons: the template order puts Final reply last, and the block stays at 250 words.
- A3: the block is at most 250 words by `wc -w`, 9 lines of a bold label followed by imperative sentences, under the voice limits. Measured: 250 words; sentence counts in Self-check. The block links only references whose trigger can occur in every skill: `delegation`, `revisions`, `tdd`, `retention`.
- A5: the Role line sets the role. The agent is the coordinator unless an assignment names it a leaf. A leaf does not delegate or ask the user and returns questions, conflicts and next actions to the coordinator. The final-reply region sends a leaf to the assignment result fields in `delegation`. Detail stays in `delegation` Assigned leaves.

## References for W9

| Reference | Linked from | Status | Must contain |
| --- | --- | --- | --- |
| `delegation` | Block, final reply, implement | Existing | Assignment contract, Assigned leaves, Assignment results, independent review conditions (readme-138 to readme-140) |
| `revisions` | Block | New | P4 procedure (readme-043 to readme-047), follow-up steering (readme-032, readme-033) |
| `tdd` | Block | Existing | Unchanged scope |
| `retention` | Block, implement | Existing | Record choice, spec and queue requirement, no-record cases |
| `naming`, `queue`, `visuals`, `corrections`, `commits`, `closeout` | implement | Existing | Unchanged scope |
| `completion` | none yet | New rewrite of the untracked file | Examples only (kept 20261110 decision 10); formatting rules readme-160 to readme-165 are in the final-reply source |

Templates linked by the pilot: `templates/notes.md.template`, `templates/spec.md.template`.

Skills linked by the pilot (W6-W8 must keep these paths): `specify`, `architect`, `investigate`, `review`, `refactor`.

## Behavior changes against baseline implement (`34186da`)

Principle-driven:

1. P3: when evidence contradicts an accepted decision, the skill revisits it with the user and records the outcome. Baseline: "revisit clarification, design, or investigation", preserving accepted constraints, and README "reopen within authority". Unaffected increments continue.
2. P8 and 20261110 decision 3: every task reply uses the full form (Result with status, Evidence, next-action table or None with a reason). Baseline: the form was a default for substantive replies, and None needed no reason.
3. 20261110 decision 4: the coordinator delegates at every task size and states a local fallback. Baseline: README listed implementation as delegated work, with exceptions for orientation.

Not principle-driven:

4. Status glyphs are dropped; the four status words remain (readme-159).
5. The TDD line says "explicitly selected level"; the standing-preference detail stays in `tdd`.
6. Rules the skill took from the README are now in the skill: corrections trigger (step 5), local commits and separate push authority (step 11), domain skills (Establish), preserve unrelated changes (step 8), independent review trigger (Establish, conditions in `delegation`). Commit and push authority also needs a line in `refactor` (W7).
7. The description adds the output and "Not for ...; use refactor".
8. The baseline `## Commit verified increments` and `## Next action` sections are folded into `## Increments and record` and `## Final reply`. Valid next actions are listed explicitly; their content matches the baseline.

## Open questions

- Q1: `model-routing`, `worker-lifecycle` and `handoff` have no every-skill trigger, and P-a forbids chains. Proposal: merge `model-routing` and `worker-lifecycle` into `delegation` (39 + 30 + 70 baseline lines, under 200), and `handoff` into `retention`.
- Q2: readme-015 and readme-066 (host and project restrictions, host prompts) are removed as restating host behavior. Confirm, or the block needs one more sentence.
- Q3: readme-175 allowed explore and status conversation to stay local. Under 20261110 decision 4 it is removed; confirm that the conversation itself stays with the coordinator.
- Q4: `completion` (examples only) has no linking skill yet; AC14 needs one, or the file is removed.
- Q5: readme-121 (greetings are not task replies) and the removal of the task-local check exception (readme-173) come from the discarded part of 20261110 decision 10. They are marked as proposals.

## Self-check (2026-11-11)

See the coordinator report for the commands and counts. Not run: package build, link check, contract check on the whole draft, `sync_shared.py`, `check_skill_template.py` (other workers' scripts, stubs at the time).
