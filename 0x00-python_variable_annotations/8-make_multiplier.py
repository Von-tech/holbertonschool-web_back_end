#!/usr/bin/env python3
""" Task 8: Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  Returns a function that multiplies a float by multiplier """
    def multiply_func(new_mult: float) -> float:
        """ Return product """
        return multiplier * new_mult
    return multiply_func
