# Notification Policy

## Incident notifications

SNS topic: incident-intake-high-severity

Trigger:
- Report passes validation.
- Report is newly created.
- Severity is high.

Recipient:
- My own email address, for lab confirmation only.

Notification content:
- Report ID
- Severity
- Fictional location code
- Time received

Do not send report summaries or personal data.

## Operational notifications

Separate SNS topic: incident-intake-operations

Trigger:
- CloudWatch Lambda Errors alarm reaches ALARM state.

Recipient:
- My own email address, for lab confirmation only.

## Reliability

Store a durable notification task alongside the report.

Use a separate notification worker with retries.

Consumers must tolerate duplicate SNS deliveries.

Do not claim exactly-once notification delivery.
