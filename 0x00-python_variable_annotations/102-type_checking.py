#!/usr/bin/env python3
"""
Using mypy to validate the following piece of code
and apply any necessary changes.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """ Using mypy """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
