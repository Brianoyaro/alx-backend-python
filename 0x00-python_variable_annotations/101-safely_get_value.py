#!/usr/bin/env python3
"""TypeVar anotation"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[None, T] = None) -> Union[T, Any]:
    """returns the value associated with a key else None"""
    if key in dct:
        return dct[key]
    else:
        return default
