#!/usr/bin/env python3
"""Module that defines a function that
lists all documents in a collection"""


def list_all(mongo_collection) -> list:
    """List all documents in a MongoDB collection"""
    documents = []
    for document in mongo_collection.find({}):
        documents.append(document)
    return documents
