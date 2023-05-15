#!/usr/bin/env python3
"""
A simple helper function
"""

from typing import List

index_range = __import__('0-simple_helper_function').index_range


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Return the specified page of the
    dataset based on the page and page_size parameters.
    """
    assert isinstance(
        page, int) and page > 0, "page must be a positive integer"
    assert isinstance(
        page_size, int
        ) and page_size > 0, "page_size must be a positive integer"

    dataset = self.dataset()
    start, end = index_range(page, page_size)

    if start >= len(dataset):
        return []

    return dataset[start:end]
