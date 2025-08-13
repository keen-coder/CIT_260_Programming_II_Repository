# Python has three logical operators that allow you to combine multiple boolean expressions.
#   and     both sub expressions must be true for the result to be true
#   or      one of the sub expressions must be true for the result to be true
#   not     works on one operand, reverses the result, true becomes false and false becomes true
# Review the truth tables from section 3.5 of the textbook if needed.

temperature: int = 10
minutes: int = 20

# both boolean expressions must be true for the entire AND expression to be true
if temperature < 20 and minutes > 12:
    print('The temperature is in the danger zone.')


# one or both of the expressions can be true for the entire OR expression to be true
if temperature < 20 or temperature > 100:
    print('The temperature is too extreme')

# not simply takes the result and flips it to the opposite
if not(temperature > 100):
    print('This is below the maximum temperature')


# Example of using the and operator
MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on the job

salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter the number of years employed: '))

if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')

# Example of using the or operator

if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')