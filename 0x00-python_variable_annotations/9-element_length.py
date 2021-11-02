#!/usr/bin/env python3
""" Task 9: Lets duck type an iterable object """

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """  Returns the length of each el in a list as tuple """
    return [(i, len(i)) for i in lst]
