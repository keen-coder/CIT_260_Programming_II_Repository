# Table of student data
students = [
    ["Name",    "Age", "Grade"],
    ["Alice",   20,    "A"],
    ["Bob",     22,    "B"],
    ["Charlie", 21,    "C"]
]

for row in students:
    print(row)

# Printing a 2D List row by row (no indexing)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for col in row:
        print(col, end=' ')

print()
# Printing a 2D List row by row (with indexing)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        print(matrix[row][col], end=' ')
print()


# Printing a 2D list col by col with indexing
# NOTE: This only works if your list dimensions are the same
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        print(matrix[col][row], end=' ')
print()

# Printing a 2D list col by col when the dimensions are not uniform

matrix = [[1, 2, 3],
          [4, 5],
          [6],
          [7, 8, 9, 10]]

# Find the number of columns
# Use a list comprehension to create a list of row lengths
# Find the maximum value from the resulting list comprehension
num_cols = max([len(row) for row in matrix])

for col in range(num_cols):
    for row in range(len(matrix)):
        if col < len(matrix[row]):  # only print if element exists
            print(matrix[row][col], end=" ")
print()