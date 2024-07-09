#!/usr/bin/env python3
"""
Module for asynchronous generator exercise.
"""

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers.

    Yields:
        float: A random float number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
