#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """introduction to Callable

    Keyword arguments:
    multiplier -- a float
    Return: a function that multiplies a float by multiplier.
    """
    return lambda value: multiplier * value
