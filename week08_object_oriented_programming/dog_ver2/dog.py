# defined in dog.py

class Dog:
    def __init__(self, name='default_name', breed='default_breed'):
        self.__name = name
        self.__breed = breed
    def get_name(self):
        return self.__name
    def get_breed(self):
        return self.__breed
    def set_name(self, name):
        self.__name = name
    def set_breed(self, breed):
        self.__breed = breed

    def __str__(self):
        result = ''

        result += f'Name:\t{self.__name}\n'
        result += f'Breed:\t{self.__breed}'

        return result


    # def __str__(self):
    #     result = f'Name:\t{self.__name}, Breed:\t{self.__breed}'
    #     return result