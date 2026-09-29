# AWS DevOps 30-Day Portfolio

A hands-on DevOps portfolio covering Linux, Git, AWS,
Python APIs, Docker, CI/CD, Terraform, Kubernetes, Helm,
serverless architecture, monitoring, security and operational
recovery.

The projects were built as practical exercises rather than
production systems. AWS resources used for labs are destroyed
when they are no longer required.

## Projects

### Project 01 — Secure S3 Handover

**Problem:** Teams need a controlled way to work with files
in AWS without exposing credentials or making data public.

**Solution:** Built an AWS CLI and S3 workflow using IAM
Identity Center authentication and secure bucket practices.

[View Project](./project-01-s3-handover/)

**Tools:** AWS CLI, Amazon S3, IAM Identity Center, Git

---

### Project 02 — Inventory API

**Problem:** A small API needs a repeatable path from local
development to containerised deployment.

**Solution:** Built and tested a FastAPI service, containerised
it with Docker, added CI/security checks, and deployed it
locally with Kubernetes and Helm.

[View Project](./project-02-inventory-api/)

**Tools:** Python, FastAPI, Pytest, Ruff, Docker, GitHub
Actions, Trivy, Kubernetes, Kind, Helm

---

### Project 03 — Terraform AWS Foundation

**Problem:** Manually created cloud environments become
inconsistent and difficult to reproduce.

**Solution:** Defined a small AWS foundation with Terraform,
including networking, secure S3 storage, remote state and
automated validation.

[View Project](./project-03-terraform-foundation/)

**Tools:** Terraform, AWS, VPC, S3, IAM, GitHub Actions,
Checkov

---

### Project 04 — Serverless Incident Intake

**Problem:** Repeated and incomplete field reports are
difficult to track and escalate reliably.

**Solution:** Built a portfolio prototype in which API Gateway
accepts fictional reports, Lambda validates and processes
them, DynamoDB stores unique reports, SNS handles
high-severity notifications and CloudWatch provides
observability.

[View Project](./project-04-incident-intake/)

**Tools:** Python, Pytest, Terraform, API Gateway, Lambda,
DynamoDB, SNS, CloudWatch, IAM

> This is a learning prototype using fictional data and is not
> a production emergency-response system.

## Engineering Practices Demonstrated

- Infrastructure as Code
- Git-based change control
- CI validation
- Unit testing
- Containerisation
- Kubernetes deployment
- Helm packaging
- Least-privilege IAM
- Structured logging
- Cloud monitoring
- Idempotent request processing
- Deployment rollback
- Infrastructure cleanup
- Security scanning

## Security

No AWS access keys, private keys, Terraform state,
`.env` files or real incident data should be committed
to this repository.

AWS authentication uses short-lived credentials through
IAM Identity Center for the lab environment.

## Testing

Projects include automated tests and validation where
appropriate, including:

- Pytest
- Ruff
- Terraform fmt
- Terraform validate
- Checkov
- Trivy
- Kubernetes health probes
- API verification tests

## Cleanup

Temporary AWS and local Kubernetes resources are removed
after labs unless deliberately retained for continued work.

Terraform destruction plans are reviewed before resources
are removed.


## Architecture

Architecture diagrams for all portfolio projects are available
in [docs/architecture](./docs/architecture/README.md).
