#!/usr/bin/env python3
"""Module defines measure_runtime which measures
the total execution time and returns it"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing
    async_comprehension four times in parallel"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
