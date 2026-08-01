# Development Guide

This guide explains how to set up a development environment, understand the project structure, run tests, maintain code quality, and contribute to **mini-scanner**.

---

# Prerequisites

Before contributing, install:

- Python 3.11+
- Git
- pip
- Docker (optional)
- Make (optional)

Verify installation:

```bash
python --version
git --version
```

---

# Clone the Repository

```bash
git clone https://github.com/Rohit30Confluence/mini-scanner.git
cd mini-scanner
```

---

# Create a Virtual Environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

# Install Dependencies

Install the package in editable mode:

```bash
pip install -e .
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

or

```bash
pip install -e ".[dev]"
```

---

# Project Structure

```
mini-scanner/
├── mini_scanner/
│   ├── __init__.py
│   ├── scanner.py
│   ├── cli.py
│   ├── config.py
│   ├── exceptions.py
│   └── ...
├── tests/
├── docs/
├── .github/
├── pyproject.toml
├── Makefile
└── README.md
```

---

# Development Workflow

1. Create a new branch:

```bash
git checkout -b feature/my-feature
```

2. Implement your changes.

3. Run formatting and quality checks.

4. Run the full test suite.

5. Commit your changes.

6. Push the branch.

7. Open a Pull Request.

---

# Code Formatting

Format the codebase:

```bash
make format
```

Or run tools individually:

```bash
black .
isort .
ruff format .
```

---

# Linting

```bash
make lint
```

Equivalent:

```bash
ruff check .
```

---

# Type Checking

```bash
make typecheck
```

Equivalent:

```bash
mypy mini_scanner
```

---

# Running Tests

Run all tests:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=mini_scanner --cov-report=term-missing
```

---

# Using Tox

Run every configured environment:

```bash
tox
```

Run a single environment:

```bash
tox -e py313
tox -e lint
tox -e docs
```

---

# Pre-commit Hooks

Install:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

---

# Documentation

Preview documentation locally:

```bash
mkdocs serve
```

Build documentation:

```bash
mkdocs build
```

---

# Docker Development

Build:

```bash
docker build -t mini-scanner .
```

Run:

```bash
docker compose run --rm mini-scanner
```

Run tests:

```bash
docker compose run --rm tests
```

---

# Continuous Integration

Every Pull Request should pass:

- Unit tests
- Code formatting
- Linting
- Type checking
- Dependency review
- CodeQL analysis

Do not merge changes that fail CI.

---

# Release Process

1. Update the version.
2. Update the changelog.
3. Run the full test suite.
4. Create a Git tag.
5. Push the tag.
6. Publish a GitHub Release.
7. Publish to PyPI (if applicable).

---

# Debugging

Useful commands:

```bash
pytest -vv
```

```bash
pytest -k scanner
```

```bash
pytest --lf
```

```bash
pytest --maxfail=1
```

---

# Code Style

- Follow PEP 8.
- Prefer descriptive variable and function names.
- Add type hints where practical.
- Keep functions focused and small.
- Write docstrings for public APIs.
- Add or update tests for new features and bug fixes.

---

# Security

- Never commit secrets or credentials.
- Validate user input.
- Handle network errors gracefully.
- Report security issues privately according to the project's Security Policy.

---

# Getting Help

If you have questions:

- Read the documentation.
- Search existing GitHub Issues.
- Open a new Issue if needed.
- Start a GitHub Discussion for broader design questions.

---

# Contributing Checklist

Before submitting a Pull Request:

- [ ] Tests pass.
- [ ] Code is formatted.
- [ ] Linting passes.
- [ ] Documentation updated.
- [ ] Changelog updated (if applicable).
- [ ] Commit messages are clear.
- [ ] CI passes successfully.

---

# Thank You

Thank you for contributing to **mini-scanner**. Every improvement—whether a bug fix, documentation update, or new feature—helps make the project more useful and maintainable.