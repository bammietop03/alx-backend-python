#!/usr/bin/env python3
"""
Augment the following code with the correct
 duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Args:
        lst: The input sequence.

    Returns:
        The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
