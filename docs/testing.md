# Testing Guide

This document describes the testing strategy, project structure, and best practices for **mini-scanner**.

---

# Testing Philosophy

The project prioritizes:

- Correctness
- Reliability
- Reproducibility
- Maintainability
- Fast feedback

Every new feature should include tests, and every bug fix should include a regression test.

---

# Test Structure

```
tests/
├── test_cli.py
├── test_config.py
├── test_formatter.py
├── test_scanner.py
├── test_utils.py
└── ...
```

Each test file should correspond to a module in `mini_scanner/`.

---

# Running Tests

Run the full test suite:

```bash
pytest -v
```

Run with coverage:

```bash
pytest --cov=mini_scanner --cov-report=term-missing
```

Run a specific test file:

```bash
pytest tests/test_scanner.py
```

Run a single test:

```bash
pytest tests/test_scanner.py::test_scan_single_port
```

---

# Coverage Goals

Recommended minimums:

| Metric | Goal |
|---------|------|
| Statements | 90%+ |
| Branches | 85%+ |
| Critical modules | 100% preferred |

Coverage is a useful indicator, but it does not replace meaningful test cases.

---

# Writing Tests

Tests should be:

- Independent
- Deterministic
- Fast
- Easy to read
- Focused on one behavior

Prefer descriptive test names:

```python
def test_closed_port_returns_closed_state():
    ...
```

Avoid generic names like:

```python
def test1():
    ...
```

---

# Mocking

Use mocks when testing code that depends on external systems such as sockets or the filesystem.

Example:

```python
from unittest.mock import patch

@patch("socket.socket")
def test_socket_connection(mock_socket):
    ...
```

---

# Regression Tests

Whenever a bug is fixed:

1. Write a test that reproduces the issue.
2. Verify the test fails before the fix.
3. Apply the fix.
4. Confirm the test now passes.

---

# Continuous Integration

Every Pull Request should automatically run:

- Unit tests
- Coverage
- Linting
- Type checking
- Security checks

No Pull Request should be merged while CI is failing.

---

# Performance Testing

Monitor:

- Scan duration
- CPU usage
- Memory usage
- Thread scaling

Benchmark significant performance changes before merging.

---

# Best Practices

- Keep tests isolated.
- Avoid external network dependencies where possible.
- Use fixtures for shared setup.
- Test both expected and error conditions.
- Review tests during code review, not just production code.

---

# Troubleshooting

## Failing Tests

Run with verbose output:

```bash
pytest -vv
```

Stop after the first failure:

```bash
pytest --maxfail=1
```

Run only the last failed tests:

```bash
pytest --lf
```

---

# Future Improvements

Potential additions:

- Integration tests against local test services
- Property-based testing
- Fuzz testing
- Performance benchmarks
- Cross-platform testing
- Mutation testing

---

# Related Documentation

- Development Guide
- Contributing Guide
- API Reference
- Security Guide