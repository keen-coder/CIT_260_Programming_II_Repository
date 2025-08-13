# Python allows you to enforce that a function can only take positional arguments using the 
# / (forward-slash). 

# Here the / tells the compiler that all calls to my_function must use keyword arguments.
def my_function(a: int, b: int, c: int, /):
    pass

def main():
    
    my_function(a=1, b=2, c=3)  # Uses keyword arguments, will cause a compile error
    my_function(1, 2, 3)        # Uses positional arguments, is correct. 

if __name__ == "__main__":
    main()