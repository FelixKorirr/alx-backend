#!/usr/bin/env python3
'''This module demonstrates FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''This class represent the subclass FIFOCache'''

    def __init__(self):
        '''Initializes this subclass'''
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        '''Adds key-value pairs to cache '''
        if key is None or item is None:
            pass
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.cache_keys.pop(0)
            print(f'DISCARD : {oldest_key}')
            del self.cache_data[oldest_key]
        self.cache_data[key] = item
        self.cache_keys.append(key)

    def get(self, key):
        '''Returns the values in self.cache_data'''
        if key is None:
            return None
        return self.cache_data[key]
