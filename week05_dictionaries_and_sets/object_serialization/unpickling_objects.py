import pickle

FILE_PATH = 'week05_dictionaries_and_sets/object_serialization/'

populations = {}

# Open a file in BINARY MODE to read our objects:
with open(FILE_PATH + 'populations.bin', 'rb') as in_file:
    populations = pickle.load(in_file)
print(populations)

customers = {}

# Unpickle a complex object
with open(FILE_PATH + 'customers.bin', 'rb') as in_file:
    customers = pickle.load(in_file)

print(customers)

# Unpickle Multiple objects
populations = {}
customers = {}

with open(FILE_PATH + 'combined.bin', 'rb') as in_file:
    populations = pickle.load(in_file)
    customers = pickle.load(in_file)

print(populations)
print(customers)