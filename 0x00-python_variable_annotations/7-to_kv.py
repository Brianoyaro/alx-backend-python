#!/usr/bin/env python3
"""type annotates a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """retuns a tuple containing k and v squared"""
    return (k, float(v ** 2))
