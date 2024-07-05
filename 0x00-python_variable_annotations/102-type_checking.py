#!/usr/bin/env python3

from typing import List, Tuple, Union


def zoom_array(lst: List[int], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on a list of integers by repeating each element multiple times.

    Args:
        lst (List[int]): The list of integers to zoom in on.
        factor: The factor by which each element should be repeated.

    Returns:
        Tuple: Zoomed-in tuple with integers repeated according to the factor.
    """
    zoomed_in = tuple(item for item in lst for _ in range(factor))
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
