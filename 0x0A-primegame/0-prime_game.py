#!/usr/bin/python3
# File: 0-prime_game.py
# Author: Oluwatobiloba Light
"""Prime Game"""


def isWinner(x, nums):
    """
    This function determines the winner of the game based on the number of 
    rounds (x) and the starting number set (nums) for each round.

    Args:
        x: Number of rounds
        nums: Array of starting numbers for each round

    Returns:
        str: Name of the player who wins the most rounds ("Maria" or "Ben")
             None: If the winner cannot be determined (both win equal rounds)
    """
    maria_wins = ben_wins = 0
    for _ in range(x):
        num = nums.pop(0)
        if num % 2 == 0:
            ben_wins += 1
        else:
            if len(nums) > 0 and nums[0] % 2 != 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
