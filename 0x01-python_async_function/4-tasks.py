#!/usr/bin/env python3
"""
This contains asynchronous coroutine that spawns task_wait_random n times
with a specified max_delay and returns the list of delays in ascending order.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates asyncio.Task for the wait_random coroutine with specified max_delay

    Args:
        max_delay (int): The maximum number of seconds to wait for each delay.

    Returns:
        asyncio.Task: The asyncio.Task object representing the coroutine task.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum number of seconds to wait for each delay.

    Returns:
        List[float]: A list of all the delays (float values) in ascending order
    """
    async def run_task(max_delay: int) -> float:
        return await task_wait_random(max_delay)

    tasks = [run_task(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Implementing sorting without using sort() due to concurrency
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        delays.remove(min_delay)
        sorted_delays.append(min_delay)

    return sorted_delays
