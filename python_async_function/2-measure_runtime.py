#!/usr/bin/env python3

import asyncio
import time
import importlib

# Dynamically import the wait_n function
concurrent = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent.wait_n


async def measure_time(n, max_delay):
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


def measure_time_sync(n, max_delay):
    return asyncio.run(measure_time(n, max_delay))
