#!/usr/bin/env python3
'''This module demonstrates LIFO Caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''Represents subclass LIFOCache'''

    def __init__(self):
        '''Initializes LIFOCache'''

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds / updates a cache'''

        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(True)
            print(f'DISCARD: {first_key}')

    def get(self, key):
        '''Returns the value in cache_data dictionary
        linked to key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
