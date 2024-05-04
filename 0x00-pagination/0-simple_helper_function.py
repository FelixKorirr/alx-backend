#!/usr/bin/env python3
'''Simple helper function'''


def index_range(page, page_size):
    '''returns a tuple of size two containing
    a start index and end index'''
    data = list(range(0, 101))
    start_idx = ((page - 1) * 10)
    end_idx = start_idx + page_size

    return (data[start_idx], data[end_idx])
