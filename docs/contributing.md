# Contributing

Thank you for your interest in contributing to **mini-scanner**.

Whether you're fixing a bug, improving documentation, adding tests, or implementing a new feature, your contribution is appreciated.

---

# Before You Start

Before opening an Issue or Pull Request:

- Search existing Issues to avoid duplicates.
- Read the project's `CONTRIBUTING.md`.
- Ensure your change aligns with the project's goals.
- Keep Pull Requests focused on a single logical change.

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/Rohit30Confluence/mini-scanner.git
cd mini-scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e ".[dev]"
```

or

```bash
pip install -r requirements-dev.txt
```

---

# Creating a Branch

Always create a feature branch.

```bash
git checkout -b feature/add-ipv6-support
```

Examples:

```
feature/banner-improvements
bugfix/socket-timeout
docs/api-reference
refactor/thread-pool
```

---

# Code Style

Follow these guidelines:

- PEP 8
- Black formatting
- isort import ordering
- Ruff linting
- mypy type checking
- Descriptive naming
- Small, focused functions
- Public APIs should include docstrings

---

# Running Checks

Format:

```bash
make format
```

Lint:

```bash
make lint
```

Type checking:

```bash
make typecheck
```

Run tests:

```bash
pytest
```

Run everything:

```bash
make check
```

---

# Writing Tests

Every new feature or bug fix should include appropriate tests.

Tests belong in:

```
tests/
```

Naming:

```
test_scanner.py
test_cli.py
test_config.py
```

Keep tests:

- Independent
- Repeatable
- Easy to understand
- Fast to execute

---

# Documentation

Update documentation whenever behavior changes.

Possible files include:

```
README.md
docs/
CHANGELOG.md
```

Examples are encouraged for new features.

---

# Commit Messages

Use clear, concise commit messages.

Good examples:

```
Add IPv6 scanning support

Fix socket timeout handling

Improve CLI help output

Add unit tests for banner grabbing

Update installation guide
```

Avoid:

```
fix

update

changes

misc
```

---

# Pull Requests

Before submitting:

- Sync with the latest `main` branch.
- Ensure CI passes.
- Resolve merge conflicts.
- Update documentation if necessary.
- Keep the PR focused on a single topic.

Include:

- What changed
- Why it changed
- How it was tested
- Any known limitations

---

# Reviewing Code

When reviewing contributions:

- Verify correctness.
- Check readability.
- Suggest improvements respectfully.
- Ensure tests cover new functionality.
- Confirm documentation remains accurate.

---

# Reporting Bugs

Include:

- Operating system
- Python version
- mini-scanner version
- Command executed
- Expected behavior
- Actual behavior
- Error messages or stack traces
- Steps to reproduce

---

# Suggesting Features

Feature requests should explain:

- The problem being solved
- Proposed solution
- Alternative approaches considered
- Potential impact on existing users

---

# Security Issues

Do **not** report security vulnerabilities through public GitHub Issues.

Follow the project's `SECURITY.md` policy for responsible disclosure.

---

# Code of Conduct

All contributors are expected to follow the project's `CODE_OF_CONDUCT.md`.

Be respectful, constructive, and welcoming to others.

---

# Recognition

Every accepted contribution—code, documentation, tests, bug reports, or ideas—helps improve the project and is appreciated.

Thank you for contributing to **mini-scanner**!