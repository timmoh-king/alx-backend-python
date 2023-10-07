#!/usr/bin/env python3

"""
    Given the parameters and the return values
    add type annotations to the function
    Hint: look into TypeVar
"""
from typing import TypeVar, Mapping, Union, Any


T = TypeVar('T', None, Any)
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
