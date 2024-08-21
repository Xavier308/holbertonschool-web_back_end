#!/usr/bin/env python3
"""Provides statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

if __name__ == "__main__":
    # Establish connection to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Access the nginx collection in the logs database
    collection = client.logs.nginx

    # Count total documents in the nginx collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Display count of different HTTP methods used in logs
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the documents where method is 'GET' and path is '/status'
    status_checks = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_checks} status checks")
