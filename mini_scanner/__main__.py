"""
Command-line entry point for Mini Scanner.
"""

from __future__ import annotations

import argparse
import logging
import sys

from .config import Config
from .exceptions import (
    ConfigurationError,
    PortValidationError,
    ScanError,
    TargetResolutionError,
)
from .output import print_results
from .parser import parse_ports
from .scanner import Scanner
from .target import resolve_target
from .version import __version__

LOGGER = logging.getLogger("mini_scanner")


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="mini-scanner",
        description="Lightweight concurrent TCP port scanner.",
    )

    parser.add_argument(
        "target",
        help="Hostname or IP address to scan.",
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Ports or ranges (e.g. 22,80,443,8000-8100).",
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
        help="Maximum worker threads.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON.",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Write output to a file.",
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
    """CLI entry point."""

    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    try:
        config = Config(
            timeout=args.timeout,
            workers=args.workers,
        )

        ports = parse_ports(args.ports)

        target = resolve_target(
            args.target,
            ipv6=config.ipv6,
        )

        scanner = Scanner(config)

        results = scanner.scan(
            target=target,
            ports=ports,
        )

        print_results(
            target=target,
            results=results,
            json_output=args.json,
            output_file=args.output,
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