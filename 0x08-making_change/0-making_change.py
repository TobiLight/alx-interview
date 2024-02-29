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
    # Greedy approach
    # if total <= 0:
    #     return 0

    # sorted_coins = sorted(coins, reverse=True)
    # counter = 0

    # for coin in sorted_coins:
    #     while total >= coin:
    #         counter += 1
    #         total -= coin

    # if total == 0:
    #     return counter

    # return -1

    # Dynamic programming
    if total <= 0:
        return 0

    answers = [float('inf')] * (total + 1)
    answers[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                answers[amount] = min(
                    answers[amount], answers[amount - coin] + 1)

    if answers[total] != float('inf'):
        return answers[total]

    return -1
