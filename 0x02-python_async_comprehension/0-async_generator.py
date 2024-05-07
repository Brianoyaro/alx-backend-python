#!/usr/bin/env python3
"""async generatorn module"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """generates 10 numbers randomly"""
    for _ in range(10):
        await asyncio.sleep(1)
        val = random.uniform(0, 10)
        yield val
