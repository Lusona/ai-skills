# Intent interviews

Read before asking the user about intent, priorities or acceptable tradeoffs that are unclear.

## Ownership

- The coordinator owns the conversation with the user.
- As a leaf, return focused questions, and the decision each one affects, before writing a synthesis that depends on the answers. Then use the answers the coordinator supplies.
- Meanwhile, continue gathering evidence that does not depend on the answers.
- In an unattended batch, reuse settled intent and defer consequential gaps.

## Asking

- Ask through the host's native question tool when it is permitted for the current mode: `AskUserQuestion` in Claude Code, or an exposed `request_user_input` or `request_user_input_async` tool. Otherwise ask in plain text.
- Do not switch modes to ask.
- Do not treat silence or a preselected option as consent. Follow the host's approval rules.

## Interviewing

- Start from the supplied intent and established decisions.
- Investigate discoverable facts using available evidence. Ask the user about desired outcomes, priorities, experience and tradeoffs.
- Do not infer what the user wants or understands from repository behavior.
- Ask 1 focused question, or a group of at most 3 related questions. Order them by dependency and by the previous answers.
- Explain choices with concrete scenarios. Ask the user to react to each scenario.
- Adapt explanations and experiments to the understanding the user has shown. Do not change a decision, or what the evidence shows, to do so.
- Do not use a fixed questionnaire. Do not ask questions only to fill record fields.
- Ask about the intended long-term experience. Distinguish aspirations, initial scope, deferred capabilities and commitments.
- Reuse the existing vision. Keep your questions within the requested scope.
- State each consequential interpretation to the user and ask for correction before settling the output.
- When corrected, revise the questions and proposals.
- Distinguish evidence, assumptions, proposals and decisions.
- Reuse earlier answers. Answer direct questions first.
- Stop when further answers would not change the outcome, or when the user asks to move on.
- Label the remaining assumptions. An unresolved blocking decision stays blocking.
- Do not draft a document in place of asking an open intent question.

## Examples

Read only the example that matches a concrete difficulty with interview technique. The examples are not scripts or a required question order. They grant no permission to save documents or implement.

| Example | Difficulty |
| --- | --- |
| Future experience | Establish the future a proposed feature serves |
| Ambition and initial scope | Separate the long-term ambition from the initial scope |
| Next delivery | Connect priorities to the vision |
| Context reuse | Reuse settled answers |
| Correction | Revise an incorrect interpretation |

### Future experience

> **User:** I want to add a dashboard for team managers.
> **Assistant:** What should managers be able to understand or decide that they struggle with today?
> **User:** They discover delays too late and spend meetings collecting updates.
> **Assistant:** Is the longer-term ambition to help managers detect delays sooner, or to let teams coordinate without managers collecting updates? Both could matter; which change is more important to you?
> **User:** Teams should coordinate themselves. Managers should handle exceptions.
> **Assistant:** That suggests the dashboard should make unresolved exceptions visible. It might eventually need fewer routine status details as teams gain better coordination tools. Can you describe a situation the team should handle independently, and one that should reach a manager?

Technique: ask what future the proposed feature serves. Use a concrete scenario to clarify the distinction. Keep the interpretation provisional.

### Ambition and initial scope

> **User:** We want to make it easier for independent tutors to run their businesses. Scheduling is the first problem.
> **Assistant:** When the product has matured, what should a tutor's working day look like?
> **User:** They should spend their time teaching. Scheduling, payments, and follow-ups should mostly happen automatically.
> **Assistant:** The intended future is a business that requires less routine administration. Scheduling is the initial scope; payments and follow-ups remain part of the ambition. What should tutors always control themselves, even if we could automate it?
> **User:** Prices and communication with parents. We can draft messages, but tutors should approve them.
> **Assistant:** Then tutor control over pricing and parent communication is a product principle. The scheduling scope should respect that principle, and future automation should preserve it. Have I captured the distinction correctly?

Technique: do not define the whole product from the first delivery. Establish a principle that guides later decisions. Offer correction without asking the user to approve settled answers again.

### Next delivery

> **User:** Let's build tutor booking first. Payments can wait.
> **Assistant:** Booking can deliver value before payments. For the longer-term experience, should a parent book individual lessons, or establish an ongoing arrangement with a tutor?
> **User:** Mostly ongoing weekly lessons, with occasional changes.
> **Assistant:** Recurring arrangements therefore belong in the capability map. A first delivery could support one-off bookings to test demand, or weekly bookings to test the main workflow. Weekly bookings would also require rules for cancellations and exceptions. Which uncertainty matters more right now?
> **User:** Whether tutors and parents can manage a weekly schedule without messaging back and forth.
> **Assistant:** Then I recommend weekly bookings with a simple cancellation and rescheduling flow as the first outcome. Payments remain deferred. The first delivery tests the coordination problem central to your vision.

Technique: base the recommendation on the user's learning priority and long-term workflow, not on implementation convenience. A proposed first outcome is not a specification or permission to execute it.

### Context reuse

> **User:** We already agreed on the tutor vision. Can we move payment reminders ahead of payment collection?
> **Assistant:** Yes. Reminders could use payment status entered by the tutor, with automated collection added later. That would reduce follow-up work but retain manual bookkeeping. Is that tradeoff acceptable for the next delivery?
> **User:** Yes, provided reminders are drafts the tutor approves.
> **Assistant:** That also preserves the established communication principle. The revised proposed order is payment tracking and reminder drafts, followed later by automated collection.

Technique: answer the question, use the established intent, and ask only about the new tradeoff. Stop once the requested question is resolved.

### Correction

> **User:** I want tutors to spend less time on administration.
> **Assistant:** Should the mature product handle routine parent communication automatically?
> **User:** No. Personal contact is part of the service. I want tutors to prepare for those conversations faster, not send fewer messages.
> **Assistant:** I interpreted less administration as less direct communication. Your goal is to reduce preparation work while preserving personal contact. What does a tutor currently have to gather before speaking with a parent?
> **User:** Notes from previous lessons and whether the student did the practice work.
> **Assistant:** Then a capability to explore is preparing that information for the tutor before the conversation. Automatic messaging does not follow from the goal you described.

Technique: after a correction, revise both the next question and the proposed capability. Do not keep the earlier interpretation as an accepted requirement.
