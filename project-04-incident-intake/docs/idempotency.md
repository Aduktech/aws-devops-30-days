# Idempotency Design

## Problem

A client may retry a report after a network failure.
Retries must not create duplicate reports.

## Approach

Every request must include an Idempotency-Key header.

1. Validate the incoming report.
2. Calculate a SHA-256 fingerprint of its normalised content.
3. Attempt a conditional write to DynamoDB using the
   idempotency key as the partition key.
4. Use attribute_not_exists to prevent duplicate creation.
5. If the key already exists:
   - Same fingerprint: return the existing report.
   - Different fingerprint: return HTTP 409.

## High-Severity Notifications

A new, validated high-severity report requires an SNS alert.

Record a durable notification task when saving the report.
A separate worker can publish the notification and retry
temporary failures.

Use a stable notification ID to identify repeated delivery
attempts.

## Important Limitation

A conditional DynamoDB write prevents duplicate report
records, but SNS delivery is not guaranteed to happen
exactly once.

Notification consumers must also handle duplicates.
