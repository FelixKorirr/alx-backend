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

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """

        get_page_data = self.get_page(page, page_size)
        dataset_method_result = self.dataset()
        total_items = len(dataset_method_result)
        total_pages = total_items // page_size
        if total_items % page_size != 0:
            total_pages += 1

        my_dict = {
            'page_size': page_size,
            'page': page,
            'data': get_page_data,
            'next_page': (page + 1) if page < total_pages else None,
            'prev_page': (page - 1) if page > 1 else None,
            'total_pages': total_pages
        }

        return my_dict
