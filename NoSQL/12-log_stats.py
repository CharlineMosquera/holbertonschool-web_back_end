#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngix = client.logs.nginx

    count = ngix.count_documents({})
    print("{} logs".format(count))
    print("Methods:")
    for method in methods:
        count = ngix.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    count = ngix.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(count))
