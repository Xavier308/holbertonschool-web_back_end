#!/usr/bin/env python3
"""
This module measures the average execution time of multiple concurrent
executions of the `wait_n` function.
"""

import asyncio
import time
import importlib

# Dynamically import the wait_n function from another module
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time it takes to execute `wait_n` concurrently.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


def measure_time_sync(n: int, max_delay: int) -> float:
    """
    Synchronously measures the average execution time of `wait_n`.

    This function serves as a synchronous wrapper to run the async
    `measure_time` function conveniently from synchronous code.
    """
    return asyncio.run(measure_time(n, max_delay))
