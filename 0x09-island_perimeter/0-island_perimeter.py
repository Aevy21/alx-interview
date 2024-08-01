#!/usr/bin/python3
"""
Calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a grid.
    
    Args:
        grid (list of list of int): 2D grid representing the map with land (1) and water (0).
    
    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    /* Iterate over each cell in the grid */
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                /* Add 4 for the current land cell */
                perimeter += 4

                /* Check for neighboring land cells and reduce perimeter if shared sides exist */
                if i > 0 and grid[i - 1][j] == 1:  /* Check the top cell */
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  /* Check the bottom cell */
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  /* Check the left cell */
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  /* Check the right cell */
                    perimeter -= 1

    return perimeter