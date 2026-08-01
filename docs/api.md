# Python API Reference

The **mini-scanner** Python API enables you to integrate TCP port scanning into your own Python applications.

---

# Installation

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

# Importing

```python
from mini_scanner import Scanner
```

---

# Scanner Class

The `Scanner` class is the primary interface for creating and running scans.

```python
scanner = Scanner()
```

## Constructor

```python
Scanner(
    timeout=2.0,
    workers=100,
    banner=False,
)
```

### Parameters

| Parameter | Type | Default | Description |
|------------|------|---------|-------------|
| timeout | float | 2.0 | Connection timeout (seconds) |
| workers | int | 100 | Number of concurrent worker threads |
| banner | bool | False | Enable banner grabbing |

---

# scan()

Scans one host for the specified ports.

```python
results = scanner.scan(
    host="scanme.nmap.org",
    ports=[22, 80, 443],
)
```

## Parameters

| Name | Type | Description |
|------|------|-------------|
| host | str | Hostname or IPv4 address |
| ports | list[int] | List of TCP ports to scan |

---

## Returns

Returns a list of scan results.

Example:

```python
[
    {
        "host": "scanme.nmap.org",
        "port": 22,
        "state": "open",
        "service": "ssh",
        "banner": "OpenSSH 9.x"
    }
]
```

---

# Basic Example

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

# Custom Configuration

```python
scanner = Scanner(
    timeout=5,
    workers=200,
    banner=True,
)
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

# Scan Common Ports

```python
results = scanner.scan(
    host="example.com",
    ports=[22, 80, 443],
)
```

---

# Scan a Port Range

```python
ports = list(range(1, 1025))

results = scanner.scan(
    host="example.com",
    ports=ports,
)
```

---

# JSON Export

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

# Result Structure

Each scan result contains:

| Field | Type | Description |
|--------|------|-------------|
| host | str | Target hostname |
| port | int | TCP port |
| state | str | open / closed |
| service | str | Detected service (if available) |
| banner | str | Service banner (if enabled) |

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

---

# Exceptions

Applications should handle common network errors gracefully.

Example:

```python
from mini_scanner import Scanner

scanner = Scanner()

try:
    results = scanner.scan(
        host="example.com",
        ports=[22],
    )
except Exception as exc:
    print(exc)
```

If your project exposes custom exceptions (for example, `ScannerError` or `InvalidPortError`), catch those instead of the generic `Exception`.

---

# Performance Tips

- Reuse a single `Scanner` instance when scanning multiple hosts.
- Increase `workers` for faster scans on capable hardware.
- Increase `timeout` when scanning high-latency networks.
- Disable banner grabbing if only port status is required.

---

# Thread Safety

Each `Scanner` instance is intended for a single scan at a time. If your application performs concurrent scans, create one `Scanner` instance per thread or task unless the library explicitly documents thread-safe shared use.

---

# Best Practices

- Validate user-supplied hostnames and ports.
- Scan only systems you own or are authorized to assess.
- Export results as JSON for automation.
- Handle exceptions appropriately in production applications.

---

# See Also

- Installation
- Quick Start
- CLI Reference
- Configuration
- Examples
- Development Guide
- Security Policy