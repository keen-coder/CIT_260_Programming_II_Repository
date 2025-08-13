# Instead of using nested if structures, usually it is better to use an if-elif-else structure
# when you have more than 2 options.

# We can rewrite the example from 04_nested_decision_structures.py to make the logical more understandable.

# Credit: Starting out with Python, Tony Gaddis

A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input('Enter your test score: '))

if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')