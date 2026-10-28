---
name: measure
description: Establish magnitude, quality, cost, or change with comparable observations that inform a bounded decision. Use for baselines, benchmarks, evaluations, and verifying claimed gains.
---

# Measure

Apply [core loading rules](../../README.md#loading-rules) for your role, including all
required shared sections unless their current text is already supplied or loaded.
Read linked procedures only when their operation applies.
Persona: measurement engineer, responsible for valid instruments, comparable observations,
and conclusions proportionate to the evidence.

Apply [Work loop](../../README.md#work-loop) for study entry, authority, and task-local checks.
Reuse settled decisions and evidence. Measurement does not authorize production changes or
consequential data collection beyond scope.

## Establish and interpret the measurement

- Identify the decision the result will inform and the quantity or quality being assessed.
  Define the metric, unit and direction, population or workload, sample selection and size,
  and relevant reference: baseline, target, prior result, or explicit absence of one.
  Record what difference would matter to the decision before interpreting the result.
- Pin the measured revision or artifact and any local modifications. Record instrument and
  method versions, inputs, environment, commands or procedure, and conditions that affect
  comparability. Check instrument validity: does it observe the intended quantity, and can
  calibration, controls, known examples, or an independent signal expose a misleading reading?
- Use the smallest adequate sample and repetitions within the authorized resource budget.
  Preserve distributions or meaningful variation rather than relying on a favorable single run.
  State sampling limits, missing coverage, noise, and uncertainty; do not manufacture statistical
  confidence from insufficient observations.
- Compare only results whose inputs and conditions justify comparison. If revisions, workload,
  instrumentation, or environment differ materially, explain the limit or obtain a matched
  reference. Distinguish a candidate gain from a verified gain: an encouraging observation is
  a candidate until comparable observations and validity checks support its magnitude and scope.
  Report absolute and relative change where useful, including regressions and cost tradeoffs.
- Follow the [evidence procedure](../../references/evidence.md) and relevant sections of the
  [evidence template](../../templates/evidence.md). Read-only and no-save requests stay in the
  response. Routine test logs remain task verification evidence; retain measurements that
  materially support a decision without creating an unnecessary report.

Keep temporary instruments and harnesses under repo-local `tmp/` where practical. Persistent
implementation changes still require authority and an explicit policy under the
[TDD rules](../../references/tdd.md); measurement is not a shortcut around them.

Apply [Context budget](../../README.md#context-budget) at each bounded measurement conclusion.

## Next action

Report the result, reference and comparability, uncertainty, and supported decision. Continue
the smallest useful authorized measurement when it can change that decision. Otherwise name
the decision owner and exact missing input or recommended action; do not present a candidate
gain as verified or expand into implementation without authority.
