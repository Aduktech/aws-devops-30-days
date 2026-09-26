import json
import logging
import os
import uuid

from pydantic import ValidationError

from app.idempotency import report_fingerprint
from app.validation import IncidentReport


logger = logging.getLogger("incident-intake")
logger.setLevel(logging.INFO)

# Local testing only. Replace with DynamoDB before deployment.
REPORTS = {}


def log_event(level, event, **fields):
    """Log metadata without exposing report contents."""
    message = json.dumps({"event": event, **fields})
    getattr(logger, level)(message)


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    try:
        headers = {
            key.lower(): value
            for key, value in (event.get("headers") or {}).items()
        }

        key = headers.get("idempotency-key")

        if not isinstance(key, str) or not (
            8 <= len(key) <= 128
        ):
            return response(
                400,
                {"error": "A valid Idempotency-Key is required"},
            )

        try:
            body = json.loads(event.get("body") or "{}")
        except (json.JSONDecodeError, TypeError):
            return response(
                400,
                {"error": "Request body must be valid JSON"},
            )

        if not isinstance(body, dict):
            return response(
                400,
                {"error": "Request body must be a JSON object"},
            )

        try:
            report = IncidentReport.model_validate(body)
        except ValidationError:
            log_event("warning", "validation_failed")
            return response(
                400,
                {"error": "Invalid report fields"},
            )

        fingerprint = report_fingerprint(report)

        if key in REPORTS:
            existing = REPORTS[key]

            if existing["fingerprint"] != fingerprint:
                return response(
                    409,
                    {"error": "Idempotency key conflict"},
                )

            log_event(
                "info",
                "duplicate_request",
                report_id=existing["report_id"],
            )

            return response(
                200,
                {
                    "report_id": existing["report_id"],
                    "status": "already_processed",
                },
            )

        report_id = str(uuid.uuid4())

        notification_required = report.severity == "high"

        REPORTS[key] = {
            "report_id": report_id,
            "fingerprint": fingerprint,
            "report": report.model_dump(mode="json"),
            "notification_status": (
                "pending" if notification_required
                else "not_required"
            ),
        }

        log_event(
            "info",
            "report_created",
            report_id=report_id,
            severity=report.severity,
            notification_required=notification_required,
        )

        return response(
            201,
            {
                "report_id": report_id,
                "status": "created",
                "notification_required": notification_required,
            },
        )

    except Exception:
        log_event("error", "unexpected_processing_error")

        return response(
            500,
            {"error": "Internal server error"},
        )
