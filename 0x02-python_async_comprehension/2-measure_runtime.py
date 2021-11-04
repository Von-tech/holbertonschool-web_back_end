#!/usr/bin/env python3
""" Task 2. Run time for four parallel comprehensions """
from typing import List
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that executes 4 times in parallel using asyncio.gather """
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension(),
                         )
    end = time.time()
    return (end - start)
