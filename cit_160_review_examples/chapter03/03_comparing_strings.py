# Python allows you to compare two strings using the == operator to check if the strings are
# exactly the same.
# String comparisons are case sensitive.

# Credit: Example from Starting out with Python, Gaddis

password = input('Enter the password: ')

if password == 'abcd1234':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')

# NOTE: the other relational operators can also be used to compare strings. Review the Chapter 03
# section called "Other String Comparisons" to understand how and why this works and what is actually
# being compared.