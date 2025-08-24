import random



#Generate a list of random elements using the append function 
# append(item) adds a item to the end of the list
my_list = []
for x in range(0, 10):
    my_list.append(random.randint(0, 100))

print(f'Append List:\t{my_list}')

# count(item) Can be used to count how many times 'item' appears in the list
colors = ['blue', 'red', 'orange', 'green', 'blue', 'pink', 'blue', 'purple', 'green']
blue_count = colors.count('blue')
print(f'The color blue appears {blue_count} times')

# index(item) Returns the first index of where item appears, raise a ValueError if item is not found

index = colors.index('green')

print(f'The first time green appears is at index {index}')

# Since yellow does not appear, this will raise a ValueError
# index = colors.index('yellow')

# insert(index, item) inserts an item at the given index the list is expanded to fit the new item
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10) # insert 10 at index 2
print(f'insert 10 at index 2: {numbers}')


# sort() will sort your list!
jumble = []
for x in range(0, 10):
    jumble.append(random.randint(0, 100))

print(f'Before Sorting: {jumble}')
jumble.sort()
print(f'After sorting: {jumble}')

# remove(item) will remove first first occurrence of item from the list
colors = ['red', 'green', 'blue', 'red', 'purple']
colors.remove('red')
print(colors)

# If you want to remove something from the list at a specific index, use the del statement
colors = ['red', 'green', 'blue', 'red', 'purple']
del colors[3]
print(colors)

# reverse() will reverse the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)

# sum() can return the sum of a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = sum(numbers)
print(f'the sum of {numbers} = {sum}')

# min() and max() can find the min and max of a list
min_max = []

for x in range(0, 10):
    min_max.append(random.randint(0, 100))

print(min_max)
print(min(min_max))
print(max(min_max))