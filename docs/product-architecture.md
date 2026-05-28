# Product Architecture

Flyhigh's product is a personal engineering harness, implemented as a Codex plugin plus portable assets.

## System Model

```text
                        +----------------------+
                        | User / Maintainer    |
                        +----------+-----------+
                                   |
                                   v
+------------------+     +---------+----------+     +------------------+
| Target Project   |<--->| Codex Session      |<--->| External Tools   |
| code, tests, docs|     | tools, subagents   |     | MCP, browser     |
+--------+---------+     +---------+----------+     +------------------+
         ^                         ^
         |                         |
         |              +----------+-----------+
         |              | Flyhigh Plugin Pack  |
         |              | skills/references    |
         |              | templates/scripts    |
         |              +----------+-----------+
         |                         |
         v                         v
+------------------+     +---------------------+
| Run Artifacts    |     | Local Memory        |
| reports/runs     |     | .flyhigh/memory     |
+------------------+     +---------------------+
```

Flyhigh does not own the agent loop. It shapes the loop through instructions, skills, scripts, artifacts, and policy.

## Canonical Assets

### Harness Spec

The spec defines portable contracts:

- skill contract;
- run artifact contract;
- memory schema;
- policy classes;
- eval fixture shape;
- adapter mapping.

### Codex Implementation

Codex implementation is the first-class product surface:

- `.codex-plugin/plugin.json`;
- `skills/*/SKILL.md`;
- `AGENTS.md` template;
- validation scripts.

### Compatibility Adapters

Adapters are generated or derived:

- Claude `CLAUDE.md`;
- Claude slash command wrappers;
- hook examples;
- OpenCode/OpenAgent mapping;
- editor-specific notes.

Adapters must not become canonical.

## Capability Map

| Capability | v0 surface | Later surface |
| --- | --- | --- |
| Project bootstrap | skill + `scripts/bootstrap-project` | richer scaffold script |
| Read-only analysis | skill | evidence artifact writer |
| Planning | skill + templates | plan validator |
| Implementation | skill | scope guard |
| Review | skill + rubric | review eval fixture |
| QA | skill + rubric | run artifact checker |
| Memory | Markdown schema | index and stale-fact detector |
| Policy | `scripts/policy-preflight` | stricter preflight validators and hooks |
| Skill evolution | `scripts/run-evals` + fixture rubrics | promotion workflow |
| Adapter sync | `scripts/generate-adapters` | adapter drift validator |

## V1 Script Surface

- `scripts/create-run` and `scripts/validate-run` manage run artifacts.
- `scripts/policy-preflight` emits conservative safety warnings.
- `scripts/generate-adapters` and `scripts/validate-adapters` keep compatibility files derived.
- `scripts/run-evals` runs local fixture-backed checks.
- `scripts/render-v1-dashboard` renders progress from SSOT state.
- `scripts/validate-v1` proves the v1 baseline.

## Data Boundaries

Flyhigh can read and write its own plugin repository. In target projects, it should only write:

- project instructions when requested;
- `.flyhigh/memory/` when useful;
- `reports/runs/` artifacts for substantial work;
- files explicitly required by the user's task.

## Scale Strategy

Scaling comes from repeatable contracts, not centralized runtime ownership:

1. Use skills for repeated procedures.
2. Use templates for repeated artifacts.
3. Use scripts for deterministic checks.
4. Use memory for durable facts.
5. Use evals to decide whether changes improve the harness.
6. Use adapters only after the canonical asset is stable.
