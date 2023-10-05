#!/usr/bin/env python3
"""duck type an iterable object"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck typing"""
    return [(i, len(i)) for i in lst]
