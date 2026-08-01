"""
Tests for the port parser.
"""

import pytest

from mini_scanner.exceptions import PortValidationError
from mini_scanner.parser import parse_ports


def test_single_port():
    """Parse a single port."""

    assert parse_ports("80") == [80]


def test_multiple_ports():
    """Parse multiple comma-separated ports."""

    assert parse_ports("22,80,443") == [22, 80, 443]


def test_port_range():
    """Parse a simple range."""

    assert parse_ports("20-25") == [20, 21, 22, 23, 24, 25]


def test_mixed_ports():
    """Parse ports mixed with ranges."""

    assert parse_ports("22,80,1000-1002") == [
        22,
        80,
        1000,
        1001,
        1002,
    ]


def test_duplicates_removed():
    """Duplicate ports should be removed."""

    assert parse_ports("80,80,80,22,22") == [22, 80]


def test_unsorted_input():
    """Returned ports should always be sorted."""

    assert parse_ports("443,80,22") == [22, 80, 443]


@pytest.mark.parametrize(
    "text",
    [
        "",
        " ",
        ",",
        ",,",
    ],
)
def test_empty_input(text):
    """Reject empty specifications."""

    with pytest.raises(PortValidationError):
        parse_ports(text)


@pytest.mark.parametrize(
    "text",
    [
        "abc",
        "http",
        "22,http",
        "80-abc",
    ],
)
def test_non_numeric(text):
    """Reject non-numeric values."""

    with pytest.raises(PortValidationError):
        parse_ports(text)


@pytest.mark.parametrize(
    "text",
    [
        "0",
        "-1",
        "65536",
        "99999",
    ],
)
def test_invalid_port_numbers(text):
    """Ports must be between 1 and 65535."""

    with pytest.raises(PortValidationError):
        parse_ports(text)


@pytest.mark.parametrize(
    "text",
    [
        "100-90",
        "1000-999",
        "20-10",
    ],
)
def test_invalid_ranges(text):
    """Range start cannot exceed range end."""

    with pytest.raises(PortValidationError):
        parse_ports(text)


def test_large_range():
    """Large ranges should parse correctly."""

    ports = parse_ports("1-1024")

    assert len(ports) == 1024
    assert ports[0] == 1
    assert ports[-1] == 1024


def test_whitespace():
    """Whitespace should be ignored."""

    assert parse_ports(" 22 , 80 , 443 ") == [22, 80, 443]


def test_mixed_duplicates():
    """Duplicates across ranges and single ports should be removed."""

    assert parse_ports("20-22,21,22") == [20, 21, 22]


def test_full_valid_range():
    """Maximum valid range."""

    ports = parse_ports("1-65535")

    assert ports[0] == 1
    assert ports[-1] == 65535
    assert len(ports) == 65535