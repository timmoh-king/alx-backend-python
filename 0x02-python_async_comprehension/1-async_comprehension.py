#!/usr/bin/env python3

"""
    Import async_generator from the previous task
    write a coroutine called async_comprehension that takes no args
    The coroutine will collect 10 random numbers using an async
    then return the 10 random numbers.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """1. Async Comprehensions"""
    return [i async for i in async_generator()]
