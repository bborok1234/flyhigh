# Engineering Principles

- Start from the user's target result and constraints.
- Read the codebase before designing changes.
- Prefer existing patterns and utilities.
- Keep diffs scoped and reversible.
- Add abstractions only when they remove real complexity.
- Preserve user changes and unrelated work.
- Verify before claiming completion.
- Record durable decisions, rejected alternatives, and validation gaps.

## Agent-Specific Rules

- Use subagents only for bounded, independent work that benefits from isolation or parallelism.
- Do not hide risky actions inside scripts.
- Do not install dependencies without a clear reason.
- Do not convert a local workflow into a service unless the need is proven.

