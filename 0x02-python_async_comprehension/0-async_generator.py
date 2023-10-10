#!/usr/bin/env python3
""" Async Generators """

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator, Generator


async def async_generator() -> Generator[float, None, None]:
    """first go at async generators

    Yields:
        Generator[float, None, None]: _description_
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
