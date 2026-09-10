import os
import logging

from fastapi import FastAPI, status
from pydantic import BaseModel, Field


APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

app = FastAPI(
    title="Inventory Alert API",
    version="0.1.0",
)


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


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    quantity: int = Field(ge=0)
    reorder_level: int = Field(ge=0)


@app.get("/")
def root():
    return {
        "service": "inventory-alert-api",
        "version": "0.1.0",
        "environment": APP_ENV,
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": APP_ENV,
    }


@app.get("/items")
def get_items():
    return items


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    new_item = {
        "id": max((existing["id"] for existing in items), default=0) + 1,
        "name": item.name,
        "quantity": item.quantity,
        "reorder_level": item.reorder_level,
    }

    items.append(new_item)

    logger.info("Created inventory item: %s", new_item["name"])

    return new_item
