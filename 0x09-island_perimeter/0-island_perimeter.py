#!/usr/bin/python3
# File: 0-island_perimeter.py
# Author: Oluwatobiloba Light
"""Perimeter of an island"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
      grid: A list of lists of integers, where 0 represents water and 1
      represents land.

    Returns:
      The perimeter of the island as an integer.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter