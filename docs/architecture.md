# Flyhigh Architecture

Flyhigh is a layered plugin and skillset. It composes with Codex, Claude Code, and similar tools by using their native extension points instead of introducing a competing runtime.

This file describes the current scaffold architecture. The product-grade architecture and roadmap live in:

- `docs/competitive-landscape.md`
- `docs/product-architecture.md`
- `docs/operating-model.md`
- `docs/security-and-policy.md`
- `docs/evaluation-program.md`
- `docs/roadmap.md`

## Layers

```text
User intent
  -> Codex or compatible coding agent
    -> Project instructions: AGENTS.md / CLAUDE.md
    -> Flyhigh plugin package
      -> Skills
      -> References
      -> Templates
      -> Scripts
      -> Eval fixtures
    -> Target project repository
```

## Dependency Direction

Domain projects install or copy Flyhigh assets. Flyhigh never imports a domain project.

```text
project -> flyhigh
flyhigh -X-> project
```

This keeps the harness reusable. Domain-specific work belongs in project-local skills or references.

## Core Components

### Plugin Manifest

`.codex-plugin/plugin.json` identifies Flyhigh as a distributable Codex plugin. The manifest stays minimal and points to bundled skills and assets.

### Skills

Skills are the main product surface. Each skill is a short playbook with frontmatter, trigger description, workflow steps, expected outputs, and validation guidance. Skills load detailed guidance from `references/` only when needed.

### References

Reference files hold stable standards: engineering principles, review rubric, QA expectations, memory schema, and workflow taxonomy. They prevent `SKILL.md` files from becoming oversized.

### Templates

Templates provide project-local artifacts such as `AGENTS.md`, `DESIGN.md`, `PRD.md`, `TEST_SPEC.md`, and `RUN_REPORT.md`.

### Scripts

Scripts provide deterministic checks and small transformations:

- plugin manifest validation;
- skill frontmatter validation;
- run summary extraction;
- local memory update helper.

They must be safe, local-first, and dependency-light.

### Evals

Evals define fixtures and scoring ideas for harness quality. Early evals are intentionally lightweight and file-based so they can run anywhere.

## Runtime Model

Flyhigh does not own a long-running runtime. A normal Codex session invokes a Flyhigh skill, reads references as needed, edits the target repo, runs project tests, and writes artifacts. If a future backend is needed, it must be an adapter, not the core.

## Data Model

Substantial work should produce a run folder:

```text
reports/runs/YYYY-MM-DD-task-slug/
  manifest.json
  plan.md
  events.jsonl
  tool-calls.jsonl
  verification.md
  final.md
```

The manifest records task, repo, agent surface, relevant commands, and artifacts. The Markdown files keep human-readable intent and evidence. JSONL files can be appended by future hooks or scripts.

## Extension Points

- Codex: plugin, skills, `AGENTS.md`, MCP, native subagents, browser, computer-use.
- Claude Code: `CLAUDE.md`, skills, slash commands, hooks, subagents, MCP, plugins.
- Other agents: templates and references remain usable even without native plugin support.
