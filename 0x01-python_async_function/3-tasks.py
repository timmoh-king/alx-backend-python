#!/usr/bin/env python3

"""
    Import wait_random from 0-basic_async_syntax
    Write a function task_wait_random that takes:
    integer max_delay and returns a asyncio.Task.
"""

wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import asyncio


def task_wait_random(max_delay: int) -> List[list]:
    task = asyncio.create_task(wait_random(max_delay))
    return task
