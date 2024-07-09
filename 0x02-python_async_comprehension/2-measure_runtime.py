#!/usr/bin/env python3

"""
Module to measure the runtime of async_comprehension executed 4x in parallel.
"""

import asyncio
from typing import List
from time import perf_counter
from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension 4x in parallel

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]

    await asyncio.gather(*tasks)

    end_time = perf_counter()
    return end_time - start_time


async def main() -> None:
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime:.6f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
