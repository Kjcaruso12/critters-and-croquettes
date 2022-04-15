from views import Varmint_Village, Slither_Inn, Critter_Cove, Chip_number
from models import Turtle, PettingZoo, Wetlands, Lamb, Bass


areaList = []

varmint_village = Varmint_Village()
slither_inn = Slither_Inn()
critter_cove = Critter_Cove()

areaList.append(varmint_village)
areaList.append(slither_inn)
areaList.append(critter_cove)

bob = Turtle("Bob", "Snapping Turtle", "unsuspecting victims", 678543)
meep = Lamb("Meep","Lamb", "morning", "grass", 123567)
bruce = Bass("Bruce", "Bass", "fish", 654098)
varmint_village2 = PettingZoo("Varmint Village", "critters that like to dig and scurry")
critter_cove2 = Wetlands("Critter Cove", "scaly critters that enjoy a good swim")
varmint_village2.add_animal(bob)
varmint_village2.add_animal_type_check(meep)
varmint_village2.add_animal_pythonic(meep)
varmint_village2.add_animal_pythonic(bruce)
critter_cove2.add_animal_type_check(meep)
critter_cove2.add_animal_pythonic(meep)
critter_cove2.add_animal_pythonic(bruce)
for animal in varmint_village2.animals:
    print(animal)
for animal in critter_cove2.animals:
    print(animal)
# print(slither_inn.last_critter_added)

# for area in areaList:
#     print(f"{area.attraction_name} is where you'll find {area.description}, like")
#     for animal in varmint_village.animals:
#         print(f'   * {animal.name} the {animal.species}')

# Chip_number()

