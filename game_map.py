from non_copyable import NonCopyable


class Map(NonCopyable):
    def __init__(self, rows, items):
        self.__rows = rows
        self.__items = items

    @property
    def height(self):
        return len(self.__rows)

    @property
    def items(self):
        return self.__items

    def row(self, y):
        return self.__rows[y]

    def is_wall(self, x, y):
        if not (0 <= y < len(self.__rows) and 0 <= x < len(self.__rows[y])):
            return True
        return self.__rows[y][x] == "#"

    def is_door(self, x, y):
        return self.__rows[y][x] == "?"

    def open_door(self, x, y):
        self.__rows[y] = self.__rows[y].replace("?", ".")

    def item_at(self, x, y):
        for item in self.__items:
            if item.x == x and item.y == y:
                return item
        return None

    def remove_item(self, item):
        self.__items.remove(item)
