# mini_scanner

An educational TCP connect scanner built to illustrate the software
engineering principles behind tools like Nmap (Section 28 of the
Nmap Encyclopedia project): modular architecture, separation of
concerns, error handling, logging, configuration, and testing.

**Scope note:** this is a TCP *connect* scan only (a full three-way
handshake via the OS socket API, like `nmap -sT`). It does not do
raw-socket SYN scans, OS fingerprinting, or NSE-style scripting —
those are documented conceptually in later sections but intentionally
out of scope for this build. Use only against hosts you own or are
explicitly authorized to test.

---

## Project Goals

- Learn socket programming, OS APIs, and network protocols by building,
  not just reading about them
- Practice modular software architecture with single-responsibility components
- Build real error handling, logging, configuration, and test coverage
- Produce a small, maintainable codebase that mirrors how mature
  networking tools are structured internally

## Architecture

```
User -> CLI -> Parser -> Target Manager -> Scanner Engine
      -> Result -> Output Formatter -> Report
```

## Module Descriptions

| Module | File | Responsibility |
|---|---|---|
| CLI | `main.py` | Parse argv, wire modules together, nothing else |
| Parser | `parser.py` | Validate/normalize target + port input |
| Target Manager | `target.py` | Resolve hostnames to IPs, build `Target` objects |
| Scanner Engine | `scanner.py` | Coordinate the scan; TCP connect probes via thread pool |
| Result | `result.py` | Data container for scan output (no logic) |
| Output | `output.py` | Render results as text or JSON |
| Logger | `logger.py` | Structured execution logging (file + console) |
| Config | `config.py` | Central, validated configuration defaults |

## Build Instructions

Requires Python 3.10+ (uses `X | None` type syntax) and no third-party
runtime dependencies — only the standard library.

```bash
cd mini_scanner
python3 -m mini_scanner.main <target> [options]
```

## Usage

```bash
# Default port range (1-1024), text output
python3 -m mini_scanner.main scanme.example.com

# Custom port list/ranges
python3 -m mini_scanner.main 192.168.1.10 -p 22,80,443,8000-8100

# JSON output, custom timeout and concurrency
python3 -m mini_scanner.main 10.0.0.5 -p 1-65535 -o json -t 0.3 -c 500
```

CLI flags:

| Flag | Meaning | Default |
|---|---|---|
| `target` | Hostname or IP (positional, required) | — |
| `-p / --ports` | Ports, e.g. `80`, `1-1024`, `22,80,443` | `1-1024` |
| `-t / --timeout` | Per-port connect timeout (seconds) | `1.0` |
| `-c / --concurrency` | Max simultaneous connection attempts | `200` |
| `-o / --output` | `text` or `json` | `text` |
| `--log-file` | Path to execution log | `mini_scanner.log` |

## Testing

```bash
pip install pytest
python3 -m pytest tests/ -v
```

23 tests cover parser validation, config validation, result data
handling, output formatting, and a live integration test that scans
a locally-bound test server (no external network access required).

## Limitations

- TCP connect scan only — no SYN/UDP/raw-socket scanning
- No OS or service version fingerprinting
- No scripting engine (see Nmap Encyclopedia Section 30+ for NSE design)
- Banner grabbing is best-effort and passive (no active protocol probing)
- Not optimized for very large port ranges across many hosts simultaneously

## Future Enhancements (see Section 28.15)

- Config file support (JSON/YAML) instead of CLI-only overrides
- UDP scan mode
- Structured plugin system for post-scan checks (NSE-inspired)
- Progress reporting during long scans
- CSV/XML output formats
