# Boolean variables are variables that have a value of either True or False.  They can be assigned
# one of these values by using the True or False literals, or by assigning the variable the result
# of a boolean expression.

is_cat = True
is_dog = False

sales = 3000.45
quota_met = sales >= 2000

# Boolean variables can be tested as conditions in a if or elif structure

if quota_met:
    print('All sales quotas have been met for the day!')

# this is the same as

if quota_met == True:
    print('All sales quotas have been met for the day!')

