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
        Tuple: Zoomed-in tuple with elements repeated according to the factor.
    """
    return tuple(item for item in lst for _ in range(factor))
