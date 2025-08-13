# Generally speaking, all input coming into your program whether it is from a file, or user input
# should be validated.  One way to do that is to use a loop to continuously check until the correct
# value is entered.

# Example: Calculating retail prices with validation

MARK_UP: float = 2.5 # The markup percentage
another: str = 'y' # Variable to control the loop.

while another == 'y' or another == 'Y':
    wholesale: float = float(input("Enter the item's wholesale cost: "))
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input('Enter the correct ' +
                                'wholesale cost: '))
        
    retail:float = wholesale * MARK_UP
    
    print(f'Retail price: ${retail:,.2f}')
    
    another = input('Do you have another item? (Enter y for yes): ') 