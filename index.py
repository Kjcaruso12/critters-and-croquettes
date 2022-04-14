from views import Varmint_Village, Slither_Inn, Critter_Cove

varmint_village = Varmint_Village()
slither_inn = Slither_Inn()
critter_cove = Critter_Cove()

print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like")
for animal in varmint_village.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like")
for animal in slither_inn.animals:
    print(f'   * {animal.name} the {animal.species}')

print(f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like")
for animal in critter_cove.animals:
    print(f'   * {animal.name} the {animal.species}')