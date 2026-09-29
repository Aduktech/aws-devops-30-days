## Project 01 — AWS/S3 Authentication

### What failed?

AWS commands could not always run when the temporary
Identity Center session was unavailable or expired.

### How I found the cause

I checked the active AWS identity and CLI authentication
state rather than assuming the S3 configuration was broken.

### What I changed

I used the dedicated AWS CLI profile and renewed the
Identity Center session when required.

### How I would prevent it next time

I would include authentication verification as a
pre-deployment check and continue using short-lived
credentials rather than static access keys.


## Project 02 — Kubernetes Image Availability

### What failed?

A deliberately bad Kubernetes release could not start
because the requested container image did not exist.

### How I found the cause

I checked Pod status, described the failed Pod and reviewed
Kubernetes events, which exposed the image pull failure.

### What I changed

I rolled the Deployment back to the previous working image.

### How I would prevent it next time

CI should verify that the intended image exists and passes
tests/security scanning before deployment.

## Project 03 — Terraform IAM Permissions

### What failed?

Terraform operations failed with AccessDenied errors for
specific IAM and AWS API actions.

### How I found the cause

I read the AWS error response and identified the exact
denied action rather than treating it as a generic
Terraform failure.

### What I changed

I reviewed the IAM Identity Center permission set and
identified the minimum permissions required by the
Terraform workflow.

### How I would prevent it next time

I would derive deployment permissions from the Terraform
resource requirements before applying infrastructure and
test them in a non-production environment.


## Project 04 — Serverless Request Reliability

### What failed?

The initial local design stored reports in application
memory, which could not provide reliable duplicate
protection across Lambda execution environments.

The first notification design also exposed a failure window
between storing a report and publishing its SNS message.

### How I found the cause

I analysed retries and the sequence of persistence and
notification operations.

### What I changed

I moved duplicate protection to a DynamoDB conditional
write using an idempotency key and request fingerprint.

### How I would prevent it next time

I would use a durable outbox or event-driven notification
workflow so notification delivery can be retried
independently without creating duplicate reports.
