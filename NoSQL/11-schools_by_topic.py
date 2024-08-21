#!/usr/bin/env python3
"""Find schools by topic in MongoDB."""


def schools_by_topic(mongo_collection, topic):
    """Retrieve and return schools that include a specific topic."""
    # Find and return all schools containing the given topic
    return mongo_collection.find({"topics": topic})
