#!/usr/bin/env python3

"""
    Use mypy to validate the following piece of code
"""
from typing import Tuple, Iterable, Sequence, List, Union


def zoom_array(lst: Iterable[Sequence], factor: Union[int, float] = 2) -> Tuple:
    """12. Type Checking"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
