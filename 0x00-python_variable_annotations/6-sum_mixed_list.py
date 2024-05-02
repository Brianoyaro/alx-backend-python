#!/usr/bin/env python3
"""typecasts a list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of elements in mxd_lst"""
    sum_: float = 0.0
    for val in mxd_lst:
        sum_ += val
    return sum_
