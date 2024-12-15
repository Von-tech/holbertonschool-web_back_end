from pymongo import MongoClient

def list_all(mongo_collection):
    """
    This function lists all documents in a MongoDB collection.
    Parameters:
    mongo_collection (pymongo.collection. Collection): The MongoDB collection to query.

    Returns:
    list: A list of all documents in the collection. If the collection is empty, it returns an empty list.
    """

    return list(mongo_collection.find())
