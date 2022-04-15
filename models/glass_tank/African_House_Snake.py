from models.animal.Animal import Animal
from movements.slithering import Slithering

class African_House_Snake(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def __str__(self):
        return f"{self.name} the {self.species}"