# Operating Model

Flyhigh should make one engineer behave like a small disciplined engineering organization while staying local and inspectable.

## Modes

### Direct Mode

Use normal Codex behavior with Flyhigh skill guidance. This is the default for small tasks.

### Evidence Mode

For investigation, review, QA, and risky implementation, write run artifacts and validation notes.

Use `scripts/create-run` and `scripts/validate-run` when the task reaches L3 or higher.

### Handoff Mode

For long-running work or context pressure, create a compact handoff that another session can resume.

### Improvement Mode

After repeated tasks, update memory and propose skill changes. Skill changes remain staged until evals support them.

Use `scripts/run-evals` before promoting harness behavior changes.

## Default Lifecycle

```text
bootstrap once
  -> analyze when uncertain
  -> plan when scope is broad or risky
  -> implement with local patterns
  -> review for defects
  -> qa to prove the claim
  -> ship or handoff
  -> learn durable facts
```

## Role Discipline

Flyhigh keeps roles as workflow stances, not permanent personas:

- Explorer: map files and facts.
- Planner: define scope and validation.
- Executor: make scoped changes.
- Reviewer: find defects first.
- Verifier: prove or disprove completion.
- Archivist: update memory and handoff.

Subagents are useful only when a role needs isolation or parallelism.

## Context Hygiene

- Keep project instructions under control.
- Move detailed guidance to references.
- Avoid loading every reference by default.
- Summarize long investigations into artifacts.
- Archive stale memory instead of letting it conflict.

## Run Levels

| Level | Use | Required artifact |
| --- | --- | --- |
| L0 | tiny answer or local check | final note only |
| L1 | small scoped edit | validation summary |
| L2 | multi-file or risky work | run report |
| L3 | long-running or reusable work | full run folder |
| L4 | harness improvement | eval record plus promotion decision |

## V1 Progress Dashboard

When working on Flyhigh itself, update `state/v1-status.json` and JSONL state logs, then run `scripts/render-v1-dashboard`. The generated dashboard is a view, not the source of truth.

## Stop Conditions

Every workflow should stop when:

- the claim is proven;
- the blocker is concrete;
- the next branch requires approval;
- or further work no longer improves correctness.
