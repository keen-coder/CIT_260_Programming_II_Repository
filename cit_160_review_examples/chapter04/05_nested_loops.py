# Any loop can be nested inside of any other loop. Inner loops must complete all iterations before
# outer loops can continue to their next iterations.

# Example: Computing average test scores for a bunch of students

num_students: int = int(input('How many students do you have? '))
num_test_scores: int = int(input('How many test scores per student? '))

for student in range(num_students):
    total: float = 0.0
    
    print(f'Student number {student + 1}')
    print('-----------------')
    
    for test_num in range(num_test_scores):
        print(f'Test number {test_num + 1}', end='')
        score: float = float(input(': '))
        
        total += score
    
    average: float = total / num_test_scores
    
    print(f'The average for student number {student + 1} is: {average:.1f}')
    print()

# Example 2: Printing a pattern of stars

for row in range(7):
    for col in range(7):
        print('*', end='')
    print()