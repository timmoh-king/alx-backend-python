#!/usr/bin/env python3

"""
    Import wait_random from the previous python file
    write an async routine called wait_n that takes in 2 int arguments:
    n and max_delay  You will spawn wait_random n times with the specified max_delay
    wait_n should return the list of all the delays (float values) in ascending order
"""

wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    list = []
    for i in range(n):
        list.append(await asyncio.create_task(wait_random(max_delay)))
    print(list)
    return list.sort()
