# Competitive Landscape

Flyhigh should be judged against current agent harness systems, not against prompt snippets.

## Reference Systems

### Codex Plugins And Skills

Codex distinguishes plugins from skills: plugins connect Codex to tools and information, while skills encode repeatable processes. Flyhigh should use plugins for packaging and skills for engineering workflows.

### Claude Code Extension Stack

Claude Code separates persistent project context, skills, subagents, hooks, MCP, and plugins. Flyhigh should preserve the same separation of concerns while staying Codex-first.

### Oh My Codex

OMX demonstrates the value of a Codex orchestration layer: workflow skills, runtime state, team coordination, HUD/status, read-only exploration paths, and verification gates. Flyhigh should learn from this but avoid becoming a required wrapper runtime.

### Oh My OpenAgent

Oh My OpenAgent shows the power of cross-agent routing, lifecycle hooks, skill loading, multi-agent coordination, model selection, and compatibility across OpenCode, Claude Code, and other tools. Flyhigh should adopt the portability idea without making routing the core product.

### GStack-Style Setups

GStack-style harnesses emphasize disciplined roles, reproducible workflows, and opinionated Claude Code configuration. Flyhigh should adopt role discipline and repeatability while keeping artifacts portable and inspectable.

### Webwright

Webwright's useful lesson is terminal-native reproducibility: the agent should leave executable evidence, scripts, logs, and artifacts rather than only a chat answer.

### 12-Factor Agents

The key lesson is that agent systems become reliable when prompts, context, state, tools, control flow, and human approval are treated as software boundaries.

### SkillOpt

Skill evolution should be evaluated. Flyhigh should treat skills as versioned assets promoted by measured outcomes, not by subjective preference alone.

## Flyhigh Positioning

Flyhigh is a personal, Codex-first harness spec and plugin pack:

- lighter than a wrapper runtime;
- more durable than a prompt collection;
- more personal than a generic team platform;
- more eval-governed than ad hoc skill folders;
- more portable than a single-agent configuration.

## Differentiators

1. `Spec-first`: define contracts for skills, runs, memory, policy, evals, and adapters.
2. `Codex-first`: use Codex plugin and skill surfaces as the primary distribution model.
3. `Adapter-aware`: generate Claude/OpenCode-compatible surfaces from canonical Flyhigh assets.
4. `Eval-governed`: promote skill changes only with evidence.
5. `Memory-disciplined`: preserve durable project knowledge without transcript bloat.
6. `Policy-explicit`: separate allow, rationale-required, approval-required, and denied actions.
7. `Local-first`: start with files and scripts before services.

## Design Implication

Flyhigh should not compete by adding a bigger autonomous loop. It should compete by making normal Codex work more structured, reusable, verifiable, and improvable across projects.

