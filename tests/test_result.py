"""
Tests for result.py
"""

from mini_scanner.result import PortStatus, ScanResult


def test_open_result():
    result = ScanResult(
        port=80,
        status=PortStatus.OPEN,
    )

    assert result.is_open
    assert not result.is_closed


def test_json_conversion():
    result = ScanResult(
        port=22,
        status=PortStatus.OPEN,
        banner="OpenSSH",
    )

    data = result.to_dict()

    assert data["port"] == 22
    assert data["status"] == "open"
    assert data["banner"] == "OpenSSH"


def test_string_representation():
    result = ScanResult(
        port=443,
        status=PortStatus.CLOSED,
    )

    assert "443" in str(result)
    assert "closed" in str(result)