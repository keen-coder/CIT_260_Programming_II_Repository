class Character:

    def __init__(self, health=0):
       self.__health = self.set_health(health)
       
       # self.__health = self.set_health(health)
        
        
    def __set_health(self, health):
        if health < 0 or health > 100:
            raise ValueError('ERROR: Health must be between 0 and 100.')
        else:
            self.__health = health

    def get_health(self):
        return self.__health