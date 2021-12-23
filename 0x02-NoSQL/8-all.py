#!/usr/bin/env python3
""" Write a Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """ Method that will lists all docs """
    if mongo_collection:
        return mongo_collection.find()
    else:
        return []
