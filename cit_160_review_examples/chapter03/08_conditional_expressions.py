# Conditional expressions are created using a "ternary" operator.  A ternary operator is one which
# takes three operands. These expressions can be used to create short expressions instead of using
# a full if/else structure

score: int = 75

# normal if/else structure
if score > 60:
    grade:int = 'Pass'
else:
    grade:int = 'Fail'

# this can be shortened to:
grade: int = 'Pass' if score > 60 else 'Fail'    

# Example 2
num1: int = int(input('Enter a number: '))
num2: int = int(input('Enter another number: '))
max: int = num1 if num1 > num2 else num2
print(f'The bigger number is {max}.')