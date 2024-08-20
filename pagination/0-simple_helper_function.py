#!/usr/bin/env python3
"""
This module defines a function index_range that calculates the start and end
indexes for pagination based on page and page_size parameters.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
