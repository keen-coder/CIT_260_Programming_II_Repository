# Normally print() will print everything on one line and insert an invisible new line \n character
# to the end of the output.
# You can suppress this behaviour using the 'end' argument of the print() function.

# the following prints on three lines
print('one')
print('two')
print('three')

# the following prints on one line
# the value for the argument can be any valid character
print('one', end=' ')
print('two', end=' ')
print('three', end=' ')

print() # this empty statement is used to add a newline character to the previous output.

# prints all on one line with @ symbol in between
print('one', end='@')
print('two', end='@')
print('three', end='@')
print()

# prints all on one line with nothing in between
print('one', end='')
print('two', end='')
print('three', end='')
print()

# The print function also has another argument called the seperator (sep) argument.  With this argument
# you can specify what you want to separate multiple items with, instead of a space. 

# prints on one line with spaces in between
print('One', 'Two', 'Three')

# prints on one line with no spaces in between
print('One', 'Two', 'Three', sep='')

# prints on one line with '*' in between
print('One', 'Two', 'Three', sep='*')

# prints on one line with +++ in between
print('One', 'Two', 'Three', sep='+++')


# Python has special characters called escape characters.  All escape characters start with a \ (backslash).
# which must be included inside a string literal.
# The following are the most commonly used escape characters, you can look up more online in the Python
# documention.
#   \n new line character, advances the output to the next line
#   \t tab character, output skips over to the next horizontal tab
#   \' single quote, prints a single quote. 
#   \" double quote, prints a double quote. 
#   \\ backslash, prints a single backslash.

# Prints on there separate lines
print('One\nTwo\nThree')

# Prints tabs between each item
print('Mon\tTues\tWed')
print('Thur\tFri\tSat')

# Prints quotation marks in the middle of the string
print("Your assignment is to read \"Hamlet\" by tomorrow.")
print('I\'m ready to begin.')

# Prints backslashes in the output
print('The path is C:\\temp\\data.')