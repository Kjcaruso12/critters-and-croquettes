# import the python datetime module to help us create a timestamp
from datetime import date
from models.animal.Animal import Animal
from movements.walking import Walking

class Goat(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(f'on {date.today()}, {self.name} had its chin scratched so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} the {self.species}"