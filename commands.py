from enum import Enum


class Command(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    QUIT = 5
    NONE = 6


DEFAULT_KEYS = {
    "w": Command.UP,
    "s": Command.DOWN,
    "a": Command.LEFT,
    "d": Command.RIGHT,
    "q": Command.QUIT,
}
