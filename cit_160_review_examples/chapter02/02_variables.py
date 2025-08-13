
# Variables are created with an assignment statement which uses the = sign to assign the value on the right
# to the variable name on the left. In python variables are 'weakly typed' meaning you do not have to assign
# a data type to the variable. The type of the variable is determined by the value or object that you assign
# to the name. Variables cannot exist without a value.

# Type Hints:
#   Example:    variable_name: type
#   Type Hints DO NOT enforce the data type.  It is simply a way to make your code more readable. Please
#   use them as much as possible.

# Compute the area of a rectangle
width: int = 10
height: int = 20 

area = width * height

print(f'The area of a rectangle with height = {height}, and width = {width} is {area}')

# Multiple values can be assigned to multiple variables at the same time
# NOTE: Type hints are not supported with multiple variable assignment
a, b, c = 22, 26, 77

# Variables can be assigned any data type
pi: float = 3.14159265         # floating-point value
name: str = 'Susan Cline'    # string value

# Variables can be reassigned to new values
width: int = 57

# Variables can also be reassigned new values that are different data types
# However, this is VERY BAD and poorly designe code.  Once a variable has been assigned a specific type,
# it should keep that type throughout the lifetime of the program.

width: str = '483' # This is BAD DESIGN and will most likely break your code.
