#!/usr/bin/env python3
""" Task 1. Async Comprehensions """
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """  collect 10 random numbers & return the 10 rand numbers """
    return [i async for i in async_generator()]
