# SkillOpt Engine

Flyhigh implements a local, practical SkillOpt-inspired workflow. It does not automatically call an optimizer model yet. Instead, it implements the artifacts, state transitions, scoring, rejection buffer, and promotion gate needed to prevent skills from changing by vibes.

## Canonical Skill Layout

```text
skills/active/   deployable skills
skills/staging/  candidate edits
skills/archive/  previous active versions
```

## State

```text
state/skillopt/runs/
state/skillopt/rejected-edits.jsonl
state/skillopt/promotions.jsonl
```

## Workflow

1. `scripts/init-skill-cycle` records rollout evidence and minibatch reflection.
2. `scripts/propose-skill-edit` creates a bounded add/delete/replace patch.
3. `scripts/apply-skill-patch` materializes the candidate.
4. `scripts/score-skill-candidate` compares baseline and candidate scores.
5. `scripts/promote-skill` promotes only non-regressing candidates.
6. `scripts/reject-skill-edit` records rejected candidates with evidence.
7. `scripts/validate-skillopt` verifies the state machine.

The fixture `scripts/validate-skillopt-fixture` demonstrates a regressing candidate being rejected and recorded.

