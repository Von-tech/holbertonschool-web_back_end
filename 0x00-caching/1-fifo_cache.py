#!/usr/bin/env python3
"""Task 1: FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system """
    def __init__(self):
        """ Initialize new instance """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """ Puts key/item in cache dict """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_list:
                self.cache_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                deleted_key = self.cache_list.pop(0)
                print("DISCARD: {deleted_key}")
                del self.cache_data[deleted_key]
        """ The key is deleted and returned """

    def get(self, key):
        """ Gets key from cache dict if it exists """
        return self.cache_data.get(key)
