# import the python datetime module to help us create a timestamp
from datetime import date

class Goldfish:

    def __init__(self, name, species, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
        self.__chip_number = chip_num

    def feed(self):
      return (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def chip_number(self):
      return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
      pass