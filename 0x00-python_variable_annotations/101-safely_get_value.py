#!/usr/bin/env python3
"""
Module for safely retrieving a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary-like object.
        key (Any): The key to lookup in the dictionary.
        default ((Union[T, None], optional):
        The default value to return if key is not found (default is None)).

    Returns:
        Union: The value from the dictionary if found, else the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
