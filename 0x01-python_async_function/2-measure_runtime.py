#!/usr/bin/env python3

"""
    From the previous file, import wait_n into 2-measure_runtime.py
    Create a measure_time function with integers n and max_delay as args
    measure wait_n(n, max_delay), and returns total_time / n.
    use time module to measure the approximate elapsed time
"""

wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time


async def measure_time(n: int, max_delay: int) -> float:
    """
        Returns the average time for wait_n
    """
    time = await asyncio.gather(wait_n(n, max_delay))
    print(sum(time))
    return sum(time) / n
