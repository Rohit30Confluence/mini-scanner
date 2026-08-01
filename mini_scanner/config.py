"""
Configuration models for Mini Scanner.
"""

from __future__ import annotations

from dataclasses import dataclass

from .exceptions import ConfigurationError


@dataclass(frozen=True, slots=True)
class Config:
    """
    Runtime configuration for the scanner.

    Attributes:
        timeout:
            Socket timeout in seconds.

        workers:
            Maximum number of concurrent worker threads.

        banner_grab:
            Attempt to retrieve service banners.

        max_banner_size:
            Maximum number of bytes read from a banner.

        retries:
            Number of connection retries.

        ipv6:
            Enable IPv6 target resolution.
    """

    timeout: float = 1.0
    workers: int = 100
    banner_grab: bool = True
    max_banner_size: int = 1024
    retries: int = 0
    ipv6: bool = False

    def __post_init__(self) -> None:
        """Validate configuration values."""

        if self.timeout <= 0:
            raise ConfigurationError(
                "timeout must be greater than zero"
            )

        if self.workers < 1:
            raise ConfigurationError(
                "workers must be at least 1"
            )

        if self.workers > 1000:
            raise ConfigurationError(
                "workers cannot exceed 1000"
            )

        if self.max_banner_size < 1:
            raise ConfigurationError(
                "max_banner_size must be positive"
            )

        if self.max_banner_size > 4096:
            raise ConfigurationError(
                "max_banner_size cannot exceed 4096 bytes"
            )

        if self.retries < 0:
            raise ConfigurationError(
                "retries cannot be negative"
            )