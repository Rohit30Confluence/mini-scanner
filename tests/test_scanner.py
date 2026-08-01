"""
Tests for scanner.py
"""

from unittest.mock import MagicMock, patch

from mini_scanner.config import Config
from mini_scanner.result import PortStatus
from mini_scanner.scanner import Scanner
from mini_scanner.target import Target


def make_target():
    return Target(
        hostname="localhost",
        address="127.0.0.1",
        family=2,  # socket.AF_INET
    )


@patch("mini_scanner.scanner.socket.socket")
def test_open_port(mock_socket):
    sock = MagicMock()
    sock.connect_ex.return_value = 0
    sock.recv.return_value = b"OpenSSH"

    mock_socket.return_value.__enter__.return_value = sock

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [22])[0]

    assert result.port == 22
    assert result.status is PortStatus.OPEN
    assert result.banner == "OpenSSH"


@patch("mini_scanner.scanner.socket.socket")
def test_closed_port(mock_socket):
    sock = MagicMock()
    sock.connect_ex.return_value = 111

    mock_socket.return_value.__enter__.return_value = sock

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [80])[0]

    assert result.status is PortStatus.CLOSED


@patch("mini_scanner.scanner.socket.socket")
def test_filtered_port(mock_socket):
    sock = MagicMock()
    sock.connect_ex.side_effect = TimeoutError

    mock_socket.return_value.__enter__.return_value = sock

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [443])[0]

    assert result.status is PortStatus.FILTERED


@patch("mini_scanner.scanner.socket.socket")
def test_banner_failure(mock_socket):
    sock = MagicMock()
    sock.connect_ex.return_value = 0
    sock.recv.side_effect = TimeoutError

    mock_socket.return_value.__enter__.return_value = sock

    scanner = Scanner(Config())
    result = scanner.scan(make_target(), [21])[0]

    assert result.status is PortStatus.OPEN
    assert result.banner is None


@patch("mini_scanner.scanner.socket.socket")
def test_multiple_ports(mock_socket):
    sock = MagicMock()

    def connect(addr):
        return 0 if addr[1] in (22, 80) else 111

    sock.connect_ex.side_effect = connect
    sock.recv.return_value = b"banner"

    mock_socket.return_value.__enter__.return_value = sock

    scanner = Scanner(Config())
    results = scanner.scan(make_target(), [22, 23, 80])

    assert len(results) == 3

    open_ports = [r.port for r in results if r.is_open]

    assert open_ports == [22, 80]