"""
End-to-end integration tests for Mini Scanner.
"""

from __future__ import annotations

import socket
import threading

from mini_scanner.config import Config
from mini_scanner.result import PortStatus
from mini_scanner.scanner import Scanner
from mini_scanner.target import resolve_target


def _run_server(server: socket.socket, stop_event: threading.Event) -> None:
    """Accept connections until told to stop."""

    server.settimeout(0.2)

    while not stop_event.is_set():
        try:
            client, _ = server.accept()
            client.sendall(b"Mini Scanner Test Server\r\n")
            client.close()
        except TimeoutError:
            continue
        except OSError:
            break


def test_scan_local_server():
    """Scan a real local TCP server."""

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    server.bind(("127.0.0.1", 0))
    server.listen(5)

    port = server.getsockname()[1]

    stop_event = threading.Event()

    thread = threading.Thread(
        target=_run_server,
        args=(server, stop_event),
        daemon=True,
    )

    thread.start()

    try:
        target = resolve_target("127.0.0.1")

        scanner = Scanner(
            Config(
                timeout=1.0,
                banner_grab=True,
            )
        )

        result = scanner.scan(
            target,
            [port],
        )[0]

        assert result.port == port
        assert result.status is PortStatus.OPEN
        assert result.banner is not None
        assert "Mini Scanner" in result.banner

    finally:
        stop_event.set()
        server.close()
        thread.join(timeout=1)


def test_scan_closed_port():
    """A closed localhost port should not be reported as OPEN."""

    target = resolve_target("127.0.0.1")

    scanner = Scanner(
        Config(timeout=0.5)
    )

    result = scanner.scan(
        target,
        [65534],
    )[0]

    assert result.status in (
        PortStatus.CLOSED,
        PortStatus.FILTERED,
        PortStatus.ERROR,
    )


def test_multiple_ports():
    """Scanning multiple ports returns one result per port."""

    target = resolve_target("127.0.0.1")

    scanner = Scanner(Config())

    ports = [22, 80, 443]

    results = scanner.scan(
        target,
        ports,
    )

    assert len(results) == len(ports)

    assert sorted(
        r.port for r in results
    ) == sorted(ports)


def test_result_sorting():
    """Scanner should always return sorted results."""

    target = resolve_target("127.0.0.1")

    scanner = Scanner(Config())

    ports = [8080, 80, 22]

    results = scanner.scan(
        target,
        ports,
    )

    assert [r.port for r in results] == sorted(ports)


def test_banner_disabled():
    """Banner grabbing can be disabled."""

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )

    server.bind(("127.0.0.1", 0))
    server.listen(1)

    port = server.getsockname()[1]

    stop_event = threading.Event()

    thread = threading.Thread(
        target=_run_server,
        args=(server, stop_event),
        daemon=True,
    )

    thread.start()

    try:
        target = resolve_target("127.0.0.1")

        scanner = Scanner(
            Config(
                banner_grab=False,
            )
        )

        result = scanner.scan(
            target,
            [port],
        )[0]

        assert result.status is PortStatus.OPEN
        assert result.banner is None

    finally:
        stop_event.set()
        server.close()
        thread.join(timeout=1)