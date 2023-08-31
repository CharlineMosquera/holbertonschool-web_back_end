#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of int and float"""
    return sum(mxd_lst)
