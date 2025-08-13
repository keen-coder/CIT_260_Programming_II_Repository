# Exceptions or Exception Handling is a way to try to detect possible runtime errors in your program
# and be able to recover from them gracefully, without your program crashing.

# Potential exceptions are handled using a try/except


def main():
    try:
        hours = int(input('How many hours did you work? '))
        pay_rate = float(input('Enter your hourly pay rate: '))
        gross_pay = hours * pay_rate
        
        print(f'Gross pay: ${gross_pay:,.2f}')
    
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must')
        print('be valid numbers.')

if __name__ == '__main__':
    main()