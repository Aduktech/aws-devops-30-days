.PHONY: build up lint format-check test ci logs down

build:
	docker compose build

up:
	docker compose up -d --build

lint:
	ruff check .

format-check:
	ruff format --check .

test:
	docker compose exec api pytest -q

ci:
	ruff check .
	ruff format --check .
	pytest -q
	docker build -t inventory-alert-api:ci .

logs:
	docker compose logs --follow

down:
	docker compose down
