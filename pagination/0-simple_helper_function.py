#!/usr/bin/env python3
"""Module containing a function that calculates the page indexes."""


def index_range(page, page_size):
    """Function that calculates the initial and
    final indexes and returns them in a tuple."""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
