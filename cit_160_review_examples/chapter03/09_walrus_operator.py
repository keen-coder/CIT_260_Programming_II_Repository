# The walrus operator := is used to assign a value to a variable AND return the value that was 
# assigned. This operator is not used a lot, but may be useful for some things.

# This assigns the value of 42 to result AND prints it out. You can then use the variable result
# elsewhere in the program if necessary
print(result := 42)
print(result + 10)

# Another example:
# NOTE: The walrus operator has the lowest precedence of all the operators.

hours = 20
pay_rate = 15.34

if (pay := hours * pay_rate) > 40:
    print('You worked overtime.')
