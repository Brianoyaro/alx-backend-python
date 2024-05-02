#!/usr/bin/env python3
"""type annotates a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
