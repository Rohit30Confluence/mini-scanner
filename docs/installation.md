# Installation

This guide explains how to install **mini-scanner** on Linux, macOS, Windows, and Docker.

---

# Requirements

- Python 3.11 or newer
- pip
- Git (optional, for source installation)

Verify your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Install from PyPI

Once the package is published:

```bash
pip install mini-scanner
```

Verify installation:

```bash
mini-scanner --help
```

---

# Install from Source

Clone the repository:

```bash
git clone https://github.com/Rohit30Confluence/mini-scanner.git
```

Move into the project:

```bash
cd mini-scanner
```

Install:

```bash
pip install .
```

or for development:

```bash
pip install -e .
```

---

# Development Installation

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

or

```bash
pip install -e ".[dev]"
```

Install Git hooks:

```bash
pre-commit install
```

---

# Linux

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip git
```

Fedora:

```bash
sudo dnf install python3 python3-pip git
```

Arch Linux:

```bash
sudo pacman -S python python-pip git
```

---

# macOS

Using Homebrew:

```bash
brew install python git
```

Install mini-scanner:

```bash
pip3 install mini-scanner
```

---

# Windows

Download Python from:

https://www.python.org/downloads/

During installation:

- Enable **Add Python to PATH**
- Install pip

Then:

```powershell
pip install mini-scanner
```

---

# Docker

Build the image:

```bash
docker build -t mini-scanner .
```

Run:

```bash
docker run --rm mini-scanner --help
```

Example scan:

```bash
docker run --rm mini-scanner example.com --ports 22,80,443
```

---

# Docker Compose

Build:

```bash
docker compose build
```

Run:

```bash
docker compose run --rm mini-scanner
```

---

# Verify Installation

Display help:

```bash
mini-scanner --help
```

Run a quick scan:

```bash
mini-scanner scanme.nmap.org
```

Expected output:

```text
Host: scanme.nmap.org

22/tcp   OPEN
80/tcp   OPEN
443/tcp  CLOSED
```

---

# Updating

PyPI:

```bash
pip install --upgrade mini-scanner
```

Git:

```bash
git pull
pip install -e .
```

---

# Uninstall

```bash
pip uninstall mini-scanner
```

---

# Troubleshooting

## Python Not Found

Verify:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Permission Errors

Use a virtual environment:

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

---

## Docker Issues

Ensure Docker is running:

```bash
docker --version
```

---

## Getting Help

If installation problems persist:

- Open a GitHub Issue
- Read the Troubleshooting documentation
- Review the FAQ