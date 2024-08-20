#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            index_map = {i: dataset[i] for i in range(len(dataset))}
            self.__indexed_dataset = index_map
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Retrieve a page with hypermedia pagination that
           is resilient to deletions.
        """
        assert 0 <= index < len(self.__indexed_dataset), "Index out of range"

        indexed_data = self.__indexed_dataset
        current_index = index
        result_data = []

        while (len(result_data) < page_size and
               current_index < len(indexed_data)):
            if current_index in indexed_data:
                result_data.append(indexed_data[current_index])
            current_index += 1

        if current_index < len(indexed_data):
            next_index = current_index
        else:
            next_index = None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(result_data),
            'data': result_data
        }
