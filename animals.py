from petting_area import Alpaca, Donkey, Goat, Lamb, Llama
from glass_tank import Copperhead, Kenyan_Sand_Boa, Rosy_Boa, African_House_Snake, Rat_Snake
from pond import Bluegill, Carp, Goldfish, Bass, Minnow
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
carl = Llama("Carl", "Llama", "morning", "grass")
frank = Alpaca("Frank", "Alpaca", "midday", "grass")
shane = Donkey("Shane", "Donkey", "afternoon", "straw")
marge = Goat("Marge", "Goat", "midday", "everything")
susan = Lamb("Susan", "Lamb", "morning", "grass")

varmint_village.add_animal(carl)
varmint_village.add_animal(frank)
varmint_village.add_animal(shane)
varmint_village.add_animal(marge)
varmint_village.add_animal(susan)

slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
steve = Copperhead("Steve", "Copperhead", "rodents")
bolt = Kenyan_Sand_Boa("Bolt", "Kenyan Sand Boa", "rodents")
rose = Rosy_Boa("Rose", "Rosy Boa", "rodents")
pip = African_House_Snake("Pip", "African House Snake", "rodents")
paige = Rat_Snake("Paige", "Rat Snake", "rodents")

slither_inn.add_animal(steve)
slither_inn.add_animal(bolt)
slither_inn.add_animal(rose)
slither_inn.add_animal(pip)
slither_inn.add_animal(paige)

critter_cove = Wetlands("Critter Cove", "feathered friends and fantastic fish")
charlie = Bluegill("Charlie", "Bluegill", "insects")
garp = Carp("Garp", "Carp", "insects")
renee = Goldfish("Renee", "Goldfish", "insects")
jinx = Bass("Jinx", "Bass", "fish")
colby = Minnow("Colby", "Minnow", "insects")

critter_cove.add_animal(charlie)
critter_cove.add_animal(garp)
critter_cove.add_animal(renee)
critter_cove.add_animal(jinx)
critter_cove.add_animal(colby)

print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like")
for animal in varmint_village.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like")
for animal in slither_inn.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like")
for animal in critter_cove.animals:
    print(f'   * {animal.name} the {animal.species}')