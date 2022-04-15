from models import PettingZoo, Llama, Alpaca, Donkey, Goat, Lamb

def Varmint_Village():

    varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
    carl = Llama("Carl", "Llama", "morning", "grass", 345678)
    frank = Alpaca("Frank", "Alpaca", "midday", "grass", 876432)
    shane = Donkey("Shane", "Donkey", "afternoon", "straw", 765432)
    marge = Goat("Marge", "Goat", "midday", "everything", 654321)
    susan = Lamb("Susan", "Lamb", "morning", "grass", 908321)

    varmint_village.add_animal(carl)
    varmint_village.add_animal(frank)
    varmint_village.add_animal(shane)
    varmint_village.add_animal(marge)
    varmint_village.add_animal(susan)

    return varmint_village