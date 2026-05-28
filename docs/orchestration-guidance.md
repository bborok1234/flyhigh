# Orchestration Guidance

Flyhigh v1 supports advanced coordination through guidance and local artifacts, not through a wrapper runtime.

## When To Use Subagents

Use subagents when work is independent, bounded, and benefits from context isolation:

- read-only repository mapping while the leader plans;
- independent review of a completed diff;
- QA exploration across a different surface;
- documentation audit separate from implementation.

Do not use subagents for tiny tasks, shared-file edits without coordination, or decisions that require one owner.

## Worktree Isolation

Use a separate worktree when a change is broad, experimental, generated-artifact-heavy, or better reviewed as an isolated diff. Avoid worktrees for small focused edits where overhead hides the actual change.

## Review And QA Separation

Keep review and QA as separate stances:

- Review asks what is wrong or risky.
- QA asks what evidence proves the claim.

A single agent may perform both, but the report should keep the two concerns distinct.

## Handoff Discipline

For long work, produce a run artifact or handoff note with goal, files changed, commands run, validation state, open risks, and next concrete action.

## Context Compaction

Before compaction or a long pause, update run artifacts, write durable memory only, update Flyhigh state/dashboard when working on Flyhigh itself, and avoid copying raw transcript into memory.

## Long-Running Continuation

For large goals, keep one structured progress layer. Markdown docs can explain decisions, but active status should be structured and renderable.

