# Constants are a name the represents a value that should not change throughout the lifetime of your program
# In other programming languages, constants are usually enforced with a keyword that prevents that
# particular name from being able to change it's value. In Python, constants are NOT enforced, BUT
# as a good programmer, any time you see a name written in all caps, that indicates that this name / value
# should be treated as a constant and should NOT be changed once defined.

PI: float = 3.14159264
MAGIC_NUMBER: int = 10
BLUE_COLOR: str = 'blue'

# Constants can also be used to associate names with values that are otherwise "mysterious" in your code.
# Example

# You could write a console menu as follows
menu: str = '1. Access account information\n' \
            '2. Access payment options\n' \
            '3, Access your shopping cart\n' \
            'Enter your choice (1-3): '

choice: int = int(input(menu))

if (choice == 1):
    # code for option 1
    pass
elif (choice == 2):
    # code for option 2
    pass
elif (choice = 3):
    # code for option 3
    pass

