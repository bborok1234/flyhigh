# Operator Decisions Eval

The decision console suite passes when Flyhigh records at least one open operator decision with:

- a concrete question;
- a recommended option that exists in the options list;
- at least two options;
- impact and follow-up text for every option;
- risk, evidence, owner, and execution path fields.

The suite is intentionally local and dependency-light. It validates that dashboard choices come from structured SSOT data instead of prose-only status reports.
