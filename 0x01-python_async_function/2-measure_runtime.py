#!/usr/bin/env python3
"""measure runtime"""
import time
import asyncio
# from typing import Float
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns average time taken to run async tasks n times"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    total_time = stop - start
    return total_time / n
