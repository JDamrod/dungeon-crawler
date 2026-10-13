from actor import Actor


class Enemy(Actor):
    def __init__(self, x, y):
        super().__init__("Potwor", "E", x, y, 5)
        self.__power = 1

    def attack_power(self):
        return self.__power

    def next_step(self, target):
        dx = target.x - self._x
        dy = target.y - self._y
        if abs(dx) + abs(dy) > 6:
            return self._x, self._y
        if abs(dx) >= abs(dy):
            if dx > 0:
                return self._x + 1, self._y
            return self._x - 1, self._y
        if dy > 0:
            return self._x, self._y + 1
        return self._x, self._y - 1
