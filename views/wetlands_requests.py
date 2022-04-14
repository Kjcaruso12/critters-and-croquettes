from models import Wetlands, Bluegill, Carp, Goldfish, Bass, Minnow

def Critter_Cove():

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

    return critter_cove