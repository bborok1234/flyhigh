# Basic Run Artifact Rubric

The run artifact fixture passes when:

- `scripts/create-run` creates a dated run folder under `reports/runs/`.
- The run folder contains `manifest.json`, `plan.md`, `events.jsonl`, `tool-calls.jsonl`, `verification.md`, and `final.md`.
- `scripts/validate-run` accepts the generated folder.
- The manifest contains required fields and lists all required artifacts.

