#!/usr/bin/env python3
"""type annotated functions"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sums floats inside list

    Keyword arguments:
    input_list -- list of floats
    Return: sum of list elements
    """
    return sum(input_list)
