from models import SnakePit, Copperhead, Kenyan_Sand_Boa, Rosy_Boa, African_House_Snake, Rat_Snake

def Slither_Inn():

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

    return slither_inn