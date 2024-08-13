#!/usr/bin/env python3
"""
This module contains a type-annotated function
to create a tuple with a string and the square of a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple containing a string and the square of a number.

    Args:
        k (str): The string to be included in the tuple.
        v (Union[int, float]): The number to be squared and included in the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first
        element is the string and the second element is
        the square of the provided number.
    """
    return (k, float(v ** 2))
