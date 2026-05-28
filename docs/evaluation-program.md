# Evaluation Program

Flyhigh needs evals because harness quality otherwise becomes anecdotal.

## Eval Targets

### Bootstrap Accuracy

Can the harness infer stack, commands, tests, and conventions without hallucinating?

### Analysis Quality

Does it find the right files, separate evidence from inference, and avoid overreading?

### Plan Quality

Does the plan define scope, non-goals, acceptance criteria, and validation before edits?

### Implementation Discipline

Does the agent make the smallest coherent change and preserve unrelated work?

### Review Quality

Does review find real defects and avoid generic style commentary?

### QA Completeness

Does validation actually prove the claim?

### Memory Usefulness

Do memory updates improve future sessions without bloating context?

### Adapter Fidelity

Do generated Claude/OpenCode surfaces preserve the canonical Flyhigh intent?

## Fixture Shape

```text
evals/fixtures/<area>/<case>/
  input/
  expected/
  rubric.md
  notes.md
```

## Score Dimensions

- correctness;
- evidence quality;
- scope control;
- instruction compliance;
- validation strength;
- diff size;
- cost and time;
- safety.

## Promotion Workflow

```text
candidate skill change
  -> run relevant fixtures
  -> compare against active skill
  -> record result
  -> promote, revise, or reject
```

## V1 Eval Runner

Automated scoring is intentionally lightweight in v1. `scripts/run-evals` runs local validators and writes `evals/reports/latest.json`.

A useful manual eval records:

- task;
- skill version;
- expected outcome;
- observed outcome;
- failures;
- decision.

## Long-Term Goal

Flyhigh should become self-improving in a narrow engineering sense: it can propose changes to its own skills and templates, but only the changes that pass evals become active.
