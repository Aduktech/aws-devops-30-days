# Day 7 - S3 Access and Recovery

## What I Learned

Today I completed the controlled S3 file-handover project.

I learned that a normal uploader should not receive the same permissions as an engineer who manages the bucket.

The uploader policy limits listing and uploading to the `forms/` prefix and allows only required objects to be read.

## Recovery

I identified the Version ID of the original fictional form.

I retrieved the old version and copied it to a separate recovery key.

The current form remained Approved while the recovery copy contained the original Draft version.

## Documentation

I created an upload-and-recovery runbook and a project README.

The README records the architecture, threats, controls, limitations and cleanup considerations.

## Main Lesson

Reliable cloud storage requires access control, version recovery, documented operating procedures and safe cleanup in addition to simply storing files.
