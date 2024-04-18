#!/usr/bin/env python3
"""
a type-annotated function sum_list which takes a list input_list
 of floats as argument and returns their sum as a float.
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Sum the input_list
    """
    # sum: float = 0
    # for x in input_list:
    #     sum += x

    return sum(input_list)
