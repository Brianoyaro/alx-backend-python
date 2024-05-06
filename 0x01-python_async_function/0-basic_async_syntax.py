#!/usr/bin/env python3
"""basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """runs an async function and retuns delay duration"""
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
