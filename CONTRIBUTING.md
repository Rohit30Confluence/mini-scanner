# Contributing to mini-scanner

Thank you for your interest in contributing to **mini-scanner**.

We welcome bug reports, feature requests, documentation improvements, and code contributions.

---

# Getting Started

## 1. Fork the Repository

Click **Fork** on GitHub and clone your fork.

```bash
git clone https://github.com/YOUR_USERNAME/mini-scanner.git
cd mini-scanner
```

Add the upstream repository:

```bash
git remote add upstream https://github.com/Rohit30Confluence/mini-scanner.git
```

---

## 2. Create a Virtual Environment

Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -e .
pip install -r requirements-dev.txt
```

---

# Development Workflow

Create a feature branch.

```bash
git checkout -b feature/my-feature
```

Keep your branch up to date.

```bash
git fetch upstream
git rebase upstream/main
```

---

# Code Style

Before opening a Pull Request, run:

```bash
black .
isort .
pytest -v
```

If type checking is configured:

```bash
mypy .
```

---

# Testing

Run the complete test suite.

```bash
pytest -v
```

All tests should pass before submitting a Pull Request.

---

# Commit Messages

Use clear commit messages.

Examples:

```
Fix banner parsing
Add IPv6 timeout tests
Improve CLI output
Refactor scanner worker pool
```

---

# Pull Requests

Please ensure:

- Tests pass
- Documentation is updated if needed
- No unnecessary files are included
- Commits are clean and focused

---

# Reporting Bugs

Include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Complete error output

---

# Suggesting Features

Feature requests should explain:

- The problem
- The proposed solution
- Why it benefits users
- Possible alternatives

---

# Security

Do **not** report security vulnerabilities through public GitHub Issues.

Please follow the instructions in:

`SECURITY.md`

---

# Code of Conduct

By participating in this project, you agree to follow the project's Code of Conduct.

---

Thank you for helping improve **mini-scanner**.