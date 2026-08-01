# Internals

This document explains how **mini-scanner** works internally. It is intended for contributors who want to understand, debug, or extend the implementation.

---

# Architecture Overview

```
                    User
                      │
                      ▼
               Command Line (CLI)
                      │
                      ▼
             Argument Validation
                      │
                      ▼
                Configuration
                      │
                      ▼
                Scanner Engine
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Host Resolver   Thread Pool     Port Scheduler
      │               │                │
      └───────────────┼────────────────┘
                      ▼
               Socket Connections
                      │
              Connection Success?
                │              │
              Yes             No
                │              │
                ▼              ▼
        Banner Grabber    Closed Result
                │
                ▼
        Result Aggregator
                │
                ▼
            Output Formatter
          ┌─────────┴─────────┐
          ▼                   ▼
       Text Output        JSON Output
```

---

# Scanner Lifecycle

A typical scan follows these steps:

1. Parse CLI arguments.
2. Validate the target host.
3. Parse the requested ports.
4. Resolve the hostname to an IP address.
5. Create worker threads.
6. Attempt TCP connections.
7. Optionally retrieve banners.
8. Aggregate results.
9. Format output.
10. Exit with an appropriate status code.

---

# Thread Pool

The scanner uses a fixed-size worker pool.

Each worker:

- Retrieves the next port.
- Attempts a TCP connection.
- Records the result.
- Repeats until all ports have been processed.

This approach balances throughput with resource usage.

---

# Socket Lifecycle

For each port:

1. Create a socket.
2. Set the timeout.
3. Attempt `connect()`.
4. Mark the port as open or closed.
5. Retrieve a banner if enabled.
6. Close the socket.

Sockets should always be closed, even if an exception occurs.

---

# Port Parsing

Supported formats include:

Single port:

```
22
```

List:

```
22,80,443
```

Range:

```
1-1024
```

Mixed:

```
22,80,443,8000-8100
```

The parser should:

- Reject invalid ports.
- Remove duplicates.
- Return ports in ascending order.

---

# Result Model

Each result should contain structured information.

Example:

```python
{
    "host": "example.com",
    "port": 80,
    "state": "open",
    "service": "http",
    "banner": "Apache/2.4"
}
```

Keeping results structured allows multiple output formats without changing the scanner logic.

---

# Banner Grabbing

Banner grabbing occurs only after a successful TCP connection.

The scanner reads up to the configured maximum banner size.

Failures to retrieve a banner should not mark the scan as failed.

---

# Output Formatting

The formatter converts structured scan results into:

- Human-readable text
- JSON

The scanner itself should not contain formatting logic.

---

# Error Handling

Expected errors include:

- Invalid host
- Invalid port
- DNS resolution failure
- Connection timeout
- Socket errors

Use specific exceptions where appropriate and present clear error messages to users.

---

# Extension Points

Potential areas for future development include:

- IPv6 support
- UDP scanning
- Async scanning
- Plugin architecture
- Additional output formats
- Service fingerprinting
- Progress indicators

Keeping responsibilities separated makes these features easier to implement.

---

# Testing Internal Components

Core components should be tested independently:

- Port parser
- Host resolver
- Scanner engine
- Formatter
- Configuration
- CLI
- Exception handling

This improves confidence and simplifies debugging.

---

# Design Principles

The project follows these principles:

- Single Responsibility Principle
- Separation of Concerns
- Explicit Error Handling
- Readability over cleverness
- Minimal external dependencies
- Comprehensive automated testing

---

# Contributor Notes

When modifying the internals:

- Preserve backward compatibility where practical.
- Add tests for new functionality.
- Update documentation alongside code changes.
- Keep public APIs stable unless a breaking change is intentional.