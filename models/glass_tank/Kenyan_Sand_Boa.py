# import the python datetime module to help us create a timestamp
from datetime import date
from models.animal.Animal import Animal

class Kenyan_Sand_Boa(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'on {date.today()}, {self.name} had "Aladdin" put on the TV so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"