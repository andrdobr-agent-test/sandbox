# Contributing

## Branch naming

- Humans: `<type>/<short-description>`, for example `docs/readme`.
- Agents: `agent/<github-login>/<short-description>`. The PR broker rejects any
  agent PR whose head branch does not start with `agent/<login>/`.

## Pull requests

- Keep each PR focused on a single concern.
- Explain the motivation, not just the mechanics, in the description.
- Fill in the pull-request template checklist.
- Request review from a human. Bot approvals do not satisfy the review gate.

## Review requirements

The `human-reviews` check counts only human-authored `APPROVED` reviews:

- Human-authored PR: 1 human approval.
- Bot/agent-authored PR: 2 human approvals.

The author's own review never counts. A red `human-reviews` check on a fresh PR
means it is waiting for review.

## Local verification

There is no build step. Before opening a PR:

1. Review `git diff main...HEAD` and confirm the change is scoped.
2. Confirm no secrets, tokens, or credentials are included.
3. Verify the `human-reviews` workflow logic still matches the table above if
   the workflow itself was changed.
