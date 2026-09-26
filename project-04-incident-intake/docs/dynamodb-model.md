# DynamoDB Data Model

Table: incident-reports
Partition key: idempotency_key (String)

Example attributes:
- idempotency_key
- report_id
- request_fingerprint
- category
- severity
- location_code
- summary
- time_received
- notification_status

Access patterns:
1. Insert a report only if its idempotency key is absent.
2. Retrieve an existing submission by its idempotency key.
3. Return the original report ID for identical retries.
4. Reject reuse of the same key with different report content.

Use a conditional PutItem with:
attribute_not_exists(idempotency_key)

Notification processing will need a durable outbox
and an appropriate index or separate table.

Do not scan the entire reports table to find
pending notifications.
