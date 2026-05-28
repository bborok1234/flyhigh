# Skill System

Flyhigh skills are small, task-shaped playbooks. They should make an agent more consistent without consuming the whole context window.

## Skill Anatomy

Each skill folder contains:

```text
skills/<skill-name>/
  SKILL.md
```

`SKILL.md` must include YAML frontmatter:

```yaml
---
name: flyhigh-<name>
description: Clear trigger and task boundary.
---
```

The body should include:

- when to use the skill;
- expected inputs;
- workflow;
- outputs;
- validation;
- which references to load when needed.

## Skill Boundaries

Skills should do one repeatable job:

- `project-bootstrap`: inspect a repo and create or refresh project instructions;
- `analyze`: read-only investigation;
- `plan`: PRD and test-spec shaping;
- `implement`: scoped code changes;
- `review`: defect-focused review;
- `qa`: validation and adversarial checks;
- `ship`: release, commit, and PR readiness;
- `learn`: memory and skill improvement capture;
- `session-handoff`: summarize current state for future continuation.

## Progressive Disclosure

Keep skills short. Put durable standards in `references/`, reusable output shapes in `templates/`, and fragile deterministic work in `scripts/`.

## Codex Invocation

Codex users should be able to invoke a skill by name and get a predictable workflow. The skill should assume normal Codex capabilities: read files, edit files, run commands, use MCP tools, spawn native subagents when materially useful, and report validation evidence.

## Claude Compatibility

Claude Code can map these skills to slash commands or native skills. Claude-specific hooks and subagents are compatibility wrappers, not the source of truth.

## Skill Quality Rules

- State the stop condition.
- Do not ask for permission for ordinary reversible work.
- Ask for destructive, external-production, credential-gated, or materially branching actions.
- Avoid unrelated refactors.
- Preserve user changes.
- Verify claims with command output or inspected artifacts.
- Report validation gaps explicitly.

