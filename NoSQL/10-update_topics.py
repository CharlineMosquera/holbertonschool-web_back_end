#!/usr/bin/env python3
"""Module that defines a function that changes all
topicsof a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based on the school name"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter_query, update_query)
    return result.modified_count
