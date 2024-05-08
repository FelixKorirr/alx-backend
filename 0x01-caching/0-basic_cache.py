#!/usr/bin/env python3
'''Task 0 module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Represents subclass BasicCache'''

    def put(self, key, item):
        '''Adds key value pairs to a dictionary
            Args:
                key : unique identifier
                item : value to be added
        '''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''Accesses the value using the unique ID
            Args:
                key : unique ID
        '''
        if key is None:
            return None
        else:
            for k, v in self.cache_data.items():
                if k == key:
                    return v
