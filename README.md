# Mini Scanner

> A lightweight, modular TCP port scanner built in Python for learning network programming, concurrent scanning, and clean software architecture.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

Mini Scanner is an open-source TCP port scanner designed to demonstrate modern Python development practices while providing a clean, modular, and extensible codebase.

Unlike large security frameworks, Mini Scanner focuses on readability, maintainability, and education. It is intended for developers, students, and security enthusiasts who want to understand how network scanners work internally.

The project provides a solid foundation that can be extended with advanced networking capabilities in future releases.

---

## Features

- TCP Connect Port Scanning
- Concurrent Scanning using ThreadPoolExecutor
- Banner Grabbing
- Hostname Resolution
- Configurable Timeout
- Human-readable Terminal Output
- JSON Output
- Modular Architecture
- Logging Support
- Unit Tests
- Easy to Extend

---

## Why Mini Scanner?

Mini Scanner was created to demonstrate professional software engineering practices while implementing a real-world networking utility.

The project emphasizes:

- Clean Architecture
- Separation of Concerns
- Readable Code
- Type Hints
- Testing
- Documentation
- Extensibility

Instead of becoming another clone of Nmap, Mini Scanner aims to be an educational networking framework that developers can easily understand and extend.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mini-scanner.git

cd mini-scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -e .
```

---

# Quick Start

Scan localhost

```bash
mini-scanner scan localhost
```

Scan an IP address

```bash
mini-scanner scan 192.168.1.10
```

Scan a hostname

```bash
mini-scanner scan scanme.nmap.org
```

Scan a custom port range

```bash
mini-scanner scan localhost --ports 1-1000
```

Increase timeout

```bash
mini-scanner scan localhost --timeout 2
```

Output as JSON

```bash
mini-scanner scan localhost --json
```

---

# Example Output

```
Target: scanme.nmap.org

PORT      STATUS      SERVICE

22        OPEN        ssh
80        OPEN        http
443       OPEN        https
9929      OPEN        nping-echo
```

JSON Output

```json
{
  "host": "scanme.nmap.org",
  "ports": [
    {
      "port": 22,
      "status": "open",
      "banner": "OpenSSH"
    },
    {
      "port": 80,
      "status": "open",
      "banner": "nginx"
    }
  ]
}
```

---

# Project Architecture

```
              CLI
               │
               ▼
          Argument Parser
               │
               ▼
         Target Resolver
               │
               ▼
         Scanner Engine
               │
               ▼
         Result Objects
               │
               ▼
        Output Formatter
```

Every module has a single responsibility, making the project easy to understand, test, and extend.

---

# Project Structure

```
mini-scanner/

├── mini_scanner/
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py
│   ├── scanner.py
│   ├── parser.py
│   ├── config.py
│   ├── target.py
│   ├── result.py
│   ├── output.py
│   ├── logger.py
│   └── exceptions.py
│
├── tests/
│
├── docs/
│
├── examples/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

# How It Works

1. Parse command-line arguments.
2. Validate the target and ports.
3. Resolve the hostname to an IP address.
4. Create worker threads.
5. Attempt TCP connections.
6. Record open ports.
7. Grab service banners when available.
8. Format the results.
9. Display or export the scan output.

---

# Development

Install development dependencies

```bash
pip install -r requirements-dev.txt
```

Run tests

```bash
pytest
```

Run linting

```bash
ruff check .
```

Format code

```bash
black .
```

Sort imports

```bash
isort .
```

Type checking

```bash
mypy .
```

Coverage

```bash
coverage run -m pytest
coverage report
```

---

# Testing

The project includes automated tests for:

- Parser
- Scanner
- Output Formatter
- Configuration
- Result Objects

Future releases will expand coverage for:

- IPv6
- Banner Grabbing
- CLI
- Logging
- Timeout Handling
- Concurrent Scanning

---

# Roadmap

## Version 1.0

- TCP Connect Scan
- Banner Grabbing
- JSON Output
- Logging
- Unit Tests

## Version 1.1

- IPv6 Support
- CSV Export
- Multiple Targets
- Better Error Handling

## Version 1.2

- Async Scanner
- CIDR Support
- Progress Bar
- Service Detection

## Version 2.0

- UDP Scanner
- SYN Scan (where supported)
- Plugin System
- REST API
- Docker Image
- Web Dashboard

---

# Security

Mini Scanner is intended for authorized security testing only.

Always obtain permission before scanning networks or systems that you do not own or administer.

The authors are not responsible for misuse of this software.

Please report security issues responsibly.

See **SECURITY.md** for details.

---

# Contributing

Contributions are welcome.

You can contribute by:

- Reporting bugs
- Suggesting features
- Improving documentation
- Writing tests
- Refactoring code
- Improving performance

Please read **CONTRIBUTING.md** before submitting pull requests.

---

# License

This project is licensed under the MIT License.

See the **LICENSE** file for more information.

---

# Acknowledgements

Mini Scanner is inspired by networking fundamentals, Python's standard socket library, and the open-source community's emphasis on readable, maintainable software.

---

## Disclaimer

This project is provided for educational, research, and authorized security assessment purposes only.

Users are solely responsible for ensuring compliance with applicable laws, regulations, and organizational policies. Unauthorized scanning of systems or networks may be illegal.

Use this software responsibly.