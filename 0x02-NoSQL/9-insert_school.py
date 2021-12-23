#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Method that will inserts a new doc in a collection """
    the_Doc = {}
    for k, v in kwargs.items():
        the_Doc[k] = v
    new_insert = mongo_collection.insert_one(the_Doc)
    return new_insert.inserted_id





                    
