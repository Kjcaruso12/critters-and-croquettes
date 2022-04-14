# import the python datetime module to help us create a timestamp
from datetime import date
from models.animal.Animal import Animal

class Goat(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed(self):
        print(f'on {date.today()}, {self.name} had its chin scratched so it would eat its {self.food}')

    def __str__(self):
        return f"{self.name} is a {self.species}"