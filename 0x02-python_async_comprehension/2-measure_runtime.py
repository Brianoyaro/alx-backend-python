#!/usr/bin/env python3
"""module measuring time for async comprehension"""
import time
import asyncio
comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measurs time taken running 4 async comprehensions"""
    start = time.perf_counter()
    await asyncio.gather(comp(), comp(), comp(), comp())
    stop = time.perf_counter()
    time_taken = stop - start
    return time_taken
