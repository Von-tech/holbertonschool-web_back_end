#!/usr/bin/env python3
""" Task 0: The basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Async coroutine that waits for a random delay between 0 & max_delay """
    r_delay = random.uniform(0, max_delay)
    await asyncio.sleep(r_delay)
    return r_delay
