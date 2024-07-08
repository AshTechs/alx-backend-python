#!/usr/bin/env python3
"""
This module contains asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random
from typing import Union

async def wait_random(max_delay: int = 10) -> Union[int, float]:
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
