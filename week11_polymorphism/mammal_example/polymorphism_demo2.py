# This program demonstrates polymorphism.

from mammal import Mammal
from dog import Dog
from cat import Cat


def main():
    # Create an Mammal object, a Dog object, and
    # a Cat object.
    mammal = Mammal('regular animal')
    dog = Dog()
    cat = Cat()

    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('I am a string')

# The show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods.

def show_mammal_info(creature):
    if isinstance(creature, Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal!')

# Call the main function.
if __name__ == '__main__':
      main()