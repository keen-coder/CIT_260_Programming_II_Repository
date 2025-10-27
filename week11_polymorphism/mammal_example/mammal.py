# The Mammal class represents a generic mammal.

class Mammal:

    # The __init__ method accepts an argument for
    # the mammal's species.
    
    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message
    # indicating the mammal's species.
    
    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    
    def make_sound(self):
        print('Grrrrr')
