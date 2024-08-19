#!/usr/bin/env python3
"""Module to demonstrate asynchronous generator capabilities."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yields a random float between 0 and 10.

    This function pauses for 1 second between each yield to simulate
    asynchronous tasks such as I/O operations. It generates and yields
    10 random numbers in total.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Pause execution for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
