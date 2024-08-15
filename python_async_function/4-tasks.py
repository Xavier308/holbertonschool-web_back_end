#!/usr/bin/env python3
"""
This module take the code from wait_n and alter it into a new function
task_wait_n.
"""

import asyncio
from typing import List, Any

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Identical to task 1 but task_wait_random is being called """
    allDelays: List = []

    for i in range(n):
        allDelays.append(task_wait_random(max_delay))

    List_of_tasks: List[Any] = []

    for results in asyncio.as_completed(allDelays):
        """ wait for as_completed to return """
        completed: float = await results
        List_of_tasks.append(completed)

    return List_of_tasks
