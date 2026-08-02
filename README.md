# Mini Scanner

> A lightweight, modular TCP port scanner built in Python for learning network programming, concurrent scanning, and clean software architecture.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://img.shields.io/badge/Python-3.10%2B-blue) [![License](https://img.shields.io/badge/License-MIT-green)](https://img.shields.io/badge/License-MIT-green) [![Status](https://img.shields.io/badge/Status-Active-success)](https://img.shields.io/badge/Status-Active-success)

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
- Web Interface (local Flask console + static demo)
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

```
git clone https://github.com/Rohit30Confluence/mini-scanner.git

cd mini-scanner
```

Create a virtual environment:

```
python -m venv .venv
```

Linux/macOS

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

Install dependencies

```
pip install -e .
```

---

# Quick Start

Scan localhost

```
mini-scanner scan localhost
```

Scan an IP address

```
mini-scanner scan 192.168.1.10
```

Scan a hostname

```
mini-scanner scan scanme.nmap.org
```

Scan a custom port range

```
mini-scanner scan localhost --ports 1-1000
```

Increase timeout

```
mini-scanner scan localhost --timeout 2
```

Output as JSON

```
mini-scanner scan localhost --json
```

Prefer a browser? See [Web Interface](#web-interface) below.

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

```
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

# Web Interface

Mini Scanner ships with two ways to use it from a browser instead of the CLI. Both share the same visual design — a patch-panel display where each scanned port lights up green (open), red (closed), or amber (filtered) — but they differ in what actually happens behind the button.

## 1. Live scanner (`webapp/`, run locally)

A Flask app that runs real scans using the same TCP-connect / concurrent-threads / banner-grab logic as the CLI. It calls into the `mini_scanner` package directly when installed, so results match the CLI exactly.

```
pip install -r requirements-web.txt
cd webapp
python app.py
```

Then open **http://localhost:5000**. To share it with others, deploy `webapp/` to a host that runs Python (e.g. Render or Railway) — GitHub Pages can't run this part, since it only serves static files. Full deploy steps are in `webapp/README_WEBUI.md`.

Built-in safety limits: scans require you to confirm authorization to test the target, are capped at 1024 ports and a 5-second per-port timeout, and are rate-limited per IP (6 scans/minute) to keep a public deployment from being used for abusive sweeps.

## 2. Static demo (`docs/`, hosted on GitHub Pages)

A pure HTML/CSS/JS version of the same UI, hosted for free directly from this repo via **Settings → Pages**. Since Pages only serves static files, this version **simulates** results client-side (deterministically, from your input) rather than performing real network scans — it's there to demo the interface and output format without needing a server. This is clearly labeled in the UI itself.

Live at: `https://rohit30confluence.github.io/mini-scanner/` (enable under repo **Settings → Pages** → Source: Deploy from a branch → `main` / `docs`, if not already active).

| | Live scanner (`webapp/`) | Static demo (`docs/`) |
|---|---|---|
| Real network scan | ✅ Yes | ❌ Simulated |
| Hosting | Local, or Render/Railway/etc. | GitHub Pages (free, built-in) |
| Requires a server | Yes (Flask) | No |
| Good for | Actually scanning authorized targets | Showing off the UI, no setup |

---

# Project Architecture

```
      CLI                      Browser
       │                          │
       ▼                          ▼
  Argument Parser          Web UI (Flask / static)
       │                          │
       ▼                          ▼
 Target Resolver  ────────▶ Scanner Engine
                                   │
                                   ▼
                            Result Objects
                                   │
                                   ▼
                           Output Formatter
```

Every module has a single responsibility, making the project easy to understand, test, and extend. The web UI reuses the same Scanner Engine / Result Objects as the CLI rather than duplicating scan logic.

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
├── webapp/                  # Live Flask web console (real scans)
│   ├── app.py
│   ├── scan_engine.py
│   ├── templates/
│   └── static/
│
├── docs/                    # Static GitHub Pages demo (simulated scans)
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── tests/
│
├── examples/
│
├── pyproject.toml
├── requirements-web.txt
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

# How It Works

1. Parse command-line arguments (or a browser form, in the web UI).
2. Validate the target and ports.
3. Resolve the hostname to an IP address.
4. Create worker threads.
5. Attempt TCP connections.
6. Record open ports.
7. Grab service banners when available.
8. Format the results.
9. Display in the terminal, render on the web patch panel, or export as JSON.

---

# Development

Install development dependencies

```
pip install -r requirements-dev.txt
```

Run tests

```
pytest
```

Run linting

```
ruff check .
```

Format code

```
black .
```

Sort imports

```
isort .
```

Type checking

```
mypy .
```

Coverage

```
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
- Web UI (Flask routes + scan engine)
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
- ~~Web Dashboard~~ — shipped: see [Web Interface](#web-interface)

---

# Security

Mini Scanner is intended for authorized security testing only.

Always obtain permission before scanning networks or systems that you do not own or administer. This applies to the web interface as well as the CLI — the live scanner requires explicit confirmation of authorization before running any scan.

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
- Improving the web UI (`webapp/` and `docs/`)

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
