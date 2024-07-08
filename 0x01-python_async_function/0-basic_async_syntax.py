#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
between 0 and a specified max_delay (inclusive) seconds and returns the delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
