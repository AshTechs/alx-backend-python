#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that spawns multiple instances
of wait_random and returns a list of delays in ascending order.
"""

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random  # Replace with the actual path

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` instances of wait_random with a specified `max_delay` and returns
    a list of delays in ascending order.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): The maximum number of seconds to wait in each call.

    Returns:
        List[float]: A sorted list of delays (float values).
    """
    tasks: List[asyncio.Task] = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]
    return delays

# For testing purposes when running as standalone script
if __name__ == "__main__":
    import asyncio

    async def main():
        print(await wait_n(5, 5))
        print(await wait_n(10, 7))
        print(await wait_n(10, 0))

    asyncio.run(main())
