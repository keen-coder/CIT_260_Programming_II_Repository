# Any type of if structure can be nested inside the if, else, or elif section. Structures can be
# nested as deep as you want, but the deeper you go, the more complicated your logic will become.

# Credit: Starting out with Python, Tony Gaddis
# Example 1:

MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on the job

salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print(f'You must have been employed '
              f'for at least {MIN_YEARS} '
              f'years to qualify.')
else:
        print(f'You must earn at least $'
              f'{MIN_SALARY:,.2f} '
              f'per year to qualify.')
        

# Credit: Starting out with Python, Tony Gaddis
# Example 2:

A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input('Enter your test score: '))

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')