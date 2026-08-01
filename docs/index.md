# mini-scanner

A lightweight, fast, and extensible TCP port scanner written in Python.

[![CI](https://github.com/Rohit30Confluence/mini-scanner/actions/workflows/ci.yml/badge.svg)](https://github.com/Rohit30Confluence/mini-scanner/actions/workflows/ci.yml)
[![CodeQL](https://github.com/Rohit30Confluence/mini-scanner/actions/workflows/codeql.yml/badge.svg)](https://github.com/Rohit30Confluence/mini-scanner/actions/workflows/codeql.yml)
[![License](https://img.shields.io/github/license/Rohit30Confluence/mini-scanner)](../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)]()

---

## Features

- Fast multithreaded TCP port scanning
- Configurable connection timeout
- Banner grabbing
- JSON and text output
- Modular architecture
- Easy Python API
- Command-line interface
- Docker support
- Comprehensive test suite
- GitHub Actions CI/CD

---

## Installation

```bash
pip install mini-scanner
```

Or install from source:

```bash
git clone https://github.com/Rohit30Confluence/mini-scanner.git
cd mini-scanner
pip install -e .
```

---

## Quick Example

Scan common ports:

```bash
mini-scanner example.com
```

Scan specific ports:

```bash
mini-scanner example.com --ports 22,80,443
```

Save results:

```bash
mini-scanner example.com --output results.json --format json
```

---

## Python API

```python
from mini_scanner import Scanner

scanner = Scanner()

results = scanner.scan(
    host="scanme.nmap.org",
    ports=[22,80,443],
)

for result in results:
    print(result)
```

---

## Project Structure

```
mini-scanner/
├── mini_scanner/
├── tests/
├── docs/
├── .github/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

## Documentation

- Installation
- Quick Start
- CLI Reference
- API Reference
- Examples
- Development Guide
- Security Policy

---

## Development

Run tests:

```bash
pytest
```

Run formatting:

```bash
make format
```

Run linting:

```bash
make lint
```

Run all quality checks:

```bash
make check
```

---

## Contributing

Contributions are welcome.

Please read the Contributing Guide before opening an issue or pull request.

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.