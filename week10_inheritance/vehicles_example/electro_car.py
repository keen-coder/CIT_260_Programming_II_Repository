from automobile import Automobile

class ElectroCar(Automobile):
   
    def __init__(self, make, model, mileage, price, batt_cap):
        super().__init__(make, model, mileage, price)

        self.__batt_cap = batt_cap

    def get_batt_cap(self):
        return self.__batt_cap
