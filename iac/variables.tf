variable "owner" {
  description = "GitHub organization that owns the repository."
  type        = string
  default     = "andrdobr-agent-test"
}

variable "repository" {
  description = "Repository the rulesets apply to."
  type        = string
  default     = "sandbox"
}

variable "policy_bot_app_id" {
  description = "App ID of the policy-bot GitHub App. Only this App can satisfy the required status check."
  type        = number
}

variable "policy_bot_context" {
  description = "Status check context posted by policy-bot for the default branch."
  type        = string
  default     = "policy-bot: main"
}
