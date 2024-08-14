#!/usr/bin/env python3
"""
This module provides functionality to run multiple instances of the
`wait_random` function concurrently, collecting and returning their
results. The `wait_n` coroutine creates multiple tasks and waits for
all to complete, returning the list of delays.
"""

import asyncio
import importlib

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Run `wait_random` concurrently for `n` times with `max_delay`.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
