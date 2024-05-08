#!/usr/bin/env python3
'''This module demonstrates FIFO caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''This class represent the subclass FIFOCache'''

    def __init__(self):
        '''Initializes this subclass'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds key-value pairs to cache '''

        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        '''Returns the value linked to argument key'''
        if key is None:
            return None
        return self.cache_data[key]
