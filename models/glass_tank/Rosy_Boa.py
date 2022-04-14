from models.animal.Animal import Animal

class Rosy_Boa(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"