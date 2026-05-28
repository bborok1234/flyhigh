# GitHub Operations Research Notes

Flyhigh's GitHub layer is based on these operating principles.

## Inputs Reviewed

- CodeGraph: local code knowledge and impact context should reduce blind file scans before splitting work.
- OpenHuman: fresh context, memory trees, and integration sync loops are useful patterns for keeping operator context current.
- Academic Research Skills: human checkpoints and integrity gates are better than unsupervised full automation for high-stakes outputs.
- agentmemory: durable shared memory should outlive a single agent session and remain searchable across tools.
- Harness engineering talk summary: PRs should act as collaboration hubs, while repeated review feedback should be absorbed into docs, tests, lints, or reviewer agents.
- GitHub CLI docs: `gh issue create` and `gh pr create` support body files, labels, and other metadata; PR creation can link issues from body text.

## Flyhigh Design Consequences

- GitHub issue/PR work starts as local structured proposals.
- Publishing is separated from proposal generation.
- Human approval is explicit state, not implied by a generated body.
- Local markdown outbox files are reviewable before any remote write.
- Dashboard state is the operator source of truth.
- Future parallel agents should claim separate operation IDs and avoid mutating the same proposal without a state transition.

## References

- https://github.com/colbymchenry/codegraph
- https://github.com/tinyhumansai/openhuman
- https://github.com/Imbad0202/academic-research-skills
- https://github.com/rohitg00/agentmemory
- https://gist.github.com/intellectronica/1a9018ed642096fc81b0eeb1f2c8b63c
- https://cli.github.com/manual/gh_issue_create
- https://cli.github.com/manual/gh_pr_create
