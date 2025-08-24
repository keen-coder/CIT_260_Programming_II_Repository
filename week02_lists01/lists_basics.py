import random

# Create a list using square brackets
numbers = [32, 56, 19, 123, 49548]
costs = [4.56, 23.90, 582.23]
people = ['Abby', 'George', 'Samantha', 'Susie', 'Kevin']

# You can make lists with mixed data types, but these are harder to process and can lead to logic errors
student_info = ['Jane Smith', '5705555555', 23, 4.5]

# The print function can easily print lists to the console
print(numbers)
print(costs)
print(people)
print(student_info)

# Lists can be created with the range() function
numbers = list(range(5))
print(numbers)

numbers = list(range(1, 10, 5))
print(numbers)

# Lists can also be created using the repetition operator (*)
numbers = [0] * 5
print(numbers)

numbers = [1, 2, 3] * 7
print(numbers)

# for Loops are a great way to process a list, whether you are simply printing it out in a different way
# or you need to do something do each element of the list
numbers = []

for x in range(0,9):
    numbers.append(random.randint(10, 30))

print(numbers)

# Multiply each element by 10 and print it out
for x in numbers:
    print(x * 10, end=" ")
print()

# With indexing you can access individual elements of a list
numbers = [4, 7, 3, 8, 2, 7, 9]
print(numbers[0])
print(numbers[4])

# You can also change individual values of the list
# Loops also work great with indexing
# The len() function can be used to get the length (number of elements) inside the list
# Paired with the range() function can give you a for loop to iterate over the list using indicies.

# Iterate over the list and multiply each value by 10 and store the new value back in the list
for index in range(0, len(numbers)):
    numbers[index] *= 10

print(numbers)

# The following raises an IndexError
# my_list = [10, 20, 30, 40]
# index = 0

# while index < 5:
#     print(my_list[index])
#     index += 1

# Lists can be concatenated together using the plus + operator:

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list3 = list1 + list2
print(list3)