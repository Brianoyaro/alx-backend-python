#!/usr/bin/env python3
"""executing multiple coroutines"""
import asyncio
from typing import List
wr = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """returns a list after running async tasks n times"""
    res = await asyncio.gather(*(wr(max_delay) for _ in range(n)))
    return sorted(res)
