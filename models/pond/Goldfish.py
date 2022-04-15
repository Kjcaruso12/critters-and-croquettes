# import the python datetime module to help us create a timestamp
from datetime import date
from models.animal.Animal import Animal
from movements.swimming import Swimming

class Goldfish(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        self.swimming = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} the {self.species}"