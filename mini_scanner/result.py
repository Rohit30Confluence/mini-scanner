"""
Scan result models.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum


class PortStatus(str, Enum):
    """Possible TCP port states."""

    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"
    ERROR = "error"


@dataclass(frozen=True, slots=True)
class ScanResult:
    """
    Represents the result of scanning a single TCP port.
    """

    port: int
    status: PortStatus
    banner: str | None = None

    @property
    def is_open(self) -> bool:
        return self.status is PortStatus.OPEN

    @property
    def is_closed(self) -> bool:
        return self.status is PortStatus.CLOSED

    @property
    def is_filtered(self) -> bool:
        return self.status is PortStatus.FILTERED

    @property
    def has_banner(self) -> bool:
        return bool(self.banner)

    def to_dict(self) -> dict:
        """Convert to a JSON-friendly dictionary."""

        data = asdict(self)
        data["status"] = self.status.value
        return data

    def __str__(self) -> str:
        if self.banner:
            return f"{self.port:<5} {self.status.value:<10} {self.banner}"

        return f"{self.port:<5} {self.status.value}"