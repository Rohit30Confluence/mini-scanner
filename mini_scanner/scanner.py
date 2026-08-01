import errno
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable

from .config import Config
from .result import PortStatus, ScanResult
from .target import Target

ERROR_STATUS_MAP = {
    0: PortStatus.OPEN,
    errno.ECONNREFUSED: PortStatus.CLOSED,
    errno.ETIMEDOUT: PortStatus.FILTERED,
    errno.EHOSTUNREACH: PortStatus.ERROR,
    errno.ENETUNREACH: PortStatus.ERROR,
    errno.EACCES: PortStatus.ERROR,
}


class Scanner:
    """
    Concurrent TCP connect scanner.
    """

    def __init__(self, config: Config) -> None:
        self.config = config

    def scan(
        self,
        target: Target,
        ports: Iterable[int],
    ) -> list[ScanResult]:
        """
        Scan the supplied ports.
        """

        ports = list(ports)
        workers = min(self.config.workers, max(1, len(ports)))

        results: list[ScanResult] = []

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    self._scan_port,
                    target,
                    port,
                ): port
                for port in ports
            }

            for future in as_completed(futures):
                results.append(future.result())

        return sorted(results, key=lambda result: result.port)

    def _scan_port(
        self,
        target: Target,
        port: int,
    ) -> ScanResult:
        """
        Scan a single TCP port.
        """

        try:
            with socket.socket(
                target.family,
                socket.SOCK_STREAM,
            ) as sock:
                sock.settimeout(self.config.timeout)

                result = sock.connect_ex(
                    (
                        target.address,
                        port,
                    )
                )

                status = ERROR_STATUS_MAP.get(
                    result,
                    PortStatus.ERROR,
                )

                banner = None

                if (
                    status is PortStatus.OPEN
                    and self.config.banner_grab
                ):
                    banner = self._grab_banner(sock)

                return ScanResult(
                    port=port,
                    status=status,
                    banner=banner,
                )

        except TimeoutError:
            return ScanResult(
                port=port,
                status=PortStatus.FILTERED,
            )

        except OSError:
            return ScanResult(
                port=port,
                status=PortStatus.ERROR,
            )

    def _grab_banner(
        self,
        sock: socket.socket,
    ) -> str | None:
        """
        Attempt to read a service banner.
        """

        try:
            banner = sock.recv(
                self.config.max_banner_size
            )

            if not banner:
                return None

            return banner.decode(
                "utf-8",
                errors="replace",
            ).strip()

        except (
            TimeoutError,
            UnicodeDecodeError,
            OSError,
        ):
            return None