from models import PettingZoo, Llama, Alpaca, Donkey, Goat, Lamb

def Varmint_Village():

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

    return varmint_village