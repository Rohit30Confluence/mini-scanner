.PHONY: install lint format test coverage build clean

install:
	pip install -e .[dev]

format:
	black .
	isort .

lint:
	ruff check .
	mypy mini_scanner

test:
	pytest

coverage:
	pytest --cov=mini_scanner --cov-report=term-missing

build:
	python -m build

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	find . -type d -name "__pycache__" -exec rm -rf {} +