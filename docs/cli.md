# Command Line Interface (CLI)

The **mini-scanner** command-line interface provides a simple and flexible way to scan TCP ports, grab banners, and export results.

---

# Syntax

```bash
mini-scanner [OPTIONS] HOST
```

Example:

```bash
mini-scanner scanme.nmap.org
```

---

# Arguments

| Argument | Description |
|-----------|-------------|
| `HOST` | Target hostname or IPv4 address |

Examples:

```bash
mini-scanner example.com
```

```bash
mini-scanner 192.168.1.10
```

```bash
mini-scanner localhost
```

---

# Options

## Scan Ports

Specify individual ports:

```bash
mini-scanner example.com --ports 22,80,443
```

Port range:

```bash
mini-scanner example.com --ports 1-1024
```

Mixed:

```bash
mini-scanner example.com --ports 22,80,443,8000-8100
```

---

## Timeout

Default:

```text
2 seconds
```

Example:

```bash
mini-scanner example.com --timeout 5
```

---

## Workers

Number of concurrent threads.

Example:

```bash
mini-scanner example.com --workers 200
```

Lower value:

```bash
mini-scanner example.com --workers 25
```

---

## Banner Grabbing

Retrieve service banners.

```bash
mini-scanner example.com --banner
```

Example output:

```text
22/tcp   OPEN    OpenSSH 9.x
80/tcp   OPEN    nginx
```

---

## Output Format

Text (default):

```bash
mini-scanner example.com
```

JSON:

```bash
mini-scanner example.com --format json
```

---

## Save Output

```bash
mini-scanner example.com \
    --output results.json \
    --format json
```

---

## Verbose

```bash
mini-scanner example.com --verbose
```

---

## Version

```bash
mini-scanner --version
```

Example:

```text
mini-scanner 1.0.0
```

---

## Help

```bash
mini-scanner --help
```

---

# Examples

## Scan Common Ports

```bash
mini-scanner scanme.nmap.org
```

---

## Scan Top Web Ports

```bash
mini-scanner example.com --ports 80,443,8080,8443
```

---

## Scan SSH

```bash
mini-scanner server.example.com --ports 22
```

---

## Scan Entire First 1024 Ports

```bash
mini-scanner example.com --ports 1-1024
```

---

## JSON Output

```bash
mini-scanner example.com \
    --format json \
    --output report.json
```

---

## Banner Grabbing

```bash
mini-scanner example.com \
    --banner
```

---

## Fast Scan

```bash
mini-scanner example.com \
    --workers 300 \
    --timeout 1
```

---

## Reliable Scan

```bash
mini-scanner example.com \
    --workers 50 \
    --timeout 5
```

---

# Exit Codes

| Code | Meaning |
|------:|---------|
| `0` | Scan completed successfully |
| `1` | Invalid command-line arguments |
| `2` | Invalid target host |
| `3` | Network or socket error |
| `4` | User interrupted the scan |
| `5` | Unexpected internal error |

---

# Best Practices

- Scan only systems you own or have permission to test.
- Use reasonable worker counts to avoid overwhelming networks.
- Increase timeout for high-latency connections.
- Save JSON output for automation and scripting.
- Keep the tool updated to benefit from bug fixes and new features.

---

# See Also

- Installation
- Quick Start
- Configuration
- Examples
- API Reference
- Development Guide
- Security Policy