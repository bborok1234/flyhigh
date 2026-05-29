# GitHub Operations

Flyhigh treats GitHub as an operator-facing collaboration surface, not a blind publishing target.

## State Model

```text
state/github/operations.jsonl
state/github/repositories.json
state/github/sync-log.jsonl
state/github/outbox/
```

Each operation is an issue or PR proposal with:

- why it exists;
- body content;
- labels;
- linked Flyhigh work items;
- evidence;
- approval status;
- publish status.
- repository mapping and publish readiness.

## Lifecycle

```text
needs_approval -> approved -> prepared -> published
                         \-> blocked
```

External writes require both:

- an operation in `approved` or `prepared` state;
- a mapped repository with `publish_ready=true`;
- a scoped `publish_issue` operator response applied into the operation;
- `FLYHIGH_GITHUB_EXECUTE=1` and `scripts/publish-github-operation --execute`.

The default publish path is dry-run only.

Approval is scoped. Approval for proposal, outbox preparation, or dry-run does not imply publish approval.

Merges use a separate governance path:

- `state/reviews/direction-reviews.jsonl` records whether to continue, split, close, defer, or create work.
- `state/github/merge-gates.jsonl` records PR readiness, validation, risk, blockers, and merge decision.
- `scripts/merge-approved-pr` merges only after `scripts/evaluate-merge-gate` passes.

## Commands

```bash
scripts/propose-github-operation
scripts/approve-github-operation GH-001 --approved-by <name>
scripts/prepare-github-outbox --id GH-001
scripts/publish-github-operation GH-001 --repo /path/to/repo
scripts/decide OD-001 approve publish_issue --operator <name>
scripts/apply-operator-decisions
scripts/list-github-operations
scripts/list-github-repositories
scripts/sync-github-state
scripts/validate-github-repositories
scripts/validate-github-ops
scripts/validate-dashboard-truth
scripts/review-direction
scripts/evaluate-merge-gate
scripts/merge-approved-pr MG-001
```

Dry-run publish records `dry_run_command` and `dry_run_at` back into `state/github/operations.jsonl`, and appends a sync record. This keeps operator-visible evidence even when no remote GitHub write is performed.

Repository mapping records GitHub auth status, local path strategy, remote URL, publish blockers, `observed_at`, and whether the row was `live_observed`. `scripts/sync-github-state` is the only normal writer for live repository readiness. A missing remote keeps `publish_ready=false` even when issue content, outbox, and scoped approval are ready. `scripts/validate-dashboard-truth` rechecks local git, `gh auth`, open issues, and open PRs so the dashboard cannot silently present stale GitHub facts as current truth.

## Design Notes

- Candidate generation and approval are separate so operators can reject, merge, split, or reorder work before it reaches GitHub.
- Outbox files are local markdown artifacts that can be reviewed before any remote write.
- Publish approval is recorded separately as `publish_approval_scope=publish_issue`.
- Repository readiness is a separate gate; approval does not imply remote configuration.
- PRs are treated as collaboration hubs: body text must name scope, evidence, validation, and linked work.
- The dashboard renders the GitHub operation board from the same state files.
