#!/usr/bin/env python3
""" A coroutine called async_generator that takes no arguments. """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ A coroutine called async_generator that takes no arguments. """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10