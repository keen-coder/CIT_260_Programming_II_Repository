# Functions that do not return a value are called "void functions". Otherwise a value-returning
# function does exactly that.  It returns a value to the point where it was called in the program.

# Use a return statement to return a value from a function.

# You can return any type of value (int, float, str, bool, list, tuple, etc.) from a function.

DISCOUNT_PERCENTAGE = 0.20


def get_regular_price() -> float:
    price: float = float(input("Enter the item's regular price: "))
    return price

def discount(price) -> float:
    return price * DISCOUNT_PERCENTAGE

def main():
    reg_price: float = get_regular_price()
    sale_price: float = reg_price - discount(reg_price)
    print(f'The sale price is ${sale_price:,.2f}.')

if __name__ == "__main__":
    main()