#!/usr/bin/env python3
""" a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Constructs a tuple where the first element is the string k
    and the second element is the square of the int/float v.

    Args:
        k: The string key.
        v: The integer or float value.

    Returns:
        A tuple containing the string k and the square of v as a float.
    """
    return k, float(v ** 2)
