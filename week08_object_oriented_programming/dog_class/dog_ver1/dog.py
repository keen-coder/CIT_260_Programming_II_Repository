# defined in dog.py

class Dog:
    def __init__(self, name='default_name', breed='default_breed'):
        self.name = name
        self.breed = breed
    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def set_name(self, name):
        self.name = name
    def set_breed(self, breed):
        self.breed = breed