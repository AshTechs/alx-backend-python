#!/usr/bin/env python3
"""
This module contains a function to measure the total execution time for
wait_n(n, max_delay) and returns the average time per call.
"""

import asyncio
import time
from typing import Union
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum number of seconds to wait for each delay.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
