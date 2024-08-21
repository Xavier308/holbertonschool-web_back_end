#!/usr/bin/env python3
"""Insert a document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document into the specified collection."""
    # Insert the document and return the new document's ID
    return mongo_collection.insert_one(kwargs).inserted_id
