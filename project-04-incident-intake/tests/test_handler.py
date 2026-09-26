import json

import pytest

from app import handler


@pytest.fixture(autouse=True)
def clear_reports():
    handler.REPORTS.clear()
    yield
    handler.REPORTS.clear()


def make_event(key="demo-report-001", **changes):
    report = {
        "category": "fire",
        "severity": "high",
        "location_code": "LAB-001",
        "summary": "Simulated fire drill incident",
        "time_received": "2026-09-24T09:00:00Z",
    }
    report.update(changes)

    return {
        "headers": {"Idempotency-Key": key},
        "body": json.dumps(report),
    }


def test_new_report():
    result = handler.lambda_handler(make_event(), None)
    assert result["statusCode"] == 201
    assert json.loads(result["body"])["notification_required"]


def test_identical_retry():
    event = make_event()

    first = handler.lambda_handler(event, None)
    second = handler.lambda_handler(event, None)

    assert first["statusCode"] == 201
    assert second["statusCode"] == 200

    first_id = json.loads(first["body"])["report_id"]
    second_id = json.loads(second["body"])["report_id"]

    assert first_id == second_id
    assert len(handler.REPORTS) == 1


def test_conflicting_retry():
    handler.lambda_handler(make_event(), None)

    result = handler.lambda_handler(
        make_event(summary="Different simulated incident"),
        None,
    )

    assert result["statusCode"] == 409


def test_invalid_severity():
    result = handler.lambda_handler(
        make_event(severity="critical"),
        None,
    )

    assert result["statusCode"] == 400


def test_invalid_json():
    event = make_event()
    event["body"] = "{broken"

    result = handler.lambda_handler(event, None)

    assert result["statusCode"] == 400


def test_low_severity_requires_no_notification():
    result = handler.lambda_handler(
        make_event(severity="low"),
        None,
    )

    assert result["statusCode"] == 201
    assert not json.loads(result["body"])["notification_required"]


def test_unexpected_error(monkeypatch):
    def fail(_report):
        raise RuntimeError("Simulated internal failure")

    monkeypatch.setattr(handler, "report_fingerprint", fail)

    result = handler.lambda_handler(make_event(), None)

    assert result["statusCode"] == 500
    assert "Simulated internal failure" not in result["body"]
