#!/usr/bin/env python3

import asyncio
import importlib

# Dynamically import the wait_random function
wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


def task_wait_random(max_delay):
    # Schedule the wait_random coroutine as a task and return the task
    return asyncio.create_task(wait_random(max_delay))
