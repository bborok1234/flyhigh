# Domain Projects

Flyhigh core stays domain-neutral. Domain projects install Flyhigh and keep their project-specific skills in the target project.

## Commands

```bash
scripts/install-into-project <target>
scripts/audit-project <target>
scripts/validate-installation
```

## Installed Shape

```text
AGENTS.md
.flyhigh/memory/
.flyhigh/domain-skills/
.flyhigh/dashboard/state.json
reports/runs/
```

The readiness fixture under `examples/` demonstrates this separation without placing domain logic in Flyhigh core.
