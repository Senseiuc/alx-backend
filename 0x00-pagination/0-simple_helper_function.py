#!/usr/bin/env python3
"""
0. Simple helper function: Pagination Task 0
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function takes two arguments
    - page
    - page_size
    and returns a tuple of size two
    containing a start index and end index
    corresponding to the range of indexes to
    return in a list for those particular pagination
    parameters
    """
    upper_bound = page * page_size
    return (upper_bound - page_size, upper_bound)
