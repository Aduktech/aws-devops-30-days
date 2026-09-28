import importlib
import json
import os
from unittest.mock import MagicMock

import pytest
from botocore.exceptions import ClientError

os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"
os.environ["AWS_EC2_METADATA_DISABLED"] = "true"
os.environ["TABLE_NAME"] = "test-table"
os.environ["TOPIC_ARN"] = (
    "arn:aws:sns:eu-west-2:123456789012:test-topic"
)

from app import handler


@pytest.fixture(autouse=True)
def mock_aws(monkeypatch):
    db = MagicMock()
    topic = MagicMock()
    monkeypatch.setattr(handler, "ddb", db)
    monkeypatch.setattr(handler, "sns", topic)
    return db, topic


def event(key="fictional-001", severity="high"):
    return {
        "headers": {"Idempotency-Key": key},
        "body": json.dumps({
            "category": "fire",
            "severity": severity,
            "location_code": "LAB-001",
            "summary": "Fictional smoke report for testing",
        }),
    }


def test_high_severity_is_saved_and_published(mock_aws):
    db, topic = mock_aws
    result = handler.lambda_handler(event(), None)

    assert result["statusCode"] == 201
    db.put_item.assert_called_once()
    topic.publish.assert_called_once()


def test_low_severity_does_not_publish(mock_aws):
    _, topic = mock_aws
    result = handler.lambda_handler(event(severity="low"), None)

    assert result["statusCode"] == 201
    topic.publish.assert_not_called()


def test_invalid_report_is_rejected(mock_aws):
    db, _ = mock_aws
    bad = event()
    bad["body"] = json.dumps({"category": "fire"})

    result = handler.lambda_handler(bad, None)

    assert result["statusCode"] == 400
    db.put_item.assert_not_called()


def test_duplicate_returns_existing_id(mock_aws):
    db, topic = mock_aws

    # First request succeeds
    first = handler.lambda_handler(event(), None)
    first_id = json.loads(first["body"])["report_id"]

    # Save the item written during the first request
    saved_item = db.put_item.call_args.kwargs["Item"]

    # Simulate DynamoDB rejecting the second request as a duplicate
    db.put_item.side_effect = ClientError(
        {
            "Error": {
                "Code": "ConditionalCheckFailedException",
                "Message": "Duplicate",
            }
        },
        "PutItem",
    )

    # Return the previously stored report
    db.get_item.return_value = {"Item": saved_item}

    second = handler.lambda_handler(event(), None)

    assert second["statusCode"] == 200
    assert json.loads(second["body"])["report_id"] == first_id
    assert topic.publish.call_count == 1
