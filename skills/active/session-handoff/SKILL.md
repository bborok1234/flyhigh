---
name: flyhigh-session-handoff
description: Use when ending, pausing, or compacting a session; summarize current state, decisions, files changed, validation, blockers, and next actions.
---

# Session Handoff

Use this skill when future continuation matters.

## Workflow

1. Summarize the user goal and current status.
2. List files changed or created.
3. Record commands run and validation evidence.
4. Create or update a run artifact for substantial work.
5. Note unresolved issues and blockers.
6. Provide the next concrete action.
7. Avoid unnecessary transcript detail.

## References

- `templates/RUN_REPORT.md`
- `references/memory-schema.md`

## Outputs

- Handoff note suitable for a future agent.
- Optional run report.

## Stop Condition

Stop when another session can resume without reconstructing context from scratch.
