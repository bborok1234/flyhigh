# Dashboard

Flyhigh treats the dashboard as a human product surface, not a log dump.

## Source Of Truth

The dashboard is generated from structured state:

- `state/v1-status.json`
- `state/decisions.jsonl`
- `state/operator-decisions.jsonl`
- `state/operator-responses.jsonl`
- `state/issues.jsonl`
- `state/iterations.jsonl`
- `state/github/repositories.json`
- `state/github/merge-gates.jsonl`
- `state/reviews/direction-reviews.jsonl`
- `state/skillopt/*`
- `evals/reports/*`
- `policies/default-policy.json`
- `spec/harness-spec.json`

## Commands

```bash
scripts/render-dashboard
```

Output:

```text
dashboard/flyhigh.html
```

The dashboard is Korean-first and answers: why the work exists, what the operator must decide now, which recommendation is favored, what each option changes, which issues are in todo/doing/review/done, what decisions were made, how far the work is, what passed validation, which skills are evolving, and what happens after a decision.
