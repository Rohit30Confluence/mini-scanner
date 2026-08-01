# Contributing to Mini Scanner

First off, thank you for considering contributing to Mini Scanner!

We welcome bug reports, feature requests, documentation improvements, code contributions, and ideas that improve the project.

---

# Table of Contents

- Code of Conduct
- Getting Started
- Development Setup
- Running Tests
- Coding Standards
- Commit Messages
- Pull Requests
- Reporting Bugs
- Suggesting Features

---

# Code of Conduct

By participating in this project, you agree to follow our Code of Conduct.

Please read the `CODE_OF_CONDUCT.md` before contributing.

---

# Getting Started

Fork the repository.

Clone your fork.

```bash
git clone https://github.com/YOUR_USERNAME/mini-scanner.git

cd mini-scanner
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements-dev.txt

pip install -e .
```

---

# Running Tests

Run all tests.

```bash
pytest
```

Run coverage.

```bash
pytest --cov=mini_scanner
```

---

# Code Style

This project uses:

- Black
- Ruff
- isort
- MyPy

Before submitting a Pull Request, run:

```bash
black .

isort .

ruff check .

mypy .

pytest
```

---

# Commit Messages

Use Conventional Commits.

Examples:

```
feat(scanner): add banner grabbing

fix(parser): validate port ranges

docs(readme): improve installation guide

test(scanner): increase coverage

refactor(output): simplify formatting
```

---

# Pull Requests

Before opening a Pull Request:

- Ensure tests pass.
- Update documentation if needed.
- Add tests for new functionality.
- Keep changes focused and small.
- Write a clear description of the changes.

---

# Reporting Bugs

Please include:

- Operating System
- Python Version
- Steps to Reproduce
- Expected Behavior
- Actual Behavior
- Error Messages
- Logs (if available)

---

# Suggesting Features

Feature requests should include:

- Problem statement
- Proposed solution
- Alternatives considered
- Additional context

---

# Development Principles

We value:

- Readability over cleverness.
- Simplicity over unnecessary complexity.
- Clear documentation.
- Comprehensive testing.
- Backward compatibility where practical.

---

# Project Goals

Mini Scanner aims to be:

- Educational
- Modular
- Well-tested
- Easy to understand
- Easy to extend
- Friendly to contributors

---

# Questions?

If you have questions or ideas, please open a GitHub Discussion or Issue.

We appreciate every contribution, no matter how small.

Happy coding!