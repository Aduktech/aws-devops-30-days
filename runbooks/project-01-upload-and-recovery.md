# Project 01 — Upload and Recovery Runbook

## Purpose

This runbook explains how an authorised operator uploads a fictional file to the controlled Amazon S3 handover bucket and recovers a previous object version when required.

The procedure is designed for the AWS DevOps training environment.

## Owner

DevOps Lab Operator

## Pre-Check

Before uploading or recovering a file:

1. Sign in through IAM Identity Center using MFA.
2. Load the lab configuration with `source .env.local`.
3. Confirm the AWS identity with `aws sts get-caller-identity --profile devops-lab`.
4. Confirm the selected Region with `echo "$AWS_REGION"`.
5. Confirm the target bucket with `echo "$BUCKET"`.
6. Confirm S3 Versioning is enabled.
7. Confirm bucket encryption is configured.
8. Confirm public access remains blocked.
9. Stop if the AWS account, Region or bucket is not the expected lab environment.

## Upload

Upload the fictional form:

`aws s3 cp sample-form.txt "s3://$BUCKET/forms/sample-form.txt"`

### Expected Result

The upload should complete successfully and the object should appear under `forms/`.

Verify with:

`aws s3api list-objects-v2 --bucket "$BUCKET" --prefix forms/`

When the same key already exists and versioning is enabled, S3 should preserve the previous version and create a new object version.

## Recovery

List available versions:

`aws s3api list-object-versions --bucket "$BUCKET" --prefix forms/sample-form.txt`

Identify the exact Version ID that must be recovered.

Download the required version:

`aws s3api get-object --bucket "$BUCKET" --key forms/sample-form.txt --version-id "VERSION-ID" recovered-form.txt`

Verify the recovered file before replacing anything.

Copy the verified recovery file to a separate recovery key:

`aws s3 cp recovered-form.txt "s3://$BUCKET/recovery/sample-form-v1.txt"`

### Expected Result

The recovery object should appear under `recovery/`.

The current object under `forms/` should remain unchanged.

The recovered file should contain the expected historical content.

## Rollback

If the recovered version is incorrect, do not replace the current object.

Identify the correct Version ID and repeat the recovery procedure.

If the recovered version is later approved to become the current file, upload the verified recovered file to the original object key.

Because bucket versioning is enabled, this should create another version rather than remove the previous history.

## Security Rules

The AWS root user must not be used for normal uploads or recovery.

The bucket must remain private.

Public access blocking must remain enabled.

Users must receive only the permissions required for their role.

Passwords, access keys, MFA codes and SSO tokens must never be stored in the repository.

Only fictional data should be used in this lab.
