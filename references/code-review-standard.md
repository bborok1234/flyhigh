# Code Review Standard

Review as a defect finder, not a summarizer.

## Finding Requirements

Each finding should include:

- severity;
- file and line when possible;
- concrete failure mode;
- why the current behavior is risky;
- a focused remediation.

## Priority Order

1. Correctness bugs and regressions.
2. Security, privacy, or permission risks.
3. Data loss or destructive behavior.
4. Missing validation for changed behavior.
5. Maintainability issues that create real future risk.

Summaries belong after findings. If no issues are found, say so and list residual test gaps.

