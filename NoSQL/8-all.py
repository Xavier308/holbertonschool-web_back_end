#!/usr/bin/env python3
"""List all documents."""


def list_all(mongo_collection):
    """List all documents in the collection."""
    # Retrieve documents from collection
    documents = mongo_collection.find()

    # Convert cursor to a list and return it
    return list(documents)
