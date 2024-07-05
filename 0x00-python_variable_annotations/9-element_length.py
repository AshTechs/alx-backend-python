#!/usr/bin/env python3
"""
Module for getting the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List: List of tuples where each tuple contains an element & its length
    """
    return [(i, len(i)) for i in lst]
