"""
Tests for the concurrent scanner.
"""

from __future__ import annotations

import errno
import socket
from unittest.mock import MagicMock, patch

from mini_scanner.config import Config
from mini_scanner.result import PortStatus
from mini_scanner.scanner import Scanner
from mini_scanner.target import Target


def make_target() -> Target:
    """Create a reusable test target."""

    return Target(
        hostname="localhost",
        address="127.0.0.1",
        family=socket.AF_INET,
    )


def make_socket(connect_result=0, banner=b"HTTP/1.1 200 OK\r\n"):
    """Create a mocked socket."""

    sock = MagicMock()

    sock.connect_ex.return_value = connect_result
    sock.recv.return_value = banner

    manager = MagicMock()
    manager.__enter__.return_value = sock
    manager.__exit__.return_value = False

    return manager, sock


@patch("mini_scanner.scanner.socket.socket")
def test_open_port(mock_socket):
    """Open ports should be detected."""

    manager, _ = make_socket(connect_result=0)
    mock_socket.return_value = manager

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [80])[0]

    assert result.port == 80
    assert result.status is PortStatus.OPEN


@patch("mini_scanner.scanner.socket.socket")
def test_closed_port(mock_socket):
    """Closed ports should be detected."""

    manager, _ = make_socket(errno.ECONNREFUSED)
    mock_socket.return_value = manager

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [22])[0]

    assert result.status is PortStatus.CLOSED


@patch("mini_scanner.scanner.socket.socket")
def test_filtered_port(mock_socket):
    """Timeouts should be reported as filtered."""

    manager, _ = make_socket(errno.ETIMEDOUT)
    mock_socket.return_value = manager

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [443])[0]

    assert result.status is PortStatus.FILTERED


@patch("mini_scanner.scanner.socket.socket")
def test_unknown_error(mock_socket):
    """Unexpected errno values become ERROR."""

    manager, _ = make_socket(errno.ENETUNREACH)
    mock_socket.return_value = manager

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [8080])[0]

    assert result.status is PortStatus.ERROR


@patch("mini_scanner.scanner.socket.socket")
def test_banner_grab(mock_socket):
    """Banner grabbing should work."""

    manager, _ = make_socket(
        connect_result=0,
        banner=b"SSH-2.0-OpenSSH_9.0\r\n",
    )
    mock_socket.return_value = manager

    scanner = Scanner(Config(banner_grab=True))
    result = scanner.scan(make_target(), [22])[0]

    assert result.status is PortStatus.OPEN
    assert "OpenSSH" in result.banner


@patch("mini_scanner.scanner.socket.socket")
def test_banner_disabled(mock_socket):
    """Banner grabbing can be disabled."""

    manager, sock = make_socket(connect_result=0)
    mock_socket.return_value = manager

    scanner = Scanner(
        Config(
            banner_grab=False,
        )
    )

    result = scanner.scan(make_target(), [80])[0]

    sock.recv.assert_not_called()
    assert result.banner is None


@patch("mini_scanner.scanner.socket.socket")
def test_multiple_ports(mock_socket):
    """Scanner should return one result per port."""

    manager, _ = make_socket(connect_result=0)
    mock_socket.return_value = manager

    ports = [22, 80, 443, 8080]

    scanner = Scanner(Config())

    results = scanner.scan(
        make_target(),
        ports,
    )

    assert len(results) == len(ports)
    assert [r.port for r in results] == sorted(ports)


@patch("mini_scanner.scanner.socket.socket")
def test_socket_exception(mock_socket):
    """Socket exceptions become ERROR."""

    mock_socket.side_effect = OSError()

    scanner = Scanner(Config())

    result = scanner.scan(
        make_target(),
        [1234],
    )[0]

    assert result.status is PortStatus.ERROR


@patch("mini_scanner.scanner.socket.socket")
def test_banner_decode_failure(mock_socket):
    """Invalid UTF-8 should not crash banner parsing."""

    manager, _ = make_socket(
        connect_result=0,
        banner=b"\xff\xfe\xfa",
    )
    mock_socket.return_value = manager

    scanner = Scanner(Config())

    result = scanner.scan(
        make_target(),
        [80],
    )[0]

    assert result.status is PortStatus.OPEN


@patch("mini_scanner.scanner.socket.socket")
def test_worker_limit(mock_socket):
    """Scanner should work with many workers and few ports."""

    manager, _ = make_socket(connect_result=0)
    mock_socket.return_value = manager

    scanner = Scanner(
        Config(
            workers=500,
        )
    )

    results = scanner.scan(
        make_target(),
        [80],
    )

    assert len(results) == 1