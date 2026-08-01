"""
Tests for Config.
"""

import pytest

from mini_scanner.config import Config
from mini_scanner.exceptions import ConfigurationError


def test_default_configuration():
    """Verify default values."""

    config = Config()

    assert config.timeout == 1.0
    assert config.workers == 100
    assert config.retries == 0
    assert config.banner_grab is True
    assert config.max_banner_size == 1024
    assert config.ipv6 is False


def test_custom_configuration():
    """Verify custom values."""

    config = Config(
        timeout=2.5,
        workers=50,
        retries=2,
        banner_grab=False,
        max_banner_size=2048,
        ipv6=True,
    )

    assert config.timeout == 2.5
    assert config.workers == 50
    assert config.retries == 2
    assert config.banner_grab is False
    assert config.max_banner_size == 2048
    assert config.ipv6 is True


@pytest.mark.parametrize(
    "timeout",
    [
        0,
        -1,
        -5,
    ],
)
def test_invalid_timeout(timeout):
    """Timeout must be positive."""

    with pytest.raises(ConfigurationError):
        Config(timeout=timeout)


@pytest.mark.parametrize(
    "workers",
    [
        0,
        -1,
        -100,
    ],
)
def test_invalid_workers(workers):
    """Workers must be positive."""

    with pytest.raises(ConfigurationError):
        Config(workers=workers)


@pytest.mark.parametrize(
    "retries",
    [
        -1,
        -5,
    ],
)
def test_invalid_retries(retries):
    """Retries cannot be negative."""

    with pytest.raises(ConfigurationError):
        Config(retries=retries)


@pytest.mark.parametrize(
    "size",
    [
        0,
        -1024,
    ],
)
def test_invalid_banner_size(size):
    """Banner size must be positive."""

    with pytest.raises(ConfigurationError):
        Config(max_banner_size=size)


def test_config_is_immutable():
    """Config should be frozen."""

    config = Config()

    with pytest.raises(AttributeError):
        config.timeout = 5.0


def test_config_equality():
    """Two identical configs should compare equal."""

    assert Config() == Config()


def test_config_repr():
    """repr() should contain useful information."""

    text = repr(Config())

    assert "Config" in text
    assert "timeout" in text
    assert "workers" in text