#!/usr/bin/env python3
"""Task 0: Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache system that inherits from the parent class """
    def put(self, key, item):
        """ Puts key/item in cache dict """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets key from cache dict if it exists """
        return self.cache_data.get(key)
