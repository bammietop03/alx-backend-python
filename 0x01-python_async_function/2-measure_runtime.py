#!/usr/bin/env python3
"""Create a measure_time function with integers n and max_delay
 as arguments that measures the total execution time for
 wait_n(n, max_delay), and returns total_time / n.
 Your function should return a float."""

import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time for wait_n(n, max_delay)"""
    start_time = time()
    asyncio.run(wait_n(n, max_delay))

    # Calculate total execution time
    total_time = time() - start_time
    # Calculate average time per coroutine call
    avg_time_per_call = total_time / n
    return avg_time_per_call
