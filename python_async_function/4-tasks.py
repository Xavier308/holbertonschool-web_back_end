#!/usr/bin/env python3
"""
This module leverages the `task_wait_random` function from the `3-tasks` module
to execute multiple asyncio tasks concurrently. It defines a coroutine,
`task_wait_n`, that schedules multiple delay tasks and gathers their results.
"""

import asyncio
import importlib

# Dynamically import the task_wait_random function from the 3-tasks module
tasks_module = importlib.import_module('3-tasks')
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    Execute multiple instances of `task_wait_random` concurrently.

    This coroutine creates `n` asyncio tasks using `task_wait_random` and waits
    for all of them to complete, gathering and returning the list of resulting
    delays.

    Args:
    n (int): Number of tasks to execute concurrently.
    max_delay (int): Maximum delay for each `wait_random` task.

    Returns:
    list: A list of floats representing the delays from each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
