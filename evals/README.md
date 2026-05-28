# Flyhigh Evals

Flyhigh evals begin as lightweight fixtures and rubrics. They exist to improve skills through measured outcomes.

## Initial Fixture Types

- repo onboarding accuracy;
- small bugfix success;
- review finding quality;
- QA completeness;
- unnecessary diff reduction;
- instruction-following compliance;
- run artifact completeness.

## Current Fixtures

- `fixtures/bootstrap/basic-node-repo`: verifies that `scripts/bootstrap-project` can infer a small Vite/React/TypeScript repository and create project instructions, memory files, and a bootstrap report.
- `fixtures/run-artifact/basic`: verifies run artifact creation and validation.
- `fixtures/policy/basic`: verifies conservative policy warnings.
- `fixtures/adapters/basic`: verifies generated adapter surfaces.
- `fixtures/skills/basic`: verifies skill metadata and contract requirements.

## Fixture Shape

```text
evals/fixtures/<name>/
  input/
  expected/
  rubric.md
```

Automated scoring can be added after the rubrics stabilize.

Run the current bootstrap fixture check from the repository root:

```bash
scripts/validate-bootstrap-fixture
scripts/validate-run-fixture
scripts/validate-policy-fixture
scripts/run-evals
```
