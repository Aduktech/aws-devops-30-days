
import json
import logging
import sys
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

logger = logging.getLogger("inventory-api")
logger.setLevel(logging.INFO)
logger.handlers.clear()

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)


def log_event(event: str, **details) -> None:
    """Write one JSON log event to standard output."""
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": "INFO",
        "event": event,
        **details,
    }

    logger.info(json.dumps(record))


# ---------------------------------------------------------
# API
# ---------------------------------------------------------

app = FastAPI(
    title="Inventory Alert API",
    version="0.1.0",
    description="A fictional inventory service for DevOps training.",
)


# ---------------------------------------------------------
# Data model
# ---------------------------------------------------------

class InventoryItem(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    quantity: int = Field(ge=0, le=100000)
    reorder_level: int = Field(ge=0, le=100000)


# Fictional training data only.
items = [
    {
        "id": 1,
        "name": "Printer Paper",
        "quantity": 24,
        "reorder_level": 10,
    },
    {
        "id": 2,
        "name": "Blue Pens",
        "quantity": 8,
        "reorder_level": 15,
    },
    {
        "id": 3,
        "name": "USB-C Cables",
        "quantity": 6,
        "reorder_level": 5,
    },
]


# ---------------------------------------------------------
# Request logging
# ---------------------------------------------------------

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)

    log_event(
        "request_completed",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
    )

    return response


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "service": "inventory-alert-api",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "inventory-alert-api",
    }


@app.get("/items")
def list_items():
    return {
        "count": len(items),
        "items": items,
    }


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: InventoryItem):
    existing = next(
        (
            current
            for current in items
            if current["name"].lower() == item.name.lower()
        ),
        None,
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="An item with this name already exists.",
        )

    new_item = {
        "id": len(items) + 1,
        **item.model_dump(),
    }

    items.append(new_item)

    log_event(
        "inventory_item_created",
        item_id=new_item["id"],
        item_name=new_item["name"],
    )

    return new_item
