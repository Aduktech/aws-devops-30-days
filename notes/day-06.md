
# Day 6 - Controlled S3 File Handover

## Problem

Teams sometimes share important forms through WhatsApp, personal email and USB drives. This can make it difficult to control access and identify the correct version of a file.

## Solution

I created a private Amazon S3 handover bucket.

The bucket uses:

- IAM-based access
- Block Public Access
- SSE-S3 encryption
- S3 Versioning
- resource tags

## Version Test

I uploaded a fictional draft form.

I changed the same file and uploaded it again using the same S3 object key.

S3 retained both versions.

The latest version contained the approved form while the older version remained available.

## Recovery Test

I obtained the Version ID of the older object and downloaded that specific version.

The recovered copy contained the original draft information.

## Security

I did not use the AWS root user.

I did not create an administrator access key.

The devops-lab identity received only the permissions required for this lab.

The bucket remains private.

## Key Lesson

S3 Versioning protects against accidental overwriting because older object versions can still be recovered.
