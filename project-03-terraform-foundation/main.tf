terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_s3_bucket" "lab" {
  bucket = "devops-lab-250675045042-1789472413"

  tags = {
    Project     = "30-Day-DevOps"
    Environment = "Lab"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.lab.bucket
}
