#!/usr/bin/env python3
"""
add type annotations to the function
"""
from typing import Mapping, Any, TypeVar, Union


# Define a type variable ~T representing the value type
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct: The dictionary to search for the key.
        key: The key to search for in the dictionary.
        default: The default value to return if the key is not
        found (optional, default is None).

    Returns:
        The value corresponding to the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
