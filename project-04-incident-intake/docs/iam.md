# IAM Permissions — Incident Intake

## Purpose

This document defines the intended IAM permissions for the serverless incident intake system. All components must follow the principle of least privilege.

## IAM Permission Matrix

| Principal | Permission | Scope |
|---|---|---|
| API Gateway | Invoke Lambda (`lambda:InvokeFunction`) | Incident intake function only |
| Intake Lambda execution role | `dynamodb:PutItem`, `dynamodb:GetItem` | Incident reports table |
| Notification worker execution role | DynamoDB read/update (`GetItem`, `Query`, `UpdateItem`) and `sns:Publish` | Outbox table and incident SNS topic |
| Intake Lambda execution role | CloudWatch Logs write | Intake function's log group |
| Notification worker execution role | CloudWatch Logs write | Notification worker's log group |
| CloudWatch alarm | Publish alarm notification to SNS | Operations SNS topic |

## Security Requirements

- Use separate IAM execution roles for the intake function and notification worker.
- Grant API Gateway permission to invoke only the incident intake function through a resource-based Lambda policy.
- Restrict DynamoDB permissions to the tables and operations each function requires.
- Restrict SNS publishing to the designated incident or operations topic.
- Restrict CloudWatch Logs write access to each function's log group.
- Configure the CloudWatch alarm's SNS notification through the designated operations topic and its appropriate topic policy.
- Do not grant `AdministratorAccess` to either Lambda execution role.
- Review permissions before deploying to production.

## Implementation Note

These are the intended permissions for the final architecture. The actual IAM policies and resource ARNs will be configured during deployment.
