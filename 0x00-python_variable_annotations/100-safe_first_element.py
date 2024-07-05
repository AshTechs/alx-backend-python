#!/usr/bin/env python3
"""
Module for safely retrieving the first element from a list.
"""

from typing import Sequence, Union


def safe_first_element(lst: Sequence) -> Union[Sequence, None]:
    """
    Safely retrieves the first element from a list.

    Args:
        lst (Sequence): The input list.

    Returns:
        Union[Sequence, None]:
        - The first element of the list,
        - None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
