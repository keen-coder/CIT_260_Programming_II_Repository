# Sentinel values are special values which are used to end a series of values.

# Example 01: Computing Property Tax

TAX_FACTOR: int = 0.0065 # Represents the tax factor.
print('Enter the property lot number or enter 0 to end.')

lot: int = int(input('Lot number: '))

while lot != 0:
    value: float = float(input('Enter the property value: '))
    tax: float = value * TAX_FACTOR
    print(f'Property tax: ${tax:,.2f}')
    print('Enter the next lot number or enter 0 to end.')
    lot = int(input('Lot number: '))