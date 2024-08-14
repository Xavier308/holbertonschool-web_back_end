# Python Async Project

## Description
This project focuses on asynchronous programming in Python, covering concepts such as async/await syntax, executing async programs with asyncio, running concurrent coroutines, creating asyncio tasks, and using the random module.

## Learning Objectives
By the end of this project, you should be able to explain:

- The async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Requirements
- Python 3.7 (interpreted/compiled on Ubuntu 18.04 LTS)
- Pycodestyle style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules should have documentation

## Files
1. `0-basic_async_syntax.py`
2. `1-concurrent_coroutines.py`
3. `2-measure_runtime.py`
4. `3-tasks.py`
5. `4-tasks.py`

## Tasks

### 0. The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` and waits for a random delay between 0 and `max_delay` seconds.

### 1. Let's execute multiple coroutines at the same time with async
Write an async routine `wait_n` that spawns `wait_random` n times with the specified `max_delay`.

### 2. Measure the runtime
Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)`.

### 3. Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

### 4. Tasks
Alter the code from `wait_n` into a new function `task_wait_n` using `task_wait_random`.

## Author
Emmanuel Turlay, Staff Software Engineer at Cruise