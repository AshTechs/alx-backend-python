#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension executed four times in parallel.
"""

import asyncio
from time import perf_counter
from typing import List
from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension 4x in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    return end_time - start_time


async def main() -> None:
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime:.6f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
