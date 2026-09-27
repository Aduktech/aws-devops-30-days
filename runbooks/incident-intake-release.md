# Incident Intake Release Runbook

## Before release

- Confirm CI tests and security checks pass.
- Review the Terraform plan.
- Record the Git commit and previous working version.
- Confirm monitoring and rollback instructions are ready.
- Obtain human approval.

## Release checks

1. Confirm the Lambda deployment completed.
2. Send a fictional test report.
3. Confirm the expected HTTP response.
4. Confirm the report was stored once.
5. Retry with the same idempotency key.
6. Confirm that no duplicate record was created.
7. Inspect CloudWatch logs and metrics.
8. Confirm notification delivery for a high-severity test.

## Rollback criteria

Investigate and initiate rollback if:

- The 5-minute API error rate exceeds 2%.
- The health or synthetic check fails twice consecutively.
- New reports are being lost or incorrectly duplicated.
- The release introduces a significant security issue.

## Recovery

- Stop further rollout.
- Identify the last known-good application version.
- Restore that version using the approved deployment method.
- Re-run synthetic tests.
- Check DynamoDB records and pending notifications.
- Confirm error rates return to acceptable levels.
- Record the incident and recovery evidence.

## Important

Do not automatically roll back database schema changes
without confirming compatibility and data safety.
