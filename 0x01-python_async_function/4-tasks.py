#!/usr/bin/env python3
""" Task 4: Tasks """
import asyncio
import typing import List, Any

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Similar to wait_n """
    allDelays: List = []

    for i in range(n):
        allDelays.append(task_wait_random(max_delay))

    new_list: List[Any] = []

    for y in asyncio.as_completed(allDelays):
        done: float = await y
        new_list.append(done)

    return new_list
