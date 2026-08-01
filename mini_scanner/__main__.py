"""
Command-line interface for Mini Scanner.
"""

from __future__ import annotations

import argparse
import logging
import sys

from mini_scanner.config import Config
from mini_scanner.exceptions import (
    ConfigurationError,
    PortValidationError,
    ScanError,
    TargetResolutionError,
)
from mini_scanner.output import print_results
from mini_scanner.parser import parse_ports
from mini_scanner.scanner import Scanner
from mini_scanner.target import resolve_target
from mini_scanner.version import __version__

LOGGER = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI parser."""

    parser = argparse.ArgumentParser(
        prog="mini-scanner",
        description="Lightweight concurrent TCP port scanner.",
    )

    parser.add_argument(
        "target",
        help="Hostname or IPv4 address to scan.",
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Ports or ranges (example: 22,80,443,8000-8100)",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds.",
    )

    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=100,
        help="Maximum concurrent worker threads.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def main() -> int:
    """Application entry point."""

    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    try:
        ports = parse_ports(args.ports)

        config = Config(
            timeout=args.timeout,
            workers=args.workers,
        )

        target = resolve_target(args.target)

        scanner = Scanner(config)

        results = scanner.scan(
            target=target,
            ports=ports,
        )

        print_results(
            target=target,
            results=results,
            json_output=args.json,
        )

        return 0

    except (
        ConfigurationError,
        PortValidationError,
        TargetResolutionError,
    ) as exc:
        LOGGER.error("%s", exc)
        return 2

    except ScanError as exc:
        LOGGER.error("%s", exc)
        return 3

    except KeyboardInterrupt:
        LOGGER.warning("Scan interrupted by user.")
        return 130

    except Exception:
        LOGGER.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    sys.exit(main())