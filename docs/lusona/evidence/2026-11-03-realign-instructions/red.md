# Red run before instruction edits, 2026-11-03, HEAD 545b6e0

```
$ python3 -m unittest scripts.test_instructions
FAIL: test_skills_do_not_restate_core_clauses (scripts.test_instructions.InstructionTests.test_skills_do_not_restate_core_clauses)
AssertionError: Lists differ: [(PosixPath('skills/architect/SKILL.md'), [1950 chars]ol')] != []
FAIL: test_workflow_guide_owns_catalog_and_routing_tables (scripts.test_instructions.InstructionTests.test_workflow_guide_owns_catalog_and_routing_tables)
AssertionError: Lists differ: ['routing table missing from references/wo[66 chars].md'] != []
Ran 8 tests in 0.047s
FAILED (failures=2)

$ python3 scripts/check_instructions.py
restated: skills/architect/SKILL.md:69: "permitted native question tool"
restated: skills/architect/SKILL.md:73: "without a separate save request"
restated: skills/batch/SKILL.md:13: "does not authorize"
restated: skills/batch/SKILL.md:24: "permitted native question tool"
restated: skills/design/SKILL.md:18: "permitted native question tool"
restated: skills/design/SKILL.md:56: "does not authorize"
restated: skills/experiment/SKILL.md:3: "does not authorize"
restated: skills/experiment/SKILL.md:30: "does not authorize"
restated: skills/experiment/SKILL.md:42: "without a separate save request"
restated: skills/explore/SKILL.md:55: "without a separate save request"
restated: skills/frame-product/SKILL.md:36: "does not authorize"
restated: skills/frame-product/SKILL.md:47: "does not authorize"
restated: skills/implement/SKILL.md:3: "do not authorize"
restated: skills/implement/SKILL.md:15: "without a separate save request"
restated: skills/implement/SKILL.md:23: "does not authorize"
restated: skills/implement/SKILL.md:58: "do not authorize"
restated: skills/implement/SKILL.md:96: "does not authorize"
restated: skills/investigate/SKILL.md:42: "without a separate save request"
restated: skills/map-capabilities/SKILL.md:47: "does not authorize"
restated: skills/map-capabilities/SKILL.md:54: "does not authorize"
restated: skills/measure/SKILL.md:15: "does not authorize"
restated: skills/measure/SKILL.md:40: "without a separate save request"
restated: skills/refactor/SKILL.md:15: "without a separate save request"
restated: skills/refactor/SKILL.md:33: "permitted native question tool"
restated: skills/review/SKILL.md:60: "permitted question tool"
restated: skills/specify/SKILL.md:35: "without a separate save request"
restated: skills/specify/SKILL.md:43: "permitted native question tool"
tables: routing table missing from references/workflow-guide.md
tables: routing table duplicated in skills/status/SKILL.md
29 finding(s).
```
