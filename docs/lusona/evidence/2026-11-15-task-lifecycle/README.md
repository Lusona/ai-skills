# Task lifecycle evidence

Owning record: [spec](../../specs/20261115-reconcile-task-lifecycle.md).

- `baseline.tar.gz`: plugin and shared sources captured before lifecycle edits, including the prior uncommitted language pass. SHA-256: `7ee7e324329f1cc608f5cddbf1d4d2e7f9100208339b91798b4a8a3d7e6ab43b`.
- `trial-preparation.tar.gz`: frozen baseline/candidate plugin copies, per-file hashes, matched R/I/B prompts, grading criteria, and scratch-only controlled-task launcher. Extract under repository `tmp/` to restore `tmp/lifecycle-trials/`.
- No trials executed. Resource decision pending: six calls, 600 seconds each, 3600 seconds total, $10 total proposed; observed configured model `opus`, effort `xhigh`, Claude Code 2.1.325. Per-call CLI cap $1.60 is not a guaranteed billing bound. Do not execute without the pending decision.
- Prepared trials use controlled task-state fixtures, with actual fixture-owned processes for background and retained/sentinel cases. They do not establish native Claude team shutdown. Actor state observations precede harness cleanup; harness cleanup cannot count as actor compliance.
- Repository evaluator C18 consumes independent evidence classifications; it does not automatically collect native lifecycle state. Missing observations remain inconclusive.

Static checks, test counts, review findings and remaining acceptance are in the spec. No behavior improvement claim is made.
