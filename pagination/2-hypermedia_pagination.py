#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names with hypermedia.
"""

import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """ Calculate the start and end index for pagination. """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Fetch a page of the dataset """
        assert isinstance(page, int), "page must be an integer"
        assert page > 0, "page must be a positive integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page_size > 0, "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Return paginated data with hypermedia information """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }
