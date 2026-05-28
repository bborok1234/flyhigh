# Flyhigh

Flyhigh is a personal Codex-first engineering harness. It packages a canonical harness spec, active skills, decision memory, run artifacts, policy gates, SkillOpt-inspired skill evolution, eval suites, generated Codex/Claude/OpenCode surfaces, project installation helpers, and a Korean human dashboard.

It is not a separate agent runtime. It sits on top of Codex and remains compatibility-aware for Claude Code and similar tools.

## Core Workflows

- `flyhigh-project-bootstrap`: inspect a repo and create or refresh project instructions.
- `flyhigh-analyze`: perform read-only investigation with evidence.
- `flyhigh-plan`: produce PRD and test-spec artifacts before broad work.
- `flyhigh-implement`: make scoped edits while preserving existing changes.
- `flyhigh-review`: review for defects, regressions, risks, and missing tests.
- `flyhigh-qa`: verify claims with tests, builds, static checks, or artifact inspection.
- `flyhigh-ship`: prepare final validation, commit or PR readiness, and release notes.
- `flyhigh-learn`: update memory and propose skill improvements based on outcomes.
- `flyhigh-session-handoff`: summarize current state for a future session.

## First Use

1. Install or copy this plugin into your Codex plugin location.
2. In a target project, invoke `flyhigh-project-bootstrap`.
3. Review the generated or updated `AGENTS.md`.
4. Use `flyhigh-analyze`, `flyhigh-plan`, `flyhigh-implement`, and `flyhigh-qa` for normal work.
5. Use `flyhigh-learn` after meaningful tasks to keep memory current.

From this repository, bootstrap a target project directly:

```bash
scripts/bootstrap-project /path/to/target-repo
```

The script writes:

- `AGENTS.md` or `AGENTS.flyhigh.generated.md` when an instructions file already exists;
- `.flyhigh/memory/` skeleton;
- `.flyhigh/bootstrap-report.md`.

## V1 Commands

```bash
scripts/create-run "Task title" --repo /path/to/target-repo
scripts/validate-run /path/to/target-repo/reports/runs/YYYY-MM-DD-task
scripts/policy-preflight --root /path/to/target-repo
scripts/generate-adapters
scripts/validate-adapters
scripts/run-evals
scripts/render-v1-dashboard
scripts/validate-v1
```

## Full Harness Commands

```bash
scripts/validate-spec
scripts/record-decision --id decision-id --title "..." --context "..." --decision "..." --rationale "..."
scripts/list-decisions
scripts/validate-decisions
scripts/init-skill-cycle --skill qa --id cycle-id
scripts/propose-skill-edit --id candidate-id --skill qa --operation add --target end --replacement "..."
scripts/apply-skill-patch candidate-id
scripts/score-skill-candidate candidate-id
scripts/promote-skill candidate-id
scripts/reject-skill-edit candidate-id --reason "..."
scripts/check-policy --kind command --value "rm -rf build"
scripts/explain-policy --kind file --value package.json
scripts/run-eval-suite all
scripts/generate-codex-surface
scripts/generate-claude-surface
scripts/generate-opencode-surface
scripts/install-into-project /path/to/project
scripts/render-dashboard
scripts/validate-dashboard-quality
scripts/validate-full-harness
scripts/create-issue --id FH-100 --title "..." --why "..."
scripts/update-issue FH-100 --lane doing
scripts/list-issues
scripts/record-iteration --id ITER-100 --goal "..." --summary "..."
scripts/propose-github-operation --id GH-100 --kind issue --title "..." --why "..." --body "..."
scripts/approve-github-operation GH-100 --approved-by operator
scripts/prepare-github-outbox --id GH-100
scripts/publish-github-operation GH-100 --repo /path/to/project
scripts/list-github-operations
scripts/list-github-repositories
scripts/validate-github-repositories
scripts/validate-github-ops
scripts/list-operator-decisions
scripts/decide OD-001 approve publish_issue --operator operator
scripts/list-operator-responses
scripts/apply-operator-decisions
scripts/validate-operator-decisions
scripts/validate-hitl-governance
scripts/review-direction
scripts/validate-direction-reviews
scripts/evaluate-merge-gate
scripts/validate-merge-gates
scripts/merge-approved-pr MG-001
scripts/harness-loop
```

## Progress Dashboard

Flyhigh tracks v1 progress from structured state:

```text
state/v1-status.json
state/v1-decisions.jsonl
state/v1-events.jsonl
state/v1-risks.jsonl
```

Render the single-file dashboard with:

```bash
scripts/render-dashboard
```

Then open:

```text
dashboard/flyhigh.html
```

## Repository Layout

```text
.codex-plugin/      Codex plugin manifest
skills/             Reusable task playbooks
references/         Durable standards loaded only when needed
templates/          Project artifact templates
scripts/            Local validation and helper scripts
docs/               Design package
evals/              Evaluation concepts and fixtures
examples/           Usage examples
```

## Design Package

- `docs/vision.md`: product thesis and non-goals.
- `docs/competitive-landscape.md`: how Flyhigh differs from current harnesses.
- `docs/product-architecture.md`: product-grade system model.
- `docs/operating-model.md`: day-to-day engineering lifecycle.
- `docs/security-and-policy.md`: safety model and future enforcement.
- `docs/evaluation-program.md`: eval-driven skill improvement plan.
- `docs/orchestration-guidance.md`: subagent, worktree, review, QA, and handoff guidance.
- `docs/roadmap.md`: staged path from scaffold to stable harness.
- `docs/skillopt-engine.md`: SkillOpt-inspired state machine and promotion flow.
- `docs/dashboard.md`: Korean dashboard source and rendering model.
- `docs/dashboard-design-system.md`: operator dashboard design system and content rules.
- `docs/decision-memory.md`: durable decision tracking.
- `docs/policy-system.md`: policy classes and commands.
- `docs/eval-program.md`: eval suite commands and reports.
- `docs/adapter-system.md`: generated surface model.
- `docs/domain-projects.md`: installing Flyhigh into future projects.
- `docs/github-operations.md`: GitHub issue/PR proposal, approval, outbox, and publish lifecycle.
- `docs/github-operations-research.md`: references and design consequences for GitHub operations.
- `docs/merge-governance-research.md`: direction review and merge gate rules.
- `docs/decision-console.md`: operator-facing decision prompt model for dashboard choices.

## Run Artifacts

Substantial work should write artifacts under the target project:

```text
reports/runs/YYYY-MM-DD-task-slug/
  manifest.json
  plan.md
  events.jsonl
  tool-calls.jsonl
  verification.md
  final.md
```

## Validation

From this repository:

```bash
scripts/validate-plugin
scripts/validate-skills
scripts/validate-bootstrap-fixture
scripts/validate-run-fixture
scripts/validate-policy-fixture
scripts/validate-adapters
scripts/run-evals
scripts/validate-v1
scripts/validate-full-harness
```

These scripts are dependency-light and intended to run in local shells.
