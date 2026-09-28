# Incident Intake Operations Runbook

## Trigger

Begin this procedure when:

- CloudWatch raises an alarm;
- the API returns unexpected 5xx responses;
- reports appear not to be stored;
- high-severity notification delivery appears to fail.

## 1. Identify

Record:

- alert time;
- affected environment;
- request ID where available;
- report ID where available;
- current deployed version.

Do not copy report summaries or sensitive information
into operational notes.

## 2. Inspect logs

Search CloudWatch using the request ID or report ID.

Determine whether the failure occurred during:

- validation;
- DynamoDB persistence;
- SNS publishing;
- another Lambda operation.

## 3. Confirm data state

Use DynamoDB GetItem with the known idempotency key.

Determine whether the report:

- was never stored;
- was stored successfully;
- was stored with notification pending;
- was fully processed.

Do not blindly resubmit a report before checking its
existing state.

## 4. Mitigate

Possible actions include:

- retrying a safe operation;
- restoring the previous Lambda version;
- stopping a faulty release;
- investigating AWS service or IAM failures.

Preserve idempotency during recovery.

## 5. Communicate

Record:

- what failed;
- current impact;
- mitigation performed;
- whether reports or notifications were affected.

Do not expose fictional or real report contents unnecessarily.

## 6. Verify recovery

Confirm:

- API responds correctly;
- DynamoDB persistence works;
- duplicate protection works;
- CloudWatch errors have stopped;
- high-severity notification path works.

## 7. Record outcome

Document:

- root cause;
- timeline;
- affected version;
- recovery action;
- evidence;
- follow-up improvement.
