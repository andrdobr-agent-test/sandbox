# sandbox
Agent user-app smoke repo (App installed here)

## Merge policy

Merging is enforced by the approval policy in [`.policy.yml`](.policy.yml). A PR can only be merged once every rule that applies to it is satisfied:

| Rule | Applies when | Required approvals |
|------|--------------|--------------------|
| Security team has approved | Changes under `.github/` | 1 from `andrdobr-agent-test/security` |
| Owner of `haha` has approved | The `haha` file changes | 1 from `0x64nl` |
| Bot PR has two approvals | PR opened by `andrdobr-agent-bot[bot]` | 2 from users with write access |
| Agent branch has two approvals | PR comes from an `agent/*` branch | 2 from users with write access |

Reviewers are requested automatically when a rule applies.
