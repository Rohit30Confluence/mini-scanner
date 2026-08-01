# Troubleshooting

This guide helps diagnose and resolve common issues encountered when installing, running, or developing **mini-scanner**.

---

# Installation Issues

## Python Not Found

### Symptoms

```text
python: command not found
```

or

```text
python3: command not found
```

### Solution

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed, install Python 3.11 or later and ensure it is available in your system's `PATH`.

---

## pip Not Found

### Symptoms

```text
pip: command not found
```

### Solution

Use:

```bash
python -m pip --version
```

If necessary:

```bash
python -m ensurepip --upgrade
```

---

## Virtual Environment Issues

Create:

```bash
python -m venv .venv
```

Activate:

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

# Scanner Issues

## Host Cannot Be Resolved

### Symptoms

```text
Name or service not known
```

### Checks

- Verify hostname spelling.
- Confirm DNS resolution.
- Test with:

```bash
ping example.com
```

or

```bash
nslookup example.com
```

---

## All Ports Report Closed

Possible causes:

- Host offline
- Firewall filtering
- Wrong IP
- Incorrect timeout

Try increasing timeout:

```bash
mini-scanner example.com --timeout 5
```

---

## Scan Is Slow

Possible causes:

- High latency
- Large port range
- Low worker count

Increase workers:

```bash
mini-scanner example.com \
    --workers 200
```

Reduce timeout:

```bash
mini-scanner example.com \
    --timeout 1
```

---

## Banner Is Empty

Many services:

- Disable banners
- Require protocol-specific requests
- Delay responses

An empty banner does not necessarily indicate a problem.

---

# Docker Issues

## Docker Build Fails

Check Docker:

```bash
docker --version
```

Rebuild without cache:

```bash
docker build --no-cache -t mini-scanner .
```

---

## Container Exits Immediately

Run:

```bash
docker run --rm mini-scanner --help
```

Verify the container entrypoint and command configuration.

---

# Development Issues

## Tests Fail

Run:

```bash
pytest -vv
```

Run one file:

```bash
pytest tests/test_scanner.py
```

Run one test:

```bash
pytest tests/test_scanner.py::test_scan_single_port
```

---

## Formatting Fails

Format everything:

```bash
make format
```

Or:

```bash
black .
isort .
ruff format .
```

---

## Lint Errors

Run:

```bash
ruff check .
```

Many issues can be fixed automatically:

```bash
ruff check --fix .
```

---

## Type Checking Errors

Run:

```bash
mypy mini_scanner
```

Review the reported files and add or correct type annotations where appropriate.

---

# CI Issues

## GitHub Actions Fails

Verify locally:

```bash
make check
```

Also run:

```bash
tox
```

Ensure all tests and quality checks pass before pushing changes.

---

## Documentation Build Fails

Build locally:

```bash
mkdocs build --strict
```

Common causes:

- Missing documentation pages
- Broken links
- Invalid Markdown
- Incorrect navigation entries

---

# Packaging Issues

Build:

```bash
python -m build
```

Verify:

```bash
twine check dist/*
```

If the build fails, confirm that `pyproject.toml` is valid and required files are present.

---

# Networking Issues

## Connection Timed Out

Increase timeout:

```bash
mini-scanner example.com --timeout 5
```

Confirm:

- Internet connectivity
- Firewall settings
- Target availability

---

## Permission Denied

Some environments restrict outbound network access.

Verify local firewall rules and organizational policies before scanning.

---

# Performance Tips

- Scan only required ports.
- Reuse a `Scanner` instance when using the Python API.
- Increase worker threads gradually while monitoring system resources.
- Disable banner grabbing when only port status is needed.

---

# Before Reporting a Bug

Include:

- Operating system
- Python version
- mini-scanner version
- Command executed
- Expected behavior
- Actual behavior
- Full error message
- Steps to reproduce

---

# Getting Help

If the issue persists:

1. Review the documentation.
2. Search existing GitHub Issues.
3. Open a new Issue with detailed reproduction steps.
4. Start a GitHub Discussion for design or usage questions.

Providing complete information helps others reproduce and resolve issues more quickly.