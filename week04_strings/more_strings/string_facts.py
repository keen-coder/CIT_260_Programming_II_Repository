# Iterate over a string using a for loop=======================================
color = 'turquoise'

for ch in color:
    print(ch, end=' ')

# prints: t u r q u o i s e
#==============================================================================

# Functions and Strings========================================================
alpha = 'abcdefg'
print(len(alpha))   # prints: 7
print(max(alpha))   # prints: g (the letter with the highest Unicode value)
print(min(alpha))   # prints: a (the letter with the lowest Unicode value)   
#==============================================================================

# String concatenation ========================================================
string1 = 'hello'
string2 = 'world'
string3 = string1 + ' ' + string2
print(string3) # prints: hello world
string3 += ' strings!'
print(string3) # prints: hello world strings! 
# =============================================================================

# String Indexing==============================================================
poppins = 'supercalifragilisticexpialidocious'
print(poppins[10]) # prints: r
print(poppins[17]) # prints: t

# The next line does not work because 
# strings are immutable.
# poppins[0] = 'z' # Raises a TypeError
#==============================================================================

# Strings and in Operator======================================================
colors = 'red green blue'

print('green' in colors)    # prints: True
print('pink' in colors)     # prints: False
print('pink' not in colors) # prints: True
print('e' in colors)        # prints: True
#==============================================================================

# Repetition operator with strings=============================================
laugh = 'ha' * 5                # 'hahahahaha'
echo = 'Echo! ' * 3             # 'Echo! Echo! Echo! '
meow = 'Meow ' * 4              # 'Meow Meow Meow Meow '
robot_beep = 'Beep-boop ' * 2   # 'Beep-boop Beep-boop '
zeros = '0' * 7                 # '0000000'
#==============================================================================

# String Slices================================================================
fruit = 'pineapple'
slice1 = fruit[0:4]     # 'pine'      (first 4 letters)
slice2 = fruit[4:]      # 'apple'     (index 4 to the end)
slice3 = fruit[:5]      # 'pinea'     (index 0 to 4)
slice4 = fruit[1:8:2]   # 'iepa'      (every 2nd character from index 1 to 7)
slice5 = fruit[-5:]     # 'apple'     (last 5 characters)
slice6 = fruit[::-1]    # 'elppaenip' (reversed string)
#==============================================================================

# String Methods - Basic Transformations=======================================
s = 'hello world'

capitalized = s.capitalize()       # 'Hello world'
centered = s.center(20, '-')       # '----hello world-----'
lowered = s.lower()                # 'hello world'
uppered = s.upper()                # 'HELLO WORLD'
swapcased = s.swapcase()           # 'HELLO WORLD'
titlecased = s.title()             # 'Hello World'
#==============================================================================

# String Methods - Search & Count Methods======================================
s = 'banana banana smoothie'

count_banana = s.count('banana')   # 2
found_index = s.find('smoothie')   # 14
found_index2 = s.index('banana')   # 0
rfound_index = s.rfind('banana')   # 7
rindex_banana = s.rindex('banana') # 7
#==============================================================================

# String Methods - Boolean Check Methods=======================================
s1 = 'Python3'
s2 = '123'
s3 = '   '
s4 = 'HELLO'
s5 = 'hello'
s6 = 'Hello World'

is_alnum = s1.isalnum()            # True
is_alpha = s1.isalpha()            # False
is_ascii = s1.isascii()            # True
is_decimal = s2.isdecimal()        # True
is_digit = s2.isdigit()            # True
is_identifier = s1.isidentifier()  # True
is_lower = s5.islower()            # True
is_numeric = s2.isnumeric()        # True
is_printable = s1.isprintable()    # True
is_space = s3.isspace()            # True
is_title = s6.istitle()            # True
is_upper = s4.isupper()            # True
#==============================================================================

# String Methods - Strip & Justify Methods=====================================
s = '   banana   '

stripped = s.strip()               # 'banana'
lstripped = s.lstrip()             # 'banana   '
rstripped = s.rstrip()             # '   banana'
left_justified = s.ljust(15, '.')  # '   banana......'
right_justified = s.rjust(15, '.') # '......   banana'
#==============================================================================

# String Methods - Split & Join Methods========================================
s = 'apple,banana,cherry'

split_list = s.split(',')                   # ['apple', 'banana', 'cherry']
rsplit_list = s.rsplit(',', 1)              # ['apple,banana', 'cherry']
lines = 'line1\nline2\nline3'.splitlines()  # ['line1', 'line2', 'line3']
joined = '-'.join(['a', 'b', 'c'])          # 'a-b-c'
#==============================================================================

# String Methods - Start/End Check Methods=====================================
s = 'once upon a time'

starts = s.startswith('once')      # True
ends = s.endswith('time')          # True
#==============================================================================

# String Methods - Replace Method==============================================
s = 'I love bananas'

replaced = s.replace('bananas', 'apples')  # 'I love apples'
#==============================================================================