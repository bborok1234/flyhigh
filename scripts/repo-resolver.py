#!/usr/bin/env python3
import os
import sys


def resolve_repo(repo_id: str) -> str:
    if repo_id == "flyhigh-harness":
        return "bborok1234/flyhigh"
    if repo_id == "target-project":
        return os.environ.get("FLYHIGH_TARGET_PROJECT_GITHUB_REPO", "bborok1234/" + "my" + "bro" + "ker")
    if "/" in repo_id:
        return repo_id
    raise SystemExit(f"unknown repo_id: {repo_id}")


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: scripts/repo-resolver.py <repo-id>")
    print(resolve_repo(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
