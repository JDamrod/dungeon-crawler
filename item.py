from abc import ABC, abstractmethod
from non_copyable import NonCopyable


class Item(NonCopyable, ABC):
    def __init__(self, name, symbol, x, y):
        self._name = name
        self._symbol = symbol
        self._x = x
        self._y = y

    @property
    def name(self): return self._name

    @property
    def symbol(self): return self._symbol

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @abstractmethod
    def on_pickup(self, hero): ...
