"""
Output formatting utilities for Mini Scanner.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .result import PortStatus, ScanResult
from .target import Target


def print_results(
    target: Target,
    results: Iterable[ScanResult],
    *,
    json_output: bool = False,
    output_file: str | None = None,
) -> None:
    """
    Print scan results.

    Args:
        target:
            Target that was scanned.

        results:
            Scan results.

        json_output:
            Print JSON instead of table output.

        output_file:
            Optional output file.
    """

    results = list(results)

    if json_output:
        text = _json_output(target, results)
    else:
        text = _table_output(target, results)

    if output_file:
        Path(output_file).write_text(
            text,
            encoding="utf-8",
        )
    else:
        print(text)


def _table_output(
    target: Target,
    results: list[ScanResult],
) -> str:
    """
    Build human-readable output.
    """

    lines = []

    lines.append(f"Target : {target.hostname}")
    lines.append(f"Address: {target.address}")
    lines.append("")

    lines.append(f"{'PORT':<8}{'STATE':<12}BANNER")
    lines.append("-" * 70)

    open_ports = 0

    for result in results:

        banner = result.banner or ""

        lines.append(
            f"{result.port:<8}"
            f"{result.status.value:<12}"
            f"{banner}"
        )

        if result.status is PortStatus.OPEN:
            open_ports += 1

    lines.append("")
    lines.append(f"Open ports : {open_ports}")
    lines.append(f"Scanned    : {len(results)}")

    return "\n".join(lines)


def _json_output(
    target: Target,
    results: list[ScanResult],
) -> str:
    """
    Build JSON output.
    """

    data = {
        "target": {
            "hostname": target.hostname,
            "address": target.address,
        },
        "summary": {
            "ports_scanned": len(results),
            "open_ports": sum(
                r.status is PortStatus.OPEN
                for r in results
            ),
        },
        "results": [
            result.to_dict()
            for result in results
        ],
    }

    return json.dumps(
        data,
        indent=4,
    )