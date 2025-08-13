# When you pass arguments to parameters without doing anything else special i.e. 
# my_function(1, 2, 3, 4), this is called using positional arguments.
# The values are passed to the arguments in the same order they are listed.

# Keyword arguments allow you to pass the arguments in any order, as long as you indicate the
# name of the parameter that the argument should be assigned to. i.e. my_function(b=4, c=1, d=2, a=3)

def show_interest(principal: float, rate: float, periods: float):
    interest = principal * rate * periods
    print(f'The simple interest will be ${interest:,.2f}.')

def main():
   show_interest(rate=0.01, periods=10, principal=10000.0)

if __name__ == '__main__':
    main()
