#!/usr/bin/env python3
"""Task 3: LRU caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU cache system """
    def __init__(self):
        """ Initialize new instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Puts key/item in cache dict """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                deleted_key = list(self.cache_data.keys())[0]
                self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(deleted_key))

    def get(self, key):
        """ Gets key from cache dict if it exists """
        if key is None or key not in self.cache_data:
            return None
        """ Satisfying requirement """
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
