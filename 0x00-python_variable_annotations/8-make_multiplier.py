#!/usr/bin/env python3
"""type annotates callable functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns multiplier miltiplied by secondary float"""
    def func(value: float) -> float:
        return multiplier * value
    return func
