import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from app.validation import IncidentReport


EXAMPLE = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "report.json"
)


def test_valid_report():
    data = json.loads(EXAMPLE.read_text())
    report = IncidentReport.model_validate(data)

    assert report.category == "fire"
    assert report.severity == "high"


def test_invalid_severity():
    data = json.loads(EXAMPLE.read_text())
    data["severity"] = "extreme"

    with pytest.raises(ValidationError):
        IncidentReport.model_validate(data)


def test_missing_summary():
    data = json.loads(EXAMPLE.read_text())
    del data["summary"]

    with pytest.raises(ValidationError):
        IncidentReport.model_validate(data)


def test_timestamp_requires_timezone():
    data = json.loads(EXAMPLE.read_text())
    data["time_received"] = "2026-09-24T09:00:00"

    with pytest.raises(ValidationError):
        IncidentReport.model_validate(data)
