# Flyhigh Vision

Flyhigh is a personal engineering harness for Codex-first work. It packages reusable skills, project instructions, templates, validation scripts, and memory conventions so coding agents can operate consistently across large repositories without becoming a separate agent runtime.

## Product Thesis

Modern coding agents already have strong execution surfaces: file editing, shell access, browser automation, MCP tools, native subagents, and project instructions. Flyhigh should not replace those surfaces. It should make them easier to steer, verify, and improve over time.

OpenAI frames Codex plugins as connectors to tools and information, and skills as process playbooks. Claude Code uses a similar extension ladder: persistent project context, skills, subagents, hooks, MCP, and packaging. Flyhigh uses those ideas as a Codex-first personal operating layer.

Flyhigh's ambition is to become a personal engineering harness comparable to current serious Codex and Claude Code harnesses, but with a different center of gravity: canonical contracts, local-first evidence, memory hygiene, and eval-governed skill evolution.

## Non-Goals

- Do not build an autonomous agent runtime.
- Do not create a task queue, background daemon, or hosted service in the core.
- Do not include app-specific business logic.
- Do not hide the user's normal Codex workflow behind opaque automation.
- Do not optimize for demos at the cost of reproducibility.

## Target User

The first user is one engineer maintaining many projects with Codex and adjacent coding agents. That user needs repeatable behavior, context hygiene, review discipline, cross-session memory, and project bootstrap more than another chat interface.

## Success Criteria

Flyhigh is successful when it can be installed into a new project and quickly provide:

- a concise `AGENTS.md` suited to that repository;
- reusable skills for analysis, planning, implementation, review, QA, shipping, learning, and session handoff;
- run artifacts that make important agent work inspectable and resumable;
- memory conventions that retain decisions without bloating every session;
- policy checks that prevent common agent mistakes;
- eval loops that improve skills based on outcomes.

At maturity, Flyhigh should also provide adapter generation, policy preflights, run completeness checks, and a small eval lab that can prove whether a skill change improved real engineering outcomes.

## Design Principles

- Codex-first, portable second.
- Skills carry process; plugins package distribution.
- Project instructions stay short and current.
- Detailed guidance belongs in references and templates.
- Every substantial workflow ends with evidence.
- Memory records decisions and hazards, not transcripts.
- Policies block unsafe classes of action before they become habits.
- Improvement is eval-driven, not vibe-driven.
