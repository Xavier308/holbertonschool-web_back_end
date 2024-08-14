#!/usr/bin/env python3

import asyncio
import importlib

# Dynamically import the wait_random function
wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


async def wait_n(n, max_delay):
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
