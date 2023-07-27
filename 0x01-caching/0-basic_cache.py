#!/usr/bin/env python3
"""
A basic cache class that inherits from
Base Caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache class
    """

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

    def put(self, key, item):
        """
        Adds an item to the cache data dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
