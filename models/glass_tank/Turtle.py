from models.animal.Animal import Animal
from movements import Walking, Swimming

class Turtle(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def run(self):
        print(f'{self} crawls')

    def __str__(self):
        return f"{self.name} the {self.species}"