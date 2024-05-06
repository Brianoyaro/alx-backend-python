#!/usr/bin/env python3
"""executing multiple coroutines"""
import asyncio
wr = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List:
    """returns a list after running async tasks n times"""
    res = await asyncio.gather(*(wr(max_delay) for _ in range(n)))
    return res
