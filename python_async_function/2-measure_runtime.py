#!/usr/bin/env python3
"""module measuring time the total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures approximate elapsed time."""
    initial = time.time()
    asyncio.run(wait_n(n, max_delay))
    final = time.time()
    return (final - initial) / n
