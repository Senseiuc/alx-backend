#!/usr/bin/env python3
"""
Simple helper function: Pagination Task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns the index range for a given page and page size
    """
    upper_bound = page * page_size
    return (upper_bound - page_size, upper_bound)
