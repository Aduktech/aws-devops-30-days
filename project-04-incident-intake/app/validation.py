from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class IncidentReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: Literal["fire", "security", "medical", "other"]
    severity: Literal["low", "medium", "high"]
    location_code: Literal["LAB-001", "LAB-002", "LAB-003"]
    summary: str = Field(min_length=10, max_length=300)
    time_received: datetime

    @field_validator("time_received")
    @classmethod
    def require_timezone(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("Timestamp must include a timezone")
        return value
