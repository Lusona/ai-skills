# Notes: independent review of the skill rewrite (W13)

Spec: [20261111-loop-principles-and-skill-rewrite](../specs/20261111-loop-principles-and-skill-rewrite.md), AC17.
Date: 2026-11-11. Reviewers: two read-only leaves that wrote none of the change; findings saved by the
coordinator (subagents cannot write report files).

## Reviewer A: draft plugin content

Scope: `drafts/lusona/**`, `drafts/shared/*`, `drafts/skill-template.md`, destination maps. Baseline `34186da`.

Counts: 2 blocking, 20 non-blocking. Destination audit: 84 rows sampled (64 rule rows across all 21 sources,
10 batch `exec` rows, 10 non-rule rows); 1 partial miss (readme-144), 1 stale row (readme-181); all 1026
inventory rows have a destination. Checks on `drafts/lusona`: voice 0, template 0, contract 0, sync in sync,
instructions exit 1 (F2).

| ID | Sev | Location | Defect | Violates |
| --- | --- | --- | --- | --- |
| F1 | blocking | `shared/every-task.md:1`; `references/delegation.md:82`; `batch/references/leaf-rules.md:7`, `assignments.md:8`; `batch/SKILL.md:55` | Block forbids leaf delegation without exception; references allow it with an explicit grant | A5; V8 |
| F2 | blocking | `README.md:33-48`; `references/workflow-guide.md:20-35` | Skill catalog table duplicated; `check_instructions.py drafts/lusona` exits 1 | AC16; S3 |
| F3 | non-blocking | `references/revisions.md:3,5-8` | Trigger "follow-up request changes the objective" named by no skill or block (readme-032 unreachable) | S2, AC14 |
| F4 | non-blocking | `design/SKILL.md:36` | Failure mode "accepted choice reopened" has no exception for new input | P3 |
| F5 | non-blocking | `status/SKILL.md:31,77` | Saving exception not stated as an exception to the block's Saving line | Decision 19 |
| F6 | non-blocking | `batch/references/authority.md:35-40` | Unattended batch: no rule for new input contradicting an accepted decision | P3/P6 |
| F7 | non-blocking | `retention.md:51`=`delegation.md:71`; `queue.md:26`=`delegation.md:87`; Icebox exclusion, ceiling, 2 rounds defined 2-3 times in batch files | Duplicated policy | V8 |
| F8 | non-blocking | `closeout.md:3,34-37` | Trigger "after an enduring change" named by no skill | S2, AC14 |
| F9 | non-blocking | `files.md:3` | Legacy-record handling not linked from implement, refactor, review, investigate, architect, others | AC9, S2 |
| F10 | non-blocking | `architect/SKILL.md:72-76` | Updates a spec without linking `queue` | S2 |
| F11 | non-blocking | `batch/references/authority.md:3`, `deferral-and-resumption.md:3`, `repairs.md:3` | Triggers not named by `batch/SKILL.md` | S2, AC14 |
| F12 | non-blocking | `queue.md:54`; `experiment/SKILL.md:52`; `refactor/SKILL.md:60` | Unlinked reference mention; skill-to-skill dependencies | P-a, V8 |
| F13 | non-blocking | `shared/final-reply.md:1` | "Greetings are not task replies" (decision 16 Q5, readme-121) stated nowhere | Decision 16 |
| F14 | non-blocking | `final-reply.md:3-9` | No field for consequential decisions or unresolved issues (readme-144) | AC13 |
| F15 | non-blocking | `review/SKILL.md:70,75` | Report file vs reply content unclear | Executability |
| F16 | non-blocking | `design/SKILL.md:63,66` | Writes `visuals/<record-id>/` before the record supplying the ID exists | Executability |
| F17 | non-blocking | `completion.md:25,33` vs `retention.md:104,113` | Example moves to a new session at 42%; retention says checkpoint, no new session required | P7, V8 |
| F18 | non-blocking | `batch.md.template`, `review.md.template:6`; "writer(s)" 23 uses; "decision owner" | Mixed terms | V4 |
| F19 | non-blocking | `implement:21`, `refactor:49,70`, `review:74` | "can use", "can run" permissive statements | V1 |
| F20 | non-blocking | `readme-destinations.md:44,167,201-209` | 11 rows name merged files; map A overrides | AC13 |
| F21 | non-blocking | `naming.md:60` | Bare `../../scripts/work-record.*` path relative to a skill | ADR |
| F22 | non-blocking | `workflow-guide.md:3` | Trigger fires in every skill; only status and batch link it; no skill links the terminology table | V4, S2 |

Checked without finding: K1-K5; template headings vs `34186da`; TDD gate and commit authority; decisions 17-18 content.

Limits: sample audit; wording inside present rules not compared; host behavior not observed; package build,
link check, unit tests, helper tests and suite not run by this reviewer.

## Reviewer B: checks, packaging and suite code

Scope: new and changed `scripts/*`, `INSTALL.md`, `PRIVACY.md`, `evals/loop-conformance` changes, draft helpers.
Fixtures and probes: `tmp/w13b/` (git-ignored).

Counts: 3 blocking, 11 non-blocking. Tests: `unittest discover scripts` 167 OK; suite 150 OK; mutation probe
(stubbing each findings function or C12/C14-C17 function) turned 1-29 tests red each time. Live
`test-work-record.sh` exit 1 (pre-existing broken template link); draft copy passes. `pwsh` absent.

| ID | Sev | Location | Defect (fixture → result) | Violates |
| --- | --- | --- | --- | --- |
| B1 | blocking | `scripts/check_contract.py:50,105-116` | K4 authority check ignores negation: `tmp/w13b/f1` ("queue states authorize implementation") → exit 0 (coordinator reproduced) | AC7 |
| B2 | blocking | `scripts/check_contract.py:84-94` | K2 path removed from `files.md` still passes because other files name it: `tmp/w13b/f8` → exit 0 (coordinator reproduced) | AC5 |
| B3 | blocking | `scripts/check_instructions.py:112-123`; `drafts/lusona/README.md:33` | Catalog table duplicated → exit 1 (same as A-F2; coordinator reproduced) | AC16 |
| N1 | non-blocking | package build | Draft build fails on root-doc links (deferred to W14; W10 condition unmet until then) | AC16 |
| N2 | non-blocking | `scripts/check_skill_template.py:311` | Backticked bare `../../references/tdd.md` passes | ADR |
| N3 | non-blocking | `scripts/check_skill_template.py:277` | Any link counts as a trigger sentence | AC14 |
| N4 | non-blocking | `scripts/check_voice.py:98,122` | Link text and frontmatter description not scanned (documented exclusion; scope question) | AC3 |
| N5 | non-blocking | `scripts/check_contract.py:139,149` | Added early `exit 0` in helper tests not detected | AC6 |
| N6 | non-blocking | `scripts/check_contract.py:77` | `name: "implement"` (quoted) reported as K1 finding | AC4 |
| N7 | non-blocking | `scripts/check_rule_inventory.py:28` | Baseline `skills/batch/references/execution.md` not in the inventory (covered by the batch destination map, 141 sentences) | AC13 |
| N8 | non-blocking | `evals/loop-conformance/README.md:128` | Says pass marks not accepted | Decision 19 |
| N9 | non-blocking | live package | Ships `completion_reply.py`; manifests declare hooks (W14) | AC15 |
| N10 | non-blocking | `scripts/sync_shared.py:43` | End marker with trailing text accepted | AC12 |
| N11 | non-blocking | `scripts/check_contract.py:105` | Statuses found only in `completion.md` satisfy K4 (matches decision 12 scope, not AC7 wording) | AC7 |

Checked without finding: draft helpers differ only in template path; C1-C11 code unchanged; lock hashes match;
`pass-marks.json` is evaluator material; INSTALL/PRIVACY at baseline.

## Corrections and re-verification (decision 20)

Date: 2026-11-11. Corrections by two leaves (checks; draft content) and the coordinator (block line,
N8, sync). Re-verified by a third read-only leaf that wrote none of the corrections.

| ID | Disposition |
| --- | --- |
| F1 | Fixed: block Role line allows delegation under a grant; references use "delegation grant". Re-verified |
| F2 / B3 | Fixed provisionally: README skill table replaced by a link to `workflow-guide#skills`; README keep-or-drop open with the user. Re-verified |
| B1 | Fixed; re-verification bypasses b1a-b1h caught test-first. Limits in the docstring: affirmative across sentences, table cells, or a list without a ":" lead-in |
| B2 | Fixed; comment, fenced-code and negated-mention bypasses caught. Accepted limit: a queue state named only in prose counts (baseline queue.md has no Icebox row) |
| B3 bypass | Fixed: catalog detected by linked skill rows, any header |
| F3-F22 | Fixed (content leaf report); F7 residual pairs removed by the coordinator except `corrections.md:15` / `batch/SKILL.md:92` (the batch side links corrections) |
| N2-N7, N10, N11 | Fixed test-first. N11 makes the live plugin report 3 K4 findings instead of 2 (TDD levels now counted only in shared regions) |
| N8 | Fixed: suite README states pass marks accepted (decision 19) |
| N1, N9 | Deferred to W14 |
| Re-verification new | "grants" term, F14 wording and F6 duplicate fixed by the coordinator; nested-leaf shutdown assigned to the granting leaf (decision 21) |
