terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "incident-intake"
      Environment = "lab"
      ManagedBy   = "Terraform"
    }
  }
}

# Used for resources that should not inherit the default tags
provider "aws" {
  alias  = "untagged"
  region = var.aws_region
}
