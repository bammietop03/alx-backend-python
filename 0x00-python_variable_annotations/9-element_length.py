#!/usr/bin/env python3
"""
Annotate the below functions parameters and
return values with the appropriate types
"""
from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of the input list
    along with its length.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples where each tuple contains a sequence from lst
        and its length.
    """
    return [(i, len(i)) for i in lst]
