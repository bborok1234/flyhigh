# Dashboard Refresh Contract

Flyhigh treats `dashboard/flyhigh.html` as a generated operator surface. The source of truth remains the structured SSOT under `state/`, `spec/`, `policies/`, `skills/`, and eval reports.

## Contract

Every workflow that changes dashboard-relevant SSOT must do one of two things:

1. Run `scripts/render-dashboard` before it finishes.
2. Leave the dashboard stale so `scripts/validate-dashboard-freshness` and `scripts/validate-full-harness` fail.

This makes dashboard refresh a harness invariant instead of a memory task.

## Freshness Metadata

`scripts/render-dashboard` writes:

- `dashboard/flyhigh.html`
- `dashboard/flyhigh.freshness.json`

The metadata records:

- `schema_version`
- `renderer_version`
- `rendered_at`
- `source_count`
- `source_hash`
- `latest_source_mtime`
- per-source path, size, mtime, and sha256

The rendered HTML also embeds the same `source_hash` and `renderer_version` in a comment and shows a `Dashboard freshness` panel for the human operator.

## Validation

Use:

```bash
scripts/validate-dashboard-freshness
scripts/validate-dashboard-quality
scripts/validate-full-harness
scripts/harness-loop
```

`scripts/validate-dashboard-freshness` recomputes the current source hash and compares it with the metadata and the HTML marker. If a tracked SSOT source changed without a dashboard render, validation fails.

`scripts/harness-loop` renders the dashboard after its final automatic iteration update, then validates freshness again.

## Truthfulness

Freshness only proves that the HTML matches Flyhigh SSOT. It does not prove the SSOT matches the outside world. For repository and GitHub facts, Flyhigh uses a second gate:

```bash
scripts/sync-github-state
scripts/validate-dashboard-truth
```

`scripts/sync-github-state` observes local git remotes, `gh auth`, open GitHub issues, and open PRs without performing remote writes. It records the observation in:

- `state/github/repositories.json`
- `state/github/live-state.json`

The dashboard shows this as `Live state`, including `observed_at`, open issue counts, open PR counts, and whether each repo was `live-observed`.

`scripts/validate-dashboard-truth` re-observes the same facts and fails if the cached SSOT disagrees with the live state. A dashboard can be fresh but false; in that case the truth validator blocks completion.

## SSOT-Changing Scripts

Scripts that mutate state should either call `scripts/render-dashboard` directly after writing state or rely on `scripts/harness-loop` as the required completion gate. PRs that change SSOT without refreshing the dashboard are not merge-ready because `scripts/validate-full-harness` includes the freshness validator.
