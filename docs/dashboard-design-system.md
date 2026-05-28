# Dashboard Design System

Flyhigh dashboard is an operator surface, not a report dump.

## Product Register

- Audience: one operator reviewing long-running AI engineering work.
- Mode: product UI, not marketing.
- Voice: factual, terse, decision-oriented.
- Anti-patterns: generic hero copy, equal-weight cards, long evidence dumps, nested cards, decorative gradients, vague "next steps".

## Information Hierarchy

1. 운영 브리핑: 지금 볼 것, 검증 관심, GitHub 준비, 결정 필요, 최근 반복.
2. Decision Console: question, recommendation, autonomy level, approval scope, options, impact, risk, apply gate, copy command, evidence, execution path.
3. Summary metrics: work, GitHub, validation.
4. 지금 판단할 항목: only actionable rows.
5. Work and GitHub boards.
6. GitHub repository mapping: auth, local path strategy, remote URL, publish readiness, blockers.
7. Direction review and merge gates: issue actions, PR actions, validation, blockers, merge readiness.
8. Recent iterations and decisions.
9. Eval/system evidence.

## Visual System

- Neutral background, white panels, restrained borders.
- Accent is used only for focus/action state.
- Green means verified, amber means attention.
- Cards are 8-10px radius and never nested as decorative wrappers.
- Long commands and evidence are secondary; they live in `details` or code blocks.

## Content Rules

- Every prominent row must answer: what is it, why does it matter, what happens next.
- Every open operator decision must show a recommended choice, the alternatives, approval scope, impact, apply gate, copy-ready response command, and execution path.
- Completed items are summarized, not allowed to dominate the first scan.
- Dry-run and approval evidence must be visible without reading raw JSON.
- GitHub publish readiness must show auth, mapped repo, remote, and blockers before any execute path.
- Merge readiness must show direction review, issue lifecycle decisions, validation evidence, and blockers before landing.
- Generic descriptions such as "best solution" or "improve productivity" are prohibited.
