# ============================================================================
# mini-scanner Makefile
# ============================================================================

PYTHON ?= python
PIP ?= pip
PACKAGE := mini_scanner

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install       Install package"
	@echo "  dev           Install development dependencies"
	@echo "  test          Run test suite"
	@echo "  test-cov      Run tests with coverage"
	@echo "  lint          Run Ruff"
	@echo "  format        Format code"
	@echo "  typecheck     Run mypy"
	@echo "  check         Run all quality checks"
	@echo "  build         Build package"
	@echo "  clean         Remove generated files"
	@echo "  precommit     Run pre-commit on all files"

install:
	$(PIP) install -e .

dev:
	$(PIP) install -r requirements-dev.txt

test:
	pytest -v

test-cov:
	pytest --cov=$(PACKAGE) --cov-report=term-missing --cov-report=xml

lint:
	ruff check .

format:
	black .
	isort .
	ruff format .

typecheck:
	mypy $(PACKAGE)

check:
	black --check .
	isort --check-only .
	ruff check .
	pytest -v

build:
	$(PYTHON) -m build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -f coverage.xml

precommit:
	pre-commit run --all-files