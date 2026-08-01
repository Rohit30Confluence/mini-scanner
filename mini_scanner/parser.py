"""
Port parsing utilities for Mini Scanner.
"""

from __future__ import annotations

from typing import List

from .exceptions import PortValidationError

MIN_PORT = 1
MAX_PORT = 65535


def parse_ports(port_string: str) -> List[int]:
    """
    Parse a comma-separated list of ports and ranges.

    Examples:
        80
        22,80,443
        1-1024
        22,80,443,8000-8100

    Returns:
        Sorted list of unique ports.

    Raises:
        PortValidationError
    """

    if not port_string:
        raise PortValidationError("Port list cannot be empty.")

    ports = set()

    for item in port_string.split(","):

        item = item.strip()

        if not item:
            raise PortValidationError("Empty port value detected.")

        if "-" in item:
            ports.update(_parse_range(item))
        else:
            ports.add(_parse_port(item))

    return sorted(ports)


def _parse_port(value: str) -> int:
    """Parse a single TCP port."""

    try:
        port = int(value)
    except ValueError as exc:
        raise PortValidationError(
            f"Invalid port: '{value}'."
        ) from exc

    if not MIN_PORT <= port <= MAX_PORT:
        raise PortValidationError(
            f"Port {port} must be between {MIN_PORT} and {MAX_PORT}."
        )

    return port


def _parse_range(value: str) -> set[int]:
    """Parse a port range."""

    try:
        start_str, end_str = value.split("-", maxsplit=1)
    except ValueError as exc:
        raise PortValidationError(
            f"Invalid port range: '{value}'."
        ) from exc

    start = _parse_port(start_str)
    end = _parse_port(end_str)

    if start > end:
        raise PortValidationError(
            f"Invalid range '{value}': start port is greater than end port."
        )

    return set(range(start, end + 1))