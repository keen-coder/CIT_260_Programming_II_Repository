# Any variable or constant defined outside of a function block is considered to be a 'global variable'
# or 'global constant'.

# In general, global variables are BAD BAD BAD, but global constants are OK when not abused.

# Global variables can lead to strange logic errors and can be hard to debug.


radius: float = 6.234   # radius is a global variable

PI: float = 3.14159265  # PI is a global constant (indicated by the name being in all caps). These
                        # are generally OK to use since their values should NEVER be changed ANYWHERE
                        # within your python project.

def my_function():
    x: int = 10     # x is a local variable

def my_function2():
    radius = 9.42345    # TRICKY! This is a local variable version of radius.  It is separate from the
                        # global version of radius.

def my_function3():
    global radius       # If you wish to change the value of a global variable inside of the function
    radius = 10         # you need to use the keyword global followed by the global variable name
                        # before you try to change its value.  This tells the function you intend
                        # to use the name from the global scope, and not the name in terms of the local
                        # scope.