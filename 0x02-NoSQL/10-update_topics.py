#!/usr/bin/env python3
""" Write a Python function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
        """ Method that changes topics """
        mongo_collection.update({"name": name}, {"$set": {"topics": topics}}, multi=True)


                                
