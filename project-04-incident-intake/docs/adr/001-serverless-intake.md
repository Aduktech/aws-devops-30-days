# ADR 001: Serverless Incident Intake

Status: Accepted for the learning project

## Context

We need to receive occasional fictional incident reports,
validate them, prevent duplicate records and notify a
designated recipient about high-severity reports.

Traffic is expected to be low and unpredictable.

## Decision

Use:
- API Gateway HTTP API for HTTPS requests.
- AWS Lambda for validation and processing.
- DynamoDB for unique reports and notification tasks.
- SNS for high-severity notifications.
- CloudWatch for logs, metrics and error alarms.
- Terraform for repeatable deployment.

## Reasons

The application is event-driven and does not require
an always-running server.

AWS manages the underlying infrastructure, reducing
the operational work needed for this small project.

## Trade-offs

- Lambda has execution-time and concurrency limits.
- Cold starts may affect occasional requests.
- Several AWS services must be configured securely.
- Notifications require retry and duplicate-handling logic.
- Usage-based services can still generate charges.

## Alternatives

EC2: A continuously running server is unnecessary
for the expected traffic.

Kubernetes: The operational complexity is not justified
for this small, single-service learning project.

## Constraints

Use fictional data only.
No real incident reports or personal information.
No production deployment during the learning exercise.
