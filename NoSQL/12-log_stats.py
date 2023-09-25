#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

# Connect to your MongoDB server and select the collection
client = MongoClient("mongodb://localhost:27017")
db = client["logs"]  # Replace with your database name
collection = db["nginx"]  # Replace with your collection name

# Calculate the total number of logs
total_logs = collection.count_documents({})

# Initialize counts for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {
    method: collection.count_documents({"method": method})
    for method in http_methods
    }

# Calculate the number of logs with method=GET and path=/status
status_check_count = collection.count_documents({
    "method": "GET", "path": "/status"})

# Display the statistics
print(f"{total_logs} logs")
print("Methods:")
for method in http_methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
