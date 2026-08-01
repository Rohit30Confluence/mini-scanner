"""
Tests for output.py
"""

import json

from mini_scanner.output import print_results
from mini_scanner.result import PortStatus, ScanResult
from mini_scanner.target import Target


def make_target():
    return Target(
        hostname="localhost",
        address="127.0.0.1",
        family=2,
    )


def test_json_output(tmp_path):
    file = tmp_path / "output.json"

    print_results(
        target=make_target(),
        results=[
            ScanResult(
                port=80,
                status=PortStatus.OPEN,
            )
        ],
        json_output=True,
        output_file=str(file),
    )

    data = json.loads(file.read_text())

    assert data["summary"]["open_ports"] == 1


def test_table_output(tmp_path):
    file = tmp_path / "report.txt"

    print_results(
        target=make_target(),
        results=[
            ScanResult(
                port=22,
                status=PortStatus.OPEN,
                banner="OpenSSH",
            )
        ],
        output_file=str(file),
    )

    text = file.read_text()

    assert "22" in text
    assert "OpenSSH" in text