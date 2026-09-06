
# S3 Controlled File Handover Runbook

## Purpose

This runbook explains how an authorised lab user uploads and recovers files from the controlled S3 handover bucket.

The bucket is private, uses S3 server-side encryption and has versioning enabled.

Only fictional training data should be used in this lab.

## Before Starting

Confirm that the AWS SSO session is active:

`aws sso login --profile devops-lab`

Confirm the AWS identity:

`aws sts get-caller-identity --profile devops-lab`

Load the local lab configuration if required:

`source .env.local`

Confirm the target bucket:

`echo "$BUCKET"`

Never continue if the AWS account or bucket is not the expected one.

## Upload a File

Upload the local file to the controlled `forms` prefix:

`aws s3 cp sample-form.txt "s3://$BUCKET/forms/sample-form.txt"`

Confirm that the object exists:

`aws s3 ls "s3://$BUCKET/forms/"`

## Check Available Versions

List all versions of the file:

`aws s3api list-object-versions --bucket "$BUCKET" --prefix forms/sample-form.txt`

The version where `IsLatest` is `true` is the current version.

Older versions remain available when bucket versioning is enabled.

## Recover an Older Version

Identify the required Version ID.

Download that specific version:

`aws s3api get-object --bucket "$BUCKET" --key forms/sample-form.txt --version-id "VERSION-ID" recovered-file.txt`

Review the recovered file before replacing anything.

## Restore an Older Version as Current

After checking the recovered file, upload it again to the same object key:

`aws s3 cp recovered-file.txt "s3://$BUCKET/forms/sample-form.txt"`

Because versioning is enabled, this creates another version instead of deleting the other versions.

## Security Rules

Do not make the bucket public.

Do not upload passwords, access keys or other credentials.

Do not use the AWS root user for file transfers.

Use the approved AWS identity and MFA.

Check the AWS identity before making important changes.

Do not disable versioning or encryption without an approved reason.

Do not upload real sensitive data while this remains a learning environment.
