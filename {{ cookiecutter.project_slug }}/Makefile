.PHONY: install-poetry lock install test lint format run docker-build docker-run

# Install
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

lock:
	poetry lock

install:
	poetry install

# Test
test:
	poetry run pytest

# Lint
lint:
	poetry run ruff check --fix src tests || exit 1
	poetry run ruff format -q src tests || exit 1
	poetry run mypy src tests --show-error-codes || exit 1

format:
	poetry run ruff check src tests --fix
	poetry run ruff format src tests

# Run
run:
	poetry run start

# Docker
docker-build:
	docker build . -t {{ cookiecutter.project_slug }}

docker-run:
	docker run {{ cookiecutter.project_slug }}
