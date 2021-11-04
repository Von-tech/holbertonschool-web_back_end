#!/usr/bin/env python3
""" Task 0. Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """  coroutine will loop 10 times, wait 1 second & yield rand num 0-10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
