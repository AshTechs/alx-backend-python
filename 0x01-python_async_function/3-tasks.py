#!/usr/bin/env python3
"""
This module contains regular function that creates and returns an asyncio.Task
for the wait_random coroutine with a specified max_delay.
"""

import asyncio
from typing import Union
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutin.

    Args:
        max_delay (int): The maximum number of seconds to wait for each delay.

    Returns:
        asyncio.Task: The asyncio.Task object representing the coroutine task.
    """
    return asyncio.create_task(wait_random(max_delay))
