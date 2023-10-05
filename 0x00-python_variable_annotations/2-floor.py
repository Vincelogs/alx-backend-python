#!/usr/bin/env python3
"""module for type annotated function 'floor'"""
from math import floor as roundup


def floor(n: float) -> int:
    """rounds(floor) up a float

    Keyword arguments:
    n -- float variable
    Return: floor of the float, n
    """
    return roundup(n)
