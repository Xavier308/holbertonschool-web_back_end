#!/usr/bin/env python3
"""
This module contains a type-annotated function
to return the floor value of a float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor value of a float.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The floor value of the float.
    """
    return math.floor(n)
