#!/usr/bin/env python3
"""
Module for creating a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of an integer or float.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple where:
        - The first element is the string
        - The second element is the square of the number.
    """
    return (k, float(v ** 2))
