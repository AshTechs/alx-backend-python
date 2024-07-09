#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields a random number
between 0 and 10 after waiting for 1 second, looping 10 times.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates a random number between 0 and 10 every second,
    yielding the result, for a total of 10 times.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
