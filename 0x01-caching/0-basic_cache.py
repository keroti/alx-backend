#!/usr/bin/env python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and represents a caching system
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
