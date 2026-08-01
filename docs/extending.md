# Extending mini-scanner

This guide explains how to extend **mini-scanner** while maintaining its architecture, code quality, and compatibility.

---

# Philosophy

New functionality should:

- Be modular
- Be testable
- Minimize breaking changes
- Follow existing coding standards
- Include documentation
- Include automated tests

Before implementing a feature, consider whether it belongs in the core scanner or should be implemented as a separate module.

---

# Project Structure

```
mini_scanner/
├── cli.py
├── config.py
├── scanner.py
├── formatter.py
├── parser.py
├── exceptions.py
├── utils.py
└── ...
```

Each module should have a clear, focused responsibility.

---

# Adding a New CLI Option

1. Define the argument in `cli.py`.

Example:

```python
parser.add_argument(
    "--progress",
    action="store_true",
    help="Display scan progress"
)
```

2. Validate the argument.

3. Pass it into the scanner configuration.

4. Add tests.

5. Update documentation.

---

# Adding a New Output Format

Current formats:

- Text
- JSON

To add another format:

1. Extend the formatter.
2. Keep the scanner output unchanged.
3. Add formatter tests.
4. Document the new format.

Example:

```python
formatter.to_yaml(results)
```

---

# Adding a Scan Type

Future scan types might include:

- UDP
- SYN (where supported)
- IPv6
- Service detection

Recommended approach:

```
Scanner
│
├── TCPScanner
├── UDPScanner
└── FutureScanner
```

Avoid mixing protocol-specific logic into a single large class.

---

# Adding Configuration Options

Configuration should support:

- Default values
- Environment variables
- CLI overrides

Maintain the precedence order:

```
CLI
↓

Environment

↓

Defaults
```

---

# Adding Exceptions

Prefer dedicated exception classes over generic exceptions.

Example:

```python
class InvalidPortError(Exception):
    """Raised when an invalid port is supplied."""
```

This improves debugging and error handling.

---

# Adding Tests

Every feature should include:

- Unit tests
- Edge case tests
- Failure tests
- Documentation updates

If fixing a bug, add a regression test before implementing the fix.

---

# Updating Documentation

When introducing a new feature, review whether these documents require updates:

- Quick Start
- CLI Reference
- API Reference
- FAQ
- Troubleshooting
- Changelog

Keeping documentation current is part of completing a feature.

---

# Performance Considerations

Before merging significant changes:

- Measure scan duration.
- Monitor memory usage.
- Check CPU utilization.
- Compare results against the current implementation.

Avoid optimizations that significantly reduce code readability unless they provide measurable benefits.

---

# Backward Compatibility

When changing public APIs:

- Preserve existing behavior where practical.
- Clearly document breaking changes.
- Update version numbers according to Semantic Versioning.

---

# Code Review Checklist

Before opening a Pull Request, confirm:

- The code follows project style.
- Tests pass.
- New tests are included.
- Documentation is updated.
- CI succeeds.
- No unnecessary dependencies are introduced.

---

# Future Extension Ideas

Potential enhancements include:

- Plugin framework
- Async scanning
- IPv6 support
- UDP scanning
- Progress reporting
- Rate limiting
- Service fingerprinting
- Export to CSV, YAML, and XML
- Interactive terminal interface
- Web-based dashboard

---

# Contributing New Features

When proposing substantial functionality:

1. Open a GitHub Discussion or Issue.
2. Describe the motivation and use case.
3. Outline the proposed design.
4. Discuss implementation details with maintainers.
5. Submit a Pull Request with tests and documentation.

This process helps ensure new features align with the project's goals and maintain long-term maintainability.