#!/usr/bin/env python3
"""Define a function that returns a tuple
with a string and the square of a number."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    return (k, v ** 2)
