.PHONY: build up test logs down

build:
	docker compose build

up:
	docker compose up -d --build

test:
	docker compose exec api python -m pytest -q

logs:
	docker compose logs --follow

down:
	docker compose down
