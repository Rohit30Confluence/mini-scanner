import socket
import threading
import time

from mini_scanner.config import Config
from mini_scanner.result import PortStatus
from mini_scanner.scanner import Scanner
from mini_scanner.target import resolve_target


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)

    port = server.getsockname()[1]

    def worker():
        conn, _ = server.accept()
        conn.sendall(b"MiniScanner Test Server")
        conn.close()
        server.close()

    threading.Thread(target=worker, daemon=True).start()

    return port


def test_local_scan():
    port = run_server()

    time.sleep(0.1)

    scanner = Scanner(Config())

    result = scanner.scan(
        resolve_target("127.0.0.1"),
        [port],
    )[0]

    assert result.status is PortStatus.OPEN