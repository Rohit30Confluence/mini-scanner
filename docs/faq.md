# Frequently Asked Questions (FAQ)

This page answers common questions about installing, using, and contributing to **mini-scanner**.

---

# General

## What is mini-scanner?

mini-scanner is a lightweight, multithreaded TCP port scanner written in Python. It is designed to be simple, extensible, and useful for learning networking concepts as well as building automation.

---

## Is mini-scanner a vulnerability scanner?

No.

mini-scanner only determines whether TCP ports are reachable and, optionally, retrieves service banners. It does not identify vulnerabilities or exploit services.

---

## Which operating systems are supported?

The project is designed to work on:

- Linux
- macOS
- Windows

with Python 3.11 or newer.

---

# Installation

## Which Python versions are supported?

The project currently supports:

- Python 3.11
- Python 3.12
- Python 3.13

---

## How do I verify the installation?

```bash
mini-scanner --help
```

or

```bash
mini-scanner --version
```

---

## Can I install from source?

Yes.

```bash
git clone https://github.com/Rohit30Confluence/mini-scanner.git

cd mini-scanner

pip install -e .
```

---

# Usage

## How do I scan a host?

```bash
mini-scanner scanme.nmap.org
```

---

## How do I scan specific ports?

```bash
mini-scanner example.com --ports 22,80,443
```

---

## How do I scan a range?

```bash
mini-scanner example.com --ports 1-1024
```

---

## Can I export results?

Yes.

```bash
mini-scanner example.com \
    --format json \
    --output results.json
```

---

## Can I use mini-scanner from Python?

Yes.

```python
from mini_scanner import Scanner

scanner = Scanner()

results = scanner.scan(
    host="example.com",
    ports=[22,80,443],
)
```

---

# Performance

## How can I make scanning faster?

You can:

- Increase worker threads
- Reduce timeout
- Scan fewer ports

Example:

```bash
mini-scanner example.com \
    --workers 300 \
    --timeout 1
```

---

## Why is scanning slow?

Possible reasons include:

- High network latency
- Firewall filtering
- Large port ranges
- Low worker count

---

# Troubleshooting

## The scanner reports ports as closed.

Check:

- Hostname spelling
- Firewall configuration
- Target availability
- Timeout settings

---

## Banner grabbing returns nothing.

Many services intentionally suppress banners or only send them after protocol-specific requests. An empty banner does not necessarily indicate a problem.

---

## Why am I getting permission errors?

Some environments restrict outbound network access or firewall rules. Verify your network configuration and ensure you have permission to perform the scan.

---

# Docker

## Can I run mini-scanner in Docker?

Yes.

Build:

```bash
docker build -t mini-scanner .
```

Run:

```bash
docker run --rm mini-scanner scanme.nmap.org
```

---

# Development

## How do I run tests?

```bash
pytest -v
```

---

## How do I run formatting?

```bash
make format
```

---

## How do I run linting?

```bash
make lint
```

---

## How do I contribute?

Read:

- `CONTRIBUTING.md`
- `docs/development.md`
- `docs/testing.md`

Then submit a Pull Request.

---

# Security

## Is it legal to scan any host?

No.

Only scan systems that you own or have explicit authorization to assess.

---

## How do I report a security issue?

Follow the instructions in the project's `SECURITY.md`. Do not disclose unpatched vulnerabilities publicly.

---

# Project

## Where can I report bugs?

Open a GitHub Issue with:

- Operating system
- Python version
- mini-scanner version
- Command used
- Expected behavior
- Actual behavior
- Error output

---

## How often is the project updated?

Updates are released as improvements, bug fixes, and new features are completed. See `CHANGELOG.md` for release history.

---

# Still Need Help?

If your question is not answered here:

- Check the documentation
- Search existing GitHub Issues
- Start a GitHub Discussion
- Open a new Issue with detailed information