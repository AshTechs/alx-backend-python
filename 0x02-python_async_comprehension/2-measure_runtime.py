#!/usr/bin/env python3
"""
Module for measuring runtime of async comprehensions.
"""

import asyncio
from time import perf_counter
from typing import List


async def async_comprehension() -> List[float]:
    """
    Async generator that yields 10 random numbers between 0 and 10.

    Returns:
        List[float]: List of 10 random floats.
    """
    return [await asyncio.sleep(1) or round(random.uniform(0, 10), 10) for _ in range(10)]


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
