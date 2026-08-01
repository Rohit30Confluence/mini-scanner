"""
Tests for target resolution.
"""

from __future__ import annotations

import socket
from unittest.mock import patch

import pytest

from mini_scanner.exceptions import TargetResolutionError
from mini_scanner.target import Target, resolve_target


def test_target_dataclass():
    """Target stores values correctly."""

    target = Target(
        hostname="localhost",
        address="127.0.0.1",
        family=socket.AF_INET,
    )

    assert target.hostname == "localhost"
    assert target.address == "127.0.0.1"
    assert target.family == socket.AF_INET


@patch("socket.getaddrinfo")
def test_resolve_ipv4(mock_getaddrinfo):
    """Resolve an IPv4 address."""

    mock_getaddrinfo.return_value = [
        (
            socket.AF_INET,
            socket.SOCK_STREAM,
            6,
            "",
            ("127.0.0.1", 0),
        )
    ]

    target = resolve_target("localhost")

    assert target.hostname == "localhost"
    assert target.address == "127.0.0.1"
    assert target.family == socket.AF_INET


@patch("socket.getaddrinfo")
def test_resolve_ipv6(mock_getaddrinfo):
    """Resolve an IPv6 address."""

    mock_getaddrinfo.return_value = [
        (
            socket.AF_INET6,
            socket.SOCK_STREAM,
            6,
            "",
            ("::1", 0, 0, 0),
        )
    ]

    target = resolve_target(
        "localhost",
        ipv6=True,
    )

    assert target.address == "::1"
    assert target.family == socket.AF_INET6


@patch("socket.getaddrinfo")
def test_resolution_failure(mock_getaddrinfo):
    """DNS failures should raise TargetResolutionError."""

    mock_getaddrinfo.side_effect = socket.gaierror()

    with pytest.raises(TargetResolutionError):
        resolve_target("does-not-exist.local")


@patch("socket.getaddrinfo")
def test_empty_resolution(mock_getaddrinfo):
    """Empty getaddrinfo result should raise an error."""

    mock_getaddrinfo.return_value = []

    with pytest.raises(TargetResolutionError):
        resolve_target("localhost")


@patch("socket.getaddrinfo")
def test_ipv4_preferred(mock_getaddrinfo):
    """IPv4 should be selected when IPv6 is disabled."""

    mock_getaddrinfo.return_value = [
        (
            socket.AF_INET,
            socket.SOCK_STREAM,
            6,
            "",
            ("192.168.1.10", 0),
        ),
        (
            socket.AF_INET6,
            socket.SOCK_STREAM,
            6,
            "",
            ("fe80::1", 0, 0, 0),
        ),
    ]

    target = resolve_target(
        "example.com",
        ipv6=False,
    )

    assert target.family == socket.AF_INET
    assert target.address == "192.168.1.10"


@patch("socket.getaddrinfo")
def test_ipv6_preferred(mock_getaddrinfo):
    """IPv6 should be selected when enabled."""

    mock_getaddrinfo.return_value = [
        (
            socket.AF_INET6,
            socket.SOCK_STREAM,
            6,
            "",
            ("2001:db8::1", 0, 0, 0),
        ),
        (
            socket.AF_INET,
            socket.SOCK_STREAM,
            6,
            "",
            ("203.0.113.1", 0),
        ),
    ]

    target = resolve_target(
        "example.com",
        ipv6=True,
    )

    assert target.family == socket.AF_INET6
    assert target.address == "2001:db8::1"


def test_target_repr():
    """repr() should be informative."""

    target = Target(
        hostname="localhost",
        address="127.0.0.1",
        family=socket.AF_INET,
    )

    text = repr(target)

    assert "Target" in text
    assert "localhost" in text
    assert "127.0.0.1" in text


def test_target_equality():
    """Two identical Target objects should compare equal."""

    target1 = Target(
        hostname="localhost",
        address="127.0.0.1",
        family=socket.AF_INET,
    )

    target2 = Target(
        hostname="localhost",
        address="127.0.0.1",
        family=socket.AF_INET,
    )

    assert target1 == target2