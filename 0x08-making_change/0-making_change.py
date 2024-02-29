#!/usr/bin/python3
# File: 0-making_change.py
# Author: Oluwatobiloba Light
"""
A function to find the fewest number of coins needed to meet a given
total amount.
"""


def makeChange(coins, total):
    """
    Finds the fewest number of coins needed to meet a given total amount.

    Args:
        coins: A list of coin denominations.
        total: The target amount to reach.

    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()

        counter = 0

        for i in coin:
            while total >= coin:
                counter += 1
                total -= coin
        if total == 0:
            return counter

        return -1
