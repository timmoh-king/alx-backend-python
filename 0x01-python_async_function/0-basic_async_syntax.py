#!/usr/bin/env python3

"""
    Write an asynchronous coroutine that takes in an integer argument max_delay
    wait_random that waits for a random delay between 0 and max_delay
    and eventually returns it
"""

import asyncio
import random
from typing import Optional


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i
