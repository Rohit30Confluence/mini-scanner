"""
Tests for config.py
"""

import pytest

from mini_scanner.config import Config


def test_default_config():
    config = Config()

    assert config.timeout == 1.0
    assert config.workers == 100


def test_custom_config():
    config = Config(timeout=2.5, workers=50)

    assert config.timeout == 2.5
    assert config.workers == 50


@pytest.mark.parametrize(
    "kwargs",
    [
        {"timeout": 0},
        {"timeout": -1},
        {"workers": 0},
        {"workers": 1001},
        {"max_banner_size": 0},
        {"retries": 0},
    ],
)
def test_invalid_configuration(kwargs):
    with pytest.raises(ValueError):
        Config(**kwargs)