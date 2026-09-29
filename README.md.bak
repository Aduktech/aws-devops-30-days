# aws-devops-30-days

# AWS DevOps 30-Day Challenge

- Region: eu-west-2
- Environment: lab
- Goal: Build practical AWS, Docker, CI/CD and Terraform skills.
- Rule: Every cloud resource is tagged and removed after each lab.

## How to run this project

This repository contains practical exercises from my 30-day AWS DevOps challenge. The commands should be run from Ubuntu on WSL2 unless stated otherwise.

### Prerequisites

- Ubuntu on WSL2
- Git
- Python 3
- Docker Desktop with WSL integration
- AWS CLI v2

### Run the Day 2 backup script

From the repository root:

```bash
chmod 700 backup.sh
./backup.sh

## Day 14 Deployment Test

- Known-good image tag: 6e6478cd0e7363ebd7e010535174106d2ee71533
- EC2 deployment time:Mon Sep 14 22:45:01 WAT 2026
- Local health check: PASS
- External health check: PASS
- Broken test deployment: health check failed as expected
- Rollback image tag: 250675045042.dkr.ecr.eu-west-2.amazonaws.com/inventory-alert-api:6e6478cd0e7363ebd7e010535174106d2ee71533
- Rollback completion time: Mon Sep 14 22:55:35 WAT 2026
- Post-rollback health check: PASS
- Remote access method: AWS Systems Manager Session Manager
- SSH port 22 exposed: No


# Terraform AWS Foundation

## Purpose

Reproducible AWS foundation for development environments.

## Resources

- VPC
- Two public subnets across Availability Zones
- Internet Gateway
- Public route table
- Security group with no inbound rules
- Private encrypted S3 artifact bucket
- S3 versioning
- S3 Block Public Access
- Remote S3 Terraform state
- S3 state locking

## Cost Design

No NAT Gateway is created because the current project does not require private-subnet outbound internet access.

## Deployment

terraform init
terraform fmt -check -recursive
terraform validate
terraform plan -var-file=dev.tfvars -out=tfplan
terraform show tfplan
terraform apply tfplan

## Verification

terraform output
aws s3api get-bucket-versioning --bucket "$(terraform output -raw artifact_bucket_name)"
aws s3api get-bucket-encryption --bucket "$(terraform output -raw artifact_bucket_name)"

## Security

- Remote encrypted Terraform state
- State versioning
- State locking
- S3 public access blocked
- Artifact encryption
- No default inbound security-group access
- Environment values supplied through variables
