# Copying a list with a list comprehension
list1 = [1, 2, 3, 4]
list2 = [item for item in list1]
print(list2)

# Creating a list of squares of numbers 1 ~ 4 
list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]
print(list2)

# Creates a list of cubes of the values in the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [n**3 for n in numbers]
print(cubes)  

# Creating a list of the lengths of each string from an existing list.
str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]
print(len_list)

# Create a list of values greater than 10 from an existing list
list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = [item for item in list1 if item < 10]
print(list2)

# Functions and Methods can be used in the result expression section
words = ["list", "comprehensions", "are", "fun!"]
upper_words = [word.upper() for word in words]
print(upper_words)


# Flatten a nested list
# In this example, note the two for loops, one after another
# These act as nested for loops
#   for row in matrix
#       for num in row
# You could still have an if clause at the end of the loops if necessary
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row] # Note the nested for loop
print(flat)

# Create a list of labels 'even' or 'odd' for an existing list of values
# NOTE: This example uses a conditional expression in the result expression
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Read all lines from a file and strip them of whitespace
with open("week03_lists02/log.txt") as f:
    lines = [line.strip() for line in f]
print(lines[:5])  # first 5 cleaned lines

# Filter data in a file, choosing only lines that refer to error messages
with open("week03_lists02/log.txt") as f:
    errors = [line.strip() for line in f if "ERROR" in line]
print(errors[:3])