#!/usr/bin/env python3
"""
Module for summing a list of float numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of float numbers.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
