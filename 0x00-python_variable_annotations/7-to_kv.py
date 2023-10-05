#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts string and int/float to tuple

    Keyword arguments:
    k -- str variable
    v -- int or float variable
    Return: a tuple of the format -> (k, v**2)
    """
    return (k, v**2)
