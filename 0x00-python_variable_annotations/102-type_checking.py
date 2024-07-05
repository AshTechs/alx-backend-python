#!/usr/bin/env python3
"""
Module for zooming in on an array by repeating each element multiple times.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zooms in on an array by repeating each element multiple times.

    Args:
        lst (Tuple): The tuple of elements to zoom in on.
        factor: The factor by which each element should be repeated.

    Returns:
        Tuple: The zoomed-in tuple with elements repeated according to factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
