#!/usr/bin/env python3
"""Defines an asynchronous routine that returns the list of all delays."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all delays"""
    delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    return [await i for i in asyncio.as_completed(delays)]  # type: ignore
