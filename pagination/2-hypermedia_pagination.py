#!/usr/bin/env python3
"""Module to manage the loading of data from a .csv file
and perform the pagination of this data."""
import csv
from typing import List


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
        """Method of data paging """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_data: tuple = index_range(page, page_size)

        return self.dataset()[page_data[0]:page_data[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """a"""
        try:
            if len(self.get_page(page + 1, page_size)) < page_size:
                next_page = None
            else:
                next_page = page + 1
        except Exception:
            next_page = None

        try:
            self.get_page(page - 1, page_size)
            prev_page = page - 1
        except Exception:
            prev_page = None

        dict_to_return = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": int(len(self.dataset()) / page_size),
        }
        return dict_to_return


def index_range(page, page_size):
    """Function that calculates the initial and
    final indexes and returns them in a tuple."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
