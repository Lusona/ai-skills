# explore

**✅ Complete — Result:** I recommend invitation links provisionally, because occasional volunteers and shared household inboxes make a strict email match a questionable basis for low-support onboarding. This is a recommendation, not an accepted decision.

I interpret “email-only” as requiring acceptance through the invited email address.

| Option | Benefit | Tradeoff |
| --- | --- | --- |
| Invitation links | Coordinators can use the communication channel the volunteer already uses, without requiring a particular email match. | A forwarded link may allow the wrong person to accept; the consequence depends on what acceptance grants. |
| Email-only invitations | Requires access to the invited inbox, restricting forwarding outside it. | A shared inbox still cannot identify an individual household member. Address mismatches, delivery problems, and email changes may need coordinator assistance. |

Keep each volunteer's identity distinct from their email address whichever option you choose. The long-term goal is returning volunteers who can use their own accounts without coordinators repeatedly resolving household email ownership.

**Evidence:** Your context supports this preference, but the support costs and forwarding harms have not been measured. If accepting a link immediately grants sensitive access, that could change the recommendation. I used only the supplied notes; no external research or operational checks were performed. I saved the comparison and open questions in [the existing invitation notes](explore/docs/lusona/notes/invitations.md).

| Proposed next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Review up to ten existing onboarding support cases for wrong-person acceptance and email-related assistance, to test the support assumption. | Portal coordinator | Access to existing cases | Bounded review requires authorization; no implementation is proposed here. |

# finished

Yes. A one-use invitation controls account creation or admission; the account then has its own sign-in lifecycle. Invitation expiry prevents later use of the invitation. It does not itself close an account already created through it, unless a separate rule explicitly connects those events.

**Next action:** None for this request; that distinction answers the conceptual question.

# status

**✅ Complete — Result:** The supplied notes record a completed diagnosis. The fix remains unauthorized, and no TDD policy has been selected.

**Evidence:** [The invitation issue notes](status/docs/lusona/notes/invitation-issue.md) report a local reproduction: expiry is compared with `created_at` rather than the current time, allowing expired invitations to work. I read that record; I did not reproduce the issue or inspect implementation code.

| Outcome | State | Remaining work |
| --- | --- | --- |
| Reject expired invitations while preserving accepted accounts | Diagnosed; fix unauthorized; TDD unset. No queue or execution record supplied. | Authorize the bounded fix and select TDD, then implement and verify both expiry rejection and preservation of accepted accounts. |

| Proposed next action | Owner | Needs | Authority |
| --- | --- | --- | --- |
| Authorize the bounded invitation-expiry fix and select `none`, `targeted`, or `strict` TDD; I recommend `targeted` coverage of the expiry boundary and existing accounts. | Project owner | Intended expiry boundary and TDD choice | Decision and implementation authority are missing; this assessment remains read-only. |

# Action log

Paths below are relative to `tmp/natural-next-action/`. Capture output in `candidate/responses.md` is separate from project records.

## Shared loading

- Ran `cat tasks.json` using its repository-relative path to read the three requests.
- Ran separate `cat` commands for `candidate/plugin/skills/explore/SKILL.md`, `candidate/plugin/skills/status/SKILL.md`, and `candidate/plugin/README.md`.
- Ran one `cat` command for the plugin's `references/interviews.md`, `references/retention.md`, and `templates/brainstorm.md`.
- Ran one `cat` command for the plugin's `references/workflow-guide.md`, `references/queue.md`, `references/files.md`, and `templates/status.md`.
- Ran one `cat` command for the plugin's `references/retention.md` and `references/evidence.md`, one for `references/delegation.md`, and one for `templates/brainstorm.md` to obtain their complete contents after combined output was truncated.
- Ran `rg --files` against `candidate/explore`, `candidate/finished`, and `candidate/status`. It listed the two project notes below.

## explore

- Read `candidate/explore/docs/lusona/notes/invitations.md` in a combined `cat` command with the status case note.
- Applied the supplied explore skill, core, interviews, retention, brainstorm template, and evidence study-entry rules. Delegation and external research were unavailable under the assignment.
- Used `apply_patch` to update the existing invitation notes with the comparison, provisional recommendation, uncertainty, and proposed bounded review.
- Ran a final `cat` of the updated invitation notes and inspected the saved text.
- Used `apply_patch` to capture the final response and this log in `candidate/responses.md`.

## finished

- Applied the same supplied explore skill and shared resources. File inventory found no project records in `candidate/finished`.
- Created no project record: this was an ordinary conceptual explanation and requested no project decision or design.
- Used `apply_patch` to capture the final response and this log in `candidate/responses.md`.

## status

- Read `candidate/status/docs/lusona/notes/invitation-issue.md` in the combined `cat` command with the exploration note.
- Applied the supplied status skill, core, workflow routing, queue rules, file compatibility rules, and status template.
- Wrote no files under `candidate/status`; the case was read-only.
- Used `apply_patch` to capture the final response and this log in `candidate/responses.md`.

Ran a final `cat` of `candidate/responses.md` and inspected all three captured responses and their action logs. No code implementation, tests, external services, commits, or child agents were used.
