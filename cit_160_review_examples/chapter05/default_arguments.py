# Python allows you to specify default values (arguments) for each parameter in your function.
# This is a good feature when you want to ensure that your function has all necessary values
# even when the user of the function may not have all the values available to pass to the function
# when called.

# NOTE: Any function parameter that does not have a default value, must be listed in the parameter
# list first.


# Here the * tells the compiler that all calls to my_function must use keyword arguments.
def my_function(*, a: int, b: int = 20, c: int = 30):
    pass


# Functions with default arguments can be called in a different number of ways.
def main():
    my_function(1, 2, 3)        # a = 1, b = 2, c = 3
    my_function(1)              # a = 1, b = 20, c = 30
    my_function(1, 2)           # a = 1, b = 2, c = 30



if __name__ == "__main__":
    main()