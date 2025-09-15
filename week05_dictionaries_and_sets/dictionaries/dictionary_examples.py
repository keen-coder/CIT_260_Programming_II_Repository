# Creating a Dictionary========================================================
# Use curly braces {} to create a dictionary

# Dictionary for a simple phone book
phonebook = {'Jason':'555-5555', 'Sally':'555−6435', 
             'Jackson':'555−9486'}

# Dictionary to store the radii of celestial bodies in the solar system
sol_sys_radii = {'sun': 696340, 'mercury': 2439.7, 'venus': 6051.8,
                 'earth': 6371.0, 'mars': 3389.5, 'jupiter': 69911.0,
                 'saturn': 58232.0, 'uranus': 25362.0, 'neptune': 24622.0,
                 'pluto': 1188.3}

# Dictionary to store configuration settings
config_dict = {    
    "db_connection_string": "jdbc:mysql://localhost:3306/somedb",
    "api_key": "someCrazyLongkey42",    
    "max_retries": 3
}
#==============================================================================


# Retrieving values from dictionaries =========================================
# Use index notation, but instead of number, you give the key 
# and you get the value in return
colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

print(colors['red'])      # prints (255, 0, 0)
print(colors['green'])    # prints (0, 255, 0)
print(colors['blue'])     # prints (0, 0, 255)
# print(colors['pink'])     # KeyError, 'pink' does not exist.
# print(colors['Red'])      # KeyError, 'Red' with uppercase 'R' does not exist.
print(colors.get('red'))  # prints (255, 0, 0)
print(colors.get('pink')) # Returns None when not found instead
                          # instead of raising a KeyError
#==============================================================================

# Using in and not in==========================================================
people_ages = {"Alice": 30, "Bob": 25, "Charlie": 35,"Diana": 28}

print("Alice" in people_ages)      # True
print("Eve" in people_ages)        # False
print("Eve" not in people_ages)    # True
print("Bob" not in people_ages)    # False

if "Charlie" in people_ages:
    print(f"Charlie's age is {people_ages['Charlie']}")

name = "Eve"
if name not in people_ages:
    print(f"{name} is not in the dictionary.")
#==============================================================================

# Adding new key/value pairs and replacing existing values=====================

animal_weights = {"Elephant": 5400.5, "Tiger": 220.3, "Kangaroo": 85.7}

# Adding a new key/value pair
animal_weights["Penguin"] = 23.4

# Replacing the old value with a new one
animal_weights["Tiger"] = 225.62 

print(animal_weights) # {'Elephant': 5400.5, 'Tiger': 225.0, 'Kangaroo': 85.7, 'Penguin': 23.4}
#==============================================================================

# Deleting a key/value pair from a dictionary==================================
fruit_prices = {"Apple": 0.99, "Banana": 0.59, "Cherry": 3.49, "Mango": 1.75}

del fruit_prices["Banana"]  # Removes Banana from the dictionary

print(fruit_prices)
# {'Apple': 0.99, 'Cherry': 3.49, 'Mango': 1.75}

#==============================================================================

# Number of Elements in a Dictionary ==========================================
book_pages = {
    "1984": 328,
    "To Kill a Mockingbird": 281,
    "The Great Gatsby": 180,
    "The Hobbit": 310,
    "Pride and Prejudice": 432,
    "The Catcher in the Rye": 277,
    "Brave New World": 311
}

print(len(book_pages)) # prints 7
#==============================================================================

# Creating an empty Dictionary=================================================
dict1 = {}
dict2 = dict()
#==============================================================================

# Iterating over a Dictionary==================================================

product_catalog = {101: "Laptop", 102: "Smartphone", 103: "Tablet",
                   104: "Monitor", 105: "Keyboard"}

for key in product_catalog:
    print (f'Product ID {key} is a {product_catalog[key]}')

#==============================================================================

# Dictionary Methods===========================================================

movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}

# .clear() Method
movie_ratings.clear()
print(movie_ratings) # prints {} (an empty dictionary)

movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}

# .get() Method
print(movie_ratings.get('Inception'))           # prints 8.8
print(movie_ratings.get('Avatar'))              # prints None
print(movie_ratings.get('Avatar', 'Not Rated')) # prints Not Rated

# .items() Method
print(movie_ratings.items())
# dict_items([('Inception', 8.8), ('The Matrix', 8.7), ('Interstellar', 8.6), ('The Prestige', 8.5)])

for key, value in movie_ratings.items():
    print(f'Title: {key}, Rating: {value}')
# prints: 
# Title: Inception, Rating: 8.8
# Title: The Matrix, Rating: 8.7
# Title: Interstellar, Rating: 8.6
# Title: The Prestige, Rating: 8.5

# .keys() Method
print(movie_ratings.keys())
# prints: dict_keys(['Inception', 'The Matrix', 'Interstellar', 'The Prestige'])

for key in movie_ratings.keys():
    print(f'Title: {key}, Rating: {movie_ratings[key]}')
# prints:
# Title: Inception, Rating: 8.8
# Title: The Matrix, Rating: 8.7
# Title: Interstellar, Rating: 8.6
# Title: The Prestige, Rating: 8.5

# .pop() Method
print(movie_ratings.pop('The Matrix')) # prints 8.7
# print(movie_ratings.pop('Avatar')) # Raises a KeyError
print(movie_ratings.pop('Avatar', 0.0)) # prints 0.0
print(movie_ratings) # prints {'Inception': 8.8, 'Interstellar': 8.6, 'The Prestige': 8.5}

# .popitem() Method
movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}

print(movie_ratings.popitem()) # ('The Prestige', 8.5)
print(movie_ratings.popitem()) # ('Interstellar', 8.6)
print(movie_ratings) # {'Inception': 8.8, 'The Matrix': 8.7}

# .values() Method
movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}

print(movie_ratings.values()) # dict_values([8.8, 8.7, 8.6, 8.5])

for value in movie_ratings.values():
    print(value)
# prints
# 8.8
# 8.7
# 8.6
# 8.5

#==============================================================================

# Merge and Update Operators===================================================

store_a = {"Apples": 30, "Bananas": 45, "Oranges": 20}
store_b = { "Bananas": 50, "Grapes": 25, "Peaches": 15}

store_merged = store_a | store_b
print(store_merged) 
# {'Apples': 30, 'Bananas': 50, 'Oranges': 20, 'Grapes': 25, 'Peaches': 15}

store_a |= store_b
print(store_a)
# {'Apples': 30, 'Bananas': 50, 'Oranges': 20, 'Grapes': 25, 'Peaches': 15}

#==============================================================================

# Dictionary Comprehensions ===================================================

# Using a loop, create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares = {}
for item in numbers:
    squares[item] = item**2
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Using a dictionary comprehension
squares = {item:item**2 for item in numbers}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary of names and their lengths
names = ['Jeremy', 'Kate', 'Peg']
str_lengths = {item:len(item) for item in names}
print(str_lengths) # {'Jeremy': 6, 'Kate': 4, 'Peg': 3}

# Create a copy of a dictionary with a comprehension
dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {k:v for k,v in dict1.items()}
print(dict2) # {'A': 1, 'B': 2, 'C': 3}

# Dictionary comprehension with an if statement
populations = {'New York': 8398748, 'Los Angeles': 3990456,
               'Chicago': 2705994, 'Houston': 2325502, 
               'Phoenix': 1660272, 'Philadelphia': 1584138}

largest = {k:v for k,v in populations.items() if v > 2000000}

print(largest) # {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994, 'Houston': 2325502}

#==============================================================================

# Nested Dictionary============================================================
customers = {    
    "John": {"age": 39, "address": "123 Main St", "email": "john@example.com"},    
    "Mary": {"age": 19, "address": "678 First St", "email": "jane@example.com"}
}

# update email for John
customers ["John"]["email"] = "john.new@example.com"

# iterate through dictionary
for name, info in customers.items():    
    print(name)    
    print(info["age"])  
    print(info["address"]) 
    print(info["email"])
