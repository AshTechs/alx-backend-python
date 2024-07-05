#!/usr/bin/env python3
"""
Module for creating a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable: A function that multiplies a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies a float by the pre-defined multiplier.

        Args:
            value (float): The float value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
