#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute concurrent coroutines

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): max delay
    Returns:
        list: sorted list of all delays (float values)
    """

    return sorted([await wait_random(max_delay) for num in range(n)])
