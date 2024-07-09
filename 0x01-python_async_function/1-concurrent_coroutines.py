#!/usr/bin/env python3
"""
This contains an async coroutine `wait_n` that spawns `wait_random` n times
with a specified max_delay and returns the list of delays in ascending order.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum number of seconds to wait for each delay.

    Returns:
        List[float]: A list of all the delays (float values) in ascending order
    """
    async def run_task(max_delay: int) -> float:
        return await wait_random(max_delay)

    tasks = [run_task(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = []
    while delays:
        min_delay = min(delays)
        delays.remove(min_delay)
        sorted_delays.append(min_delay)

    return sorted_delays


if __name__ == "__main__":
    import asyncio

    # Example usage
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
