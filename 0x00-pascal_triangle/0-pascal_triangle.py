def generate_pascals_triangle(n):
    triangle = []
    for row_num in range(n):
        row = [1] * (row_num + 1)  # Start with 1 at both ends of the row
        for i in range(1, row_num):
            row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]  # Sum from previous row
        triangle.append(row)
    return triangle
