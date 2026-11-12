# sandbox

Agent user-app smoke repo (pr-broker App installed here). Used to pilot the hardened review flow for agent-authored pull requests.

## Layout

```
.policy.yml   policy-bot review rules
iac/          Terraform: GitHub repository rulesets
src/          placeholder Python scripts
tests/        pytest tests for src/
haha          fixture for the path-owner rule
```

## Review model

| PR author | Required approvals | Notes |
| --- | --- | --- |
| Human | 1 | Not the author, not a committer. |
| pr-broker App, or any `agent/**` branch | 2 | The developer who ran the agent may be one of them, never the only one. Bot reviews do not count. |

Path owners apply on top: `.github/**` needs the `security` team, `haha` needs `0x64nl`.

Enforcement is layered:

1. **GitHub Rulesets** (`iac/`) require a PR into `main`, require the `policy-bot: main` check from the policy-bot App, and block force-push and deletion.
2. **policy-bot** (`.policy.yml`) counts approvals by author type and posts `policy-bot: main`.

Agent branches are still pushed with the developer's own PAT. Making them writable by the pr-broker App only is pending a commit route in pr-broker (see `iac/README.md`).

## Development

```bash
python3 -m venv .venv && .venv/bin/pip install -e '.[dev]'
.venv/bin/ruff format --check . && .venv/bin/ruff check . && .venv/bin/pytest -q
```
