#!/usr/bin/env python3
"""
This module contains a coroutine that collects 10 random numbers
from async_generator using an async comprehension and returns them.
"""

import asyncio
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generato

    Returns:
        List[float]: A list of 10 random numbers.
    """
    result = [await num async for num in async_generator()]
    return result