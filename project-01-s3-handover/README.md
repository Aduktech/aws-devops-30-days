# Project 01 — Secure S3 File Handover

## Overview

This project demonstrates a controlled file-handover foundation using Amazon S3.

It addresses a common problem where field, research or small-business teams share important forms through WhatsApp, personal email and USB drives. These methods can create version confusion, weak access control and poor recovery when a file is overwritten.

Only fictional training data is used.

## Architecture

```text
Authorised Staff
        |
        | SSO + MFA
        v
IAM Identity Center
        |
        v
IAM Role / Permission Set
        |
        v
Least-Privilege IAM Policy
        |
        v
Private Amazon S3 Bucket
        |
        +-- Block Public Access
        |
        +-- SSE-S3 Encryption
        |
        +-- S3 Versioning
        |
        +-- forms/
        |
        +-- recovery/
```

## Main Security Controls

The bucket remains private and public access is blocked.

Files are encrypted at rest using S3 server-side encryption.

S3 Versioning keeps older file versions when an object is updated.

IAM permissions control which actions each user or role can perform.

The uploader policy does not use `s3:*` and does not grant delete or bucket-administration permissions.

## Recovery Design

Each historical version has a Version ID.

When recovery is required, the required historical version is identified and retrieved using its Version ID.

The recovered file is first copied to a separate `recovery/` key so that the current file remains unchanged.

The recovered copy is checked before any decision is made to replace the current business version.

## Threat and Mitigation

| Threat                               | Mitigation                                         |
| ------------------------------------ | -------------------------------------------------- |
| Public exposure of files             | S3 Block Public Access                             |
| Stolen credentials                   | IAM Identity Center, MFA and temporary credentials |
| Excessive permissions                | Least-privilege IAM policies                       |
| Accidental overwrite                 | S3 Versioning                                      |
| Wrong historical version restored    | Recovery using an exact Version ID                 |
| Stored data exposed                  | SSE-S3 encryption at rest                          |
| Uploader deletes files               | No delete permission in uploader policy            |
| Changes made in wrong AWS account    | `sts get-caller-identity` pre-check                |
| Wrong bucket modified                | Bucket name checked before operations              |
| Forgotten lab resources create costs | Deliberate cleanup after testing                   |

## Limitations

This is a secure storage foundation rather than a complete document-management system.

It does not yet provide approval workflows, malware scanning, a user-facing document portal, detailed audit dashboards or automatic retention management.

Encryption does not replace access control. A valid authorised identity can still read permitted data, so IAM, MFA and credential protection remain important.

## Cost and Cleanup

S3 storage and API requests may create charges.

Versioning can increase storage use because older versions continue to consume storage.

A production system should use lifecycle rules based on the organisation's retention requirements.

For this lab, the bucket should either be deliberately retained for another exercise or safely removed once the project evidence and documentation are complete.

Because versioning is enabled, all object versions and delete markers must be removed before the bucket itself can be deleted.
