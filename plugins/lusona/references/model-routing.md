# Model routing

Coordinators read before dispatching an assignment.

Before every dispatch, select the least capable available model adequate for the assignment
and a supported reasoning setting. This is explicit routing guidance for model and reasoning
overrides, subject to user choices and host restrictions. Consider uncertainty, coupling,
failure consequences, and verification strength; file count alone does not establish complexity.

| Tier | Choose when |
| --- | --- |
| `fast` | Instructions are clear, scope is isolated, and checks can establish correctness |
| `standard` | Work requires implementation judgment within established boundaries |
| `deep` | Work involves substantial uncertainty, interacting invariants, or consequential failure |

Tiers describe the worker's model capability. The `fast` tier is unrelated to a host's fast
mode, which keeps the same model and changes output speed and cost.

Use the consuming project's instructions to map tiers to available models and supported
reasoning settings. Without a mapping, select from the host's exposed models and supported
settings using their capability descriptions. Pass the selected model and reasoning setting
explicitly through the host's dispatch controls; a tier label in the assignment does not select
a model. Do not invent identifiers or assume unsupported controls. Preserve explicit user
model choices and host restrictions. For each setting, inherit when those constraints require
it or its selection control is unavailable; still select other independently supported settings.
Report when this prevents the selected routing. Selecting the
current model remains valid when it is adequate and no less capable available model suffices.
Routing selects the worker's model; it does not change the coordinator's model.

Choose a context mode compatible with the selected model and reasoning setting. When the
host prohibits overrides with full-history forks, supply a bounded assignment with the needed
instructions and inputs instead. For hosts exposing `fork_turns` with that restriction, use
`"none"` or a supported positive turn count; omitted or `"all"` inherits the parent's model
and reasoning settings. Do not silently drop a selected override to retain full history.

Record routing in the owning change or batch record only when it affects execution; reassess
at dispatch and escalation rather than requiring a tier and rationale for every planned task.
Tiers never reduce required verification or expand scope. Keep useful parallel assignments
independent and retain the coordinator's integration and verification responsibilities.
