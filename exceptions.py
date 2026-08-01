"""
Custom exceptions used throughout Mini Scanner.
"""


class MiniScannerError(Exception):
    """Base exception for the project."""


class ConfigurationError(MiniScannerError):
    """Raised when configuration is invalid."""


class TargetResolutionError(MiniScannerError):
    """Raised when a target cannot be resolved."""


class PortValidationError(MiniScannerError):
    """Raised when invalid ports are provided."""


class ScanError(MiniScannerError):
    """Raised when a scan fails unexpectedly."""