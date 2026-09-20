variable "project_name" {
  description = "project-03-terraform-foundation"
  type        = string
  default     = "devops-foundation"
}

variable "environment" {
  description = "Deployment environment"
  type        = string

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "Environment must be dev, test or prod."
  }
}

variable "aws_region" {
  description = "AWS region for the project"
  type        = string
  default     = "eu-west-2"
}
