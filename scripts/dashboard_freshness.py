from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "dashboard_freshness.v1"
RENDERER_VERSION = "render-dashboard.v2"
METADATA_PATH = Path("dashboard/flyhigh.freshness.json")
DASHBOARD_PATH = Path("dashboard/flyhigh.html")

SOURCE_PATTERNS = [
    "spec/harness-spec.json",
    "state/**/*.json",
    "state/**/*.jsonl",
    "policies/default-policy.json",
    "evals/reports/all.json",
    "evals/reports/v1-validation.json",
    "skills/active/*/SKILL.md",
    "skills/staging/*/patch.json",
    "skills/staging/*/score.json",
    "scripts/render-dashboard",
    "scripts/dashboard_freshness.py",
    "scripts/github_state.py",
    "scripts/sync-github-state",
    "scripts/validate-dashboard-truth",
]

EXCLUDED_PREFIXES = {
    "dashboard/",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def iso_from_ns(ns: int) -> str:
    return datetime.fromtimestamp(ns / 1_000_000_000, timezone.utc).isoformat()


def source_paths(root: Path) -> list[Path]:
    paths: set[Path] = set()
    for pattern in SOURCE_PATTERNS:
        for path in root.glob(pattern):
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                if any(relative.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
                    continue
                paths.add(path)
    return sorted(paths, key=lambda item: item.relative_to(root).as_posix())


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def source_snapshot(root: Path) -> dict[str, Any]:
    sources = []
    aggregate = hashlib.sha256()
    latest_mtime_ns = 0
    for path in source_paths(root):
        stat = path.stat()
        relative = path.relative_to(root).as_posix()
        digest = file_digest(path)
        latest_mtime_ns = max(latest_mtime_ns, stat.st_mtime_ns)
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\0")
        sources.append({
            "path": relative,
            "sha256": digest,
            "size": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "mtime": iso_from_ns(stat.st_mtime_ns),
        })
    return {
        "source_count": len(sources),
        "source_hash": aggregate.hexdigest(),
        "latest_source_mtime_ns": latest_mtime_ns,
        "latest_source_mtime": iso_from_ns(latest_mtime_ns) if latest_mtime_ns else "",
        "sources": sources,
    }


def build_metadata(root: Path, rendered_at: str | None = None) -> dict[str, Any]:
    snapshot = source_snapshot(root)
    return {
        "schema_version": SCHEMA_VERSION,
        "renderer_version": RENDERER_VERSION,
        "dashboard_path": DASHBOARD_PATH.as_posix(),
        "metadata_path": METADATA_PATH.as_posix(),
        "rendered_at": rendered_at or utc_now(),
        "fresh": True,
        **snapshot,
    }


def metadata_path(root: Path) -> Path:
    return root / METADATA_PATH


def dashboard_path(root: Path) -> Path:
    return root / DASHBOARD_PATH


def write_metadata(root: Path, metadata: dict[str, Any]) -> None:
    path = metadata_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_metadata(root: Path) -> dict[str, Any]:
    path = metadata_path(root)
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
