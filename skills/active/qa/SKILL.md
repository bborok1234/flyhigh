---
name: flyhigh-qa
description: Use to validate claims with targeted tests, typechecks, builds, smoke checks, generated artifact inspection, or adversarial QA.
---

# QA

Use this skill to prove or disprove completion claims.

## Workflow

1. State the claim to prove.
2. Choose the smallest check that can prove it.
3. Run targeted checks before broad checks.
4. Inspect outputs, not just exit codes.
5. Iterate on failures when in scope.
6. Use `scripts/validate-run`, `scripts/run-evals`, or `scripts/validate-v1` when validating Flyhigh harness behavior.
7. Report evidence and remaining gaps.

## References

- `references/qa-standard.md`
- `templates/TEST_SPEC.md`

## Outputs

- Commands or inspections performed.
- Pass/fail evidence.
- Remaining risk.

## Stop Condition

Stop when the claim is proven, disproven, or blocked by a named validation gap.
