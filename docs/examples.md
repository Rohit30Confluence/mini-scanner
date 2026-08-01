# Examples

This guide provides practical examples demonstrating how to use **mini-scanner** effectively from the command line, Docker, and the Python API.

---

# Scan a Host

Scan the default ports:

```bash
mini-scanner scanme.nmap.org
```

Example output:

```text
Host: scanme.nmap.org

22/tcp   OPEN
80/tcp   OPEN
443/tcp  CLOSED
```

---

# Scan an IP Address

```bash
mini-scanner 192.168.1.100
```

---

# Scan localhost

```bash
mini-scanner localhost
```

---

# Scan Multiple Common Ports

```bash
mini-scanner example.com --ports 22,80,443,8080
```

---

# Scan a Port Range

```bash
mini-scanner example.com --ports 1-1024
```

---

# Mixed Port List

```bash
mini-scanner example.com --ports 22,80,443,8000-8100
```

---

# Increase Timeout

```bash
mini-scanner example.com --timeout 5
```

Useful for slow or high-latency networks.

---

# Faster Scanning

```bash
mini-scanner example.com \
    --workers 300 \
    --timeout 1
```

---

# Reliable Internet Scan

```bash
mini-scanner example.com \
    --workers 100 \
    --timeout 3
```

---

# Banner Grabbing

```bash
mini-scanner example.com --banner
```

Example:

```text
22/tcp   OPEN   OpenSSH 9.x
80/tcp   OPEN   nginx
443/tcp  OPEN   Apache
```

---

# JSON Output

```bash
mini-scanner example.com \
    --format json \
    --output results.json
```

Example:

```json
[
  {
    "host": "example.com",
    "port": 80,
    "state": "open",
    "service": "http"
  }
]
```

---

# Save Text Report

```bash
mini-scanner example.com \
    --output report.txt
```

---

# Verbose Output

```bash
mini-scanner example.com --verbose
```

---

# Docker Example

Build:

```bash
docker build -t mini-scanner .
```

Run:

```bash
docker run --rm mini-scanner scanme.nmap.org
```

Custom ports:

```bash
docker run --rm mini-scanner \
    example.com \
    --ports 22,80,443
```

---

# Docker Compose

```bash
docker compose run --rm mini-scanner
```

Run a scan:

```bash
docker compose run --rm mini-scanner \
    example.com \
    --ports 22,80,443
```

---

# Python API

Basic example:

```python
from mini_scanner import Scanner

scanner = Scanner()

results = scanner.scan(
    host="scanme.nmap.org",
    ports=[22, 80, 443],
)

for result in results:
    print(result)
```

---

# Scan Multiple Hosts

```python
from mini_scanner import Scanner

scanner = Scanner()

hosts = [
    "scanme.nmap.org",
    "example.com",
    "localhost",
]

for host in hosts:
    print(scanner.scan(host))
```

---

# Export JSON

```python
import json

from mini_scanner import Scanner

scanner = Scanner()

results = scanner.scan(
    host="example.com",
    ports=[22, 80, 443],
)

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
```

---

# Simple Automation Script

```bash
#!/bin/bash

HOST=$1

mini-scanner "$HOST" \
    --ports 22,80,443 \
    --format json \
    --output report.json
```

Run:

```bash
./scan.sh example.com
```

---

# Development

Run tests:

```bash
pytest
```

Run coverage:

```bash
pytest --cov=mini_scanner
```

Run formatting:

```bash
make format
```

Run linting:

```bash
make lint
```

Run all checks:

```bash
make check
```

---

# CI Example

```bash
pre-commit run --all-files
tox
```

---

# Security Notice

Only scan hosts and networks that you own or have explicit authorization to test. Unauthorized scanning may violate policies or laws.

---

# Next Steps

Continue with:

- API Reference
- Development Guide
- Contributing Guide
- Security Policy
- Changelog