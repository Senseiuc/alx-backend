#!/usr/bin/env python3
"""
A Server Class: Pagination Task 1
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns the index range for a given page and page size
    """
    upper_bound = page * page_size
    return (upper_bound - page_size, upper_bound)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        item_range = index_range(page, page_size)
        self.dataset()
        length = len(self.__dataset)
        if item_range[0] >= length:
            return []
        elif item_range[1] > length:
            return self.__dataset[item_range[0], length]
        else:
            return self.__dataset[item_range[0]:item_range[1]]
