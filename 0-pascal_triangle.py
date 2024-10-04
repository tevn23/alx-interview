#!/usr/bin/python3
"""
0-pascal_triangl
"""


def pascal_triangle(n):
    """
    Implementing the pascal triangle
    """

    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row of Pascal's triangle
    
    for i in range(1, n):
        # Create the next row
        row = [1]  # First element of the row is always 1
        # Compute the middle elements
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # Last element of the row is always 1
        row.append(1)
        triangle.append(row)
    
    return triangle
