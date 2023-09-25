#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Retrieve a list of schools having a specific topic"""
    filter_query = {"topics": topic}
    schools = list(mongo_collection.find(filter_query))
    return schools
