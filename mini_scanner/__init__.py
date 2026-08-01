"""
Mini Scanner

A lightweight, concurrent TCP port scanner built with modern Python.

Mini Scanner provides a clean, extensible API for TCP port scanning,
target resolution, result formatting, and configuration management.

Example:
    >>> from mini_scanner import (
    ...     Scanner,
    ...     Config,
    ...     resolve_target,
    ... )
    >>>
    >>> config = Config()
    >>> target = resolve_target("scanme.nmap.org")
    >>> scanner = Scanner(config)
    >>> results = scanner.scan(target, [22, 80, 443])

Author:
    Rohit Dinde

License:
    MIT
"""

from .config import Config
from .exceptions import (
    ConfigurationError,
    MiniScannerError,
    PortValidationError,
    ScanError,
    TargetResolutionError,
)
from .result import PortStatus, ScanResult
from .scanner import Scanner
from .target import Target, resolve_target
from .version import __version__

__author__ = "Rohit Dinde"
__license__ = "MIT"

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    # Configuration
    "Config",
    # Scanner
    "Scanner",
    # Target
    "Target",
    "resolve_target",
    # Results
    "ScanResult",
    "PortStatus",
    # Exceptions
    "MiniScannerError",
    "ConfigurationError",
    "TargetResolutionError",
    "PortValidationError",
    "ScanError",
]