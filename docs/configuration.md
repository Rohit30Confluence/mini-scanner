# Configuration

`mini-scanner` can be configured using command-line arguments, environment variables, or the Python API. This document explains the available options, their defaults, and recommendations for different scanning scenarios.

---

# Configuration Priority

Settings are applied in the following order (highest priority first):

1. Command-line arguments
2. Environment variables
3. Built-in defaults

For example, if `SCANNER_TIMEOUT=5` is set in the environment but the command is run with `--timeout 2`, the scanner uses **2 seconds**.

---

# Default Configuration

| Setting | Default |
|----------|---------|
| Timeout | `2.0` seconds |
| Worker Threads | `100` |
| Banner Size | `1024` bytes |
| Output Format | `text` |
| Banner Grabbing | Disabled |

---

# Command-Line Options

## Timeout

```bash
mini-scanner example.com --timeout 5
```

Controls how long the scanner waits for a connection before considering the port closed or unreachable.

Recommended values:

| Network | Timeout |
|----------|---------|
| Local LAN | `0.5–1s` |
| Internet | `2–3s` |
| High latency | `5–10s` |

---

## Worker Threads

```bash
mini-scanner example.com --workers 200
```

Higher values increase scanning speed but also increase CPU and network usage.

Recommendations:

| Environment | Workers |
|-------------|---------|
| Raspberry Pi | 25–50 |
| Laptop | 100–200 |
| Desktop | 200–500 |
| High-end Server | 500+ |

---

## Port Selection

Specific ports:

```bash
--ports 22,80,443
```

Range:

```bash
--ports 1-1024
```

Mixed:

```bash
--ports 22,80,443,8000-8100
```

---

## Banner Grabbing

Enable:

```bash
--banner
```

Disable:

```text
(default)
```

Banner grabbing attempts to read service information after a successful TCP connection.

---

## Output Format

Text:

```bash
--format text
```

JSON:

```bash
--format json
```

---

# Environment Variables

The following environment variables are supported:

| Variable | Default |
|----------|---------|
| `SCANNER_TIMEOUT` | `2.0` |
| `SCANNER_WORKERS` | `100` |
| `SCANNER_MAX_BANNER_SIZE` | `1024` |
| `SCANNER_DEFAULT_PORTS` | `22,80,443` |
| `LOG_LEVEL` | `INFO` |
| `OUTPUT_FORMAT` | `text` |
| `COLOR_OUTPUT` | `true` |
| `DEBUG` | `false` |

Example:

```bash
export SCANNER_TIMEOUT=5
export SCANNER_WORKERS=200
mini-scanner example.com
```

---

# Using a `.env` File

Copy the example configuration:

```bash
cp .env.example .env
```

Modify values as needed:

```dotenv
SCANNER_TIMEOUT=3
SCANNER_WORKERS=150
OUTPUT_FORMAT=json
```

---

# Python API Configuration

```python
from mini_scanner import Scanner

scanner = Scanner(
    timeout=2,
    workers=100,
)
```

Custom scan:

```python
results = scanner.scan(
    host="scanme.nmap.org",
    ports=[22, 80, 443],
)
```

---

# Performance Tuning

## Fast Local Scan

```text
Workers: 300
Timeout: 1 second
```

Suitable for trusted local networks.

---

## Reliable Internet Scan

```text
Workers: 100
Timeout: 3 seconds
```

Good balance between speed and reliability.

---

## Slow Networks

```text
Workers: 50
Timeout: 5–10 seconds
```

Recommended for VPNs or satellite links.

---

# Logging

Supported log levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Example:

```bash
export LOG_LEVEL=DEBUG
```

---

# JSON Output Example

```json
[
  {
    "host": "scanme.nmap.org",
    "port": 22,
    "state": "open",
    "service": "ssh"
  }
]
```

---

# Best Practices

- Use lower worker counts on resource-constrained systems.
- Increase timeout for high-latency networks.
- Prefer JSON output for automation and integrations.
- Scan only systems you own or have permission to test.
- Keep configuration consistent across development and CI environments.

---

# Troubleshooting

### Scan is slow

- Reduce timeout if the network is responsive.
- Increase worker threads if system resources allow.

### Missing open ports

- Increase the timeout.
- Verify firewall rules.
- Confirm the target host is reachable.

### High CPU usage

- Lower the number of worker threads.
- Scan smaller port ranges.

---

# Related Documentation

- Installation
- Quick Start
- CLI Reference
- Examples
- API Reference
- Development Guide
- Security Policy