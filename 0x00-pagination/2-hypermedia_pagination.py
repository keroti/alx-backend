#!/usr/bin/env python3
"""
A simple pagination fun
"""

from typing import List, Dict
import csv
import math

index_range = __import__('0-simple_helper_function').index_range


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

    def get_page(
        self, page: int = 1, page_size: int = 10
    ) -> List[List]:
        pass

    def get_page(
        self, page: int = 1, page_size: int = 10
    ) -> List[List]:
        """
        Args: page, page_size
        Returns: Dataset
        """
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        index = i[0]
        if index >= len(self.__dataset):
            return []
        else:
            return self.__dataset[index:i[1]]

    def get_hyper(self, index: int = None,
                  page_size: int = 10) -> Dict:
        """
        Dataset get gotten by changing page
        """
        dataset = self.indexed_dataset()
        assert type(index) == int and type(page_size) == int and\
            index >= 0 and index < len(dataset)
        data = []
        next_page = index
        for _ in range(page_size):
            while not dataset.get(next_page):
                next_page += 1
            data.append(dataset.get(next_page))
            next_page += 1
        new_dict = {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_page
        }
        return new_dict
