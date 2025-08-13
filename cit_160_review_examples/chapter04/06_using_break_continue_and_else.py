# When break is executed in a loop, the loop will immediately end.  Break can be used with any
# type of loop.

# Example 1: break used in a while and for loop.

n: int = 0

while n < 100:
    print(n)
    if n == 5:
        break
    n += 1
print(f'The loop stopped and n is {n}.')

for n in range(100):
    print(n)
    if n == 5:
        break

print(f'The loop stopped and n is {n}.')

# The continue statement stops the current iteration of the loop, but the loop itself will continue
# to the next iteration.

# Example 2: Using continue with a while loop and for loop

n: int = 0

while n < 10:
    n += 1
    if n % 3 == 0:
        continue
    print(n)

for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)

# The else clause in a loop is only useful when the loop contains a break statement. The code in the
# else block will ONLY execute if the loop terminates normally (the break is not executed). 
# While loops AND for loops can both have an else block.

# Example 3: A for loop with a break and else

# The else does not execute because the loop executes break
for n in range(10):
    if n == 5:
        print('Breaking out of the loop.')
        break
    print(n)
else:
    print(f'After the loop, n is {n}.')

# Here the else executes because the loop does not execute the break statement.
for n in range(3):
    if n == 5:
        print('Breaking out of the loop.')
        break
    print(n)
else:
    print(f'After the loop, n is {n}.')
