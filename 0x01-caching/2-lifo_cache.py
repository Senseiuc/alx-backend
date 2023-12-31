#!/usr/bin/env python3
"""
A basic cache class that inherits from
Base Caching
Author:SenseiUC
"""
from collections import OrderedDict
from base_caching import BaseCaching


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
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print('DISCARD:{}'.format(last_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        returns an item using the key
        """
        return self.cache_data.get(key, None)

