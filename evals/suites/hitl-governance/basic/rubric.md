# HITL Governance Eval

This suite validates that Flyhigh separates autonomous local work from scoped operator approval.

It passes when:

- every operator decision declares autonomy level, approval scope, reversibility, risk, apply gate, and stale-context guard;
- every option has its own approval scope;
- response state exists and any recorded response points to a valid decision option;
- external scopes require explicit operator approval;
- published GitHub operations cannot exist without scoped publish approval.

The suite intentionally does not perform remote writes.
