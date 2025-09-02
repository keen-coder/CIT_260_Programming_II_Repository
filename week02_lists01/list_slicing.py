# slicing syntax: [start : end : step]
# remember: the end index is not included in the results

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday', 'Saturday']

days_one = days[1:2]
print(days_one)

# Get the days from Monday to Thursday
days_slice = days[1:5]
print(days_slice)

# Get the days from Sunday to Thursday
# start value is omitted so defaults to 0
days_slice = days[:5]
print(days_slice)

# get the days from Tuesday to the end of the list
days_slice = days[2:]
print(days_slice)

# get every other day starting with Sunday
days_slice = days[::2]
print(days_slice)

# omitting start and end gives you a COPY of the original list
days_copy = days[:]
print(days_copy)

print(f'days =\t\t{days}')
print(f'days_copy =\t{days_copy}')
days_copy[3] = 78
print(f'days =\t\t{days}')
print(f'days_copy =\t{days_copy}')

# Negative values can be used to get positions relative to the end of the list
days_slice = days[-5:-1]
print(days_slice)

# You can get a reverse of a list using the following:
days_reverse = days[-1:-4:-1]
print(days_reverse)