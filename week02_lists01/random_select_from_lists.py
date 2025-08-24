import random

# The random module includes a choice() function to randomly select an element from a sequence

animals = ['hare', 'mink', 'rabbit', 'pony', 'reindeer', 'toad', 'raven', 'chicken', 'horse', 'kangaroo']

# print out 5 random animals
for x in range(0, 5):
    print(random.choice(animals))

# You can also get a list of random items using the choice() function of the random module.
# k=n is the number of random elements you want to generate
# you MUST put k= in the function parameters
random_animals = random.choices(animals, k=5)
print(random_animals)