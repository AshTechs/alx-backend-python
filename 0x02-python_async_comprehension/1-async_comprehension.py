#!/usr/bin/env python3
"""
Module for asynchronous comprehension exercise.
"""

import asyncio
from typing import List
from random import uniform

async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers using async comprehension.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [num async for num in async_generator()]
