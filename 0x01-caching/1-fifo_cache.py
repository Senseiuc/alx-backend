#!/usr/bin/python3
"""
A basic cache class that inherits from
Base Caching
Author:SenseiUC
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
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
            self.cache_data[key] = item
            keys = self.cache_data.keys()
            if len(keys) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print('DISCARD:{}'.format(first_key))

    def get(self, key):
        """
        returns an item using the key
        """
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                return None
        return None
