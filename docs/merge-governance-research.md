# Merge Governance Research

Flyhigh uses a small governance loop adapted from established project automation patterns.

## Patterns

- GitHub branch protection and merge queue separate PR authoring from merge eligibility. A PR should be current with the base branch and pass required checks before merge.
- Prow separates intent labels and commands such as approve, lgtm, and hold. Approval is not the same as merge; hold can stop otherwise mergeable work.
- Renovate separates dependency dashboard approval from automerge. A dashboard can approve intent while automerge still depends on rules and checks.
- Mergify-style queues treat merge as a gate: approved work enters a queue and is rechecked against current target state before landing.
- RFC/ADR workflows preserve direction changes as durable rationale, especially when plans are split, deferred, closed, or replaced.
- Agent-authored PR studies show that rejection often comes from unclear scope, weak evidence, or mismatched project direction, not just code defects.

## Flyhigh Rules

1. Direction review is required before merge. It records whether to continue, split, close, defer, or create issues.
2. Merge gate is separate from direction review. It records PR state, linked issues, required validation, risk, and merge decision.
3. A clean PR is not enough. Local validation evidence must exist and be named.
4. No hold means no unresolved blocker in the direction review or merge gate.
5. If implementation evidence contradicts the plan, the review may create new issues, split existing ones, or defer merge.
6. Merge is allowed only when direction review is accepted, merge gate is approved, validation passes, and the PR is clean or otherwise explicitly accepted.
7. After merge, Flyhigh records the merged state and updates dashboard evidence.
