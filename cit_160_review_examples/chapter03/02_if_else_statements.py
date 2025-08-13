# If-else statements are used to add an alternative choice to your decision making structure.
# The if section will execute when the boolean expression is true, the else section will execute
# when the boolean expression is false

# Credit: Example taken from Starting out with Python, 6th edition, Tony Gaddis.


BASE_HOURS = 40 # Base hours per week
OT_MULTIPLIER = 1.5 # Overtime multiplier

hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate

print(f'The gross pay is ${gross_pay:,.2f}.')
