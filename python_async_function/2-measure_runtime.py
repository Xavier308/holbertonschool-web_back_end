#!/usr/bin/env python3
"""
This module measures the average execution time of multiple concurrent
executions of the `wait_n` function. It includes both an asynchronous
coroutine `measure_time` and a synchronous wrapper `measure_time_sync`
to facilitate ease of use in different contexts.
"""

import asyncio
import time
import importlib

# Dynamically import the wait_n function from another module
concurrent = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent.wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time it takes to execute `wait_n` concurrently.

    Args:
    n (int): Number of concurrent tasks to run.
    max_delay (int): Maximum delay for `wait_random` used in `wait_n`.

    Returns:
    float: The average time per task in seconds.
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

    Args:
    n (int): Number of tasks to execute.
    max_delay (int): Maximum delay each task waits.

    Returns:
    float: The average execution time per task.
    """
    return asyncio.run(measure_time(n, max_delay))
