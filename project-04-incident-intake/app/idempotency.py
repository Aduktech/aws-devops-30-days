import hashlib
import json

from app.validation import IncidentReport


def report_fingerprint(report: IncidentReport) -> str:
    canonical = json.dumps(
        report.model_dump(mode="json"),
        sort_keys=True,
        separators=(",", ":"),
    )

    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
