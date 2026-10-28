# Instruction footprint reduction

Completed the user's authorized cleanup of mandatory core and delegated-agent instructions.
The baseline is the canonical working tree immediately before this cleanup, including the
previously implemented proportionate-evidence change—not its larger first prototype.

| Required source path | Before | After | Reduction |
| --- | ---: | ---: | ---: |
| Whole core file | 2,551 | 1,585 | 37.9% |
| Ordinary implementation coordinator | 5,204 | 3,764 | 27.7% |
| Ordinary implementation leaf | 3,927 | 2,641 | 32.7% |
| Correction-active coordinator | 5,204 | 4,036 | 22.4% |
| Correction-active leaf | 3,927 | 2,913 | 25.8% |
| Commit-active coordinator | 5,908 | 4,468 | 24.4% |
| All plugin Markdown | 25,076 | 24,070 | 4.0% |

Counts are whitespace-delimited words. Role paths include the implementation skill, TDD,
applicable delegation sections, and coordinator routing/lifecycle procedures. The active paths
include the moved correction procedure or full commit procedure. The net whole-plugin reduction
is 1,006 words: core −966, delegation −312, new conditional correction reference +272.
These are mandatory ordinary-path floors, not complete task-context totals or measured tokens.
Case-dependent domain, record, template, queue and discovery loads are additional. Eager full-file
host loading may reduce section-loading savings; the whole core itself also shrank substantially.

The core and delegation instructions are condensed with retained owners and triggers for their
obligations. Correction limits moved verbatim into an explicitly required procedure for observed
failure work. Commit mechanics remain in the existing procedure, required before commit/integration.
Leaf questions and shared-record changes still route through the coordinator. Required checks,
review, authority, explicit TDD, correction counters, status meaning and next actions are preserved.

## Verification

One fresh baseline actor and one candidate actor, both `gpt-6.1-sol` with medium reasoning,
answered the same frozen four-case read-only decision exercise. Neither received the evaluator
rubric, expected answers, prior response, or implementation conclusions. An independent reviewer
graded the actual returned decisions: **4/4 pass in both conditions**. Cases cover correction
limits, leaf scope/TDD, check reuse versus review/capacity, and read-only continuation/handoff.
Passing characterization was preserved; no failing-then-passing behavior is claimed.

Independent source review found no actionable defects and confirmed the loading-path arithmetic
and conditional reachability. Final package/resource checks, native manifest/catalog validation,
whitespace, preserved headings and 31 inbound anchor links pass. Final canonical sources match
the frozen candidate. The native validator's informational installation-line advice remains.

- [Independent review](review.md) and [grades](review.json)
- [Exact source diff](implementation.patch) and [counts](comparison.json)
- [Frozen sources, tasks, responses, measurement code and check evidence](evidence.zip)
- [Archive and member hashes](manifest.json)

The archive retains the original `instruction-footprint-20261027/` layout. Generated package
outputs, Git internals and bytecode caches are excluded. Actual actor responses were recorded by
the coordinator with minimal Markdown whitespace normalization; their decisions—not claims of
having executed scenarios—were graded. No broad benchmark or external CLI trial was run.

These checks establish bounded source/decision preservation, not live permission enforcement,
automatic host-loading behavior, latency, cost, installation or universal agent reliability.
No commit or publication occurred. The implementation and independent review are complete;
repository-local scratch remains available, with no active worker operations or children.
