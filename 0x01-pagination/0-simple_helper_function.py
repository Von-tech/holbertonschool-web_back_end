#!/usr/bin/env python3
""" Task 0: Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start and end index """
    range = ()
    if page == 1:
        Start_index = 0
        End_index = page * page_size
        range = (Start_index, End_index)
    else:
        Start_index = (page - 1) * page_size
        End_index = page * page_size
        range = (Start_index, End_index)
    return range
