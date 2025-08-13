# If you want to enforce that all arguments to your functions must be passed using keyword
# arguments, you can use an * to indicate this



# Here the * tells the compiler that all calls to my_function must use keyword arguments.
def my_function(*, a: int, b: int, c: int):
    pass

def main():
    my_function(1, 2, 3)        # Uses positional arguments, will cause a compile error
    my_function(a=1, b=2, c=3)  # Uses keyword arguments, is correct.

if __name__ == "__main__":
    main()