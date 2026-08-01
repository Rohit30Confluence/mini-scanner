"""
Tests for parser.py
"""

import pytest

from mini_scanner.exceptions import PortValidationError
from mini_scanner.parser import parse_ports


def test_single_port():
    assert parse_ports("80") == [80]


def test_multiple_ports():
    assert parse_ports("22,80,443") == [22, 80, 443]


def test_port_range():
    assert parse_ports("1-5") == [1, 2, 3, 4, 5]


def test_mixed_ports():
    assert parse_ports("22,80,100-102") == [22, 80, 100, 101, 102]


def test_duplicate_ports_removed():
    assert parse_ports("80,80,80") == [80]


def test_ports_are_sorted():
    assert parse_ports("443,22,80") == [22, 80, 443]


@pytest.mark.parametrize(
    "value",
    [
        "",
        ",",
        "abc",
        "70000",
        "0",
        "-1",
        "100-50",
        "22,",
        "22,,80",
        "abc-100",
        "22-abc",
    ],
)
def test_invalid_inputs(value):
    with pytest.raises(PortValidationError):
        parse_ports(value)