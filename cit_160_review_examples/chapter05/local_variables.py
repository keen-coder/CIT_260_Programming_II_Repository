# Local variables are variables that are defined within a function block of code. The scope (where
# the variable is accessible) of a local variable is the function where it is defined.


# In the code that follows, the variable 'birds' is local to the texas and california functions.
# This is why you can reuse the same variable name without any conflicts. Each version of birds
# is independent of the other and its scope is the function where it is defined.


def texas():
    birds = 5000
    print(f'texas has {birds} birds.')

def california():
    birds = 8000
    print(f'california has {birds} birds.')

def main():
    texas()
    california()

if __name__ == '__main__':
    main()