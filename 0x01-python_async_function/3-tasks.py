#!/usr/bin/env python3
'''more async'''
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """concurrency without async

    Args:
        max_delay (int): max_delay

    Returns:
        Task: Task Object
    """
    return create_task(wait_random(max_delay))
