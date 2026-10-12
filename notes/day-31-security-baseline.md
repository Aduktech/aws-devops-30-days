# Day 31 — AWS Security Baseline

## Objective

Establish the AWS security workspace and understand the
identity being used to access AWS.

## AWS Environment

AWS profile:
devops-lab

AWS region:
eu-west-2

Authentication method:
AWS IAM Identity Center (SSO)

Permission set:
To be confirmed from STS output.

## Authentication vs Authorisation

Authentication answers:

"Who are you?"

It verifies the identity attempting to access AWS.

In this lab I authenticate through AWS IAM Identity Center
using temporary credentials.

Authorisation answers:

"What are you allowed to do?"

After authentication, AWS evaluates policies and permissions
to determine whether my identity may perform a requested
action.

Authentication therefore establishes identity.

Authorisation determines permissions.

## Commands Used

    aws sts get-caller-identity

    aws configure list --profile devops-lab

    aws iam get-account-summary

## AccessDenied Evidence

## AccessDenied Evidence

Command:

    aws iam get-account-summary

Requested AWS action:

    iam:GetAccountSummary

Result:

AccessDenied

Cause:

The current authenticated identity does not have an
identity-based policy allowing iam:GetAccountSummary.

Security response:

No permissions were changed.

The denied action was documented so that any future
permission request can be specific and least-privileged.
If AccessDenied occurs, record:

- AWS command
- denied AWS action
- identity ARN
- error message
- what the command was trying to do

Do not solve AccessDenied by requesting AdministratorAccess.

## Lesson

To be completed at the end of Day 31.
## Useful Command

    aws sts get-caller-identity

This tells me which AWS identity is currently making
requests.

## Error or Question

Record any AccessDenied message encountered today.
If none occurred, write:

No AccessDenied error encountered today.

## Lesson

Authentication proves identity.

Authorisation determines what that authenticated identity
is permitted to do.

A successful login does not mean the identity has permission
to perform every AWS action.

AccessDenied should be investigated by identifying the exact
denied action rather than immediately granting broad access.
