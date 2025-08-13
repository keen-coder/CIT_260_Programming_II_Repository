# Functions can include parameters (place holder names) which can be used to accept arguments (values)
# that are passed into the function from somewhere else in the program.

# Note the use of type hints for the parameters.

def show_sum(num1: int, num2: int ):
    result: int = num1 + num2
    print(result)

def main():
    print('The sum of 12 and 45 is')
    show_sum(12, 45)

if __name__ == "__main__":
    main()