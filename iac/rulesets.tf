# Default branch: everything goes through a PR approved per .policy.yml.
# Nobody bypasses this ruleset. To get around it, change it here.
resource "github_repository_ruleset" "protect_main" {
  name        = "protect-main"
  repository  = var.repository
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~DEFAULT_BRANCH"]
      exclude = []
    }
  }

  rules {
    deletion         = true
    non_fast_forward = true

    # Native floor. Native rulesets cannot tell agent PRs from human PRs,
    # so the 2-approval rule for agent PRs lives in policy-bot.
    pull_request {
      required_approving_review_count   = 1
      dismiss_stale_reviews_on_push     = true
      require_last_push_approval        = true
      required_review_thread_resolution = true
      require_code_owner_review         = false
    }

    required_status_checks {
      strict_required_status_checks_policy = false

      required_check {
        context        = var.policy_bot_context
        integration_id = var.policy_bot_app_id
      }
    }
  }
}
