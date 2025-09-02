# Creates a shallow copy of list 1

list1 = [1, 2, 3, 4, 5]
list2 = list1

print(f'list1:\t{list1}')
print(f'list2:\t{list2}')

list1[3] = 42 # Will change both lists since there is only one list in memory
print(f'list1:\t{list1}')
print(f'list2:\t{list2}')

# Create deep copies of lists so they are independent copies in memory
# Concatenate the list to be copied with an empty list
list1 = [1, 2, 3, 4, 5]
list2 = [] + list1

list1[3] = 42
print(f'list1:\t{list1}')
print(f'list2:\t{list2}')

# Slicing can also be used to make a deep copy
list1 = [1, 2, 3, 4, 5]
list2 = list1[:]

list1[3] = 42
print(f'list1:\t{list1}')
print(f'list2:\t{list2}')

# You can also use the built in copy method
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()

list1[3] = 42
print(f'list1:\t{list1}')
print(f'list2:\t{list2}')

data = ['a', 'b', 'c']
data2 = data[:]

print(data)
print(data2)
data[1] = 'z'

print(data)
print(data2)