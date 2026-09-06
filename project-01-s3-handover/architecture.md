
# Controlled File Handover Architecture

Authorised Staff
        |
        | SSO + MFA
        v
IAM Identity Center
        |
        | Permission Set
        v
IAM Role
        |
        | Least-Privilege IAM Policy
        v
Private Amazon S3 Bucket
        |
        +-- Block Public Access
        |
        +-- SSE-S3 Encryption
        |
        +-- S3 Versioning
        |
        +-- Resource Tags
        |
        v
forms/sample-form.txt
        |
        +-- Version 1: Draft
        |
        +-- Version 2: Approved
