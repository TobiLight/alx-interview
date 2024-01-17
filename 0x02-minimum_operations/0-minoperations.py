#!/usr/bin/python3
# File: 0-minoperations.py
# Author: Oluwatobiloba Light
"""Minimum operations module"""


def minOperations(n: int) -> int:
    """
    Returns the number of operations to result in exactly n H characters
    in a file.
    """
    op = 0
    copied = 0
    string = 'H'
    str_len = len(string)

    if not isinstance(n, int):
        return 0

    while str_len < n:
        if copied == 0:
            copied = str_len
            str_len += copied
            op += 2  # the very first copy and paste operations
        elif n - str_len > 0 and (n - str_len) % str_len == 0:
            copied = str_len
            str_len += copied
            op += 2  # copy and paste operations
        elif copied > 0:
            str_len += copied
            op += 1  # paste operation
    return op
