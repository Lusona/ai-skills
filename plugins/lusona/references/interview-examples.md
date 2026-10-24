# Interview examples

Optional illustrations for a specific interviewing difficulty. Read only the relevant
section; these are not required scripts or a question sequence. The
[intent interview contract](interviews.md) governs questions, corrections,
and user authority; examples grant no permission to save documents or implement.

- [Future experience](#explore-develop-the-future-experience): move beyond a proposed feature.
- [Ambition and initial scope](#product-preserve-ambition-while-defining-initial-scope): retain the product's long view.
- [Next delivery](#capabilities-connect-the-next-delivery-to-the-vision): connect priorities to the vision.
- [Context reuse](#reuse-context-avoid-restarting-discovery): build on settled answers.
- [Correction](#correction-revise-the-interpretation): revise an incorrect interpretation.

## Explore: develop the future experience

**User:** I want to add a dashboard for team managers.

**Assistant:** What should managers be able to understand or decide that they struggle
with today?

**User:** They discover delays too late and spend meetings collecting updates.

**Assistant:** Is the longer-term ambition to help managers detect delays sooner, or to
let teams coordinate without managers collecting updates? Both could matter; which change
is more important to you?

**User:** Teams should coordinate themselves. Managers should handle exceptions.

**Assistant:** That suggests the dashboard should make unresolved exceptions visible.
It might eventually need fewer routine status details as teams gain better coordination
tools. Can you describe a situation the team should handle independently, and one that
should reach a manager?

*Why this works:* The interview moves from a proposed feature to a desired future, then
uses a concrete scenario to clarify the distinction. The interpretation remains provisional.

## Product: preserve ambition while defining initial scope

**User:** We want to make it easier for independent tutors to run their businesses.
Scheduling is the first problem.

**Assistant:** When the product has matured, what should a tutor's working day look like?

**User:** They should spend their time teaching. Scheduling, payments, and follow-ups
should mostly happen automatically.

**Assistant:** The intended future is a business that requires less routine administration.
Scheduling is the initial scope; payments and follow-ups remain part of the ambition.
What should tutors always control themselves, even if we could automate it?

**User:** Prices and communication with parents. We can draft messages, but tutors should
approve them.

**Assistant:** Then tutor control over pricing and parent communication is a product
principle. The scheduling scope should respect that principle, and future automation should
preserve it. Have I captured the distinction correctly?

*Why this works:* The first delivery does not become the entire product definition.
The interview establishes a principle that can guide later decisions and offers a correction
opportunity without requiring repeated approval of established answers.

## Capabilities: connect the next delivery to the vision

**User:** Let's build tutor booking first. Payments can wait.

**Assistant:** Booking can deliver value before payments. For the longer-term experience,
should a parent book individual lessons, or establish an ongoing arrangement with a tutor?

**User:** Mostly ongoing weekly lessons, with occasional changes.

**Assistant:** Recurring arrangements therefore belong in the capability map. A first
delivery could support one-off bookings to test demand, or weekly bookings to test the
main workflow. Weekly bookings would also require rules for cancellations and exceptions.
Which uncertainty matters more right now?

**User:** Whether tutors and parents can manage a weekly schedule without messaging back
and forth.

**Assistant:** Then I recommend weekly bookings with a simple cancellation and rescheduling
flow as the first outcome. Payments remain deferred. The first delivery tests the coordination
problem central to your vision.

*Why this works:* The recommendation follows the user's learning priority and long-term
workflow, rather than implementation convenience. A proposed first outcome is not a detailed
specification or permission to execute it.

## Reuse context: avoid restarting discovery

**User:** We already agreed on the tutor vision. Can we move payment reminders ahead of
payment collection?

**Assistant:** Yes. Reminders could use payment status entered by the tutor, with automated
collection added later. That would reduce follow-up work but retain manual bookkeeping.
Is that tradeoff acceptable for the next delivery?

**User:** Yes, provided reminders are drafts the tutor approves.

**Assistant:** That also preserves the established communication principle. The revised
proposed order is payment tracking and reminder drafts, followed later by automated collection.

*Why this works:* The model answers the question, uses established intent, and asks only
about the new tradeoff. Once the requested sequencing question is resolved, it stops.

## Correction: revise the interpretation

**User:** I want tutors to spend less time on administration.

**Assistant:** Should the mature product handle routine parent communication automatically?

**User:** No. Personal contact is part of the service. I want tutors to prepare for those
conversations faster, not send fewer messages.

**Assistant:** I interpreted less administration as less direct communication. Your goal is
to reduce preparation work while preserving personal contact. What does a tutor currently
have to gather before speaking with a parent?

**User:** Notes from previous lessons and whether the student did the practice work.

**Assistant:** Then a useful capability to explore is preparing that information for the
tutor before the conversation. Automatic messaging does not follow from the goal you described.

*Why this works:* The correction changes both the next question and the proposed capability.
The model does not retain its earlier interpretation as an accepted requirement.
