# for loops are used to write counter controlled loops which iterate over a sequence of items.

# Example: display the numbers 1 through 5

print('I will display the numbers 1 through 5.')

for num in [1, 2, 3, 4, 5]:
    print(num)

# Often you will use the range function to create a range of values to iterate over. The range(n)
# function generates a sequence which starts at 0 and counts up by 1 to n.  n is not included in
# the results.
for num in range(5):  # this is the same as for num in [0, 1, 2, 3, 4]
    print(num)

# print hello world 5 times
for x in range(5):
    print('hello world')

# Range can also take 2 values, a start value, and an ending value
for num in range(3, 10): # generates a sequence from 3 to 9
    print(num)

# A third value called the "step value" can also be added to increase the increment of the range (default)
# increment is 1.
for num in range(10, 101, 10): # generates the sequence [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(num)

# Example: Printing a table of squares.

print('Number\tSquare')
print('--------------')
for number in range(1, 11):
    square = number**2
    print(f'{number}\t{square}')



# Example: Keeping a running total

MAX: int = 5 # The maximum number
total: float = 0.0

print('This program calculates the sum of ', end='')
print(f'{MAX} numbers you will enter.')

for counter in range(MAX):
    number:int = int(input('Enter a number: '))
    total = total + number
    
print(f'The total is {total}.')