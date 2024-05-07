#!/usr/bin/envv python3
"""async comprehension module"""
import asyncio
gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """returns a list of 10 random numbers using an async comprehensing"""
    val = [i async for i in gen()]
    return val
    """result = []
    async for i in gen():
        result.append(i)
    return result"""
