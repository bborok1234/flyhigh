# Decision Console

The dashboard must help an operator decide, not only observe.

## Source

```text
state/operator-decisions.jsonl
state/operator-responses.jsonl
```

## Required Shape

Each decision prompt includes:

- `question`: what the operator must decide;
- `recommendation`: the harness recommendation;
- `rationale`: why the recommendation is favored;
- `options`: at least two choices;
- `impact`: what changes if an option is chosen;
- `follow_up`: what happens next;
- `risk`: what can go wrong;
- `evidence`: files or commands supporting the recommendation;
- `execution_path`: how the selected decision becomes work.
- `autonomy_level`: whether the agent can apply locally or needs explicit approval;
- `approval_scope`: the maximum scope this decision can approve;
- `reversibility`: whether the result is reversible;
- `risk_level`: low, medium, or high;
- `apply_gate`: conditions checked before an answer is applied;
- `valid_until_context_changes`: stale-context guard;
- `copy_command`: short text the operator can paste back to the agent.

Each option also carries its own `approval_scope`. Approval for draft, prepare, or dry-run never implies approval for publish, merge, delete, spend, or credentialed work.

## Response Flow

The operator can answer with a short scoped command:

```text
OD-001 approve publish_issue
OD-002 split_before_publish local_apply
OD-003 continue_current_work local_apply
```

The command is recorded through:

```bash
scripts/decide OD-001 approve publish_issue --operator <name>
scripts/apply-operator-decisions
```

`scripts/apply-operator-decisions` records local SSOT changes and scoped approvals. It does not perform remote writes by itself.

## Dashboard Role

Decision Console appears before the normal boards. It should answer:

1. What decision is needed?
2. What does the harness recommend?
3. What are the alternatives?
4. What is the impact of each choice?
5. What is the exact follow-up path?
6. What short command should I send back?
7. What gate will run before the agent applies it?

The operator should not need to read raw JSON or a long transcript before deciding.
