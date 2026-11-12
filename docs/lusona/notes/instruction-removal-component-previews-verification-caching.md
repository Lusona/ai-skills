# Notes: instruction-removal-component-previews-verification-caching

## 2026-11-08 — Baseline and unresolved scope

### Question and scope

User invoked `lusona:investigate` with “Instruction removal, component previews,
verification caching.” Investigation is authorized; implementation is not requested
and TDD is unset. No matching owner was found in the open work queue or searched
notes/specs. The intended problem or proposed behavior for each topic is unknown.

### Evidence

Source inspection at revision `a7097284f9a5d35c3e4d31849bc1b9a644c932bf`, initially
clean working tree. Loaded workflow instructions came from installed Lusona 2.0.2;
the investigated canonical repository sources identify version 2.0.3.

- [Loading rules](../../../plugins/lusona/README.md#loading-rules) accept supplied
  or demonstrably inherited text and reuse unchanged instructions; missing or
  changed instructions are loaded when role, operation, or source changes.
  Commit `a709728` clarifies responsibility-based roles and worker-lifecycle loading.
  This does not establish what the user means by instruction removal.
- [Visual presentation](../../../plugins/lusona/references/visuals.md#presentation)
  and [design](../../../plugins/lusona/skills/design/SKILL.md) prescribe self-contained
  HTML mockups based on the bundled template, opened in a browser. The inspected
  procedures do not explicitly prescribe rendering actual repository components.
- [TDD and verification](../../../plugins/lusona/references/tdd.md) already require
  reusing valid checks on unchanged inputs. [Delegation](../../../plugins/lusona/references/delegation.md#evaluate-and-reconcile-results)
  names changed inputs, failures, missing/unreliable evidence, and unresolved risks
  as rerun reasons. These are evidence-reuse instructions, not an executable cache.
- Commit `ec9b2c5` strengthens check-result interpretation, preservation of reusable
  setup steps, telemetry-coverage reasoning, and review of removed obligations.

Method: inspected relevant source files and the two commits; searched canonical
plugin sources, scripts, evaluation sources, and project records for removal,
preview, component, cache, and verification terms. A delegated diagnostic worker
returned the same baseline; the coordinator checked the cited core, visual,
verification, and delegation rules directly. No reproduction, tests, installation,
or browser/interactive behavior was run. Source inspection cannot establish agent
compliance or the cause of an unspecified observed failure.

### Conclusion

No defect is confirmed. Possible meanings remain hypotheses: deleting instruction
text versus reducing loading; standalone mockups versus real-component previews;
following current evidence-reuse rules versus adding automated caching. No one
interpretation has been selected. No production changes or new queue proposals
are justified by the title alone.

## Current handoff

- Authorized work: bounded investigation of the three named topics; no implementation.
- Missing input: observed problem or proposed behavior for each topic, with an
  affected workflow and concrete example. A native question was submitted.
- Next action: user clarifies scope; coordinator assigns the smallest diagnostic
  probe for a clarified behavior, preserving existing investigation authorization.
- Worker: `diagnose_topics` returned a completed read-only assignment; no active
  operations or write ownership. Host exposes no shutdown/close control, so worker
  closure is not claimed.
