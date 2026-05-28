# GitHub Repository Mapping Eval

This suite validates the repository mapping layer used before any GitHub publish operation.

It passes when:

- `state/github/repositories.json` exists;
- GitHub auth inspection is recorded without token material;
- every mapped repository has an id, role, local path, branch, remote fields, readiness, blockers, and evidence;
- `publish_ready` is false whenever a remote is missing;
- inspection records that no remote write was performed.
