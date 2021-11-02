#!/usr/bin/env python3
""" Task 6: Complex types - mixed list """

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Takes a list of floats as arg and returns their sum as a float """
    return sum(mxd_list)
