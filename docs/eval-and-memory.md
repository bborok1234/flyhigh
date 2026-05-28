# Eval And Memory

Flyhigh treats memory and skill improvement as engineering artifacts.

## Memory Model

Memory is local-first Markdown by default. A future index can be added, but the canonical record should remain human-readable.

Recommended project memory:

```text
.flyhigh/
  memory/
    project-facts.md
    decisions.md
    commands.md
    hazards.md
    failed-attempts.md
    skill-notes.md
```

## What To Remember

Remember facts that change future work:

- build and test commands;
- architectural boundaries;
- naming conventions;
- fragile files;
- recurring failures;
- accepted tradeoffs;
- rejected alternatives;
- verification gaps.

Do not remember secrets, raw logs, temporary hypotheses, or user-private material unless explicitly requested and safe.

## Eval Philosophy

Skill changes should be promoted by measured outcomes. Flyhigh follows the SkillOpt-style idea that agent skills can evolve, but only when evaluation supports the change.

## Initial Eval Areas

- repo onboarding accuracy;
- small bugfix success;
- review finding quality;
- QA completeness;
- unnecessary diff reduction;
- instruction-following compliance;
- run artifact completeness.

## Lightweight Scoring

Each eval fixture should include:

```text
input/
expected/
rubric.md
```

Scores can begin as human-reviewed checklists. Automation can be added later.

## Promotion Rule

A skill update can move from staging to active only when:

- it improves at least one target metric;
- it does not regress safety or instruction compliance;
- the reason for the change is recorded;
- the old version can be restored.

## Memory Hygiene

Memory must stay compact. Prefer one durable bullet over a page of transcript. Archive stale or contradicted facts instead of letting them silently conflict with current instructions.

