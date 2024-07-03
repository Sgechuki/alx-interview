#!/usr/bin/python3
"""
Task 0: Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    wn = len(grid)
    ln = len(grid[0])
    islands = 0
    neighbours = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                islands += 1
                if i + 1 < wn and grid[i + 1][j]:
                    neighbours += 1
                if j + 1 < ln and grid[i][j + 1]:
                    neighbours += 1
    return (islands * 4) - (neighbours * 2)
