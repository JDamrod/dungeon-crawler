from abc import ABC, abstractmethod
from non_copyable import NonCopyable


class Actor(NonCopyable, ABC):
    def __init__(self, name, symbol, x, y, hp):
        self._name = name
        self._symbol = symbol
        self._x = x
        self._y = y
        self._hp = hp
        self._max_hp = hp

    @property
    def name(self): return self._name

    @property
    def symbol(self): return self._symbol

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def hp(self): return self._hp

    @property
    def max_hp(self): return self._max_hp

    @property
    def alive(self): return self._hp > 0

    def move_to(self, x, y):
        self._x, self._y = x, y

    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)

    def attack(self, target):
        target.take_damage(self.attack_power())

    @abstractmethod
    def attack_power(self): ...
