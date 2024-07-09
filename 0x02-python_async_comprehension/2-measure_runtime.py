#!/usr/bin/env python3
"""
Module to measure the runtime of async_comprehension executed in parallel.
"""
import asyncio
from typing import List
from time import time


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime


if __name__ == "__main__":
    total_runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {total_runtime:.2f} seconds")
