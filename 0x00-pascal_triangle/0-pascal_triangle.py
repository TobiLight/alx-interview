#!/usr/bin/python3
"""Module for Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n: int - Number of lists to return

    Return:
        list(list(n)): A list of lists of integersrepresenting
        the Pascal’s triangle of n
    """
    ret = []
    if n <= 0 or type(n) is not int:
        return ret

    for i in range(n):
        ret.append([1] * (i + 1))
        for j in range(1, i):
            ret[i][j] = ret[i - 1][j - 1] + ret[i-1][j]

    return ret
