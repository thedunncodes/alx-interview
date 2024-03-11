#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """pascal_triangle(n): returns a list of lists
    of integers representing the Pascal’s triangle of n
    """

    triangle = [[1]]
    if not n <= 0:
        for i in range(n-1):
            result = []
            for j in range(len(triangle)+1):
                if not j == len(triangle):
                    sum = 0
                    sum = triangle[i][0] + 0 if j == 0\
                        else triangle[i][j-1] + triangle[i][j]
                    result.append(sum)
                else:
                    result.append(1)
            triangle.append(result)
    else:
        triangle = []
    return triangle
