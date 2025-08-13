# while loops allow you to repeat code as long as the boolean condition is True.

# Example 1:
keep_going: str = 'y'

while keep_going == 'y':
    sales: float = float(input('Enter the amount of sales: '))
    comm_rate: float = float(input('Enter the commission rate: '))

    commission: float = sales * comm_rate
    print(f'The commission is ${commission:,.2f}.')
    
    keep_going = input('Do you want to calculate another ' \
                       'commission (Enter y for yes): ')
    
# Example 2:
MAX_TEMP: float = 102.5
temperature: float = float(input("Enter the substance's Celsius temperature: "))

while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

print('The temperature is acceptable.')
print('Check it again in 15 minutes.')

# While loops can also be used a counter-controlled loops

# Example
n = 0
while n < 5:
    print(f'Inside the loop, the value of n is {n}.')
    n += 1

# Example 2:

count: int = 1
salespeople: int = int(input('Enter the number of salespeople: '))

while count <= salespeople:
    sales: float = float(input(f'Enter the sales for salesperson {count}: '))
    comm_rate: float = float(input('Enter the commission rate: '))
    
    commission: float = sales * comm_rate
    
    print(f'The commission is ${commission:,.2f}.')
    
    count += 1