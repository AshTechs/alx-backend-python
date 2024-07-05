#!/usr/bin/env python3
"""
Module for zooming in on an array by repeating each element multiple times.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zooms in on an array by repeating each element multiple times.

    Args:
        lst (Tuple[Any, ...]): The tuple of elements to zoom in on.
        factor(int, optional): Factor by which each element should be repeated

    Returns:
        Tuple[Any, ...]: Zoomed-in tuple with elements repeated to the factor.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
