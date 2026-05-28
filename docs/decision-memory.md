# Decision Memory

Decision memory records durable engineering choices so future sessions can understand why the harness changed.

## Commands

```bash
scripts/record-decision
scripts/list-decisions
scripts/validate-decisions
```

## Storage

```text
state/decisions.jsonl
```

Each decision includes id, timestamp, title, context, decision, rationale, rejected alternatives, evidence, affected files, status, and follow-up.

