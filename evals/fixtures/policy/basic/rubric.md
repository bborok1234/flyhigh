# Basic Policy Preflight Rubric

The policy fixture passes when:

- destructive command detection reports `rm -rf`;
- dependency change detection reports `package.json`;
- likely secret detection reports `.env`;
- policy preflight exits successfully while emitting warnings.

