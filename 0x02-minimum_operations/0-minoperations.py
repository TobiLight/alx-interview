#!/usr/bin/python3
# File: 0-minoperations.py
# Author: Oluwatobiloba Light
"""Minimum operations module"""


def minOperations(n: int) -> int:
    """
    Returns the number of operations to result in exactly n H characters
    in the file.
    """
    op = 0
    divider = 2

    if n <= 1:
        return op
    else:
        for i in range(divider, n):
            if n % i == 0:
                if n - i > 2:
                    op = minOperations(i) + (i * 2)
                    # print(i, n, n-i, op, (n - i) - op + 1 if (n-i) -
                    #       op + 1 > 1 else (n-i))
                    op = (n - i) - op + 1 if (n - i) - op + 1 > 1 else n - i
                    # for j in range(i, op + 1):
                    #     print('i' * (j))
                    break
                else:
                    op = n
                n //= divider
            divider += i

        return op
