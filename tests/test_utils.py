"""Tests for URL Prober utility functions."""

import pytest

from url_prober.utils import get_bool_from_arg, is_valid_url


@pytest.mark.parametrize(
    "url,expected",
    [
        # Valid URLs
        ("https://www.example.com", True),
        ("http://example.com", True),
        ("https://sub.domain.com/path", True),
        ("https://example.com:8080", True),
        ("https://example.com/path?query=1", True),
        ("http://localhost:5000", True),
        ("http://127.0.0.1:8080", True),
        # Invalid URLs
        ("", False),
        ("not_a_url", False),
        ("http://", False),
        ("https://", False),
        ("ftp://example.com", False),  # if we only want http(s)
        ("http:/example.com", False),
        ("https:example.com", False),
        ("example.com", False),
    ],
)
def test_is_valid_url(url: str, expected: bool):
    """Test URL validation with various inputs.

    Args:
        url: URL string to test
        expected: Expected validation result
    """
    assert is_valid_url(url) == expected


@pytest.mark.parametrize(
    "arg,default,expected",
    [
        # String inputs - truthy values
        ("true", True, True),
        ("True", True, True),
        ("TRUE", True, True),
        ("1", True, True),
        ("yes", True, True),
        ("Yes", True, True),
        ("YES", True, True),
        ("on", True, True),
        ("On", True, True),
        ("ON", True, True),
        # String inputs - falsy values
        ("false", True, False),
        ("False", True, False),
        ("FALSE", True, False),
        ("0", True, False),
        ("no", True, False),
        ("No", True, False),
        ("NO", True, False),
        ("off", True, False),
        ("Off", True, False),
        ("OFF", True, False),
        # Boolean inputs
        (True, False, True),
        (False, True, False),
        # None input - should return default
        (None, True, True),
        (None, False, False),
    ],
)
def test_get_bool_from_arg(arg, default, expected):
    """Test boolean argument parsing with valid inputs.

    Args:
        arg: Input value to parse
        default: Default value to use
        expected: Expected result
    """
    assert get_bool_from_arg(arg, default) == expected


def test_get_bool_from_arg_default_parameter():
    """Test that default parameter defaults to True when not specified."""
    assert get_bool_from_arg(None) is True


@pytest.mark.parametrize(
    "invalid_input",
    [
        "invalid",
        "",
        "maybe",
        "enabled",
        "disabled",
        "123",
        "-1",
    ],
)
def test_get_bool_from_arg_invalid_raises_error(invalid_input):
    """Test that invalid string inputs raise ValueError.

    Args:
        invalid_input: String that should not be accepted
    """
    with pytest.raises(ValueError):
        get_bool_from_arg(invalid_input)


@pytest.mark.parametrize(
    "invalid_type",
    [
        123,
        1.23,
        [],
        {},
        set(),
        lambda x: x,
    ],
)
def test_get_bool_from_arg_invalid_type_raises_error(invalid_type):
    """Test that non-string/non-bool types raise ValueError.

    Args:
        invalid_type: Value of invalid type
    """
    with pytest.raises(ValueError):
        get_bool_from_arg(invalid_type)
