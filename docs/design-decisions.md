# Design Decisions

This document explains the key design decisions behind **mini-scanner** and the trade-offs considered during development.

---

# Goals

The project aims to be:

- Lightweight
- Easy to understand
- Easy to extend
- Cross-platform
- Well tested
- Suitable for learning networking fundamentals

---

# Why Python?

Python was chosen because it provides:

- Excellent standard library support
- Cross-platform networking
- Fast development
- Readable code
- Large ecosystem

Trade-off:

- Lower raw performance than C or Rust.

---

# Why TCP Only?

The initial implementation focuses on TCP because:

- TCP scanning is straightforward.
- It covers the majority of common services.
- It keeps the codebase simpler.

Future versions may add UDP support.

---

# Why Threads Instead of asyncio?

A thread pool was selected because:

- Socket operations are I/O-bound.
- The implementation is easier to understand.
- It works consistently across supported Python versions.

Future versions may provide an asyncio-based scanner for higher scalability.

---

# Why a Modular Architecture?

Each module has a single responsibility.

Benefits include:

- Easier testing
- Better maintainability
- Simpler code reviews
- Easier future extensions

---

# Why Separate Formatting from Scanning?

The scanner returns structured data rather than printing directly.

Benefits:

- Reusable Python API
- Multiple output formats
- Easier testing
- Cleaner separation of concerns

---

# Configuration Strategy

Configuration sources are applied in this order:

1. Command-line arguments
2. Environment variables
3. Default values

This provides predictable behavior while allowing flexible deployments.

---

# Error Handling

The project favors explicit exceptions over silent failures.

Goals:

- Helpful error messages
- Easier debugging
- Consistent API behavior

---

# Testing Philosophy

Every bug fix should include a regression test.

The project emphasizes:

- Unit tests
- CLI tests
- Configuration tests
- Integration tests where appropriate

---

# Security Philosophy

mini-scanner is intended for defensive and educational use.

The project does not attempt to:

- Exploit vulnerabilities
- Bypass authentication
- Evade security controls

Users are responsible for ensuring they have authorization before scanning systems.

---

# Future Directions

Potential future enhancements include:

- IPv6 support
- UDP scanning
- Async scanning
- Plugin system
- Advanced service fingerprinting
- Additional export formats

Design decisions will continue to prioritize simplicity, maintainability, and correctness.