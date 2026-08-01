# Performance Guide

This guide explains how to measure, optimize, and understand the performance characteristics of **mini-scanner**.

---

# Overview

The performance of a TCP port scanner depends on several factors:

- Network latency
- Number of worker threads
- Connection timeout
- Number of ports
- Host responsiveness
- CPU performance
- Operating system networking stack

There is no single configuration that is optimal for every environment.

---

# Benchmarking

When benchmarking, record:

- Total scan duration
- Ports scanned
- Open ports found
- Worker count
- Timeout
- CPU usage
- Memory usage

Example:

```bash
time mini-scanner scanme.nmap.org --ports 1-1024
```

---

# Worker Threads

Workers determine how many ports are scanned concurrently.

Example:

```bash
mini-scanner example.com --workers 100
```

Typical recommendations:

| Environment | Workers |
|-------------|--------:|
| Raspberry Pi | 25–50 |
| Laptop | 100–200 |
| Desktop | 200–400 |
| High-end Workstation | 400–800 |

Increasing workers beyond what the system or network can handle may reduce efficiency.

---

# Timeout Selection

Timeout directly affects scan duration.

Example:

```bash
mini-scanner example.com --timeout 3
```

Recommended values:

| Environment | Timeout |
|-------------|---------|
| Local network | 0.5–1 s |
| Internet | 2–3 s |
| High-latency links | 5–10 s |

---

# Port Range Size

Scanning more ports increases runtime.

Examples:

```bash
--ports 22
```

```bash
--ports 22,80,443
```

```bash
--ports 1-1024
```

```bash
--ports 1-65535
```

Scan only the ports relevant to your task whenever possible.

---

# Banner Grabbing

Banner grabbing adds additional network operations after a successful TCP connection.

Enable:

```bash
mini-scanner example.com --banner
```

Disable it if you only need port status for faster scans.

---

# JSON vs Text Output

Text output is generally sufficient for interactive use.

JSON output is recommended when integrating with scripts or other tools.

Output formatting is usually not the primary performance bottleneck.

---

# Measuring Resource Usage

Linux/macOS:

```bash
time mini-scanner example.com
```

Monitor CPU and memory with:

```bash
top
```

or

```bash
htop
```

Windows users can use Task Manager or Performance Monitor.

---

# Optimization Tips

- Increase worker threads gradually.
- Reduce timeout on low-latency networks.
- Disable banner grabbing when unnecessary.
- Limit scans to required ports.
- Reuse a single `Scanner` instance in Python applications when scanning multiple hosts.

---

# Scaling Considerations

Performance improvements eventually plateau.

Excessively high worker counts can lead to:

- Increased context switching
- Higher memory usage
- More socket contention
- Diminishing performance gains

Benchmark changes rather than assuming higher values are always better.

---

# Benchmark Template

Record results in a table such as:

| Host | Ports | Workers | Timeout | Duration |
|------|------:|--------:|---------|---------:|
| localhost | 1024 | 100 | 1 s | 0.8 s |
| example.com | 1024 | 100 | 2 s | 2.6 s |

This makes it easier to compare changes over time.

---

# Performance Testing in CI

Performance tests should be separated from unit tests.

They may:

- Require dedicated hardware
- Produce variable results
- Increase CI execution time

Use consistent environments when comparing benchmark results.

---

# Future Improvements

Potential optimizations include:

- Async I/O implementation
- Adaptive worker scaling
- Connection pooling where appropriate
- IPv6 performance tuning
- Improved service detection efficiency
- Performance regression benchmarks

---

# Best Practices

- Benchmark before optimizing.
- Measure the impact of configuration changes.
- Prefer simple, maintainable optimizations over premature complexity.
- Test performance across different operating systems and network conditions.