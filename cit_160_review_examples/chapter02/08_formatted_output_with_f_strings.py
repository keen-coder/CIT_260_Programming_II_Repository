# f-strings are formatted string literals. This is an easy way to format your output to look a 
# certain way.

# f-string literals always start with an f character before the starting quote

fstring1: str = f'Hello world!'
fstring2: str = f"Hello World!"

print(fstring1) # nothing special about output
print(fstring2) # nothing special about output

# f-strings can be used to insert variable values into a string without having to perform
# more complex string contatenation
# NOTE: The item in the {} is called a place holder

width: int = 10
height: int = 20 
area:int = width * height

fstring3: str = f'The area of a rectangle with height = {height}, and width = {width} is {area}'
print(fstring3)

temperature: int = 45
print(f'It is currently {temperature} degrees.')

# place holders can be any valid python expression
print(f'The value is {10 + 2}.')

# You can use f-strings to round floating-point numbers
# NOTE: this does not change the value of the result, it simply changes how the value is displayed.

amount_due: float = 5000.0
monthly_payment: float = amount_due / 12.0

# Displays the result with no rounding
print(f'The monthly payment is {monthly_payment}.')

# Displays the result rounded to two decimal places
# NOTE: The numeric value in .2f can be any integer to specify the number of decimal places.
print(f'The monthly payment is {monthly_payment: .2f}.') # prints 416.67

pi: float = 3.1415926535
print(f'{pi:.3f}')

a: int = 2
b: int = 3
print(f'{a / b:.1f}')

# f-strings can also be used to insert comma separators into large numbers.
large_number: float = 1234567890.12345
print(large_number) # prints with no commas
print(f'{large_number:,}') # put a comma formatter and will print with commas on the output

# if you want to round as well, the comma formatter has to be before the rounding formatter
print(f'{large_number:,.2f}')

# Floating-point numbers can also be formatted as a percentage.
value: float = 0.534835
print(f'{value:%}')
print(f'{value:.1%}') # formats as a percentage AND rounds to 1 decimal place

# You can also format integers, use the d formatter for decimal integers.
value2: int = 123456789
print(f'{value2:,d}')

# If you really want to format your output as far as spacing goes, the format specifier can also
# indicate a minimum width for your output.

# If the value is larger than the width indicated, no additional space is added.
# If the value is smaller than the width indicated, spaces are added to the right of the output until
# the total number of characters is 10

number = 99
print(f'The number is {number:10}') # prints the output in a field that is 10 spaces wide (8 spaces and
                                    # 2 numbers for the value 99)

number = 12345.6789
print(f'The number is {number:12,.2f}') # prints in a field 12 spaces wide, rounded to 2 decimal places
                                        # and with commas


num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Each number is displayed in a field of 10 spaces
# and rounded to 2 decimal places.
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')

# You can also change the alignment of the values in the width field using >, <, or ^
#   < left-aligns the value
#   > right-aligns the value
#   ^ center-aligns the value

number: int = 12345
print(f'I have {number} apples')
print(f'I have {number:<10d} apples')
print(f'I have {number:>10d} apples')
print(f'I have {number:^10d} apples')

# The following shows a bunch of values center aligned
name1 = 'Gordon'
name2 = 'Smith'
name3 = 'Washington'
name4 = 'Alvarado'
name5 = 'Livingston'
name6 = 'Jones'

print(f'***{name1:^20}***')
print(f'***{name2:^20}***')
print(f'***{name3:^20}***')
print(f'***{name4:^20}***')
print(f'***{name5:^20}***')
print(f'***{name6:^20}***')

# Putting it all together: when using multiple designators in your f-string the proper order is:
#    [alignment][width][,][.precision][type]

# f-strings can also be concatenated, the result will be an f-string
name: str = 'Abbie Lloyd'
department: str = 'Sales'
position: str = 'Manager'
print(f'Employee Name: {name}, ' +
      f'Department: {department}, ' +
      f'Position: {position}')