from mammal import Mammal

# The Dog class is a subclass of the Mammal class.

class Dog(Mammal):

    # The __init__ method calls the superclass's
    # __init__ method passing 'Dog' as the species.
    
    def __init__(self):
        super().__init__('Dog')

    # The make_sound method overrides the superclass's
    # make_sound method.
    
    def make_sound(self):
        print('Woof! Woof!')