# AWS Security Baseline

A hands-on AWS cloud security project focused on building
and verifying practical security controls using
least-privilege principles.

## Goals

This project will explore:

- IAM identity and policy evaluation
- temporary credentials and federation
- least privilege
- permission boundaries
- KMS encryption
- secrets management
- S3 security
- network security
- CloudTrail
- AWS Config
- GuardDuty
- Security Hub
- AWS Organizations and SCP concepts
- security monitoring
- incident response
- Infrastructure as Code security

## Authentication

Authentication proves who is making a request.

This lab uses AWS IAM Identity Center and temporary
credentials rather than long-lived IAM access keys.

## Authorisation

Authorisation determines what an authenticated identity
is allowed to do.

AWS evaluates applicable policies before allowing an
API action.

## Security Principles

- No root access keys.
- No credentials in source control.
- Prefer temporary credentials.
- Use least privilege.
- Investigate AccessDenied before changing permissions.
- Avoid broad AdministratorAccess for troubleshooting.
- Record security decisions.
- Remove temporary lab resources.
