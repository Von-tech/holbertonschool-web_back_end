#!/usr/bin/env python3
"""list of arguments in int and float """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function sum_mixed_list, takes a list mxd_ls
    of integers and floats and returns their sum as a float.
    """
    return sum(mxd_lst)
