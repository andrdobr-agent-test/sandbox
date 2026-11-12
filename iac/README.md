# iac

Terraform for the repository ruleset that, with policy-bot, enforces the review model in `../.policy.yml`.

| Ruleset | Target | Effect |
| --- | --- | --- |
| `protect-main` | default branch | PR required (1 approval, stale reviews dismissed, last push approved, threads resolved), required `policy-bot: main` check from the policy-bot App, no force-push, no deletion. No bypass. |

## Apply

The token needs repository Administration read/write on the target repository. A classic PAT needs `repo`.

```bash
export GITHUB_TOKEN=...
cp terraform.tfvars.example terraform.tfvars   # fill in the policy-bot App ID
terraform init
terraform plan -var-file=terraform.tfvars
terraform apply -var-file=terraform.tfvars
```

State is local (`terraform.tfstate`, git-ignored). Keep it somewhere safe or move to a remote backend.

If the ruleset already exists, import it first so it is not duplicated:

```bash
terraform import github_repository_ruleset.protect_main sandbox:<ruleset_id>
```

## Planned

Agent branches (`agent/<login>/…`) are still pushed with the developer's own PAT. Once pr-broker creates those commits as the App (`createCommitOnBranch`), add an `agent/**` ruleset: creation, update and deletion restricted, the pr-broker App ID as the only bypass actor, and `required_signatures`. Until then, such a ruleset would reject every agent push.
