#!/usr/bin/env python3
"""Modulo defines a coroutine that collects 10 random numbers
using an asynchronous understanding on async_generator"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 random numbers using async_generator"""
    random_numbers = [num async for num in async_generator()][:10]
    return random_numbers
