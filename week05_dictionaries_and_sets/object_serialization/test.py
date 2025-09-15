import pickle

FILE_PATH = 'week05_dictionaries_and_sets/object_serialization/'



store_a = {"Apples": 30, "Bananas": 45, "Oranges": 20}
store_b = { "Bananas": 50, "Grapes": 25, "Peaches": 15}
movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}
product_catalog = {101: "Laptop", 102: "Smartphone", 103: "Tablet",
                   104: "Monitor", 105: "Keyboard"}

with open(FILE_PATH + 'unknown.bin', 'wb') as out_file:
    pickle.dump(store_a, out_file)
    pickle.dump(store_b, out_file)
    pickle.dump(movie_ratings, out_file)
    pickle.dump(product_catalog, out_file)