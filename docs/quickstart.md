# Quick Start

Get up and running with **mini-scanner** in just a few minutes.

---

# Basic Scan

Scan the default ports of a host:

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

# Scan Specific Ports

Scan selected ports:

```bash
mini-scanner scanme.nmap.org --ports 22,80,443,8080
```

---

# Scan a Port Range

```bash
mini-scanner scanme.nmap.org --ports 1-1024
```

---

# Increase Timeout

Some networks respond slowly.

```bash
mini-scanner scanme.nmap.org --timeout 5
```

---

# Change Worker Threads

Increase scanning speed:

```bash
mini-scanner scanme.nmap.org --workers 200
```

Reduce resource usage:

```bash
mini-scanner scanme.nmap.org --workers 25
```

---

# Banner Grabbing

Retrieve service banners when available:

```bash
mini-scanner scanme.nmap.org --banner
```

Example:

```text
22/tcp  OPEN   OpenSSH 9.x
80/tcp  OPEN   Apache/2.4.x
```

---

# Save Results

Save as JSON:

```bash
mini-scanner scanme.nmap.org \
    --format json \
    --output results.json
```

Save as plain text:

```bash
mini-scanner scanme.nmap.org \
    --output results.txt
```

---

# Verbose Mode

```bash
mini-scanner scanme.nmap.org --verbose
```

---

# Scan Multiple Hosts

```bash
mini-scanner 192.168.1.1
mini-scanner example.com
mini-scanner localhost
```

---

# Using the Python API

Import the scanner:

```python
from mini_scanner import Scanner

scanner = Scanner()
```

Run a scan:

```python
results = scanner.scan(
    host="scanme.nmap.org",
    ports=[22, 80, 443],
)
```

Display results:

```python
for result in results:
    print(result)
```

---

# Using Docker

Build:

```bash
docker build -t mini-scanner .
```

Run:

```bash
docker run --rm mini-scanner scanme.nmap.org --ports 22,80,443
```

---

# Development Workflow

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

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

Run all checks:

```bash
make check
```

---

# Next Steps

After completing this guide, continue with:

- CLI Reference
- Configuration
- Examples
- API Reference
- Development Guide
- Security Guide