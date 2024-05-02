#!/usr/bin/env python3
"""duck typing first element of a sequence"""
from typing import Any, Sequence, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """returns first element of lst or None"""
    if lst:
        return lst[0]
    else:
        return None
