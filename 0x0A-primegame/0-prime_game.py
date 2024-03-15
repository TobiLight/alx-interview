#!/usr/bin/python3
# File: 0-prime_game.py
# Author: Oluwatobiloba Light
"""Prime Game"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_game_winner(n):
    """
    Determine the winner of the prime game for a given n.

    Args:
    n (int): The upper limit of the consecutive integers set.

    Returns:
    str: The name of the player who wins the game ("Maria" or "Ben").
    """
    if n <= 1:
        return "Ben"

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    dp = [False] * (n + 1)
    dp[0] = False
    dp[1] = True

    for i in range(2, n + 1):
        for prime in primes:
            if i - prime >= 0 and not dp[i - prime]:
                dp[i] = True
                break

    return "Maria" if dp[n] else "Ben"


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

    for n in nums:
        winner = prime_game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
