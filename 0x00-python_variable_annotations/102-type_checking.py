#!/usr/bin/env python3
"""
Module for zooming in on an array by repeating each element multiple times.
"""

from typing import Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on an array by repeating each element multiple times.

    Args:
        lst (Tuple[Any, ...]): The tuple of elements to zoom in on.
        factor: The factor by which each element should be repeated.

    Returns:
        Tuple: The zoomed-in tuple with elements repeated according to factor.
    """
    zoomed_in = []
    for item in lst:
        zoomed_in.extend([item] * factor)
    return tuple(zoomed_in)
