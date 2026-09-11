from fastapi.testclient import TestClient

from app.main import app, items

client = TestClient(app)


def reset_items():
    items[:] = [
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


def setup_function():
    reset_items()


def test_health_returns_200():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_valid_item_creation():
    response = client.post(
        "/items",
        json={
            "name": "Ethernet Cables",
            "quantity": 20,
            "reorder_level": 5,
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Ethernet Cables"
    assert body["quantity"] == 20
    assert body["reorder_level"] == 5


def test_negative_quantity_is_rejected():
    response = client.post(
        "/items",
        json={
            "name": "Invalid Stock",
            "quantity": -10,
            "reorder_level": 5,
        },
    )

    assert response.status_code == 422
