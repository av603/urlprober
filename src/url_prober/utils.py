"""Utility functions for URL Prober."""

from typing import Union
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """Check if a given string is a valid URL.

    Args:
        url: The URL string to validate

    Returns:
        bool: True if URL is valid, False otherwise

    Examples:
        >>> is_valid_url("https://example.com")
        True
        >>> is_valid_url("not_a_url")
        False
    """
    if not url:
        return False

    try:
        result = urlparse(url)
        return all(
            [
                result.scheme in ("http", "https"),
                result.netloc,
            ]
        )
    except (AttributeError, ValueError):
        return False


def get_bool_from_arg(
    arg: Union[str, bool, None], default: bool = True
) -> bool:
    """Convert argument to boolean value.

    Args:
        arg: Value to convert:
            - str: 'true', 'false', '1', '0', etc.
            - bool: True or False
            - None: will return default value
        default: Value to return if arg is None (defaults to True)

    Returns:
        bool: Converted boolean value or default if arg is None

    Examples:
        >>> get_bool_from_arg('true')
        True
        >>> get_bool_from_arg('0')
        False
        >>> get_bool_from_arg(True)
        True
        >>> get_bool_from_arg(None)  # Returns default value (True)
        True
        >>> get_bool_from_arg(None, default=False)  # Returns specified default
        False
    """
    if arg is None:
        return default
    elif isinstance(arg, bool):
        return arg
    elif str(arg).lower() in ("true", "1", "yes", "on"):
        return True
    elif str(arg).lower() in ("false", "0", "no", "off"):
        return False

    # fallthrough case raises a ValueError
    raise ValueError(f"Invalid boolean argument: {arg}")
