#!/usr/bin/env python3
"""Asynchronous coroutine that spawns wait_randon
 n times with the specified max_delay"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay
    """
    delays = []
    for _ in range(n):
        delay_task = wait_random(max_delay)
        delays.append(await delay_task)
    return sorted(delays)
