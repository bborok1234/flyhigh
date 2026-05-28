---
name: flyhigh-project-bootstrap
description: Use when starting Flyhigh in a repository or refreshing project instructions; inspect stack, commands, tests, conventions, hazards, and create or update AGENTS.md plus optional memory skeleton.
---

# Project Bootstrap

Use this skill to onboard a repository into Flyhigh.

## Workflow

1. Inspect repository shape with fast local search.
2. Identify stack, package managers, scripts, test commands, build commands, key directories, and local conventions.
3. Run `scripts/bootstrap-project <target-repo>` from the Flyhigh repository when a deterministic bootstrap is appropriate.
4. If the target has an existing `AGENTS.md`, inspect both it and the generated `AGENTS.flyhigh.generated.md` before merging.
5. Confirm `.flyhigh/memory/` and `.flyhigh/bootstrap-report.md` were created.
6. Report what was inferred, what remains uncertain, and how to validate the project.

## References

- `references/engineering-principles.md`
- `references/memory-schema.md`

## Outputs

- Updated project instructions.
- `.flyhigh/memory/` skeleton.
- `.flyhigh/bootstrap-report.md`.
- Bootstrap summary with evidence and gaps.

## Script Usage

```bash
scripts/bootstrap-project <target-repo>
scripts/bootstrap-project <target-repo> --force
scripts/bootstrap-project <target-repo> --dry-run
```

Default behavior writes `AGENTS.md` only when it does not already exist. If `AGENTS.md` exists, the script writes `AGENTS.flyhigh.generated.md` for manual merge.

## Stop Condition

Stop when project instructions capture current commands and conventions without inventing unsupported facts.
