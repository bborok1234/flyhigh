# Workflow Contracts

Flyhigh workflows are contracts between user intent, agent action, and validation evidence. They are not hidden automation.

## Universal Contract

Every substantial workflow should answer:

- What is the target result?
- What constraints apply?
- What files, commands, and docs are authoritative?
- What evidence will prove completion?
- What should be left untouched?
- What is the stop condition?

## Standard Workflow Chain

```text
bootstrap -> analyze -> plan -> implement -> review -> qa -> ship -> learn
```

Workflows can be used independently. The chain is a default path, not a mandatory ceremony.

## Run Artifact Contract

Use this structure when the task is large, risky, or useful to replay:

```text
reports/runs/YYYY-MM-DD-task-slug/
  manifest.json
  plan.md
  events.jsonl
  tool-calls.jsonl
  verification.md
  final.md
```

Minimum `manifest.json` fields:

```json
{
  "task": "",
  "repo": "",
  "started_at": "",
  "agent_surface": "codex",
  "skills": [],
  "constraints": [],
  "artifacts": [],
  "validation": []
}
```

## Policy Contract

Agents must not silently perform high-risk actions. Flyhigh policies classify actions:

- `allow`: safe local reads, focused edits, local tests.
- `rationale_required`: dependency changes, generated code, broad refactors.
- `approval_required`: destructive commands, production writes, credential use, external publishing.
- `deny`: unrelated reversions, hidden live operations, domain actions outside the current project scope.

## Review Contract

Review findings must lead with bugs, risks, regressions, or missing tests. Summaries are secondary. Each finding needs a file and line reference when possible.

## QA Contract

QA starts from the claim being made. The agent should run the smallest validation that proves the claim, then broaden only when risk justifies it.

## Learn Contract

Learning captures durable facts:

- project conventions;
- recurring hazards;
- failed approaches;
- commands that matter;
- decisions and rationale;
- skill improvements backed by evidence.

It must not dump raw transcripts into memory.

