#!/usr/bin/env python3
"""Defines a function that takes a float multiplier as an argument
and returns a function that multiplies a float by the multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function returning a multiplicative function"""
    def multiplier_function(number: float) -> float:
        """Function performed by multiplication."""
        return number * multiplier
    return multiplier_function
