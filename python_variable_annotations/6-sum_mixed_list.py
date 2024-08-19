#!/usr/bin/env python3
"""
This module contains a type-annotated function
to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        The list of integers and floats to be summed.

    Returns:
        float: The total sum of the integers and floats in the list.
    """
    return float(sum(mxd_lst))
