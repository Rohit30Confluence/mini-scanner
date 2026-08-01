"""
Concurrent TCP scanning engine for Mini Scanner.
"""

from __future__ import annotations

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable

from .config import Config
from .result import ScanResult
from .target import Target


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

        Returns
        -------
        list[ScanResult]
        """

        results: list[ScanResult] = []

        with ThreadPoolExecutor(
            max_workers=self.config.workers
        ) as executor:

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

        return sorted(results, key=lambda r: r.port)

    def _scan_port(
        self,
        target: Target,
        port: int,
    ) -> ScanResult:
        """
        Scan a single TCP port.
        """

        family = target.family

        try:
            with socket.socket(
                family,
                socket.SOCK_STREAM,
            ) as sock:

                sock.settimeout(self.config.timeout)

                result = sock.connect_ex(
                    (
                        target.address,
                        port,
                    )
                )

                if result == 0:

                    banner = None

                    if self.config.banner_grab:
                        banner = self._grab_banner(sock)

                    return ScanResult(
                        port=port,
                        status="open",
                        banner=banner,
                    )

                return ScanResult(
                    port=port,
                    status="closed",
                    banner=None,
                )

        except TimeoutError:
            return ScanResult(
                port=port,
                status="filtered",
                banner=None,
            )

        except OSError:
            return ScanResult(
                port=port,
                status="filtered",
                banner=None,
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