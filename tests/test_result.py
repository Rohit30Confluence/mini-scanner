"""
Tests for ScanResult and PortStatus.
"""

from __future__ import annotations

from mini_scanner.result import PortStatus, ScanResult


def test_port_status_values():
    """Verify enum values."""

    assert PortStatus.OPEN.value == "open"
    assert PortStatus.CLOSED.value == "closed"
    assert PortStatus.FILTERED.value == "filtered"
    assert PortStatus.ERROR.value == "error"


def test_scan_result_creation():
    """Create a basic ScanResult."""

    result = ScanResult(
        port=80,
        status=PortStatus.OPEN,
        banner="Apache",
    )

    assert result.port == 80
    assert result.status is PortStatus.OPEN
    assert result.banner == "Apache"


def test_scan_result_without_banner():
    """Banner should default to None."""

    result = ScanResult(
        port=22,
        status=PortStatus.OPEN,
    )

    assert result.banner is None


def test_to_dict():
    """Verify dictionary conversion."""

    result = ScanResult(
        port=443,
        status=PortStatus.OPEN,
        banner="nginx",
    )

    expected = {
        "port": 443,
        "status": "open",
        "banner": "nginx",
    }

    assert result.to_dict() == expected


def test_to_dict_without_banner():
    """Banner should remain None in dictionary output."""

    result = ScanResult(
        port=53,
        status=PortStatus.OPEN,
    )

    expected = {
        "port": 53,
        "status": "open",
        "banner": None,
    }

    assert result.to_dict() == expected


def test_str_representation():
    """Human-readable string."""

    result = ScanResult(
        port=80,
        status=PortStatus.OPEN,
        banner="Apache",
    )

    text = str(result)

    assert "80" in text
    assert "open" in text
    assert "Apache" in text


def test_repr_representation():
    """repr() should contain useful information."""

    result = ScanResult(
        port=22,
        status=PortStatus.CLOSED,
    )

    text = repr(result)

    assert "ScanResult" in text
    assert "22" in text
    assert "closed" in text


def test_equality():
    """Two identical ScanResults compare equal."""

    result1 = ScanResult(
        port=443,
        status=PortStatus.OPEN,
        banner="nginx",
    )

    result2 = ScanResult(
        port=443,
        status=PortStatus.OPEN,
        banner="nginx",
    )

    assert result1 == result2


def test_inequality():
    """Different ScanResults should not compare equal."""

    result1 = ScanResult(
        port=80,
        status=PortStatus.OPEN,
    )

    result2 = ScanResult(
        port=80,
        status=PortStatus.CLOSED,
    )

    assert result1 != result2


def test_sorting():
    """Results should sort by port."""

    results = [
        ScanResult(443, PortStatus.OPEN),
        ScanResult(22, PortStatus.OPEN),
        ScanResult(80, PortStatus.OPEN),
    ]

    results.sort(key=lambda r: r.port)

    assert [r.port for r in results] == [22, 80, 443]


def test_all_statuses():
    """Each PortStatus can be stored."""

    for status in PortStatus:
        result = ScanResult(
            port=1,
            status=status,
        )

        assert result.status is status