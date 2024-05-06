#!/usr/bin/env python3
"""executing multiple coroutines"""
import asyncio
from typing import List
wait = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """runs a concurrent task n times and returns a list of values"""
    # rs = await asyncio.gather(*(wait(max_delay) for _ in range(n)))
    # return sorted(rs)
    tasks = [wait(max_delay) for _ in range(n)]
    array = []
    for task in asyncio.as_completed(tasks):
        val = await task
        array.append(val)
    return array
