# sandbox

Agent user-app smoke repo (App installed here).

This repository exists to exercise the end-to-end agent pull-request flow:
agent branch → push → PR via the PR broker → required human review.

## Contents

- `.github/workflows/require-human-reviews.yml` — required check that counts
  only human approvals.
- `.github/pull_request_template.md` — checklist applied when a PR is opened.
- `CONTRIBUTING.md` — branch naming and review expectations.

## Review gate

The `human-reviews` check is intentionally strict:

| PR author | Human approvals required |
| --------- | ------------------------ |
| Human     | 1                        |
| Bot/agent | 2                        |

Reviews from bots (including the authoring bot) are ignored. A PR is not
mergeable until the required human approvals are present.

## Agent PR workflow

1. Branch from `main` as `agent/<github-login>/<short-description>`.
2. Commit a focused change.
3. Push the branch.
4. Open the PR with the PR broker (`gh pr create ...`), which enforces the
   head-branch prefix and records the agent login in the PR body.

Keep PRs small and explain the motivation in the description. Failing the
`human-reviews` check until a human approves is expected, not a bug.
