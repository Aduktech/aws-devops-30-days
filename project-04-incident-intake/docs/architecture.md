# Incident Intake — Serverless Architecture

## Purpose

Receive fictional incident reports through an API,
validate them, prevent duplicates and store them.

High-severity reports trigger notifications.

## Architecture

Client
  |
  v
API Gateway
  |
  v
AWS Lambda
  |
  +----> DynamoDB
  |       Store unique reports
  |
  +----> SNS
          Notify for new high-severity reports

Lambda Errors
  |
  v
CloudWatch Alarm
  |
  v
SNS Operations Alert

## Security

- Use fictional incident data only.
- Validate all API input.
- Do not log report contents.
- Use least-privilege IAM permissions.
- Do not store AWS credentials in source code.
- Require appropriate API access controls.

## Cost

- No EC2 instances.
- No Kubernetes cluster.
- No NAT Gateway.
- Use Lambda, API Gateway, DynamoDB and SNS.
- Configure AWS Budget alerts before deployment.
