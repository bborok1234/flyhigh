---
name: flyhigh-implement
description: Use for scoped code or document changes after enough context exists; preserve user changes, follow local patterns, and verify changed behavior.
---

# Implement

Use this skill for focused edits.

## Workflow

1. Confirm scope and files likely to change.
2. Read surrounding code and instructions.
3. Make the smallest coherent change.
4. Prefer existing utilities and patterns.
5. Avoid unrelated refactors.
6. Run targeted validation.
7. Report files changed and verification evidence.

## References

- `references/engineering-principles.md`
- `references/qa-standard.md`

## Outputs

- Focused diff.
- Validation summary.
- Known gaps.

## Stop Condition

Stop when the requested behavior is implemented and verified, or when a concrete blocker prevents safe progress.

