# Codex And Claude Compatibility

Flyhigh is Codex-first and compatibility-aware.

## Codex Mapping

| Flyhigh concept | Codex surface |
| --- | --- |
| Always-on project rules | `AGENTS.md` |
| Reusable workflows | Skills |
| Distribution | Plugin |
| External tools | MCP / app connectors |
| Parallel bounded work | Native subagents |
| Browser and desktop QA | Browser / computer-use plugins |
| Run evidence | Repo-local reports and artifacts |

## Claude Code Mapping

| Flyhigh concept | Claude Code surface |
| --- | --- |
| Always-on project rules | `CLAUDE.md` |
| Reusable workflows | Skills or slash commands |
| Deterministic lifecycle automation | Hooks |
| External tools | MCP |
| Isolated work | Subagents |
| Distribution | Plugin / marketplace package |
| Run evidence | Repo-local reports and artifacts |

## Compatibility Rule

The canonical content lives in Flyhigh skills, references, templates, and scripts. Claude-specific or other-agent-specific files should be generated adapters.

## When To Use Each Surface

- Use project instructions for rules every session must know.
- Use skills for repeatable processes.
- Use hooks only for deterministic checks that should fire on lifecycle events.
- Use MCP for external systems and data.
- Use subagents for parallel or context-isolated work.
- Use plugins to package the setup for reuse.

## Avoiding Overfit

Do not make Codex worse to mirror another tool. Compatibility should translate concepts, not force identical behavior.

## Future Adapter Ideas

- Generate `CLAUDE.md` from `AGENTS.md` template sections.
- Generate slash command wrappers for Flyhigh skills.
- Generate hook examples for formatting, secret scanning, and validation reminders.
- Export run summaries to formats accepted by other agent tools.

