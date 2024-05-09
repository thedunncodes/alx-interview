#!/usr/bin/python3
"""
island perimeter module
"""


def island_perimeter(grid):
    ''' Measures the perimeter of a land, land is represented
    by a grid, in the grid 1 represent a land 0 represent water.
    Land is connected vertically and horizontally and the shape is measured

    Return:
        Perimeter of land area
    '''

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                prev_row = i - 1
                prev_column = j - 1
                points = 0
                if prev_column >= 0:
                    if grid[i][prev_column] == 1:
                        points += 1
                if prev_column >= 0:
                    if prev_row >= 0:
                        if grid[prev_row][j] == 1:
                            points += 1
                perimeter += 4 - (2 * points)
    return perimeter
