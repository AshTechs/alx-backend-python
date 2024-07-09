#!/usr/bin/env python3
"""
Module to measure the runtime of async_comprehension executed in parallel.
"""

import asyncio
from typing import List
from time import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    total_runtime = end_time - start_time
    return total_runtime


if __name__ == "__main__":
    total_runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {total_runtime:.2f} seconds")
