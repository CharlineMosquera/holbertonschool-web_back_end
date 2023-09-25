#!/usr/bin/env python3
"""Module that defines a function that inserts
a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs) -> str:
    """Insert a new document into a MongoDB
    collection based on keyword arguments"""
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
