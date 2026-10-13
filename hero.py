from actor import Actor


class Hero(Actor):
    def __init__(self, x, y):
        super().__init__("Bohater", "@", x, y, 10)
        self.__weapon = None
        self.__key = None

    def equip(self, weapon):
        self.__weapon = weapon

    def getkey(self, key):
        self.__key = key

    @property
    def weapon_name(self):
        if self.__weapon is None:
            return "brak"
        return self.__weapon.name
    
    @property
    def key(self):
        return self.__key

    def attack_power(self):
        if self.__weapon is None:
            return 2
        return 2 + self.__weapon.bonus
