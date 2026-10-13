from item import Item


class Potion(Item):
    def __init__(self, name, x, y, power):
        super().__init__(name, "!", x, y)
        self.__power = power

    def on_pickup(self, hero):
        hero.heal(self.__power)
