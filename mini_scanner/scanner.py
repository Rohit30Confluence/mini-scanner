import errno
import logging
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable

from .config import Config
from .result import PortStatus, ScanResult
from .target import Target

LOGGER = logging.getLogger(__name__)

MAX_RETRIES = 2
RETRY_DELAY = 0.05
BANNER_TIMEOUT = 0.5

ERROR_STATUS_MAP = {
    0: PortStatus.OPEN,
    errno.ECONNREFUSED: PortStatus.CLOSED,
    errno.ETIMEDOUT: PortStatus.FILTERED,
    errno.EHOSTUNREACH: PortStatus.FILTERED,
    errno.ENETUNREACH: PortStatus.FILTERED,
    errno.EAGAIN: PortStatus.FILTERED,
    getattr(errno, "ECONNRESET", -1): PortStatus.CLOSED,
    getattr(errno, "ECONNABORTED", -1): PortStatus.CLOSED,
    getattr(errno, "EPIPE", -1): PortStatus.CLOSED,
    errno.EACCES: PortStatus.ERROR,
}


class Scanner:
    """Concurrent TCP connect scanner."""

    def __init__(
        self,
        config: Config,
        socket_factory: Callable[..., socket.socket] = socket.socket,
    ) -> None:
        self.config = config
        self.socket_factory = socket_factory

    def scan(
        self,
        target: Target,
        ports: Iterable[int],
    ) -> list[ScanResult]:
        ports = list(ports)
        if not ports:
            return []

        workers = min(self.config.workers, len(ports))
        results: list[ScanResult] = []

        LOGGER.debug(
            "Scanning %s with %d workers",
            target.address,
            workers,
        )

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(self._scan_port, target, port): port
                for port in ports
            }

            for future in as_completed(futures):
                results.append(future.result())

        return sorted(results, key=lambda r: r.port)

    def _create_socket(self, family: int) -> socket.socket:
        sock = self.socket_factory(family, socket.SOCK_STREAM)
        sock.settimeout(self.config.timeout)
        return sock

    def _retry_connect(
        self,
        sock: socket.socket,
        address: tuple[str, int],
    ) -> int:
        result = errno.EAGAIN

        for _ in range(MAX_RETRIES + 1):
            result = sock.connect_ex(address)
            if result != errno.EAGAIN:
                break
            time.sleep(RETRY_DELAY)

        return result

    def _classify_result(self, code: int) -> PortStatus:
        status = ERROR_STATUS_MAP.get(code)
        if status is not None:
            return status

        LOGGER.debug(
            "Unhandled connect_ex code=%s (%s)",
            code,
            errno.errorcode.get(code, "UNKNOWN"),
        )
        return PortStatus.ERROR

    def _scan_port(
        self,
        target: Target,
        port: int,
    ) -> ScanResult:
        address = (target.address, port)

        try:
            with self._create_socket(target.family) as sock:
                rc = self._retry_connect(sock, address)
                status = self._classify_result(rc)

                banner = None
                if status is PortStatus.OPEN and self.config.banner_grab:
                    banner = self._grab_banner(sock)

                return ScanResult(
                    port=port,
                    status=status,
                    banner=banner,
                )

        except socket.timeout:
            return ScanResult(port=port, status=PortStatus.FILTERED)

        except OSError as exc:
            LOGGER.debug(
                "Port %d OSError errno=%s",
                port,
                exc.errno,
            )
            return ScanResult(
                port=port,
                status=ERROR_STATUS_MAP.get(
                    exc.errno,
                    PortStatus.ERROR,
                ),
            )

    def _grab_banner(
        self,
        sock: socket.socket,
    ) -> str | None:
        previous = sock.gettimeout()

        try:
            sock.settimeout(BANNER_TIMEOUT)
            banner = sock.recv(self.config.max_banner_size)

            if not banner:
                return None

            text = banner.decode(
                "utf-8",
                errors="replace",
            ).strip()

            return text or None

        except (
            socket.timeout,
            UnicodeDecodeError,
            OSError,
        ):
            return None

        finally:
            sock.settimeout(previous)
