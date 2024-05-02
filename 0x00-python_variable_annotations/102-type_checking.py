#!/usr/bin/env python3
"""module for zooming into an array"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zooms into an array and returns a list of 'zoomed' elements"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
