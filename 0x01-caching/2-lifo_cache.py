#!/usr/bin/python3
"""
A basic cache class that inherits from
Base Caching
Author:SenseiUC
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    A class that implements first in first out out
    approach of caching
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds item to the object dict
        """
        if key is not None and item is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key, _ = self.cache_data.popitem(True)
                print('DISCARD:{}'.format(last_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        returns an item using the key
        """
        return self.cache_data.get(key, None)
