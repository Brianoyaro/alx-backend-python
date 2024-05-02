#!/usr/bin/env python3
"""list of floats type casting module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of floats in input list"""
    sum_: float = 0.0
    for val in input_list:
        sum_ += val
    return sum_
