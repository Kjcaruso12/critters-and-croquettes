# import the python datetime module to help us create a timestamp
from datetime import date
from models.animal.Animal import Animal
from movements.slithering import Slithering

class Kenyan_Sand_Boa(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Aladdin" put on the TV so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} the {self.species}"