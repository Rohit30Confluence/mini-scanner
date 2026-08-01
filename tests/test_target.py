"""
Tests for target.py
"""

import pytest

from mini_scanner.exceptions import TargetResolutionError
from mini_scanner.target import resolve_target


def test_ipv4_resolution():
    target = resolve_target("127.0.0.1")

    assert target.address == "127.0.0.1"
    assert target.is_ipv4


def test_localhost_resolution():
    target = resolve_target("localhost")

    assert target.address


def test_invalid_target():
    with pytest.raises(TargetResolutionError):
        resolve_target("this-host-does-not-exist.invalid")