from views import Varmint_Village, Slither_Inn, Critter_Cove, Chip_number

areaList = []

varmint_village = Varmint_Village()
slither_inn = Slither_Inn()
critter_cove = Critter_Cove()

areaList.append(varmint_village)
areaList.append(slither_inn)
areaList.append(critter_cove)

print(slither_inn.last_critter_added)

# for area in areaList:
#     print(f"{area.attraction_name} is where you'll find {area.description}, like")
#     for animal in varmint_village.animals:
#         print(f'   * {animal.name} the {animal.species}')

# Chip_number()