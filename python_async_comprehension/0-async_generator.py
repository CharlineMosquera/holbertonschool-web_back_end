#!/usr/bin/env python3
"""Module that defines a coroutine that loops 10 times
producing a random number between 0 and 10"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """A coroutine that generates floating-point numbers asynchronously"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
