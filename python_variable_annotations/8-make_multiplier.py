#!/usr/bin/env python3
"""
This module contains a type-annotated function
that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies by a specified multiplier.

    Args:
        multiplier (float):
        The value to be used as the multiplier in the created function.

    Returns:
        Callable[[float], float]:
        A function that takes a float and returns it multiplied by
        the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
