# Flyhigh Agent Instructions

Flyhigh is a Codex-first personal engineering harness plugin and skillset.

## Operating Rules

- Keep the core domain-neutral.
- Prefer skills, references, templates, and scripts over a custom runtime.
- Keep `SKILL.md` files concise; put durable detail in `references/`.
- Preserve compatibility adapters as generated or secondary surfaces.
- Validate plugin and skill structure after edits.
- Avoid unrelated refactors and broad churn.
- Report validation evidence before claiming completion.

## File Boundaries

- `.codex-plugin/plugin.json` is the Codex plugin manifest.
- `skills/*/SKILL.md` files are user-invocable workflows.
- `references/` holds shared standards.
- `templates/` holds copyable project artifacts.
- `scripts/` holds deterministic local helpers.
- `docs/` explains design and contracts.

