# Security And Policy

Flyhigh needs explicit safety because harnesses can amplify mistakes.

## Threat Model

Primary risks:

- malicious project instructions;
- poisoned skill or hook files;
- hidden destructive shell commands;
- accidental credential exposure;
- broad unrelated rewrites;
- unreviewed dependency changes;
- stale memory causing wrong decisions;
- adapter drift across Codex and Claude surfaces.

## Policy Classes

| Class | Meaning | Examples |
| --- | --- | --- |
| Allow | Safe local action | read files, inspect git status, run targeted tests |
| Rationale required | Local action with future cost | add dependency, broad formatting, generated code |
| Approval required | High side effect | destructive commands, publishing, production writes, credential use |
| Deny | Outside harness authority | unrelated reverts, hidden network exfiltration, app-specific live actions |

## Hook Guidance

Hooks are powerful and risky. Flyhigh should treat hooks as optional adapters, not default behavior.

Good hook candidates:

- format after edit;
- block known destructive commands;
- scan for secrets before commit;
- remind about validation after risky edits.

Bad hook candidates:

- auto-publishing;
- credentialed production writes;
- broad shell execution from untrusted config;
- hidden model calls that change files.

## Skill Trust

Skills should be auditable:

- concise `SKILL.md`;
- no hidden external calls;
- scripts named for their effect;
- deterministic validators;
- versioned changes;
- eval evidence for promotion.

## Memory Safety

Memory must not store secrets or raw private material. Durable entries need evidence and dates. Contradicted entries should be marked stale rather than silently left in force.

## V1 Enforcement

The first enforcement layer is documentation and validators. V1 includes `scripts/policy-preflight`, which emits conservative warnings for:

- destructive command patterns;
- dependency and lock file changes;
- broad changed-file sets;
- likely secret files;
- generated instruction drift.

Later layers can add:

- command preflight checks;
- changed-file scope checks;
- dependency-change detector;
- memory staleness detector;
- adapter drift detector.
