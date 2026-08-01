"""
Target resolution utilities for Mini Scanner.
"""

from __future__ import annotations

import ipaddress
import socket
from dataclasses import dataclass

from .exceptions import TargetResolutionError


@dataclass(frozen=True, slots=True)
class Target:
    """
    Represents a resolved scan target.
    """

    hostname: str
    address: str
    family: int

    @property
    def is_ipv4(self) -> bool:
        return self.family == socket.AF_INET

    @property
    def is_ipv6(self) -> bool:
        return self.family == socket.AF_INET6


def resolve_target(host: str, *, ipv6: bool = False) -> Target:
    """
    Resolve a hostname or IP address.

    Args:
        host:
            Hostname or IP address.

        ipv6:
            Prefer IPv6 resolution.

    Returns:
        Target object.

    Raises:
        TargetResolutionError
    """

    host = host.strip()

    if not host:
        raise TargetResolutionError("Target cannot be empty.")

    # Already an IP address?
    try:
        ip = ipaddress.ip_address(host)

        return Target(
            hostname=host,
            address=str(ip),
            family=socket.AF_INET6 if ip.version == 6 else socket.AF_INET,
        )

    except ValueError:
        pass

    family = socket.AF_INET6 if ipv6 else socket.AF_UNSPEC

    try:
        info = socket.getaddrinfo(
            host,
            None,
            family,
            socket.SOCK_STREAM,
        )
    except socket.gaierror as exc:
        raise TargetResolutionError(
            f"Unable to resolve '{host}'."
        ) from exc

    if not info:
        raise TargetResolutionError(
            f"No address found for '{host}'."
        )

    family, _, _, _, sockaddr = info[0]

    return Target(
        hostname=host,
        address=sockaddr[0],
        family=family,
    )