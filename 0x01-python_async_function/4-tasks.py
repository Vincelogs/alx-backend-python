#!/usr/bin/env python3
"""remake of wait_n"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """execute concurrent coroutines

    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): max delay
    Returns:
        list: sorted list of all delays (float values)
    """

    return sorted([await task_wait_random(max_delay) for num in range(n)])
