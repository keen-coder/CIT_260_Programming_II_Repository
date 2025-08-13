# Python has built-in math operators to perform basic math calculations:
#   + Addition, - Subtraction, * Multiplication, / Division, // Integer Division
#   % Remainder, ** Exponent

x: int = 59
y: int = 23

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print (x ** y)

# NOTE: Python has two division operators, / and //.  / performs normal division where the result
# will be a floating-point value. // performs integer division where the result will ONLY 
# be the value to the left of the decimal place (integer division). // does not round the results.

# % computes the remainder of a division operation

a: int = 5
b: int = 2

c: float = a / b # normal division, result will be a float (2.5)
d: int = a // b # integer division, result will be an integer (2)
e: int = a % b  # remainder division, result will be an integer (1)

print(f'c = {c}')
print(f'd = {d}')
print(f'e = {e}')

# Mixed operator expressions have an order of operations (order of precedence)
# From highest precedence to lowest:
    # 1. Exponentiation: **
    # 2. Multiplication, Division, and Remainder: *, /, //, %
    # 3. Addition and subtraction: +, -
# Higher operators are computed before lower operators.  Paratehnsis can be used to change the
# precedence of an operation

exp1 = 5 + 2 * 4                # result is 13
exp2 = 10 / 2 - 3               # result is 2.0
exp3 = 8 + 12 * 2 - 4           # result is 28
exp4 = 6 - 3 * 2 + 7 - 1        # result is 6

print(exp1)
print(exp2)
print(exp3)
print(exp4)

exp5 = (5 + 2) * 4              # result is 28
exp6 = 10 / (5 - 3)             # result is 5.0
exp7 = 8 + 12 * (6 - 2)         # result is 56
exp8 = (6 - 3) * (2 + 7) / 3    # result is 9.0

print(exp5)
print(exp6)
print(exp7)
print(exp8)

# If you perform calculations with mixed-type operands (values in the math expression that have
# different data types), the result will depend on the data type of the operands.  The following
# rules are used: 
#   Two integer operands will result in an integer result.
#       int operator int = int
#   Two float values will result in a float result.
#        float operator float = float
#   With a float and integer in the same operation, the integer is temporarily converted to a float,
#   the operation is performed, and the result will be a float.
#       float operator int = float
#       int operator float = float

exp9 = 25 * 2.4375              # result is 60.9375 (int * float = float)
print(exp9)