#!/usr/bin/env python3
"""Update topics in a school document."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document by name."""
    # Update topics field for all documents matching the name
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
