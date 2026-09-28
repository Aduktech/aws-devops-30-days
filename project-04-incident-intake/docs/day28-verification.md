# Day 28 Verification Evidence

Git commit:
Date:
Environment: AWS lab / eu-west-2

## Tests

High severity request: PASS / FAIL
HTTP response: 201 / other
DynamoDB persistence: PASS / FAIL
SNS subscription confirmed: YES / NO
SNS notification received: YES / NO
CloudWatch structured log: PASS / FAIL

Invalid JSON rejected: PASS / FAIL
Invalid JSON stored: NO / YES

Low severity request: PASS / FAIL
Low severity stored: PASS / FAIL
SNS notification sent for low severity: NO / YES

Identical retry: 200 / other
Duplicate record created: NO / YES
Conflicting retry: 409 / other

CloudWatch alarm:
Outstanding issues:

## Known prototype limitations

- Public lab API has no production authentication.
- Notification retry is not yet durable.
- This is not an emergency-response production system.
