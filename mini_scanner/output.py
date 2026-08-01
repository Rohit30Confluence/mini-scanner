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
            Iterable of ScanResult objects.

        json_output:
            Print JSON instead of a formatted table.

        output_file:
            Optional output file path.
    """

    results = list(results)

    open_ports = sum(r.status is PortStatus.OPEN for r in results)
    closed_ports = sum(r.status is PortStatus.CLOSED for r in results)
    filtered_ports = sum(r.status is PortStatus.FILTERED for r in results)
    error_ports = sum(r.status is PortStatus.ERROR for r in results)

    if json_output:
        text = _json_output(
            target=target,
            results=results,
            open_ports=open_ports,
            closed_ports=closed_ports,
            filtered_ports=filtered_ports,
            error_ports=error_ports,
        )
    else:
        text = _table_output(
            target=target,
            results=results,
            open_ports=open_ports,
            closed_ports=closed_ports,
            filtered_ports=filtered_ports,
            error_ports=error_ports,
        )

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
    *,
    open_ports: int,
    closed_ports: int,
    filtered_ports: int,
    error_ports: int,
) -> str:
    """
    Generate human-readable table output.
    """

    lines: list[str] = []

    lines.append(f"Target : {target.hostname}")
    lines.append(f"Address: {target.address}")
    lines.append("")

    lines.append(f"{'PORT':<8}{'STATE':<12}BANNER")
    lines.append("-" * 70)

    for result in results:
        lines.append(
            f"{result.port:<8}"
            f"{result.status.value:<12}"
            f"{result.banner or ''}"
        )

    lines.append("")
    lines.append("Summary")
    lines.append("-" * 70)
    lines.append(f"Scanned   : {len(results)}")
    lines.append(f"Open      : {open_ports}")
    lines.append(f"Closed    : {closed_ports}")
    lines.append(f"Filtered  : {filtered_ports}")
    lines.append(f"Errors    : {error_ports}")

    return "\n".join(lines)


def _json_output(
    target: Target,
    results: list[ScanResult],
    *,
    open_ports: int,
    closed_ports: int,
    filtered_ports: int,
    error_ports: int,
) -> str:
    """
    Generate JSON output.
    """

    data = {
        "target": {
            "hostname": target.hostname,
            "address": target.address,
        },
        "summary": {
            "ports_scanned": len(results),
            "open_ports": open_ports,
            "closed_ports": closed_ports,
            "filtered_ports": filtered_ports,
            "error_ports": error_ports,
        },
        "results": [
            result.to_dict()
            for result in results
        ],
    }

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
    )