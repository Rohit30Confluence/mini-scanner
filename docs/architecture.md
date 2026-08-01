# Architecture

This document describes the internal architecture of **mini-scanner**.

---

# Overview

`mini-scanner` is a lightweight, modular TCP port scanner written in Python.

The project is organized into small, focused modules that each have a single responsibility.

```
CLI
 │
 ▼
Argument Parser
 │
 ▼
Configuration
 │
 ▼
Scanner Engine
 │
 ├── Port Parser
 ├── Thread Pool
 ├── Socket Manager
 ├── Banner Grabber
 │
 ▼
Results
 │
 ▼
Formatter
 │
 ├── Text
 └── JSON
```

---

# Project Layout

```
mini_scanner/
├── __init__.py
├── cli.py
├── config.py
├── scanner.py
├── exceptions.py
├── formatter.py
├── utils.py
└── ...
```

Each module should focus on one responsibility.

---

# CLI Layer

Responsibilities:

- Parse command-line arguments
- Validate user input
- Load configuration
- Invoke the scanner
- Display results

The CLI should contain minimal business logic.

---

# Configuration

Configuration may originate from:

1. CLI arguments
2. Environment variables
3. Built-in defaults

CLI arguments take precedence.

---

# Scanner Engine

Core responsibilities:

- Resolve hostnames
- Create TCP connections
- Manage worker threads
- Detect open ports
- Collect banners
- Return structured results

The scanner should avoid printing directly to the console.

---

# Threading Model

The scanner uses a worker pool to scan ports concurrently.

Benefits:

- Faster scans
- Controlled resource usage
- Configurable concurrency

---

# Error Handling

Errors should use custom exception types where appropriate.

Examples:

- Invalid host
- Invalid port
- Network timeout
- Socket failure

The CLI converts exceptions into user-friendly messages.

---

# Output Layer

Supported formats:

- Text
- JSON

Output formatting is separated from scanning logic.

---

# Testing Strategy

Tests are divided into:

- Unit tests
- Integration tests
- CLI tests
- Configuration tests

Each bug fix should include a regression test.

---

# Security Considerations

The scanner:

- Uses standard TCP sockets
- Does not attempt privilege escalation
- Does not exploit services
- Does not bypass authentication

Users are responsible for obtaining authorization before scanning systems.

---

# Future Architecture

Potential enhancements:

- Async scanning
- IPv6 support
- UDP scanning
- Plugin system
- Service fingerprinting
- Export formats (CSV, XML)
- Performance metrics

---

# Design Principles

The project follows these principles:

- Simplicity
- Readability
- Modularity
- Testability
- Maintainability
- Minimal dependencies