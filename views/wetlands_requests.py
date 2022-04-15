from models import Wetlands, Bluegill, Carp, Goldfish, Bass, Minnow

def Critter_Cove():

    critter_cove = Wetlands("Critter Cove", "feathered friends and fantastic fish")
    charlie = Bluegill("Charlie", "Bluegill", "insects", 777777)
    garp = Carp("Garp", "Carp", "insects", 888888)
    renee = Goldfish("Renee", "Goldfish", "insects", 123789)
    jinx = Bass("Jinx", "Bass", "fish", 999999)
    colby = Minnow("Colby", "Minnow", "insects", 987321)

    critter_cove.add_animal(charlie)
    critter_cove.add_animal(garp)
    critter_cove.add_animal(renee)
    critter_cove.add_animal(jinx)
    critter_cove.add_animal(colby)

    return critter_cove


def Chip_number():

    felix = Goldfish("Felix", "Goldfish", "insects", 234789)

    felix.chip_number = 555783

    print(felix.chip_number)