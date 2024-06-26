#!/usr/bin/env python3
"""creates a task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates and returns a asyncio task"""
    return asyncio.Task(wait_random(max_delay))
