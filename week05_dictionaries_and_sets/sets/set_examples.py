# Creating a set===============================================================
# NOTE: when printing a set, order of items may vary
colors = {'red', 'green', 'blue', 'pink', 'green', 'yellow'}
print(colors) # {'pink', 'blue', 'yellow', 'red', 'green'}

colors = set(['red', 'green', 'blue', 'pink', 'green', 'yellow'])
print(colors) # {'blue', 'yellow', 'green', 'pink', 'red'}

# To create an empty set you need to use the set() function, why?
colors = set()

#==============================================================================

# Length / Size of a Set ======================================================
colors = {'red', 'green', 'blue', 'pink', 'green', 'yellow'}
print(len(colors)) # 5
#==============================================================================

# Adding / Removing Elements ==================================================
colors1 = {'red', 'green', 'blue'}

colors1.add('red')   # Does not add the duplicate
colors1.add('pink')
print(colors) # {'blue', 'red', 'pink', 'green'}

colors1 = {'red', 'green', 'blue'}
colors2 = {'orange', 'yellow', 'purple', 'red'}

colors1.update(colors2)
print(colors1) # {'green', 'red', 'orange', 'yellow', 'blue', 'purple'}

colors = {'red', 'green', 'blue'}
colors.remove('green')
# colors.remove('pink')  # Raises a KeyError
print(colors) # {'blue', 'red'}

colors = {'red', 'green', 'blue'}
colors.discard('blue')
colors.discard('pink') # DOES NOT raise a KeyError
print(colors) # {'red', 'green'}
#==============================================================================

# Iterating over a set ========================================================
colors = {"red", "blue", "green", "yellow", "purple", "orange", "pink"}

for color in colors:
    print(color, end=' ')
# purple pink blue red orange green yellow
#==============================================================================

# Removing Duplicates from a List =============================================
my_list = [1, 5, 1, 1, 2, 3, 1, 4, 5, 1, 2, 3, 4]
no_dupes = set(my_list)
print(no_dupes) # {1, 2, 3, 4, 5}
#==============================================================================

# Set Operations ==============================================================

# Union
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1.union(set2)
print(union) # {1, 2, 3, 4, 5, 6}
union = set1 | set2
print(union) # {1, 2, 3, 4, 5, 6}

# Intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print(intersection) # {3, 4}
intersection = set1 & set2
print(intersection) # {3, 4}

# Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference = set1.difference(set2)
print(difference) # {1, 2}
difference = set1 - set2
print(difference) # {1, 2}

# Symmetric Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

sym_difference = set1.symmetric_difference(set2)
print(sym_difference) # {1, 2, 5, 6}
sym_difference = set1 ^ set2
print(sym_difference) # {1, 2, 5, 6}
#==============================================================================

# Superset and Subset =========================================================
set1 = {1, 2, 3, 4}
set2 = {2, 4}

print(set1.issubset(set2)) # False
print(set1 <= set2)        # False
print(set2.issubset(set1)) # True
print(set2 <= set1)        # True

print(set1.issuperset(set2)) # True
print(set1 >= set2)          # True
print(set2.issuperset(set1)) # False
print(set2 >= set1)          # False
#==============================================================================

# Set Comprehensions ==========================================================

colors = ["green", "red", "blue", "green", 
          "yellow", "blue", "purple", "red", 
          "orange", "pink", "green"]

# Generate a set of colors with >= 5 characters
filtered_colors = {color for color in colors if len(color) >= 5}
print(filtered_colors)

#==============================================================================