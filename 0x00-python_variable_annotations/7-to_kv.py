#!/usr/bin/env python3

"""Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        first element of the tuple is the string k
        The second element is the square of the int/float v
    """
    a: tuple = (k, )
    return a + (v, )
