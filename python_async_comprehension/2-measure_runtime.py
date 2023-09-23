#!/usr/bin/env python3
"""Module defines measure_runtime which measures
the total execution time and returns it"""
import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing
    async_comprehension four times in parallel"""
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
