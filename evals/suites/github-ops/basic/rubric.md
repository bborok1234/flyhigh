# GitHub Operations Eval

The GitHub operations layer passes when:

- operation records exist in `state/github/operations.jsonl`;
- each record has title, rationale, body, labels, linked Flyhigh items, evidence, status, lane, and approval metadata;
- no operation can be treated as published without a remote URL;
- approved or prepared operations name the approver;
- sync records exist in `state/github/sync-log.jsonl`.
