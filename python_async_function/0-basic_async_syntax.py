#!/usr/bin/env python3
"""
This module provides an asynchronous function that simulates a
random delay. The function `wait_random` is designed to pause
execution for a random duration up to a specified maximum.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random time period between 0 and `max_delay`.

    Args:
    max_delay (int): The maximum delay time in seconds. Defaults to 10.

    Returns:
    float: The actual delay time that was awaited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
