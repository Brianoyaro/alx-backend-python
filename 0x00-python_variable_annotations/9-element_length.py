#!/usr/bin/env python3
"""aiteraable object iteration annotation"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples with each element and its length"""
    return [(i, len(i)) for i in lst]
