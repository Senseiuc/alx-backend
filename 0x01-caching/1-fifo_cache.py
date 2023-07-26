#!/usr/bin/python3
"""
A basic cache class that inherits from
Base Caching
Author:SenseiUC
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class that implements first in first out out
    approach of caching
    """

    def put(self, key, item):
        """
        Adds item to the object dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            keys = self.cache_data.keys()
            if len(keys) > BaseCaching.MAX_ITEMS:
                print('DISCARD:{}'.format(list(keys)[0]))
                del self.cache_data[list(keys)[0]]

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
