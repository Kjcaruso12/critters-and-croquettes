from models import SnakePit, Copperhead, Kenyan_Sand_Boa, African_House_Snake, Rat_Snake, Turtle

def Slither_Inn():

    slither_inn = SnakePit("Slither Inn", "stupendous snakes of all sizes")
    steve = Copperhead("Steve", "Copperhead", "rodents", 333333)
    bolt = Kenyan_Sand_Boa("Bolt", "Kenyan Sand Boa", "rodents", 444444)
    nikko = Turtle("Nikko", "Turtle", "vegetation", 555555)
    pip = African_House_Snake("Pip", "African House Snake", "rodents", 666666)
    paige = Rat_Snake("Paige", "Rat Snake", "rodents", 222222)

    slither_inn.add_animal(steve)
    slither_inn.add_animal(bolt)
    slither_inn.add_animal(nikko)
    slither_inn.add_animal(pip)
    slither_inn.add_animal(paige)

    return slither_inn