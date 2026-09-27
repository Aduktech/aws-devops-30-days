# AWS Resource Plan

| Resource | Purpose |
|---|---|
| API Gateway | Receive HTTPS requests |
| Lambda | Validate and process reports |
| DynamoDB | Store unique reports and notification tasks |
| SNS reports topic | Deliver high-severity notifications |
| SNS operations topic | Deliver monitoring alerts |
| CloudWatch Logs | Record safe application logs |
| CloudWatch Alarm | Monitor Lambda Errors |
| IAM role | Give Lambda narrowly scoped permissions |

## CloudWatch Alarm

Metric: AWS/Lambda Errors
Statistic: Sum
Period: 5 minutes
Threshold: 1 or more errors
Evaluation periods: 1

## IAM

Lambda requires permission to write to the designated
DynamoDB table, publish to the designated SNS topic,
and write application logs.

Do not use AdministratorAccess.

## Deployment

The resources will be defined with Terraform during
the final project.

No AWS resources are deployed during Day 24.
