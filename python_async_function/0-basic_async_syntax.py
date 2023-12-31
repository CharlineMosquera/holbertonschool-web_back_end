#!/usr/bin/env python3
"""Wait a random time and return the delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
