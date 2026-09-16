variable "project_name" {
  description = "Name used for project resources"
  type        = string
  default     = "devops-foundation"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "lab"
}

variable "aws_region" {
  description = "AWS region for the project"
  type        = string
  default     = "eu-west-2"
}
