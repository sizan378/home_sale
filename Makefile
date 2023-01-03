ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env


endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down 

show-logs:
	docker compose logs

migrate:
	docker compose exec home-sales python3 manage.py migrate

makemigrations:
	docker compose exec home-sales python3 manage.py makemigrations

superuser:
	docker compose exec home-sales python3 manage.py createsuperuser

collectstatic:
	docker compose exec home-sales python3 manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect home_sale_postgres_data

home-sales-db:
	docker compose exec postgres-db psql --username=admin --dbname=homesale

pytest:
	docker compose exec home-sales pytest -p no:warnings --cov=.

pytest-html:
	docker compose exec home-sales pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker compose exec home-sales flake8 .

black-check:
	docker compose exec home-sales black --check --exclude=migrations .

black-diff:
	docker compose exec home-sales black --diff --exclude=migrations .
	
black:
	docker compose exec home-sales black --exclude=migrations .

isort-check:
	docker compose exec home-sales isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose exec home-sales isort . --diff --skip env --skip migrations

isort:
	docker compose exec home-sales isort . --skip env --skip migrations

