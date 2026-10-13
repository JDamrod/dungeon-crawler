from item import Item


class Weapon(Item):
    def __init__(self, name, x, y, bonus):
        super().__init__(name, "/", x, y)
        self.__bonus = bonus

    @property
    def bonus(self): return self.__bonus

    def on_pickup(self, hero):
        hero.equip(self)
