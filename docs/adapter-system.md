# Adapter System

Flyhigh keeps one canonical harness and generates tool-specific surfaces from it.

## Canonical Sources

- `spec/harness-spec.json`
- `skills/active/`

## Commands

```bash
scripts/generate-codex-surface
scripts/generate-claude-surface
scripts/generate-opencode-surface
scripts/validate-surfaces
```

## Outputs

- `adapters/codex/AGENTS.md`
- `adapters/claude/CLAUDE.md`
- `adapters/claude/commands/*.md`
- `adapters/opencode/AGENTS.md`

Generated adapters are compatibility surfaces, not the canonical source.

