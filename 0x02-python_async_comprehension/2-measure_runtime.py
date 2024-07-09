#!/usr/bin/env python3
"""
Module for measuring runtime of async comprehensions.
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
    start_time: float = perf_counter()

    results: List[List[float]] = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time: float = perf_counter()
    return end_time - start_time
