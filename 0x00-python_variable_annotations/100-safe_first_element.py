#!/usr/bin/env python3
"""
Module for safely retrieving the first element from a list.
"""

from typing import Sequence, TypeVar, Union

T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Union[T, None]:
    """
    Safely retrieves the first element from a list.

    Args:
        lst (Sequence[T]): The input list.

    Returns:
        Union: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
