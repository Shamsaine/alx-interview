#!/usr/bin/python3
"""
0-pascal_triangle.py
"""
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to n rows.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Build the triangle row by row
    for row_num in range(1, n):
        # Start each row with a 1
        row = [1]

        # Calculate the in-between values using the previous row
        for i in range(1, row_num):
            row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])

        # End each row with a 1
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle

