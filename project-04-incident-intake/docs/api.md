# Incident Intake API

## Endpoint

POST /reports

## Required header

Idempotency-Key: unique-client-generated-key

## Request fields

| Field | Type | Rules |
|---|---|---|
| category | string | fire, security, medical, other |
| severity | string | low, medium, high |
| location_code | string | LAB-001, LAB-002, LAB-003 |
| summary | string | 10–300 characters |
| time_received | string | ISO 8601 timestamp |

## Responses

201: New report accepted and stored.

200: Identical request already processed.

400: Invalid request.

409: Idempotency key reused with different content.

500: Unexpected processing error.

## Restrictions

Use fictional data only.
No names, phone numbers, addresses or real incidents.
