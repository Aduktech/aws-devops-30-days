import hashlib
import json
import logging
import os
import re
import uuid
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ddb = boto3.client("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ.get("TABLE_NAME", "")
TOPIC_ARN = os.environ.get("TOPIC_ARN", "")

CATEGORIES = {"fire", "security", "medical", "other"}
SEVERITIES = {"low", "medium", "high"}
LOCATIONS = {"LAB-001", "LAB-002", "LAB-003"}


def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(body),
    }


def log_event(event, **fields):
    logger.info(json.dumps({"event": event, **fields}))


def validate(body):
    if not isinstance(body, dict):
        return "Request body must be a JSON object"

    expected = {"category", "severity", "location_code", "summary"}

    if set(body) != expected:
        return "Required fields: category, severity, location_code, summary"

    if body["category"] not in CATEGORIES:
        return "Invalid category"

    if body["severity"] not in SEVERITIES:
        return "Invalid severity"

    if body["location_code"] not in LOCATIONS:
        return "Invalid fictional location code"

    summary = body["summary"]
    if not isinstance(summary, str) or not 10 <= len(summary) <= 300:
        return "Summary must contain 10–300 characters"

    return None


def lambda_handler(event, context):
    request_id = getattr(context, "aws_request_id", "local-test")

    try:
        headers = {
            str(k).lower(): v
            for k, v in (event.get("headers") or {}).items()
        }
        key = headers.get("idempotency-key", "")

        if not isinstance(key, str) or not re.fullmatch(
            r"[A-Za-z0-9_-]{8,128}", key
        ):
            return respond(400, {"error": "Invalid Idempotency-Key"})

        try:
            body = json.loads(event.get("body") or "")
        except (ValueError, TypeError):
            return respond(400, {"error": "Invalid JSON"})

        error = validate(body)
        if error:
            return respond(400, {"error": error})

        canonical = json.dumps(body, sort_keys=True, separators=(",", ":"))
        fingerprint = hashlib.sha256(canonical.encode()).hexdigest()

        report_id = str(uuid.uuid4())
        received = datetime.now(timezone.utc).isoformat()

        item = {
            "idempotency_key": {"S": key},
            "report_id": {"S": report_id},
            "fingerprint": {"S": fingerprint},
            "category": {"S": body["category"]},
            "severity": {"S": body["severity"]},
            "location_code": {"S": body["location_code"]},
            "summary": {"S": body["summary"]},
            "time_received": {"S": received},
            "notification_status": {
                "S": "pending" if body["severity"] == "high"
                else "not_required"
            },
        }

        try:
            ddb.put_item(
                TableName=TABLE_NAME,
                Item=item,
                ConditionExpression="attribute_not_exists(idempotency_key)",
            )
        except ClientError as exc:
            if exc.response["Error"]["Code"] != "ConditionalCheckFailedException":
                raise

            existing = ddb.get_item(
                TableName=TABLE_NAME,
                Key={"idempotency_key": {"S": key}},
                ConsistentRead=True,
            ).get("Item")

            if not existing:
                raise RuntimeError("Existing report could not be retrieved")

            if existing["fingerprint"]["S"] != fingerprint:
                return respond(409, {"error": "Idempotency key conflict"})

            log_event("duplicate_report", request_id=request_id)
            return respond(200, {
                "report_id": existing["report_id"]["S"],
                "status": "already_processed",
            })

        if body["severity"] == "high":
            try:
                sns.publish(
                    TopicArn=TOPIC_ARN,
                    Subject="Fictional high-severity lab report",
                    Message=json.dumps({
                        "report_id": report_id,
                        "severity": "high",
                        "location_code": body["location_code"],
                        "time_received": received,
                    }),
                )
                ddb.update_item(
                    TableName=TABLE_NAME,
                    Key={"idempotency_key": {"S": key}},
                    UpdateExpression="SET notification_status = :status",
                    ExpressionAttributeValues={
                        ":status": {"S": "published"}
                    },
                )
            except ClientError:
                logger.exception(
                    json.dumps({
                        "event": "notification_failed",
                        "request_id": request_id,
                    })
                )
                return respond(503, {
                    "error": "Report saved; notification pending",
                    "report_id": report_id,
                })

        log_event(
            "report_created",
            request_id=request_id,
            report_id=report_id,
            severity=body["severity"],
        )

        return respond(201, {
            "report_id": report_id,
            "time_received": received,
            "status": "created",
        })

    except Exception:
        logger.exception(json.dumps({
            "event": "processing_failed",
            "request_id": request_id,
        }))
        return respond(500, {"error": "Internal server error"})
