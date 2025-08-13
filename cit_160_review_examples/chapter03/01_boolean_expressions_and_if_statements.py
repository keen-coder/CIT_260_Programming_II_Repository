# Python has 6 relational operators which are used to create a boolean expression
#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to
#   ==  equal to
#   !=  not equal to

# Boolean expressions return a value of true or false


# if statements are used to decide if a boolean expression is true or not
# if statements will only execute IF the expression is TRUE

HIGH_SCORE: int = 95

test1: int = int(input('Enter the score for test 1: ' ))
test2: int = int(input('Enter the score for test 2: ' ))
test3: int = int(input('Enter the score for test 3: ' ))

average: int = (test1 + test2 + test3) / 3

print(f'The average score is {average}.')

if average >= HIGH_SCORE:
    print('Good job! You have a great score!')

# Simple if statements can also be written on a single line

score = 94
if score > 59: print('You passed the test!')