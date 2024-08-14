#!/usr/bin/env python3

import asyncio
import importlib

# Import task_wait_random dynamically
tasks_module = importlib.import_module('3-tasks')
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n, max_delay):
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
