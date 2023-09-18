#!/usr/bin/env python3
"""The parameters and return values of the following
function are noted with appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """funtion"""
    return [(i, len(i)) for i in lst]
