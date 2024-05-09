#!/usr/bin/python3
"""
Module for perimeter calcculation of an island.
"""


def island_perimeter(grid):
    """
    Function to calculate the land perimeter of an island.
    """
    if not grid:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check neighbors and subtract shared edges
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Top neighbor shares 2 edges
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Left neighbor shares 2 edges
                    
    return perimeter
