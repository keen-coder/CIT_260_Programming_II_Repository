import re

# findall() Function=============================================================
# NOTE: The use of the letter 'r' in front of the regex this creates a 
#  'raw string' so you don't have to worry about escaping special characters

text = 'Today is the first day of the rest of all days.'
regex = r'day' # <--- the regular expression
match = re.findall(regex, text)
print(match)        # prints ['day', 'day', 'day']
print(len(match))   # prints 3
#==============================================================================

# search() Function============================================================
text = 'Today is the first day of the rest of all days.'
regex = r'day' # <--- the regular expression
match = re.search(regex, text)
print(match)            # prints: <re.Match object; span=(2, 5), match='day'>
print(match.start())    # prints: 2
print(match.end())      # prints: 5
#==============================================================================

text = 'bob'
regex = r'bob.'

print(re.search(regex, text))
print()

# fullmatch() Function==========================================================
phone_numbers = []
regex1 = r'^\([0-9]{3}\)[0-9]{3}-[0-9]{4}$' # matches (xxx)xxx-xxxx
regex2 = r'^[0-9]{3}[0-9]{3}[0-9]{4}$'      # matches xxxxxxxxx
regex3 = r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'    # matches xxx-xxx-xxxx

with open('week04_strings/regex/phone_numbers.txt', 'r') as phone_file:
    phone_numbers = [number.strip() for number in phone_file.readlines()]

print('Valid / Invalid Phone Numbers')
for number in phone_numbers:
    is_match = re.fullmatch(regex1, number) or re.fullmatch(regex2, number) or re.fullmatch(regex3, number)
    print(f'{number}\t=\t{(is_match != None)}')
#==============================================================================