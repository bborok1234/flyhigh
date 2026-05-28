# Roadmap

Flyhigh should grow from a reliable personal plugin into a portable engineering harness spec.

## v0.1 - Foundation

Status: scaffolded.

- Codex plugin manifest.
- Core skills.
- Design package.
- References and templates.
- Basic validation scripts.

## v0.2 - Project Bootstrap That Works

Status: implemented in local script form.

- Improve `flyhigh-project-bootstrap` through real repositories.
- Generate concise `AGENTS.md`.
- Create `.flyhigh/memory/` skeleton.
- Detect stack, package manager, test commands, and conventions.
- Add bootstrap eval fixtures.

## v0.3 - Run Artifact Writer

Status: implemented in v1.

- Add script to create run folders.
- Define strict `manifest.json` schema.
- Add run completeness validator.
- Add session handoff integration.

## v0.4 - Policy Preflight

Status: implemented in v1 as conservative warnings.

- Add local checks for high-risk command patterns.
- Detect dependency changes.
- Detect broad unrelated file churn.
- Add optional Claude hook examples and Codex-compatible guidance.

## v0.5 - Eval Lab

Status: implemented in v1 with local validators and fixture rubrics.

- Add first real fixture suite.
- Add manual scoring template.
- Add skill version metadata.
- Add promotion and rollback records.

## v0.6 - Adapter Sync

Status: implemented in v1 for Claude and OpenCode surfaces.

- Generate `CLAUDE.md` from canonical project instruction template.
- Generate Claude slash command wrappers for Flyhigh skills.
- Add OpenCode/OpenAgent mapping notes.
- Add adapter drift validator.

## v0.7 - Advanced Orchestration

Status: implemented in v1 as guidance, not runtime ownership.

- Add subagent routing guidance by task type.
- Add worktree isolation patterns.
- Add multi-agent review and QA playbooks.
- Keep orchestration optional and local.

## v1.0 - Stable Personal Harness

Status: implemented as a local-first v1 baseline.

- Stable plugin manifest.
- Stable skill contracts.
- Real eval coverage for core workflows.
- Proven bootstrap on multiple projects.
- Clear upgrade and rollback story.

## Principles For Roadmap Changes

- Ship reusable contracts before automation.
- Add hooks only after the policy is clear.
- Add adapters only after the canonical asset is stable.
- Add services only after local files and scripts stop scaling.
