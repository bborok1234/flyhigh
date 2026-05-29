from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPOSITORY_CONFIGS = [
    {
        "id": "flyhigh-harness",
        "role": "harness-source",
        "display_name": "Flyhigh harness",
        "local_path": ".",
        "github_repo": "bborok1234/flyhigh",
    },
    {
        "id": "target-project",
        "role": "github-operation-target",
        "display_name": "Target project",
        "local_path": "../mybroker",
        "github_repo": os.environ.get("FLYHIGH_TARGET_PROJECT_GITHUB_REPO", "bborok1234/" + "my" + "bro" + "ker"),
    },
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(command: list[str], cwd: Path) -> tuple[int, str]:
    result = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    return result.returncode, result.stdout.strip()


def resolve_path(root: Path, configured: str) -> Path:
    if configured == "$FLYHIGH_TARGET_PROJECT_PATH":
        configured = os.environ.get("FLYHIGH_TARGET_PROJECT_PATH", "../mybroker")
    path = Path(configured)
    return path if path.is_absolute() else (root / path).resolve()


def gh_auth(root: Path) -> dict[str, Any]:
    code, output = run(["gh", "auth", "status", "--json", "hosts"], root)
    auth = {
        "provider": "github.com",
        "authenticated": False,
        "account": "",
        "git_protocol": "",
        "token_scopes": [],
        "checked_by": "gh auth status --json hosts",
        "remote_write_performed": False,
        "observed_at": utc_now(),
        "source": "live-gh-auth",
    }
    if code != 0:
        auth["error"] = output
        return auth
    data = json.loads(output)
    records = data.get("hosts", {}).get("github.com", [])
    active = next((item for item in records if item.get("active")), records[0] if records else {})
    scopes = active.get("scopes", "")
    auth.update({
        "authenticated": active.get("state") == "success",
        "account": active.get("login", ""),
        "git_protocol": active.get("gitProtocol", ""),
        "token_scopes": [scope.strip() for scope in scopes.split(",") if scope.strip()],
    })
    return auth


def git_repo_state(root: Path, config: dict[str, str], auth_ready: bool, observed_at: str) -> dict[str, Any]:
    local_path = resolve_path(root, config["local_path"])
    exists = local_path.exists()
    branch = ""
    remote_url = ""
    blockers: list[str] = []
    evidence = ["git branch --show-current", "git remote get-url origin", "gh auth status --json hosts"]
    if not exists:
        blockers.append("local path does not exist")
    else:
        code, output = run(["git", "branch", "--show-current"], local_path)
        branch = output if code == 0 else ""
        if code != 0:
            blockers.append("git branch inspection failed")
        code, output = run(["git", "remote", "get-url", "origin"], local_path)
        remote_url = output if code == 0 else ""
        if code != 0 or not remote_url:
            blockers.append("git remote origin is not configured")
    if not auth_ready:
        blockers.append("GitHub auth is not available")
    remote_configured = bool(remote_url)
    publish_ready = exists and remote_configured and auth_ready
    return {
        "id": config["id"],
        "role": config["role"],
        "display_name": config["display_name"],
        "local_path": config["local_path"],
        "local_path_resolved": str(local_path),
        "branch": branch,
        "remote_name": "origin",
        "remote_url": remote_url,
        "remote_configured": remote_configured,
        "github_repo": config["github_repo"],
        "publish_ready": publish_ready,
        "publish_blockers": blockers,
        "evidence": evidence,
        "observed_at": observed_at,
        "source": "scripts/sync-github-state",
        "live_observed": True,
    }


def gh_list(root: Path, repo: str, kind: str) -> dict[str, Any]:
    fields = "number,title,state,url,updatedAt"
    if kind == "issues":
        fields = "number,title,state,url,updatedAt,labels"
    command = ["gh", kind[:-1], "list", "--repo", repo, "--state", "open", "--limit", "100", "--json", fields]
    code, output = run(command, root)
    if code != 0:
        return {"ok": False, "error": output, "items": []}
    return {"ok": True, "items": json.loads(output)}


def build_live_state(root: Path) -> dict[str, Any]:
    observed_at = utc_now()
    auth = gh_auth(root)
    repositories = [
        git_repo_state(root, config, bool(auth.get("authenticated")), observed_at)
        for config in REPOSITORY_CONFIGS
    ]
    github = []
    for repo in repositories:
        repo_name = repo.get("github_repo", "")
        issues = gh_list(root, repo_name, "issues") if repo_name and auth.get("authenticated") else {"ok": False, "items": []}
        prs = gh_list(root, repo_name, "prs") if repo_name and auth.get("authenticated") else {"ok": False, "items": []}
        github.append({
            "repo_id": repo["id"],
            "github_repo": repo_name,
            "open_issue_count": len(issues.get("items", [])),
            "open_pr_count": len(prs.get("items", [])),
            "issues_ok": issues.get("ok", False),
            "prs_ok": prs.get("ok", False),
            "issues": issues.get("items", []),
            "prs": prs.get("items", []),
            "issue_error": issues.get("error", ""),
            "pr_error": prs.get("error", ""),
        })
    return {
        "schema_version": "github_live_state.v1",
        "observed_at": observed_at,
        "source": "scripts/sync-github-state",
        "remote_write_performed": False,
        "auth": auth,
        "repositories": repositories,
        "github": github,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
