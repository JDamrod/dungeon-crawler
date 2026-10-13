from item import Item


class Key(Item):
    def __init__(self, name, x, y):
        super().__init__(name, "K", x, y)

    def on_pickup(self, hero):
        hero.getkey(self)
