# Policy System

Flyhigh policy classifies actions before they become hidden agent behavior.

## Policy File

```text
policies/default-policy.json
```

## Classes

- `allow`
- `rationale_required`
- `approval_required`
- `deny`

## Commands

```bash
scripts/check-policy --kind command --value "rm -rf build"
scripts/explain-policy --kind file --value package.json
scripts/validate-policy
```

The policy system handles destructive commands, dependency changes, broad churn, likely secrets, generated instruction drift, adapter drift, domain leakage, and missing validation evidence.

