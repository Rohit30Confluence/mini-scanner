"""
Tests for output formatting.
"""

from __future__ import annotations

import json

from mini_scanner.output import print_results
from mini_scanner.result import PortStatus, ScanResult
from mini_scanner.target import Target


def make_target() -> Target:
    """Create a reusable target."""

    return Target(
        hostname="localhost",
        address="127.0.0.1",
        family=2,
    )


def make_results() -> list[ScanResult]:
    """Create reusable scan results."""

    return [
        ScanResult(
            port=22,
            status=PortStatus.OPEN,
            banner="OpenSSH",
        ),
        ScanResult(
            port=80,
            status=PortStatus.OPEN,
            banner="Apache",
        ),
        ScanResult(
            port=443,
            status=PortStatus.CLOSED,
        ),
        ScanResult(
            port=8080,
            status=PortStatus.FILTERED,
        ),
        ScanResult(
            port=9000,
            status=PortStatus.ERROR,
        ),
    ]


def test_table_output(capsys):
    """Human-readable table output."""

    print_results(
        target=make_target(),
        results=make_results(),
    )

    output = capsys.readouterr().out

    assert "localhost" in output
    assert "127.0.0.1" in output

    assert "22" in output
    assert "80" in output
    assert "443" in output

    assert "OpenSSH" in output
    assert "Apache" in output

    assert "Summary" in output
    assert "Open" in output
    assert "Closed" in output
    assert "Filtered" in output
    assert "Errors" in output


def test_json_output(capsys):
    """JSON output."""

    print_results(
        target=make_target(),
        results=make_results(),
        json_output=True,
    )

    output = capsys.readouterr().out

    data = json.loads(output)

    assert data["target"]["hostname"] == "localhost"
    assert data["target"]["address"] == "127.0.0.1"

    assert data["summary"]["ports_scanned"] == 5
    assert data["summary"]["open_ports"] == 2
    assert data["summary"]["closed_ports"] == 1
    assert data["summary"]["filtered_ports"] == 1
    assert data["summary"]["error_ports"] == 1

    assert len(data["results"]) == 5


def test_output_file(tmp_path):
    """Output should be written to a file."""

    output = tmp_path / "scan.txt"

    print_results(
        target=make_target(),
        results=make_results(),
        output_file=str(output),
    )

    assert output.exists()

    text = output.read_text(encoding="utf-8")

    assert "localhost" in text
    assert "Summary" in text


def test_json_file(tmp_path):
    """JSON output should be written correctly."""

    output = tmp_path / "scan.json"

    print_results(
        target=make_target(),
        results=make_results(),
        json_output=True,
        output_file=str(output),
    )

    assert output.exists()

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["summary"]["ports_scanned"] == 5


def test_empty_results(capsys):
    """No scan results."""

    print_results(
        target=make_target(),
        results=[],
    )

    output = capsys.readouterr().out

    assert "Scanned" in output
    assert "0" in output


def test_unicode_banner(capsys):
    """Unicode banners should print correctly."""

    results = [
        ScanResult(
            port=80,
            status=PortStatus.OPEN,
            banner="こんにちは",
        )
    ]

    print_results(
        target=make_target(),
        results=results,
    )

    output = capsys.readouterr().out

    assert "こんにちは" in output


def test_result_order(capsys):
    """Output should preserve the supplied order."""

    results = [
        ScanResult(443, PortStatus.OPEN),
        ScanResult(22, PortStatus.OPEN),
    ]

    print_results(
        target=make_target(),
        results=results,
    )

    output = capsys.readouterr().out

    assert output.index("443") < output.index("22")