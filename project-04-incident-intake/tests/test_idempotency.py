import json
from pathlib import Path

from app.idempotency import report_fingerprint
from app.validation import IncidentReport


EXAMPLE = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "report.json"
)


def test_identical_reports_have_same_fingerprint():
    data = json.loads(EXAMPLE.read_text())

    first = IncidentReport.model_validate(data)
    second = IncidentReport.model_validate(data)

    assert report_fingerprint(first) == report_fingerprint(second)


def test_changed_report_has_different_fingerprint():
    data = json.loads(EXAMPLE.read_text())

    first = IncidentReport.model_validate(data)

    data["summary"] = "Simulated medical emergency drill"
    second = IncidentReport.model_validate(data)

    assert report_fingerprint(first) != report_fingerprint(second)
