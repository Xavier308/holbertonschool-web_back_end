#!/usr/bin/env python3
"""
This module defines a function to initiate and return an asyncio task
based on the `wait_random` coroutine from the `0-basic_async_syntax` module.
The function facilitates asynchronous task creation for
random delay operations.
"""

import asyncio
import importlib

# Dynamically import the wait_random function from another module
wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task running the `wait_random` coroutine.

    This function encapsulates the `wait_random` coroutine in an asyncio task,
    allowing it to be scheduled and managed within the asyncio event loop.

    Args:
    max_delay (int): The maximum delay, in seconds, for the `wait_random` task.

    Returns:
    asyncio.Task: The scheduled task that will execute `wait_random`.
    """
    return asyncio.create_task(wait_random(max_delay))
