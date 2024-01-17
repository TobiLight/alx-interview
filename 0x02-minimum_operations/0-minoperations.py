#!/usr/bin/python3
# File: 0-minoperations.py
# Author: Oluwatobiloba Light
"""Minimum operations module"""


import math


def minOperations(n: int) -> int:
    """
    Returns the number of operations to result in exactly n H characters
    in the file.
    """
    string = 'H'
    def copy(string): return string
    def paste(str1, str2): return str1 + str2
    op = 0

    while len(string) < n:
        if n % len(string) == 0:
            copiedString = copy(string)
            string = paste(copiedString, string)
            op += 2
        else:
            string = paste(copiedString, string)
            op += 1

    return op
