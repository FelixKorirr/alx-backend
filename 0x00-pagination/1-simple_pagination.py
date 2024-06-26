#!/usr/bin/env python3
'''Simple helper function'''
import csv
import math
from typing import List


def index_range(page, page_size):
    '''returns a tuple of size two containing
    a start index and end index'''
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns dataset between page and page_size"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        values = index_range(page, page_size)
        data = self.dataset()
        x, y = values
        if y > len(data):
            return []
        return data[x:y]
