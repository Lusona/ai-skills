# Evidence-aware workflow evaluations

For the background behind this workflow, read [When the workflow became another job](../../docs/articles/why.md).

Six synthetic cases cover AC1–AC5 and negative boundaries from the approved
[spec](../../docs/lusona/specs/20261025-evidence-aware-workflow-and-behavioral-evaluation.md).
They are evaluation assets outside distributed plugin packages. scenarios.json contains
raw fixtures and exact sequential user turns; rubric.md is only for independent graders.
suite.lock.json freezes their hashes. Never provide the rubric or prior outcomes to actors.

The small runner captures one turn at a time with Codex CLI, loading a frozen local skill
by explicit path. This exercises local skill behavior, not native plugin installation or
Claude's --plugin-dir. Claude 2.1.310 was available but unauthenticated at setup; Codex
0.164.0 with gpt-6.1-sol and medium effort was connectivity-tested by the coordinator.
Codex uses the normal workspace-write sandbox, explicit multi_agent availability, no
approval bypass, and persisted sessions for true multi-turn resume. No installed skill,
user configuration, or external app is changed. Authentication/session storage remains
host-managed. Ambient host instructions and managed restrictions are a comparison limit.

From repository root, freeze baseline before changing canonical behavior:

```sh
python3 -m unittest discover -s evals/evidence-aware -p 'test_*.py'
python3 evals/evidence-aware/run.py freeze --plugin plugins/lusona --out tmp/evidence-aware-eval/conditions/baseline --model gpt-6.1-sol --effort medium --timeout 600
python3 evals/evidence-aware/run.py prepare --condition tmp/evidence-aware-eval/conditions/baseline --scenario revision --trial 1 --out tmp/evidence-aware-eval/runs/baseline/revision/1
python3 evals/evidence-aware/run.py turn --run tmp/evidence-aware-eval/runs/baseline/revision/1
```

Run `turn` again only after inspecting the captured turn; revision and interview have three
frozen turns in one session. All other cases have one. Repeat prepare/turn for trial 2 and 3
in fresh output paths and the selected scenarios: revision, discovery, read-only, simple,
interview, batch-refutation. Never use --ephemeral or --last to resume. The runner selects
the saved thread ID explicitly. A failed/inconclusive capture is retained and blocks that
run from silently advancing. If setup must change, preserve the failed run and have the
coordinator record the changed prerequisite and budget decision before any new attempt.

Each condition captures the model, effort, permissions, plugin file hashes, frozen suite
hashes, and timeout; each turn retains exact input/command, CLI version, JSONL transcript,
stderr, time, available usage, session IDs, before/after hashes, and resulting fixture files.
Runner hashes and the loaded runner source are saved with new turns. CLI usage describes
the root process and does not establish total worker cost.
`captured` means CLI capture completed; it does not mean a scenario passed. Independently
grade conversation AND actions/artifacts using rubric.md. Save grades and any dissent
beside the run as grade.json or grade.md, outside workspace. No grading automation is claimed.

Codex CLI JSONL can omit collaboration calls. New captures therefore also save a filtered
rollout supplement, located only by the returned session UUID under the host's sessions
directory. It retains actual function/custom tool calls and outputs, assistant messages,
worker activity and turn boundaries. System/developer content, host session/settings/rate
metadata, and user messages containing host injections are excluded; exact user prompts
remain in the input files. Some hosts encrypt collaboration message arguments in rollout
storage; the supplement preserves them as stored and cannot recover their plaintext.

Backfill an already captured turn without changing any original evidence:

```sh
python3 evals/evidence-aware/run.py supplement --run tmp/evidence-aware-eval/runs/baseline/revision/1 --turn 1
```

Each supplement is a new immutable trace/metadata pair. It is explicitly a cumulative
session capture made now and may include later resumed turns; it is never presented as
the earlier turn's original snapshot. Metadata reports capture time, source locator/bytes,
filtered-trace hash, actual tool-call counts, and distinct worker-thread IDs when supported.
Missing rollout/worker evidence remains unavailable rather than becoming zero workers or
proof of absent delegation. No unrelated session contents or authentication files are read.
Malformed, partial, or wrong-shaped rollout lines produce an incomplete supplement with
a diagnostic and the valid partial trace; they do not abort the captured actor result.

The timeout is 600 seconds per turn in the commands above: enough to permit required
delegation without an unbounded trial. The runner waits for one bounded CLI process; the
coordinator can run it through the host's yielding command session and continue updates.
No network use, dependency installation, commits, or implementation beyond fixture scope
is requested. Actor reads are limited by instruction to workspace and frozen plugin;
the OS sandbox governs writes, while read isolation from evaluator files is not an OS
security boundary. Any actor inspection of rubrics or another trial invalidates that trial.

Freeze candidate from the changed plugin into a new condition directory with identical
model/effort/timeout. For experiments copy the SAME reference plugin into separate local
directories under tmp, change only delegation or mandatory-context policy, then freeze each.
Do not change canonical defaults. Use simple+discovery for delegation, simple+batch-refutation
for context, three trials each. Review independent quality/boundaries before overhead;
retain/change/inconclusive is a valid result. Required independent review remains enabled.
See rubric.md for adjudication and reporting. Do not expand probes or retry to chase success.

Next action: coordinator freezes baseline, runs three trials per case, and dispatches
independent grading. Only actual behavioral failures are red evidence. Setup errors are not.
