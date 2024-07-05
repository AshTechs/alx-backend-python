#!/usr/bin/env python3
"""
Module for summing a list of integers and float numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and float numbers.

    Args:
        mxd_lst: The list of integers and float numbers to sum.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
