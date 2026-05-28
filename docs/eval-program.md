# Eval Program

Flyhigh uses eval suites to decide whether harness behavior is improving.

## Commands

```bash
scripts/run-eval-suite all
scripts/compare-eval-runs evals/reports/before.json evals/reports/after.json
scripts/validate-evals
```

## Suites

- bootstrap
- run artifact
- policy
- skills
- decision memory
- dashboard
- SkillOpt
- adapters

Reports are written under `evals/reports/`.

The full suite includes `github-ops`, which validates issue/PR operation proposals, approval state, local outbox readiness, and publish-state safety.
